import numpy as np
import pywt
import matplotlib.pyplot as plt
import random
from scipy import stats
from scipy import fft
import random
import pywt.data
from PIL import Image
import pandas as pd
import seaborn as sns
import os
import pickle

def convert_to_wavelet_basis(folder_dir, color, basis="db1", normalized = False):
    file_list = [os.path.join(folder_dir, filename) for filename in os.listdir(folder_dir)]
    #Setup df Dict
    image = Image.open(file_list[0]).convert('L')
    first_image = pywt.wavedec2(image, basis)
    layer_len = len(first_image)
    print(str(layer_len) + " layers being used")
    
    color_dict = {"Red":0, "Green":1, "Blue":2, "Gray":3, "Infrared": 4}
    c = color_dict[color]

    #Fill DF DICT
    layer_arr = [0] * len(file_list) * (layer_len - 1) * 3 
    orientation = [0] * len(file_list) * (layer_len - 1) * 3 
    data_arr = [0] * len(file_list) * (layer_len - 1) * 3 
    cnt = 0
    for k in range(len(file_list)):
        if c >= 3:
            image = np.array(Image.open(file_list[k]).convert('L'))
    
        else:
            image = np.array(Image.open(file_list[k]))[:,:,c]

        if normalized:
            std= np.std(image)
            mean = np.mean(image)
            image = (image- mean)/std

    
        transformed = pywt.wavedec2(image, 'db1')
        direction_names = ['H', 'V', 'D']

        for i in range(1, layer_len): 
            for j in range(len(transformed[i])):
                
                arr = np.array(transformed[i][j])
                layer_arr[cnt] = i+1
                orientation[cnt] =  direction_names[j]
                data_arr[cnt] = arr.flatten()
                cnt += 1

    df = pd.DataFrame()

    df["layer"] = layer_arr
    df["orientation"] = orientation
    df["data"] = data_arr
    new_df = pd.DataFrame(columns=["channel","layer", "orientation", "data"])
    for lo, sf in df.groupby(["layer", "orientation"])[["data"]]:#.agg(lambda sf: np.concatenate(sf["Data"].tonumpy()))
        new_df.loc[len(new_df.index)] = [color, lo[0], lo[1],  np.hstack(sf['data'])]
    
    return new_df

def getIndexDF(image, no_zero =False):
    x_freqs = fft.fftfreq(image.shape[0])
    y_freqs = fft.fftfreq(image.shape[1])
    coord_df = pd.DataFrame()
    coord_df["index_coords"] = [(x,y) for x in np.arange(image.shape[0]) for y in np.arange(image.shape[0])]
    coord_df["x_index"] = [x for x in np.arange(image.shape[0]) for y in np.arange(image.shape[0])]
    coord_df["y_index"] = [y for x in np.arange(image.shape[0]) for y in np.arange(image.shape[0])]
    coord_df["x_freq"] = [x_freqs[x] for x in np.arange(image.shape[0]) for y in np.arange(image.shape[0])]
    coord_df["y_freq"] = [y_freqs[y] for x in np.arange(image.shape[0]) for y in np.arange(image.shape[0])]
    coord_df["magnitude"] = np.sqrt(coord_df["x_freq"] ** 2 + coord_df["y_freq"] **2)
    coord_df = coord_df.set_index(["index_coords"])
    coord_df = coord_df[(coord_df["x_freq"] >= 0 )& (coord_df["y_freq"] >= 0)]
    if no_zero:
        coord_df = coord_df[(coord_df["x_freq"] != 0 )| (coord_df["y_freq"] != 0)]
    return coord_df

def convert_fourier_list(folder_dir, c):
    file_list = [os.path.join(folder_dir, filename) for filename in os.listdir(folder_dir)]
    image = np.array(Image.open(file_list[0]).convert('L'))
    coord_df = getIndexDF(image, no_zero =False).sort_values(["magnitude"])
    x = coord_df["x_index"].to_numpy()
    y = coord_df["y_index"].to_numpy()
    magnitudes = coord_df["magnitude"]
    freq_arr = []
    mag_arr =  []
    freq_arr = [0]*len(file_list)
    mag_arr = [0]*len(file_list)
    for k in range(len(file_list)):
        if c >= 3:
            image = np.array(Image.open(file_list[k]).convert('L'))
        else:
            image = np.array(Image.open(file_list[k]))[:,:,c]
        transformed = np.array(fft.fft2(image))
        freq_arr[k] = transformed[tuple(x), tuple(y)]
        mag_arr[k] = magnitudes
    sample = np.concatenate(np.array(freq_arr).T)
    mag_flat = np.concatenate(np.array(mag_arr).T)
    return sample, mag_flat

def recursive_split(freqs, mags, threshold =0.05, max_depth = 5, presplit = 0):
    magnitude_splits = []
    def recursive_helper(freqs, mags, magnitude_splits, depth, presplit):
        if depth > 0 and mags[0] != mags[-1]:
            n = (mags[-1] + mags[0])/2
            idx = np.argmax(mags>n)
            if presplit > 0:
                stat = threshold + 1
            else:
                first_sample = np.concatenate([np.real(freqs[:idx]),np.imag(freqs[:idx])])
                second_sample = np.concatenate([np.real(freqs[idx:]),np.imag(freqs[idx:])])
                stat = stats.ks_2samp(first_sample, second_sample).statistic
            if stat > threshold:
                magnitude_splits.append(n)
                recursive_helper(freqs[:idx], mags[:idx], magnitude_splits, depth-1, max(presplit-1, 0))
                recursive_helper(freqs[idx:], mags[idx:], magnitude_splits, depth-1, max(presplit-1, 0))
        elif mags[0] == mags[-1]:
            print(f"Both Endpoints Are The Same {mags[0]} and {mags[-1]} Recursion Depth of {max_depth - depth}")
        elif depth == 0:
            print(f"Recursion Depth Exceeded Endpoints are {mags[0]} and {mags[-1]}")
    recursive_helper(freqs, mags, magnitude_splits, max_depth, presplit)
    return magnitude_splits



def convert_to_fourier_basis(folder_dir, color, threshold =0.05, max_depth = 5, presplit = 0, split_list = None):
    color_dict = {"Red":0, "Green":1, "Blue":2, "Gray":3, "Infrared": 4}
    c = color_dict[color]
    freqs, mags = convert_fourier_list(folder_dir, c)
    df = pd.DataFrame(columns=["band", "channel", "magnitude_endpoints","unique_magnitudes", "data"])

    if split_list == None:
        mag_splits = recursive_split(freqs, mags, threshold, max_depth, presplit)
    else:
        mag_splits = split_list
    
    sorted_mag_split = np.sort(mag_splits)
    print(sorted_mag_split)
    prev = 0
    for i in range(len(mag_splits)):
        next_idx = np.argmax(mags>=sorted_mag_split[i])
        next_freqs = np.concatenate([np.real(freqs[prev:next_idx]),np.imag(freqs[prev:next_idx])])
        num_mags = len(np.unique(mags[prev:next_idx]))
        mag_endpoints = (min(mags[prev:next_idx]), max(mags[prev:next_idx]))

        df.loc[len(df.index)] = [i+1, color, mag_endpoints, num_mags, next_freqs]
        prev = next_idx

    return df

def getSplits(minfreq, maxfreq, mult):
    arr = []
    next_freq = minfreq
    while next_freq < maxfreq:
        arr.append(next_freq)
        next_freq *= mult
    return arr
