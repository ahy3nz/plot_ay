"""
plot_ay.py
Some matplotlib defaults and plot customization

Handles the primary functions
"""
import matplotlib as mpl
import matplotlib.pyplot as plt

def setDefaults():
    mpl.rcParams['font.fontsize'] = 18
    mpl.rcParams['axes.labelsize'] = 24
    mpl.rcParams['axes.titlesize'] = 28
    mpl.rcParams['xtick.labelsize'] = 18
    mpl.rcParams['ytick.labelsize'] = 18

def tidyUp(gridArgs, legendArgs):
    """ Umbrella function to tidy up plots

    parameters
    ----------
    gridArgs : grid arguments
    legendArgs: legend arguments
    """
    if legendArgs:
        ayLegend(legendArgs)
    if gridArgs:
        ayGrid(gridArgs)

def ayGrid(gridArgs):
    ax.grid(True, **gridArgs)

def ayLegend(legendArgs):
    ax.legend(**legendArgs)


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
