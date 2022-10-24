import matplotlib.pyplot as plt
from scipy.stats import probplot


def qq_plot(df):
    fig_qq, axes_qq = plt.subplots(1, 2, figsize=(20,5))
    probplot(df.price,plot=axes_qq[0])
    probplot(df.returns,plot=axes_qq[1])
    axes_qq[0].set_title("Price QQ")
    axes_qq[1].set_title("Returns QQ")
    return fig_qq
