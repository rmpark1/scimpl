from matplotlib.widgets import Slider

def set_font(fig, val):
    for ax in fig.axes:
        xlab = ax.get_xlabel()
        ylab = ax.get_ylabel()
        ax.set_xlabel(xlab, fontsize=val)
        ax.set_ylabel(ylab, fontsize=val)

    fig.canvas.draw_idle()

def set_ticklabel(fig, val):
    for ax in fig.axes:
        ticks = ax.xaxis.get_major_ticks() + ax.yaxis.get_major_ticks()
        for tick in ticks: tick.label.set_fontsize(val)
    fig.canvas.draw_idle()

def set_legend(fig, val):
    for ax in fig.axes:
        ax.legend(fontsize=val)
    fig.legend(fontsize=val)
    fig.canvas.draw_idle()


fig, axs = plt.subplots(2, 3)
for ax in axs.flatten():
    ax.plot([0, 1], [0, 1], label="hello")
    ax.set_xlabel("Hello")
    ax.set_ylabel("Hello")
    ax.legend()
fig.legend()

conf_fig = plt.figure()
vars = {
    "font size": ([1, 12, 25], set_font),
    "legend font size": ([1, 12, 25], set_legend),
    "tick label fontsize": ([1, 12, 25], set_ticklabel),
}

def cb_wrap(callback, fig, val):
    return callback(fig, val)

sliders = []

slider_params={}
for i, (name, (vals, callback)) in enumerate(vars.items()):
    bar = conf_fig.add_axes([.25, (.90 - .1*(i+1)), 0.65, 0.03])
    print(callback.__name__)
    slider = Slider(
        ax=bar,
        label=name,
        valmin=vals[0],
        valmax=vals[2],
        valinit=vals[1],
        orientation="horizontal",
        **slider_params,
    )
    def cb(val): return copy.deepcopy(callback)(fig, val)
    slider.on_changed(cb)
    sliders.append(slider)

plt.show()
