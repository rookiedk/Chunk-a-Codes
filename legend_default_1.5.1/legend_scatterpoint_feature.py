"""
========================
matplotlib.__version__ --> '1.5.1'
Legend shows 3 scatter points by default
========================

In addition to the basic scatter plot, this shows some legend features:
    * Using ncols to increase/decrease number of legends on plot
    * Setting the number of scatter points in the legend
"""
import matplotlib.pyplot as plt
from numpy.random import rand


fig, ax = plt.subplots()
for color in ['red', 'green', 'blue']:
    n = 750
    x, y = rand(2, n)
    scale = 200.0 * rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

# Default ax.legend
ax.legend(bbox_to_anchor=(1.1, -0.03), fontsize=12, ncol=3, frameon=False)
# Clean legend
ax.legend(bbox_to_anchor=(1.1, -0.03), scatterpoints=1, fontsize=12, ncol=3, frameon=False)
plt.show()