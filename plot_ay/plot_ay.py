"""
plot_ay.py
Some matplotlib defaults and plot customization

Handles the primary functions
"""
import matplotlib as mpl
#import matplotlib.pyplot as plt

def setDefaults():
    mpl.rcParams['font.size'] = 18
    mpl.rcParams['axes.labelsize'] = 32
    mpl.rcParams['axes.labelweight'] = 'bold'
    mpl.rcParams['axes.titlesize'] = 32
    mpl.rcParams['xtick.labelsize'] = 28
    mpl.rcParams['ytick.labelsize'] = 28
    mpl.rcParams['legend.fontsize'] = 24
    mpl.rcParams['lines.linewidth'] = 3
    mpl.rcParams['lines.markersize'] = 6
    

    mpl.rcParams['legend.framealpha'] = 1
    mpl.rcParams['legend.loc'] = 'best'
    mpl.rcParams['legend.fancybox'] = True

    mpl.rcParams['savefig.transparent'] = True
    mpl.rcParams['savefig.bbox'] = 'tight'
    mpl.rcParams['figure.figsize'] = (10,8)


def tidyUp(fig, ax, gridArgs=None, legendArgs=None, tightLayoutArgs=None):
    """ Umbrella function to tidy up plots

    Parameters
    ----------
    fig : mpl Figure
    ax : mpl Axes
    gridArgs : grid arguments
    legendArgs: legend arguments
    tightLayoutArgs: tight layout arguments

    Notes
    -----
    It might be redundant to have these additional subroutines for legends and grids.
    For now, I'll leave them in there and pass empty (or non-empty) kwargs
    """
    if legendArgs is not None:
        ayLegend(fig, ax, legendArgs)
    if gridArgs is not None:    
        ayGrid(fig, ax, gridArgs)
    if tightLayoutArgs is not None:
        ayTightLayout(fig, ax, tightLayoutArgs)

def ayGrid(fig, ax, gridArgs):
    ax.grid(True, **gridArgs)

def ayLegend(fig, ax, legendArgs):
    ax.legend(**legendArgs)

def ayTightLayout(fig, ax, tightLayoutArgs):
    fig.tight_layout(**tightLayoutArgs)


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
