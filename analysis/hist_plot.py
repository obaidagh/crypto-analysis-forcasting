import matplotlib.pyplot as plt


def hist_plot(df,bins=100):
    fig_hist, axes_hist = plt.subplots(1, 2, figsize=(20,5))

    axes_hist[0].hist(df.price,bins=bins)
    axes_hist[1].hist(df.returns,bins=bins)
    axes_hist[0].set_title("Prices Histogram")
    axes_hist[1].set_title("Returns Histogram")
    return fig_hist