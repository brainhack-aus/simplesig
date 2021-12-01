import sys
import numpy as np
import holoviews as hv
from .analyse import plot_spectrogram


def command_plot_spectrogram(infile, outfile):
    """Load data, create and save spectrogram.

    Args:
        infile (str):  input filename
        outfile (str): output filename
    """
    trace = np.load(infile)
    plot = plot_spectrogram(trace, 1024)
    hv.save(plot, outfile, format='html')


def main():
    command_plot_spectrogram(sys.argv[1], sys.argv[2])