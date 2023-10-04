import matplotlib as mpl
# The default backend; one of GTK GTKAgg GTKCairo GTK3Agg GTK3Cairo
# MacOSX Qt4Agg Qt5Agg TkAgg WX WXAgg Agg Cairo GDK PS PDF SVG
# Template.
# You can also deploy your own backend outside of matplotlib by
# referring to the module name (which must be in the PYTHONPATH) as
# 'module://my_backend'.
#
# If you omit this parameter, it will always default to "Agg", which is a
# non-interactive backend.
#backend      : qt5agg
# Note that this can be overridden by the environment variable
# QT_API used by Enthought Tool Suite (ETS); valid values are
# "pyqt" and "pyside".  The "pyqt" setting has the side effect of
# forcing the use of Version 2 API for QString and QVariant.

# The port to use for the web server in the WebAgg backend.
# webagg.port : 8888

# The address on which the WebAgg web server should be reachable
# webagg.address : 127.0.0.1

# If webagg.port is unavailable, a number of other random ports will
# be tried until one that is available is found.
# webagg.port_retries : 50

# When True, open the webbrowser to the plot that is shown
# webagg.open_in_browser : True

# if you are running pyplot inside a GUI and your backend choice
# conflicts, we will automatically try to find a compatible one for
# you if backend_fallback is True
#backend_fallback: True

#interactive  : False
#toolbar      : toolbar2   # None | toolbar2  ("classic" is deprecated)
#timezone     : UTC        # a pytz timezone string, e.g., US/Central or Europe/Paris

# Where your matplotlib data lives if you installed to a non-default
# location.  This is where the matplotlib fonts, bitmaps, etc reside
#datapath : /home/jdhunter/mpldata

# See http://matplotlib.org/api/artist_api.html#module-matplotlib.lines for more
# information on line properties.
mpl.rcParams["lines.linewidth"] =  2.0     # line width in points
mpl.rcParams["lines.linestyle"] = "-"       # solid line
mpl.rcParams["lines.color"] = "C0"      # has no affect on plot(); see axes.prop_cycle
mpl.rcParams["lines.marker"] = "None"    # the default marker
mpl.rcParams["lines.markeredgewidth"] =  1.0     # the line width around the marker symbol
mpl.rcParams["lines.markersize"] =  12            # markersize, in points
mpl.rcParams["lines.dash_joinstyle"] = "miter"        # miter|round|bevel
mpl.rcParams["lines.dash_capstyle"] = "butt"          # butt|round|projecting
mpl.rcParams["lines.solid_joinstyle"] = "miter"       # miter|round|bevel
mpl.rcParams["lines.solid_capstyle"] = "projecting"   # butt|round|projecting
mpl.rcParams["lines.antialiased"] = True         # render lines in antialiased (no jaggies)

# The three standard dash patterns.  These are scaled by the linewidth.
mpl.rcParams["lines.dashed_pattern"] = [2.8, 1.2]
mpl.rcParams["lines.dashdot_pattern"] = [4.8, 1.2, 0.8, 1.2]
mpl.rcParams["lines.dotted_pattern"] = [1.1, 1.1]
mpl.rcParams["lines.scale_dashes"] = True

mpl.rcParams["markers.fillstyle"] =  "full" # full|left|right|bottom|top|none


mpl.rcParams["hatch.color"] =  'k'
mpl.rcParams["hatch.linewidth"] = 1.0


### Boxplot
#boxplot.notch       : False
#boxplot.vertical    : True
#boxplot.whiskers    : 1.5
#boxplot.bootstrap   : None
#boxplot.patchartist : False
#boxplot.showmeans   : False
#boxplot.showcaps    : True
#boxplot.showbox     : True
#boxplot.showfliers  : True
#boxplot.meanline    : False

#boxplot.flierprops.color           : 'k'
#boxplot.flierprops.marker          : 'o'
#boxplot.flierprops.markerfacecolor : 'none'
#boxplot.flierprops.markeredgecolor : 'k'
#boxplot.flierprops.markersize      : 6
#boxplot.flierprops.linestyle       : 'none'
#boxplot.flierprops.linewidth       : 1.0

#boxplot.boxprops.color     : 'k'
#boxplot.boxprops.linewidth : 1.0
#boxplot.boxprops.linestyle : '-'

#boxplot.whiskerprops.color     : 'k'
#boxplot.whiskerprops.linewidth : 1.0
#boxplot.whiskerprops.linestyle : '-'

#boxplot.capprops.color     : 'k'
#boxplot.capprops.linewidth : 1.0
#boxplot.capprops.linestyle : '-'

#boxplot.medianprops.color     : 'C1'
#boxplot.medianprops.linewidth : 1.0
#boxplot.medianprops.linestyle : '-'

