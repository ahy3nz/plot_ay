"""
Unit and regression test for the plot_ay package.
"""

# Import package, test suite, and other packages as needed
import plot_ay
import pytest
import sys

import numpy as np


def test_plot_ay_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "plot_ay" in sys.modules

def test_defaults():
    plot_ay.setDefaults()

def test_canvas():
    plot_ay.canvas(with_attribution=True)

def test_grid():
    import matplotlib
    matplotlib.use('agg')
    import matplotlib.pyplot as plt

    x_data = np.arange(0,10)
    linear = (5 * x_data) + 2
    quadratic = x_data**2

    fig, ax = plt.subplots(1,1)
    ax.plot(x_data, linear, label='linear')
    ax.plot(x_data, quadratic, label='quadratic')
    gridArgs = {}
    gridArgs['color'] = 'r'
    gridArgs['linestyle'] = '--'
    gridArgs['linewidth'] = 5
    ax.set_xlabel("x")
    plot_ay.tidyUp(fig, ax, gridArgs=gridArgs)
    plt.close(fig)

def test_legend():
    import matplotlib
    matplotlib.use('agg')
    import matplotlib.pyplot as plt

    x_data = np.arange(0,10)
    linear = (5 * x_data) + 2
    quadratic = x_data**2

    fig, ax = plt.subplots(1,1)
    ax.plot(x_data, linear, label='linear')
    ax.plot(x_data, quadratic, label='quadratic')
    legendArgs = {} 
    legendArgs['loc'] = 1
    legendArgs['fancybox'] = True
    legendArgs['ncol'] = 2
    legendArgs['edgecolor'] = 'black'
    ax.set_xlabel("x")
    plot_ay.tidyUp(fig, ax, legendArgs=legendArgs)
    plt.close(fig)

def test_tightlayout():
    import matplotlib
    matplotlib.use('agg')
    import matplotlib.pyplot as plt

    x_data = np.arange(0,10)
    linear = (5 * x_data) + 2
    quadratic = x_data**2

    fig, ax = plt.subplots(1,2)
    ax[0].plot(x_data, linear, label='linear')
    ax[0].plot(x_data, quadratic, label='quadratic')
    ax[1].plot(x_data, linear, label='linear')
    ax[1].plot(x_data, quadratic, label='quadratic')

    tightLayoutArgs = {} 
    tightLayoutArgs['pad'] = 0.2
    tightLayoutArgs['w_pad'] = 10
    tightLayoutArgs['h_pad'] = 2
    plot_ay.tidyUp(fig, ax[0], tightLayoutArgs=tightLayoutArgs)
    plot_ay.tidyUp(fig, ax[1], tightLayoutArgs=tightLayoutArgs)
    plt.close(fig)

