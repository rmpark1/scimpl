import json
import os

import matplotlib.pyplot as plt
import numpy as np

def write_spacing_config(fig, axs, buf):
    fs = tuple(fig.get_size_inches())
    lims = [[ax.get_xlim(), ax.get_ylim()] for ax in axs.flatten()]
    spps = {p: getattr(fig.subplotpars, p) for p in
            ["left", "right", "top", "bottom", "wspace", "hspace"]}
    dat = {"fs": fs, "lims": lims, "spps": spps}
    with open(buf, "w") as f:
        f.write(json.dumps(dat))

def read_spacing_config(fig, axs, buf, lims=True):
    if not os.path.isfile(buf): return
    with open(buf, "r") as f:
        d = json.load(f)
        fig.set_size_inches(d["fs"])
        fig.subplots_adjust(**d["spps"])
        if lims:
            for ax, lims in zip(axs.flatten(), d["lims"]):
                ax.set_xlim(lims[0])
                ax.set_ylim(lims[1])

def set_plot(fig, name, show=True, overwrite=False, lims=True):
    """Use matplotlib GUI editor to format a figure, then save the
    configuration so that new data can be loaded later without restyling
    the figures.

    Args:
        fig (matplotlib.Figure.figure): The figure.
        name (str): A path for the config file.
        show (bool): Whether of not to open the editor.
        overwrite (bool): Overwrite an existing config file.
        lims (bool): Reload limits on figure.
    """
    buf = f"{name}_cfg.json"
    axs = fig.axes
    if isinstance(axs, list): axs = np.array(axs)

    if not overwrite: read_spacing_config(fig, axs, buf, lims)

    if show: plt.show()

    write_spacing_config(fig, axs, buf)
