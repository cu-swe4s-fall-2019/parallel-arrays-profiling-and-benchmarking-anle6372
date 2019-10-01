"""Functions for data visualization

Parameters
----------
L : a list containing only integers and
    floats that will be the data to be visualized
out_file_name : the name of the output data visualization figure

Returns
-------
boxplot : Creates a boxplot with the data in list L
histogram : Creates a histogram with the data in list L
combo: Creates a both a boxplot and histogram with the data in list L
"""

import matplotlib.pyplot as plt
import os.path
import matplotlib
matplotlib.use('Agg')


# method for creating boxplots
def boxplot(L, out_file_name):

    # ensures correct input type
    if L is None:
        return None
    if len(L) == 0:
        return None
    if not isinstance(L, list):
        raise TypeError('Input must be list')
    s = 0
    for l in L:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ValueError('Invalid type in list.')
    if os.path.exists(out_file_name) is True:
        print('This file name already exists')
        return

    out_file = out_file_name
    plt.title('Insert Plot Title', fontsize=20)
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.boxplot(L)
    plt.savefig(out_file, bbox_inches='tight')


# method for creating histograms
def histogram(L, out_file_name):

    # ensures correct input type
    if L is None:
        return None
    if len(L) == 0:
        return None
    if not isinstance(L, list):
        raise TypeError('Input must be list')
    s = 0
    for l in L:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ValueError('Invalid type in list.')
    if os.path.exists(out_file_name) is True:
        print('This file name already exists')
        return

    out_file = out_file_name
    plt.title('Insert Plot Title', fontsize=20)
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.hist(L)
    plt.savefig(out_file, bbox_inches='tight')


# method for creating boxplots and histograms at the same time
def combo(L, out_file_name):

    # ensures correct input type
    if L is None:
        return None
    if len(L) == 0:
        return None
    if not isinstance(L, list):
        raise TypeError('Input must be list')
    s = 0
    for l in L:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ValueError('Invalid type in list.')
    if os.path.exists(out_file_name) is True:
        print('This file name already exists')
        return

    out_file = out_file_name
    width = 10
    height = 5
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 2, 1)
    ax.boxplot(L)
    ax.set_xlabel('sample')
    ax.set_ylabel('values')
    ax = fig.add_subplot(1, 2, 2)
    ax.hist(L)
    ax.set_xlabel('frequency')
    ax.set_ylabel('values')
    fig.suptitle('Plot Title', fontsize=20)
    plt.savefig(out_file, bbox_inches='tight')
