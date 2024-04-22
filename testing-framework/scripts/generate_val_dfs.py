from utilities import *
data_dict = pd.read_pickle('../data/Panoptic Agriculture/Transformed Dataset/Panoptic_Data_Dict_Normalized.pickle')
cdfs_name = 'updated_1000_0.1-4.9_0.0-3.8'
with open(f'pickles/{cdfs_name}.pickle', 'rb') as handle:
    all_cdfs = pickle.load(handle)
all_cdfs_df = pd.DataFrame({'(r,eta),cdf' : all_cdfs.items()})
all_cdfs_df['r'] = pd.Series(all_cdfs_df["(r,eta),cdf"].str[0].str[0])
all_cdfs_df['eta'] = pd.Series(all_cdfs_df["(r,eta),cdf"].str[0].str[1])
all_cdfs_df['cdf'] = pd.Series(all_cdfs_df["(r,eta),cdf"].str[1])


for layer in range(6, 8):
    obs_x = create_obs_x(data_dict, layer)
    df = make_layer_df(obs_x, all_cdfs_df)
    total_samples = obs_x.size
    all_num_samples = np.sort(np.append(5*10**np.arange(3.0, np.floor(np.log10(total_samples))), 10**np.arange(3.0, np.ceil(np.log10(total_samples)))))
    print(list(all_num_samples))
    np.random.seed(42)
    x = obs_x[np.random.permutation(total_samples)]
    val_df = pd.concat([val_df_fixed_num(x, n, all_cdfs_df) for n in all_num_samples])
    val_df.to_csv(f'panoptic/CSVs/val_df{layer}_{cdfs_name}.csv')
    val_df.value_counts(['r', 'eta'])