#boxplot.meanprops.color           : 'C2'
#boxplot.meanprops.marker          : '^'
#boxplot.meanprops.markerfacecolor : 'C2'
#boxplot.meanprops.markeredgecolor : 'C2'
#boxplot.meanprops.markersize      :  6
#boxplot.meanprops.linestyle       : 'none'
#boxplot.meanprops.linewidth       : 1.0


mpl.rcParams["font.family"] =  "DejaVu Sans" 
mpl.rcParams["font.serif"] =  "cm10"
mpl.rcParams["font.size"] = 24.0
mpl.rcParams["font.style"] = "normal"
mpl.rcParams["font.variant"] =  "normal"
mpl.rcParams["font.weight"] =  "bold"
mpl.rcParams["font.stretch"] =  "normal"


mpl.rcParams["text.color"] = "black"

### LaTeX customizations. See http://wiki.scipy.org/Cookbook/Matplotlib/UsingTex
mpl.rcParams["text.usetex"] = True  # use latex for all text handling. The following fonts
                              # are supported through the usual rc parameter settings:
                              # new century schoolbook, bookman, times, palatino,
                              # zapf chancery, charter, serif, sans-serif, helvetica,
                              # avant garde, courier, monospace, computer modern roman,
                              # computer modern sans serif, computer modern typewriter
                              # If another font is desired which can loaded using the
                              # LaTeX \usepackage command, please inquire at the
                              # matplotlib mailing list
mpl.rcParams["text.latex.preamble"] = r'\usepackage{siunitx} \usepackage{amsmath} \boldmath'
# IMPROPER USE OF THIS FEATURE WILL LEAD TO LATEX FAILURES
                            # AND IS THEREFORE UNSUPPORTED. PLEASE DO NOT ASK FOR HELP
                            # IF THIS FEATURE DOES NOT DO WHAT YOU EXPECT IT TO.
                            # preamble is a comma separated list of LaTeX statements
                            # that are included in the LaTeX document preamble.
                            # An example:
                            # text.latex.preamble : \usepackage{bm},\usepackage{euler}
                            # The following packages are always loaded with usetex, so
                            # beware of package collisions: color, geometry, graphicx,
                            # type1cm, textcomp. Adobe Postscript (PSSNFS) font packages
                            # may also be loaded, depending on your font settings
#text.hinting : auto   # May be one of the following:
                       #   'none': Perform no hinting
                       #   'auto': Use FreeType's autohinter
                       #   'native': Use the hinting information in the
                       #             font file, if available, and if your
                       #             FreeType library supports it
                       #   'either': Use the native hinting information,
                       #             or the autohinter if none is available.
                       # For backward compatibility, this value may also be
                       # True === 'auto' or False === 'none'.
#text.hinting_factor : 8 # Specifies the amount of softness for hinting in the
                         # horizontal direction.  A value of 1 will hint to full
                         # pixels.  A value of 2 will hint to half pixels etc.

#text.antialiased : True # If True (default), the text will be antialiased.
                         # This only affects the Agg backend.

# The following settings allow you to select the fonts in math mode.
# They map from a TeX font name to a fontconfig font pattern.
# These settings are only used if mathtext.fontset is 'custom'.
# Note that this "custom" mode is unsupported and may go away in the
# future.
#mathtext.cal : cursive
#mathtext.rm  : serif
#mathtext.tt  : monospace
#mathtext.it  : serif:italic
#mathtext.bf  : serif:bold
#mathtext.sf  : sans
mpl.rcParams["mathtext.fontset"] = "stixsans" # Should be 'dejavusans' (default),
                               # 'dejavuserif', 'cm' (Computer Modern), 'stix',
                               # 'stixsans' or 'custom'
#mathtext.fallback_to_cm : True  # When True, use symbols from the Computer Modern
                                 # fonts when a symbol can not be found in one of
                                 # the custom math fonts.

#mathtext.default : it # The default font to use for math.
                       # Can be any of the LaTeX font names, including
                       # the special name "regular" for the same font
                       # used in regular text.



# default face and edge color, default tick sizes,
# default fontsizes for ticklabels, and so on.  See
# http://matplotlib.org/api/axes_api.html#module-matplotlib.axes
#axes.facecolor      : white   # axes background color
#axes.edgecolor      : black   # axes edge color
mpl.rcParams["axes.linewidth"] =  3.0     # edge linewidth
mpl.rcParams["axes.grid"] = True   # display grid or not
mpl.rcParams["axes.titlesize"] =  "large"   # fontsize of the axes title
mpl.rcParams["axes.titlepad"] = 16.0     # pad between axes and title in points
mpl.rcParams["axes.labelsize"] =  "medium" # fontsize of the x any y labels
mpl.rcParams["axes.labelpad"] =  4.0     # space between label and axis
mpl.rcParams["axes.labelweight"] = "bold"  # weight of the x and y labels
mpl.rcParams["axes.labelcolor"] = "black"
mpl.rcParams["axes.axisbelow"] = True  # draw axis gridlines and ticks below
                               # patches (True); above patches but below
                               # lines ('line'); or above all (False)

