import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import six
"""Functions to draw a dataframe as a simple table on a matplotlib"""
def set_align_for_column(table, col, align="left"):
    """
    Function to align a single column of a dataframe that was plotted as a table using matplotlib
    :param table: dataframe to be plotted as a table
    :param col: column to be set aligned
    :param align: defaults to align, can be changed to right or center
    :return:
    """
    cells = [key for key in table._cells if key[1] == col]
    for cell in cells:
        table._cells[cell]._loc = align

"""Example"""
df = pd.DataFrame({'First Column':[10,200,30], 'Second Column':[25,355,450], 'Third Column':[300,405,550]})
gs = gridspec.GridSpec(1, 1)
loc = gs.new_subplotspec([0, 0])
ax = plt.subplot(loc)
fontsize= 12
the_table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', rowLoc='center',
                             bbox=[0, -0.3, 1.06, 1.3])
the_table.auto_set_font_size(False)
the_table.set_fontsize(9.5)
row_colors = ['w', 'w']
set_align_for_column(the_table, col=0, align='left')
set_align_for_column(the_table, col=1, align='right')
set_align_for_column(the_table, col=2, align='center')
ax.set_title('1st Column is Left-Aligned\n2nd Column is Right-Aligned\n3rd Column in Center-Aligned')
for k, cell in six.iteritems(the_table._cells):
    cell.set_edgecolor('w')
    #Set title row to be a different color than other row
    if k[0] == 0 or k[1] < 0:
        cell.set_text_props(weight='bold', color='w', fontsize=fontsize)
        cell.set_facecolor('#0e77c6')
    #Use if you need rows in the middle to be colored. For example - a 'total' row
    elif k[0] == 7 or k[0] == 13 or k[0] == 16 or k[0] == 23 or k[0] == 25:
        cell.set_text_props(weight='bold', color='w', fontsize=fontsize)
        cell.set_facecolor('#7c7c7c')
    #remaining rows are of the same color
    else:
        cell.set_text_props(fontsize=fontsize - 1)
        cell.set_facecolor(row_colors[k[0] % len(row_colors)])

plt.axis('off')
plt.show()