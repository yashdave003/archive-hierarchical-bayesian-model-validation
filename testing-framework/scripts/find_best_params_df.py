from utilities import *
data_dict = pd.read_pickle('../data/Panoptic Agriculture/Transformed Dataset/Panoptic_Data_Dict_Normalized.pickle')

def combine_pickles(dir_name):
    # Assumed that the dir is in CDFs
    CDFs_DIR = os.path.join(os.getcwd(), "CDFs")
    pickles = os.listdir(os.path.join(CDFs_DIR, dir_name))
    cdfs = dict()
    for pkl in pickles:
        
        pkl_path = os.path.join(CDFs_DIR, f'{dir_name}\\{pkl}')
        with open(pkl_path, 'rb') as handle:
            new_cdf = pickle.load(handle)
            cdfs = cdfs | new_cdf
    with open(f'{os.path.join(CDFs_DIR, f"combined_{dir_name}.pickle")}', 'wb') as handle:
        pickle.dump(cdfs, handle)
    return cdfs

with open(f'panoptic/obs_x_dict.pickle', 'rb') as handle:
    obs_x_dict = pickle.load(handle)

df_dict = dict()
best_params_df = pd.DataFrame(columns = ['layer', 'num_samples', 'r', 'eta', 'kstest_stat', 'kstest_pval'])
# Can take a very long time to run, better to run it in a .py
for i, layer in enumerate(np.arange(3, 7)): 
    all_cdfs = combine_pickles(f'layer{layer}_10000')
    all_cdfs_df = pd.DataFrame({'(r,eta),cdf' : all_cdfs.items()})
    all_cdfs_df['r'] = pd.Series(all_cdfs_df["(r,eta),cdf"].str[0].str[0])
    all_cdfs_df['eta'] = pd.Series(all_cdfs_df["(r,eta),cdf"].str[0].str[1])
    all_cdfs_df['cdf'] = pd.Series(all_cdfs_df["(r,eta),cdf"].str[1])
    obs_x = obs_x_dict[layer]
    df = make_layer_df(obs_x, all_cdfs_df)
    df_dict[layer] = df
    n = obs_x.size
    result = find_best_metric(obs_x, all_cdfs_df)
    best_params_df.loc[i, :] = np.append(np.array([layer, n]), result)
    
name = 'finer_grid'
best_params_df = best_params_df.set_index('layer')
if os.path.isfile(f'panoptic/CSVs/best_params_df_{name}.csv'):
    computed_params_df = pd.read_csv(f'panoptic/CSVs/best_params_df_{name}.csv')
    best_params_df = pd.concat([computed_params_df, best_params_df], ignore_index=True, sort=True).set_index('layer')
    best_params_df.to_csv(f'panoptic/CSVs/best_params_df_{name}.csv')
else:
    best_params_df.to_csv(f'panoptic/CSVs/best_params_df_{name}.csv')