import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def acf_pacf_plot(df_column1,name,lags=50):
    fig_acf, axes_ret_acf = plt.subplots(1, 2, sharex=True,figsize=(20,5))

    plot_acf(df_column1,lags=lags,zero=False,ax=axes_ret_acf[0],auto_ylims=True)
    plot_pacf(df_column1,lags=lags,zero=False,ax=axes_ret_acf[1],method='ols',auto_ylims=True)
    axes_ret_acf[0].set_title(f"{name} AutoCorelation")
    axes_ret_acf[1].set_title(f"{name} Partial Autocorrelation")
    return fig_acf