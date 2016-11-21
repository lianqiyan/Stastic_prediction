import pandas as pd
from rpy2.robjects.lib import ggplot2
import numpy as np
import matplotlib.pyplot as plt
from rpy2.robjects import pandas2ri
pandas2ri.activate()

x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
y = np.random.normal(10, 4, 10)
color = np.random.normal(20, 4, 10)
df = pd.DataFrame({'x': x,
                   'y': y,
                   'color': color})
rdf = pandas2ri.py2ri(df)
plt.figure(1)
pp = ggplot2.ggplot(rdf) + \
     ggplot2.aes_string(x='x', y='y', fill='color') + \
     ggplot2.geom_bar(stat="identity")
pp.plot()
plt.figure(2)
gp = ggplot2.ggplot(rdf)
pp = gp + \
     ggplot2.aes_string(x='x', y='y', group=1, col='factor(color)') + \
     ggplot2.geom_point(colour="grey50", size=4) + \
     ggplot2.geom_point(size=2.5) + \
     ggplot2.geom_line()
pp.plot()
plt.figure(3)
vv = ggplot2.ggplot(rdf) + \
     ggplot2.aes_string(x='factor(y)', fill='factor(color)') +\
     ggplot2.geom_bar(width=1) +\
     ggplot2.coord_polar(theta='x')
vv.plot()
