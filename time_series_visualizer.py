import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=["date"])

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(11,6))
    ax.plot(df.index,df["value"],"r")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019",fontdict={"size":20})
    ax.set_xlabel("Date",fontdict={"size":15})
    ax.set_ylabel("Page Views",fontdict={"size":15})
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month    
    df_bar = df_bar.groupby(["year","month"])["value"].mean().unstack()
    # Draw bar plot
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    fig = df_bar.plot.bar(legend=True,figsize=(13,8)).figure
    plt.legend(title="Months", labels=months, fontsize=13, title_fontsize=13)
    plt.xlabel("Years",fontdict={"size":15})
    plt.ylabel("Average Page Views",fontdict={"size":15})
    plt.title("Monthly Page Views",fontdict={"size":20})

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
    sns.boxplot(data=df_box, x="year", y="value", hue="year", palette="bright", ax=axes[0], legend=False)
    axes[0].set_title("Year-wise Box Plot (Trend)",fontdict={"size":20})
    axes[0].set_xlabel("Year",fontdict={"size":15})
    axes[0].set_ylabel("Page Views",fontdict={"size":15})

    months_box = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="month", y="value", order=months_box, hue="month", palette="husl", ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)",fontdict={"size":20})
    axes[1].set_xlabel("Month",fontdict={"size":15})
    axes[1].set_ylabel("Page Views",fontdict={"size":15})

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
