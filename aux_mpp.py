from numpy import *

def calculate_mean_dist_from_dict_dists(dict_dists):

    """
    Returns [sum of distances navigated for each ion, mean of distances]
    """

    list1=[]
    for key,value in dict_dists.iteritems():
        list1.append([double(key),double(value)])

    return [array(list1),mean(list1, 0)[1]]

def read_txt(path1):

    with open(path1) as f:
        x = f.readlines()

    return x

def gauss(x, *p):
    A, mu, sigma = p
    return A*exp(-(x-mu)**2/(2.*sigma**2))