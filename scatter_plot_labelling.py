import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
from itertools import combinations, cycle
from matplotlib.backends.backend_pdf import PdfPages
import datetime
pdf = ('C:/Users/danandak/Desktop/Temp' +
                           datetime.datetime.today().strftime('%Y-%m-%d') + '.pdf')

pdf = PdfPages(pdf)
def scatter_plot_label(df):
    dx, dy = 0.05, 0.04  # initial offset of labels from points
    dX, dY = 0.8, 0.8  # expand the frame of the plot to make room for stretched labels
    WEIGHT = 500  # strength of links, how far from points can text be?
    K = 0.5  # preferred distance between points
    label_repulsive_weight = 0.001  # labels push away from each other
    N = len(df)
    # Colormap
    C = cycle('bgrcmk')
    # build the network:
    d_nodes, t_nodes = [], []
    G = nx.Graph()
    node2coord = {}
    X = df['A'].values
    Y = df['B'].values
    for i in range(N):
        x, y = X[i], Y[i]
        d_str = "d%i" % i
        t_str = "%i" % i
        d_nodes.append(d_str)
        t_nodes.append(t_str)
        G.add_edge(d_str, t_str, weight=WEIGHT)

        node2coord[d_str] = (x, y)
        node2coord[t_str] = (x + dx, y + dy)

    # "t" nodes are self-repulsive:
    for ni, nj in combinations(t_nodes, 2):
        G.add_edge(ni, nj, weight=-label_repulsive_weight * WEIGHT)
    # Figure Plotting starts
    plt.figure(figsize=(15, 8))
    plt.subplot(121)
    ax = plt.gca()
    # compute new layout, only "t" nodes can move:
    node2coord_springs = nx.spring_layout(G, k=K, pos=node2coord, fixed=d_nodes)
    # Call function to draw
    ax.scatter(X, Y, c=next(C), s=100)
    arrowprops = dict(shrink=0.01, width=0.5, color='k', headwidth=1)
    for i in range(N):
        d_str = "d%i" % i
        t_str = "%i" % i
        ax.annotate(t_str,
                    xy=node2coord_springs[d_str],
                    xytext=node2coord_springs[t_str],
                    arrowprops=arrowprops,
                    )
    ax.set_xlim(X.min() - dX, X.max() + dX)
    ax.set_ylim(Y.min() - dY, Y.max() + dY)
    ax.set_title('I - automatic scatter plot labelling', weight='bold')
    plt.plot([0, 1], [0, 1], '-', color=next(C))
    # Subplot on the right for reference table
    plt.subplot(122)
    ax = plt.gca()
    df['Label in Plot'] = df.index.tolist()
    custom_table = df
    the_table = ax.table(cellText=custom_table.values, colWidths=[0.3 for x in custom_table.columns],
                         colLabels=custom_table.columns, cellLoc='center',
                         rowLoc='center', bbox=[0, 0, 1.0, 1.0])
    the_table.auto_set_font_size(True)
    ax.set_title('Reference for Plot I', weight='bold')
    plt.axis('off')
    pdf.savefig(plt.gcf())
    pdf.close()
    return pdf

if __name__ =='__main__':
    df = pd.DataFrame({'A':np.random.random(20), 'B':np.random.random(20)})
    scatter_plot_label(df)