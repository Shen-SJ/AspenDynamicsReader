"""
main.py
"""
import AspenDynamicsReader as adr
import pickle


class adplot(adr.ADPlot):
    def user_plot_setting(self, index, ax_obj_list, line):
        self.change_one_ylabel(1, 'I change the D1 y label', ax_obj_list)

    def user_multiplot_setting(self, ax_list, line_group_list):
        # plot setting change
        label_list = ['C1, T13 (C)', 'QR1 (kW)',
                      'C2, T4 (C)', 'QR2 (kW)',
                      'MoleFrac. of AAol', 'MoleFlowrate of AAol (kmole/hr)',
                      'MoleFrac. of Water', 'MoleFlowrate of Water (kmole/hr)',
                      'MoleFlowrate of Solvent (kmole/hr)']
        self.change_all_ylabel(label_list, ax_list)
        self.change_one_set_linestyle(2, '--', ax_list, line_group_list)
        self.change_one_set_linecolor(1, 'b', ax_list, line_group_list)
        self.change_one_set_linecolor(2, 'r', ax_list, line_group_list)


ad = adr.ADConnector()
adp = adplot()

# 從pickle讀取檔案
with open('data_m.pickle', 'rb') as f:
    data1 = pickle.load(f)
    data2 = pickle.load(f)

# 出圖
adp.plot_dynamic_results(data1, save_filename='Dynamic_result1', figure_size=(7, 12))
adp.plot_dynamic_results(ad.set_time0_at(data1, 1), save_filename='Dynamic_result1', figure_size=(7, 12))

adp.multiplot_dynamic_results([data1, data2],
                              save_filename='Dynamic_result2',
                              figure_size=(7.5, 14),
                              set_legend_for_each_data_group=['+20% Thoughtput', '-20% Thoughtput'])
