import plotly.express as px



import pandas as pd

import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

parties = [
    [3,3,5,3,2,4,5,5], #blue and white 0
    [3, 3, 4, 3, 4, 4, 5, 5], #likud 1
    [2, 3, 3, 2, 5, 2, 4, 3], # labour 2 
    [2, 2, 2, 2, 2, 2, 3, 5], #meretz 3
    [3, 4, 2, 4, 3, 5, 3, 4], # Bible jewishness 4
    [1, 1, 1, 1.75, 4, 1, 2, 1], #The joint list 5
    [5, 5, 2, 2, 4, 5, 4, 4], # Sh"s 6
    [5, 5, 1, 1.75, 4, 1, 3, 2], #raam 7
    [3, 3, 5, 3, 4, 3, 4, 4] ]# our home israel 8 







def radar_factory(num_vars, frame='circle'):
    """
    Create a radar chart with `num_vars` axes.

    This function creates a RadarAxes projection and registers it.

    Parameters
    ----------
    num_vars : int
        Number of variables for radar chart.
    frame : {'circle', 'polygon'}
        Shape of frame surrounding axes.

    """
    # calculate evenly-spaced axis angles
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)

    class RadarAxes(PolarAxes):

        name = 'radar'
        # use 1 line segment to connect specified points
        RESOLUTION = 1

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # rotate plot such that the first axis is at the top
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            """Override fill so that line is closed by default"""
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.append(x, x[0])
                y = np.append(y, y[0])
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            # The Axes patch must be centered at (0.5, 0.5) and of radius 0.5
            # in axes coordinates.
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_vars,
                                      radius=.5, edgecolor="k")
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                # spine_type must be 'left'/'right'/'top'/'bottom'/'circle'.
                spine = Spine(axes=self,
                              spine_type='circle',
                              path=Path.unit_regular_polygon(num_vars))
                # unit_regular_polygon gives a polygon of radius 1 centered at
                # (0, 0) but we want a polygon of radius 0.5 centered at (0.5,
                # 0.5) in axes coordinates.
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5)
                                    + self.transAxes)
                return {'polar': spine}
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta


