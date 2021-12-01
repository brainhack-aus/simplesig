import numpy as np
from scipy import signal
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')
hv.renderer('bokeh').theme = 'dark_minimal'


def create_signal(duration, fs, times, widths, frequencies, amplitudes):
    """Create a test signal of gaussian-modulated sinusoids

    Args:
        duration (float): duration of signal (seconds)
        fs (float): sampling frequency of signal (Hz)
        times (list of float): list of times (in secs) at which
            frequency pulses are centred
        widths (list of float): list of pulse widths (in time) around
            the central times specified by "times"
        frequencies (list of float): list of pulse frequencies to
            correspond with times and widths
        amplitudes (list of float): list of pulse amplitudes to
            correspond with other pulse properties. 
    
    Returns:
        signal (np.array of float): numpy array containing output signal 
        t (np.array of float): array of times corresponding to output signal
    """
    t = np.arange(0, duration, 1/fs)  

    pulses = [signal.gausspulse(t-pt, fc=f, bw=1/(f * w / 2)) * amp
              for pt, w, f, amp in zip(times, widths, frequencies, amplitudes)]
    return np.stack(pulses).sum(axis=0)


def plot_spectrogram(trace, fs):
    """Create a test signal of gaussian-modulated sinusoids

    Args:
        trace (np.array of float): numpy array containing signal
        fs (float): sampling frequency (Hz)

    Returns:
        plot (hv.Plot): Holoviews spectrogram and frequency-power plot
    """
    power_dim = hv.Dimension('power', label='Power', unit='V^2/Hz')
    time_dim = hv.Dimension('time', label='Time', unit='s')
    freq_dim = hv.Dimension('freq', label='Frequency', unit='Hz')
    freqs, psd = signal.welch(trace, fs=fs, nperseg=fs*5, scaling='density')
    f, t, spec = signal.spectrogram(trace, fs, nperseg=fs, scaling='density')
    plot_opts = (
        opts.Curve(frame_width=100, frame_height=400, xticks=3, yaxis=None,
                   ylim=(1, 50)),
        opts.QuadMesh(frame_width=600, frame_height=400, ylim=(1, 50),
                      cmap='plasma')
    )
    plots = (hv.QuadMesh((t, f, spec), kdims=[time_dim, freq_dim]) +
             hv.Curve((np.sqrt(psd), freqs), power_dim, freq_dim))
    return plots.opts(*plot_opts)
