from utilities import *
data_dict = pd.read_pickle('../data/Panoptic Agriculture/Transformed Dataset/Panoptic_Data_Dict_Normalized.pickle')
obs_x_dict = pd.read_pickle('panoptic/obs_x_dict.pickle')

df_dict = dict()
best_params_df = pd.DataFrame(columns = ['layer', 'num_samples', '(r, eta)', 'kstest_stat', 'kstest_pval'])

for i, layer in enumerate(np.arange(2, 9)): 
    print(layer, "start")
    sample = obs_x_dict[layer]
    layer_cdfs = combine_pickles(f'layer{layer}_10000')
    layer_ksstats, best_param, min_stat = gridsearch(sample, layer_cdfs)
    best_params_df.loc[i, :] = [layer, sample.size, best_param, min_stat, kstwo(n=sample.size).sf(min_stat)]
    
name = 'fine_grid'
if os.path.isfile(f'panoptic/CSVs/best_params_df_{name}.csv'):
    computed_params_df = pd.read_csv(f'panoptic/CSVs/best_params_df_{name}.csv')
    best_params_df = pd.concat([computed_params_df, best_params_df], ignore_index=True, sort=True).set_index('layer')[['num_samples', 'r', 'eta', 'kstest_stat', 'kstest_pval']]
    best_params_df.to_csv(f'panoptic/CSVs/best_params_df_{name}.csv')
else:
    best_params_df.set_index('layer').to_csv(f'panoptic/CSVs/best_params_df_{name}.csv')