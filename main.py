"""
main.py
> You can use AspenDynamicsReader by Import method, but I think it's non-sense.
"""
import AspenDynamicsReader as adr
import pickle
import itertools

# 從pickle讀取檔案
with open('data_m.pickle', 'rb') as f:
    data1 = pickle.load(f)
    data2 = pickle.load(f)


# 改變圖片細節設定後出圖
def user_multiplot_setting(ax_list, line_group_list):
    """客製化特定圖形的細節參數，需要自己寫一些程式碼就是，好像有點爛
    """
    pass

    # plot setting change
    lebal_list = ['C1, T13 (C)', 'QR1 (kW)',
                  'C2, T4 (C)', 'QR2 (kW)',
                  'MoleFrac. of AAol', 'MoleFlowrate of AAol (kmole/hr)',
                  'MoleFrac. of Water', 'MoleFlowrate of Water (kmole/hr)',
                  'MoleFlowrate of Solvent (kmole/hr)']
    for ax_index, label in itertools.zip_longest(range(len(ax_list)), lebal_list):
        ax_list[ax_index].set_ylabel(label)

    # line setting change
    for i in range(len(ax_list)):
        line_group_list[i][1].set_linestyle('--')
        line_group_list[i][1].set_color('r')


# 把預設的圖設定用自定義的圖設定覆蓋掉
adr.user_multiplot_setting = user_multiplot_setting

# 出圖
adr.multiplot_dynamic_results([data1, data2],
                              save_filename='Dynamic_result2',
                              figure_size=(7.5, 14),
                              set_legend_for_each_data_group=['+20% Thoughtput', '-20% Thoughtput'])
