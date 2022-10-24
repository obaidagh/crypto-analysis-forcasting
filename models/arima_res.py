import plotly.express as px
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf


def arima_res(model):

    reisuals=model.resid

    d_fuller_result=adfuller(reisuals)

    acf_fig=plot_acf(reisuals,zero=False,auto_ylims=True)
    line_fig=px.line(x=reisuals.index.to_timestamp(),y=reisuals.T)

    print('_______________________')
    print('Residuals  Mean: %f' % reisuals.mean())
    print('Residuals Std: %f' % reisuals.std())
    print('_______________________')
    print('ADF Statistic: %f' % d_fuller_result[0])
    print('p-value: %f' % d_fuller_result[1])
    print('_______________________')

    return acf_fig,line_fig