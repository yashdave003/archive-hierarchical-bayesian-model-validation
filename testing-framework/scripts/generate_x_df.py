from utilities import *

data_dict = pd.read_pickle('../data/Panoptic Agriculture/Transformed Dataset/Panoptic_Data_Dict_Normalized.pickle')
cdfs_name = 'cdfs_100000_0.1-2.9-0.1_0-4-0.2'

with open(f'CDFs/{cdfs_name}.pickle', 'rb') as handle:
    all_cdfs = pickle.load(handle)
all_cdfs_df = pd.DataFrame({'(r,eta),cdf' : all_cdfs.items()})
all_cdfs_df['r'] = pd.Series(all_cdfs_df["(r,eta),cdf"].str[0].str[0])
all_cdfs_df['eta'] = pd.Series(all_cdfs_df["(r,eta),cdf"].str[0].str[1])
all_cdfs_df['cdf'] = pd.Series(all_cdfs_df["(r,eta),cdf"].str[1])

obs_x_dict = dict()
df_dict = dict()

for i, layer in enumerate(np.arange(2, 9)): 
    obs_x = create_obs_x(data_dict, layer)
    obs_x_dict[layer] = np.sort(obs_x)
    df = make_layer_df(obs_x, all_cdfs_df)
    df_dict[layer] = df
    n = obs_x.size
    print(layer, n)

with open(f'panoptic/obs_x_dict.pickle', 'wb') as handle:
    pickle.dump(obs_x_dict, handle)

with open(f'panoptic/layer_df_dict_{cdfs_name}.pickle', 'wb') as handle:
    all_cdfs = pickle.dump(df_dict, handle)