#axes.formatter.limits : -7, 7 # use scientific notation if log10
                               # of the axis range is smaller than the
                               # first or larger than the second
#axes.formatter.use_locale : False # When True, format tick labels
                                   # according to the user's locale.
                                   # For example, use ',' as a decimal
                                   # separator in the fr_FR locale.
#axes.formatter.use_mathtext : False # When True, use mathtext for scientific
                                     # notation.
#axes.formatter.min_exponent: 0 # minimum exponent to format in scientific notation
#axes.formatter.useoffset      : True    # If True, the tick label formatter
                                         # will default to labeling ticks relative
                                         # to an offset when the data range is
                                         # small compared to the minimum absolute
                                         # value of the data.
#axes.formatter.offset_threshold : 4     # When useoffset is True, the offset
                                         # will be used when it can remove
                                         # at least this number of significant
                                         # digits from tick labels.

mpl.rcParams["axes.spines.left"] = True   # display axis spines
mpl.rcParams["axes.spines.bottom"] = True
mpl.rcParams["axes.spines.top"] = True
mpl.rcParams["axes.spines.right"] = True

mpl.rcParams["axes.unicode_minus"] =  True    # use unicode for the minus symbol
                               # rather than hyphen.  See
                               # http://en.wikipedia.org/wiki/Plus_and_minus_signs#Character_codes
# axes.prop_cycle    : cycler('color', ['1f77b4', 'ff7f0e', '2ca02c', 'd62728', '9467bd', '8c564b', 'e377c2', '7f7f7f', 'bcbd22', '17becf'])
                      # color cycle for plot lines  as list of string
                      # colorspecs: single letter, long name, or web-style hex
mpl.rcParams["axes.autolimit_mode"] = "data" # How to scale axes limits to the data.
                            # Use "data" to use data limits, plus some margin
                            # Use "round_number" move to the nearest "round" number
#axes.xmargin        : .0  # x margin.  See `axes.Axes.margins`
#axes.ymargin        : .0  # y margin See `axes.Axes.margins`

mpl.rcParams["polaraxes.grid"] = True    # display grid on polar axes
mpl.rcParams["axes3d.grid"] = True    # display grid on 3d axes



# These control the default format strings used in AutoDateFormatter.
# Any valid format datetime format string can be used (see the python
# `datetime` for details).  For example using '%%x' will use the locale date representation
# '%%X' will use the locale time representation and '%%c' will use the full locale datetime
# representation.
# These values map to the scales:
#    {'year': 365, 'month': 30, 'day': 1, 'hour': 1/24, 'minute': 1 / (24 * 60)}

# date.autoformatter.year     : %Y
# date.autoformatter.month    : %Y-%m
# date.autoformatter.day      : %Y-%m-%d
# date.autoformatter.hour     : %m-%d %H
# date.autoformatter.minute   : %d %H:%M
# date.autoformatter.second   : %H:%M:%S
# date.autoformatter.microsecond   : %M:%S.%f


# see http://matplotlib.org/api/axis_api.html#matplotlib.axis.Tick
mpl.rcParams["xtick.top"] = False   # draw ticks on the top side
mpl.rcParams["xtick.bottom"] =  True   # draw ticks on the bottom side
mpl.rcParams["xtick.major.size"] =  10      # major tick size in points
mpl.rcParams["xtick.minor.size"] = 5     # minor tick size in points
mpl.rcParams["xtick.major.width"] = 2.0    # major tick width in points
mpl.rcParams["xtick.minor.width"] = 1.5    # minor tick width in points
mpl.rcParams["xtick.major.pad"] =  3.5      # distance to major tick label in points
mpl.rcParams["xtick.minor.pad"] = 3.4      # distance to the minor tick label in points
mpl.rcParams["xtick.color"] = 'k'      # color of the tick labels
mpl.rcParams["xtick.labelsize"] = "small" # fontsize of the tick labels
mpl.rcParams["xtick.direction"] =  'in'    # direction: in, out, or inout
mpl.rcParams["xtick.minor.visible"] =  True  # visibility of minor ticks on x-axis
mpl.rcParams["xtick.major.top"] = False   # draw x axis top major ticks
mpl.rcParams["xtick.major.bottom"] =  True   # draw x axis bottom major ticks
mpl.rcParams["xtick.minor.top"] =  False   # draw x axis top minor ticks
mpl.rcParams["xtick.minor.bottom"] =  True   # draw x axis bottom minor ticks

