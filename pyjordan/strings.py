def str_replace_all(text, dic):
    """ Dictionary replacements

    Replaces strings found in dictionary

    Parameters
    ----------
    text : string
        The text to replace
    dic : dictionary
        The dictionary of items to replace

    Reference
    ---------
    https://stackoverflow.com/a/6117042

    Warnings
    --------
    Python dictionaries don't have a reliable order for iteration. This solution only solves your problem if:
    * order of replacements is irrelevant
    * it's ok for a replacement to change the results of previous replacements

    Inefficient if `text` is too big or there are many pairs in the dictionary.

    Example
    -------
    x = "The quick brown fox"
    d = {'brown': 'green', 'quick': 'slow', 'fox': 'platypus'}
    str_replace_all(x, d)
    """

    from collections import OrderedDict

    dic = OrderedDict(dic)

    for i, j in dic.items():
        text = text.replace(i, j)

    return text