def example_data():
    # The following data is from the Denver Aerosol Sources and Health study.
    # See doi:10.1016/j.atmosenv.2008.12.017
    #
    # The data are pollution source profile estimates for five modeled
    # pollution sources (e.g., cars, wood-burning, etc) that emit 7-9 chemical
    # species. The radar charts are experimented with here to see if we can
    # nicely visualize how the modeled source profiles change across four
    # scenarios:
    #  1) No gas-phase species present, just seven particulate counts on
    #     Sulfate
    #     Nitrate
    #     Elemental Carbon (EC)
    #     Organic Carbon fraction 1 (OC)
    #     Organic Carbon fraction 2 (OC2)
    #     Organic Carbon fraction 3 (OC3)
    #     Pyrolized Organic Carbon (OP)
    #  2)Inclusion of gas-phase specie carbon monoxide (CO)
    #  3)Inclusion of gas-phase specie ozone (O3).
    #  4)Inclusion of both gas-phase species is present...

    parties1 = [
    [5.0, 2.0, 5.0, 5.0, 3.0, 3.0, 3.5, 3.0, 2.0, 3.0, 3.0, 4.0, 5.0, 4.0],#1
    [5.0, 3.0, 5.0, 4.0, 2.0, 4.0, 3.0, 5.0, 1.0, 5.0, 5.0, 5.0, 5.0, 5.0], #2
    [5.0, 1.5, 5.0, 4.0, 2.0, 2.0, 4.0, 5.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0],#3
    [5.0, 1.5, 5.0, 3.0, 3.0, 2.0, 4.0, 5.0, 2.0, 3.0, 1.0, 1.0, 2.0, 1.0],#4
    [5.0, 1.0, 5.0, 3.0, 3.0, 3.0, 4.0, 5.0, 2.0, 5.0, 5.0, 4.0, 5.0, 4.0],#5
    [1.0, 5.0, 1.0, 1.0, 3.0, 2.0, 4.0, 2.0, 5.0, 3.0, 3.0, 3.0, 1.0, 2.0],#6
    [5.0, 1.0, 5.0, 2.0, 3.0, 3.0, 4.0, 5.0, 2.0, 5.0, 5.0, 4.0, 4.0, 4.0],#7
    [1.0, 2.0, 1.0, 1.0, 3.0, 3.0, 3.0, 1.0, 5.0, 3.0, 3.0, 3.0, 2.0, 3.0], #8
    [5.0, 5.0, 4.0, 4.0, 3.0, 2.0, 1.0, 5.0, 1.0, 1.0, 1.0, 5.0, 4.0, 4.0], #9
    [5.0, 4.0, 4.0, 2.0, 5.0, 2.0, 4.0, 3.0, 2.0, 2.0, 2.0, 5.0, 4.0, 5.0], #10
    [5.0, 2.0, 4.0, 3.0, 3.0, 4.0, 2.0, 4.0, 2.0, 4.0, 5.0, 2.0, 2.0, 2.0]]#11
    """ data = [
        ['1', '2', '3 ', '4', '5', '6', '7', '8', '8', '10', '11', '12', '13', '14'],
        ('Blue and White', [[5.0, 2.0, 5.0, 5.0, 3.0, 3.0, 3.5, 3.0, 2.0, 3.0, 3.0, 4.0, 5.0, 4.0]]),
        ('Likud', [[5.0, 3.0, 5.0, 4.0, 2.0, 4.0, 3.0, 5.0, 1.0, 5.0, 5.0, 5.0, 5.0, 5.0]]),
        ('Labour', [[5.0, 1.5, 5.0, 4.0, 2.0, 2.0, 4.0, 5.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0]]),
        ('Meretz', [[5.0, 1.5, 5.0, 3.0, 3.0, 2.0, 4.0, 5.0, 2.0, 3.0, 1.0, 1.0, 2.0, 1.0]]),
        ('Bible Judiasim', [[5.0, 1.0, 5.0, 3.0, 3.0, 3.0, 4.0, 5.0, 2.0, 5.0, 5.0, 4.0, 5.0, 4.0]]),
        ('The Joint List', [[1.0, 5.0, 1.0, 1.0, 3.0, 2.0, 4.0, 2.0, 5.0, 3.0, 3.0, 3.0, 1.0, 2.0]]),
        ('Shas', [[5.0, 1.0, 5.0, 2.0, 3.0, 3.0, 4.0, 5.0, 2.0, 5.0, 5.0, 4.0, 4.0, 4.0]]),
        ("Ra'm", [[1.0, 2.0, 1.0, 1.0, 3.0, 3.0, 3.0, 1.0, 5.0, 3.0, 3.0, 3.0, 2.0, 3.0]]),
        ("Our Home Israel", [[5.0, 2.0, 4.0, 3.0, 3.0, 4.0, 2.0, 4.0, 2.0, 4.0, 5.0, 2.0, 2.0, 2.0]]),
        ("There's A Future", [[5.0, 4.0, 4.0, 2.0, 5.0, 2.0, 4.0, 3.0, 2.0, 2.0, 2.0, 5.0, 4.0, 5.0]]),
        ("The New Right", [[5.0, 2.0, 4.0, 3.0, 3.0, 4.0, 2.0, 4.0, 2.0, 4.0, 5.0, 2.0, 2.0, 2.0]]),
        ("Person #5", [[5.0, 5.0, 5.0, 5.0, 4.0, 1.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0]]),

    ] """

    data = [
        ['1', '2', '3 ', '4', '5', '6', '7', '8', '8', '10', '11', '12', '13', '14'],
        ('Person #6', [[5.0, 2.0, 4.0, 5.0, 3.0, 3.0, 2.0, 4.0, 2.0, 2.0, 1.0, 4.0, 2.0, 4.0]]),
        ('Labour - Should Have Voted', [[5.0, 1.5, 5.0, 4.0, 2.0, 2.0, 4.0, 5.0, 2.0, 3.0, 1.0, 3.0, 2.0, 3.0]]),
        ("There's A Future - Voted", [[5.0, 4.0, 4.0, 2.0, 5.0, 2.0, 4.0, 3.0, 2.0, 2.0, 2.0, 5.0, 4.0, 5.0]])

    ]
    return data


if __name__ == '__main__':
    N = 14
    theta = radar_factory(N, frame='polygon')

    data = example_data()
    spoke_labels = data.pop(0)

    fig, axs = plt.subplots(figsize=(15, 5), nrows=1, ncols=3,
                            subplot_kw=dict(projection='radar'))
    fig.subplots_adjust(wspace=1, hspace=0.5, top=0.85, bottom=0.05)


    colors = ['b', 'r', 'g', 'm', 'y']
    # Plot the four cases from the example data on separate axes
    for ax, (title, case_data) in zip(axs.flat, data):
        #ax.set_rgrids([1,2,3,4,5])
        ax.set_title(title, weight='normal', size='large', position=(0.5, 1.1),
                     horizontalalignment='center', verticalalignment='center')
        for d, color in zip(case_data, colors):
            ax.plot(theta, d, color=color)
            ax.fill(theta, d, facecolor=color, alpha=0.25)
        ax.set_varlabels(spoke_labels)

    labels = ('1.Jewish Nation', '2.Church & State', '3.National Home ', '4.Military Actions',
     '5.Diplomatic Actions', '6.State & Economy', '7.Social & Economic Equality', '8.Jewish Alliya',
      '9.Return PA Refugees', '10.Orthodox Convertion', '11.Orthodoxy&who is Jewish', '12.Party Leader', 
      '13.In Goverment', '14.Party Leader ID')
    legend = fig.legend(labels, loc="upper left",
                              labelspacing=0.1, fontsize='large')

    

    plt.show()


