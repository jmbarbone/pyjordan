
def sort_by(x, y) :
    """
    Sort x by y

    Description
    -----------
    Sort values in one list by values in another

    Parameters
    ----------
    x : list
        A list of values
    y : list
        A list of values

    Returns
    -------
    res : list
        Values of x sorted by values of y
    """
    res = [x for _, x in sorted(zip(y, x))]
    return res
