import matplotlib.pyplot as plt
import numpy as np
import matplotlib.style
import pandas as pd
import seaborn as sns


"""
ヒストグラム（全体を見るとき）
Hist(data=<DF>, column_name=<DFのcolumn>, bins=<bins>, figsize=(<横大きさ,縦大きさ>), step=<区切り>)

"""
class Hist:
    def __init__(self, data, column_name, bins=30, figsize=(10, 10), step=1):
        self.df = pd.DataFrame(data)
        self.column_name = column_name
        self.bins = bins
        self.figsize = figsize
        self.step = step
        self._show_plot()

    def _show_plot(self):
        matplotlib.style.use('bmh')
        plt.figure(figsize=self.figsize)
        target_data = self.df[self.column_name].dropna()
        plt.hist(target_data, bins=self.bins, edgecolor='white')
        plt.xticks(np.arange(int(target_data.min()), int(target_data.max()) + 1, self.step))        
        plt.show()



"""
ヒストグラム ( snsバージョン )
sns_Hist(data=<DF>, x=<横軸>, hue=<基準のcolumn>, figsize=(<横大きさ,縦大きさ>), step=<区切り>)
"""
class sns_Hist:
    def __init__(self, data, x, hue, figsize=(10, 10), step=1):
        self.df = pd.DataFrame(data)
        self.x = x
        self.hue = hue
        self.figsize = figsize
        self.step = step
        self._show_plot()

    def _show_plot(self):
        matplotlib.style.use('bmh')
        plt.figure(figsize=self.figsize)

        plot_df = self.df.dropna(subset=[self.x,
                                         self.hue])
        
        sns.histplot(data=plot_df,
                     x=self.x,
                     hue=self.hue,
                     multiple='stack'
                     )
        min_val = int(plot_df[self.x].min())
        max_val = int(plot_df[self.x].max())
        plt.xticks(np.arange(min_val, max_val + 1, self.step))    
        plt.show()

"""
 KDEプロット(滑らかなヒストグラム)
sns_kde(data=<DF>,
        x=<横軸>,
        hue=<基準のcolumn>,
        fill=<True>,                    #塗りつぶすかどうか
        common_norm=<False>,　　　　　　 #よくわからん 
        figsize=(<横大きさ,縦大きさ>),
        step=<区切り>)


"""


class sns_kde:
    def __init__(self, data, x, hue, fill=True, common_norm=False, figsize=(10, 10), step=1):
        self.df = pd.DataFrame(data)
        self.x = x
        self.hue = hue
        self.fill = fill
        self.common_norm = common_norm
        self.figsize = figsize
        self.step = step
        self._show_plot()

    def _show_plot(self):
        matplotlib.style.use('bmh')
        plt.figure(figsize=self.figsize)

        plot_df = self.df.dropna(subset=[self.x,
                                         self.hue])
        
        sns.kdeplot(data=plot_df,
                    x=self.x,
                    hue=self.hue,
                    fill=self.fill,
                    common_norm=self.common_norm
                     )
        min_val = int(plot_df[self.x].min())
        max_val = int(plot_df[self.x].max())
        plt.xticks(np.arange(min_val, max_val + 1, self.step))    
        plt.show()