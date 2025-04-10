# %% setup

#importing modules
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


DPI = 100
FIGSIZE_LARGE = (10, 5)
FIGSIZE_SMALL = (5, 5)

SAMPLE = 1000

CAT_COLS = [
    'airline',
    'flight',
    'source_city',
    'departure_time',
    'stops',
    'arrival_time',
    'destination_city',
    'class',
]

NUM_COLS = [
    'duration',
    'days_left',
    'price',
]

CAT_COLS_SMALL = CAT_COLS.copy()
CAT_COLS_SMALL.remove("flight")


# %% Plot style

import matplotlib as mpl

# Set the figure size and DPI for high resolution
# mpl.rcParams['figure.figsize'] = (10, 6)  # Size in inches
# mpl.rcParams['figure.dpi'] = 300  # High resolution for clarity

# Set the font size for titles and labels
mpl.rcParams['font.size'] = 14
mpl.rcParams['axes.titlesize'] = 16
mpl.rcParams['axes.labelsize'] = 14
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12

# Set the line width and marker size
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.markersize'] = 8

# Use a grid for better readability
mpl.rcParams['axes.grid'] = False
mpl.rcParams['grid.color'] = 'gray'
mpl.rcParams['grid.alpha'] = 0.5

# Set borders and ticks to a grey color
mpl.rcParams['axes.edgecolor'] = 'gray'
mpl.rcParams['xtick.color'] = 'gray'
mpl.rcParams['ytick.color'] = 'gray'

# Set the main plot title color to grey
mpl.rcParams['axes.titlecolor'] = 'gray'

# Set the axis title color to grey
mpl.rcParams['axes.labelcolor'] = 'gray'

# Set the style of the plot
mpl.rcParams['axes.facecolor'] = 'white'  # Background color
mpl.rcParams['savefig.facecolor'] = 'white'  # Background color for saved figures
mpl.rcParams['axes.titleweight'] = 'bold'  # Bold titles for emphasis

# Adjust legend properties
mpl.rcParams['legend.fontsize'] = 12
mpl.rcParams['legend.loc'] = 'best'
mpl.rcParams['legend.frameon'] = False
mpl.rcParams['legend.framealpha'] = 0.8  # Slightly transparent
mpl.rcParams['legend.labelcolor'] = 'gray'  # Set legend font color to gray

# Tight layout to make better use of space
mpl.rcParams['figure.autolayout'] = True

# Use a specific colormap suitable for presentations
mpl.rcParams['image.cmap'] = 'viridis'




# %%
def plot_business_economy_price_hist(data):
    fig, ax = plt.subplots(
        ncols=1,
        nrows=1,
        figsize=FIGSIZE_LARGE,
        dpi=DPI,
    )
    
    sns.histplot(
        data=data,
        x="price",
        hue="class",
        bins=100,
        ax=ax,
    )
    
    return fig
    
# %%
def plot_business_economy_price_bar(data):
    fig, ax = plt.subplots(
        ncols=1,
        nrows=1,
        figsize=FIGSIZE_SMALL,
        dpi=DPI,
    )
    
    # Create the bar plot
    sns.barplot(
        data=data,
        y="price",
        x="class",
        hue="class",
        ax=ax,
        width=0.5,
        dodge=False,
    )
    
    # Remove the y-axis label
    ax.set_ylabel('')
    
    # Set the title
    ax.set_title('Average Price per Class', fontsize=16)
    
    # Remove the top and right borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    #ax.spines['left'].set_visible(False)
    
    return fig
    
# %% main   
if __name__ == "__main__":
    print("load data")
    data = pd.read_csv('data/Clean_Dataset.csv')
    if SAMPLE:
        data = data.sample(SAMPLE)
    
    print("create business economy hist")
    fig = plot_business_economy_price_hist(data)
    fig.savefig("plots/business_economy_price_hist.svg")
    
    print("create business economy bar")
    fig = plot_business_economy_price_bar(data)
    fig.savefig("plots/business_economy_price_bar.svg")