from utilities import *
data_dict = pd.read_pickle('../data/Panoptic Agriculture/Transformed Dataset/Panoptic_Data_Dict_Normalized.pickle')
cdfs_name = 'cdfs_100000_0.1-2.9-0.1_0-4-0.2'
with open(f'CDFs/{cdfs_name}.pickle', 'rb') as handle:
    all_cdfs = pickle.load(handle)
with open(f'CDFs/cdfs_100000_3.0-7-0.4_0.1-4-0.2.pickle', 'rb') as handle:
    other_cdfs = pickle.load(handle)
all_cdfs = all_cdfs | other_cdfs
all_cdfs_df = pd.DataFrame({'(r,eta),cdf' : all_cdfs.items()})
all_cdfs_df['r'] = pd.Series(all_cdfs_df["(r,eta),cdf"].str[0].str[0])
all_cdfs_df['eta'] = pd.Series(all_cdfs_df["(r,eta),cdf"].str[0].str[1])
all_cdfs_df['cdf'] = pd.Series(all_cdfs_df["(r,eta),cdf"].str[1])

obs_x_dict = dict()
df_dict = dict()
best_params_df = pd.DataFrame(columns = ['layer', 'num_samples', 'r', 'eta', 'kstest_stat', 'kstest_pval'])
# Can take a very long time to run, better to run it in a .py
for i, layer in enumerate(np.arange(7, 9)): 
    obs_x = create_obs_x(data_dict, layer)
    obs_x_dict[layer] = obs_x
    df = make_layer_df(obs_x, all_cdfs_df)
    df_dict[layer] = df
    n = obs_x.size
    result = find_best_metric(obs_x, all_cdfs_df)
    best_params_df.loc[i, :] = np.append(np.array([layer, n]), result)
    
best_params_df = best_params_df.set_index('layer')
if os.path.isfile(f'panoptic/CSVs/best_params_df_{cdfs_name}.csv'):
    computed_params_df = pd.read_csv(f'panoptic/CSVs/best_params_df_{cdfs_name}.csv')
    best_params_df = pd.concat([computed_params_df, best_params_df], ignore_index=True, sort=True)
    best_params_df.to_csv(f'panoptic/CSVs/best_params_df_{cdfs_name}.csv')
else:
    best_params_df.to_csv(f'panoptic/CSVs/best_params_df_{cdfs_name}.csv')