mpl.rcParams["ytick.left"] =  True   # draw ticks on the left side
mpl.rcParams["ytick.right"] = False # draw ticks on the right side
mpl.rcParams["ytick.major.size"] = 10      # major tick size in points
mpl.rcParams["ytick.minor.size"] =  5      # minor tick size in points
mpl.rcParams["ytick.major.width"] =  2.0    # major tick width in points
mpl.rcParams["ytick.minor.width"] =  1.5    # minor tick width in points
mpl.rcParams["ytick.major.pad"] =  3.5      # distance to major tick label in points
mpl.rcParams["ytick.minor.pad"] = 3.4      # distance to the minor tick label in points
mpl.rcParams["ytick.color"] = 'k'      # color of the tick labels
mpl.rcParams["ytick.labelsize"] = "small" # fontsize of the tick labels
mpl.rcParams["ytick.direction"] = 'in'    # direction: in, out, or inout
mpl.rcParams["ytick.minor.visible"] = True  # visibility of minor ticks on y-axis
mpl.rcParams["ytick.major.left"] = True   # draw y axis left major ticks
mpl.rcParams["ytick.major.right"] =  True   # draw y axis right major ticks
mpl.rcParams["ytick.minor.left"] = True   # draw y axis left minor ticks
mpl.rcParams["ytick.minor.right"] = True   # draw y axis right minor ticks


mpl.rcParams["grid.color"] = "b0b0b0"    # grid color
mpl.rcParams["grid.linestyle"] =  "-"         # solid
mpl.rcParams["grid.linewidth"] = 0.4       # in points
mpl.rcParams["grid.alpha"] = 1.0       # transparency, between 0.0 and 1.0

mpl.rcParams["legend.loc"] = "best"
#legend.frameon       : True     # if True, draw the legend on a background patch
mpl.rcParams["legend.framealpha"] = 0.8# legend patch transparency
mpl.rcParams["legend.facecolor"] = "inherit"  # inherit from axes.facecolor; or color spec
mpl.rcParams["legend.edgecolor"] = "k"      # background patch boundary color
mpl.rcParams["legend.fancybox"] = True     # if True, use a rounded box for the
                                        # legend background, else a rectangle
mpl.rcParams["legend.shadow"] = True    # if True, give background a shadow effect
#legend.numpoints     : 1        # the number of marker points in the legend line
#legend.scatterpoints : 1        # number of scatter points
#legend.markerscale   : 1.0      # the relative size of legend markers vs. original
mpl.rcParams["legend.fontsize"] = "small"
# Dimensions as fraction of fontsize:
#legend.borderpad     : 0.4      # border whitespace
#legend.labelspacing  : 0.5      # the vertical space between the legend entries
#legend.handlelength  : 2.0      # the length of the legend lines
#legend.handleheight  : 0.7      # the height of the legend handle
#legend.handletextpad : 0.8      # the space between the legend line and legend text
#legend.borderaxespad : 0.5      # the border between the axes and legend edge
#legend.columnspacing : 2.0      # column separation



# See http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure
#figure.titlesize : large      # size of the figure title (Figure.suptitle())
#figure.titleweight : normal   # weight of the figure title
#figure.figsize   : 6.4, 4.8   # figure size in inches
mpl.rcParams["figure.dpi"] = 600      # figure dots per inch
#figure.facecolor : white   # figure facecolor; 0.75 is scalar gray
#figure.edgecolor : white   # figure edgecolor
mpl.rcParams["figure.autolayout"] = True  # When True, automatically adjust subplot
                            # parameters to make the plot fit the figure
                            # using `tight_layout`
#figure.constrained_layout.use: False # When True, automatically make plot
                                 # elements fit on the figure. (Not compatible
                                 # with `autolayout`, above).
#figure.max_open_warning : 20  # The maximum number of figures to open through
                               # the pyplot interface before emitting a warning.
                               # If less than one this feature is disabled.

# The figure subplot parameters.  All dimensions are a fraction of the
#figure.subplot.left    : 0.125  # the left side of the subplots of the figure
#figure.subplot.right   : 0.9    # the right side of the subplots of the figure
#figure.subplot.bottom  : 0.11    # the bottom of the subplots of the figure
#figure.subplot.top     : 0.88    # the top of the subplots of the figure
#figure.subplot.wspace  : 0.2    # the amount of width reserved for space between subplots,
                                 # expressed as a fraction of the average axis width
#figure.subplot.hspace  : 0.2    # the amount of height reserved for space between subplots,
                                 # expressed as a fraction of the average axis height
