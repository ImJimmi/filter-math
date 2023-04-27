from numpy import linspace, cos, pi, sin, exp, real, imag, mean
from matplotlib import pyplot
from random import random


def get_phase_range():
    num_cycles = 3
    return linspace(0.0, 2 * pi * num_cycles, 61 * num_cycles)


def plot_z_domain(z, axes: pyplot.Axes, color: str = "black", thickness: float = 1.5):
    x = imag(z)
    y = real(z)
    axes.plot(x, y, color=color, linewidth=thickness)
    axes.plot(mean(x), mean(y), color=color, marker="o", markersize=thickness * 3)


def plot_grid_lines(axes: pyplot.Axes):
    axes.plot([0, 0], [2, -2], color="black", linewidth=0.5, linestyle="--")
    axes.plot([-2, 2], [0, 0], color="black", linewidth=0.5, linestyle="--")


def plot_outline(axes: pyplot.Axes):
    phase = get_phase_range()
    outline = exp(1j * phase)
    plot_z_domain(outline, axes, thickness=3)


def plot_z_sine(axes: pyplot.Axes, frequency: float = 1.0):
    phase = linspace(0.0, 2 * pi, 61)
    z_sine = sin(phase) * exp(1j * phase * frequency)
    plot_z_domain(z_sine, axes, color="red")


def main():
    figure, axes = pyplot.subplots(figsize=(6, 3))

    signal = {
        phase: sin(phase) + sin(2 * phase) / 2 + sin(5 * phase) / 7 + random() * 0.2
        for phase in get_phase_range()
    }
    axes.plot([key / (2 * pi) for key in signal.keys()], signal.values())

    # plot_grid_lines(axes)
    # plot_outline(axes)
    # plot_z_sine(axes)

    # pyplot.xlim([-0.1, 1.1])
    pyplot.ylim([-1.5, 1.5])
    pyplot.show()


if __name__ == "__main__":
    main()
