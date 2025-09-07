"""
Functions for plotting graphs using matplotlib
"""

import matplotlib.pyplot as plt

def line(x_arr, y_arr, colors, labels, x_label, y_label, title, legend, x_invert=False, y_invert=False):
    """Generate line plots

    Args:
        x_arr : array
            Array of x axis values
        y_arr : array
            Array of y axis values
        colors : array
            Array of colors for each domain
        labels : array
            Array of labels for each domain
        x_label : str
            x-axis label
        y_label : str
            y-axis label
        title : str
            Main plot title
        legend: str
            Legend location
        x_invert : bool
            If True, invert x-axis
        y_invert : bool
            If True, invert y-axis
    """

    for x,y,c,l in zip(x_arr,y_arr,colors,labels):
        plt.plot(x,y,'-o',c=c,label=l)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc=legend)
    
    if x_invert==True:
        plt.gca().invert_xaxis()
    if y_invert==True:
        plt.gca().invert_yaxis()


def scatter(x_arr, y_arr, colors, labels, x_label, y_label, title, legend, x_invert=False, y_invert=False):
    """Generate scatter plots

    Args:
        x_arr : array
            Array of x axis values
        y_arr : array
            Array of y axis values
        colors : array
            Array of colors for each domain
        labels : array
            Array of labels for each domain
        x_label : str
            x-axis label
        y_label : str
            y-axis label
        title : str
            Main plot title
        legend: str
            Legend location
        x_invert : bool
            If True, invert x-axis
        y_invert : bool
            If True, invert y-axis
    """

    for x,y,c,l in zip(x_arr,y_arr,colors,labels):
        plt.scatter(x,y,c=c,label=l)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc=legend)
    
    if x_invert==True:
        plt.gca().invert_xaxis()
    if y_invert==True:
        plt.gca().invert_yaxis()