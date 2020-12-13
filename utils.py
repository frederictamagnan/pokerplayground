import numpy as np

def split(a, n):
    """
    https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
    :param a:
    :param n:
    :return:
    """
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

def get_list_maximum_values(list_):
    """
    https://stackoverflow.com/questions/17568612/how-to-make-numpy-argmax-return-all-occurrences-of-the-maximum
    :param list_:
    :return:
    """

    winner = np.argwhere(list_ == np.amax(list_))

    return winner.flatten().tolist()

idx_to_card=[(idx,(idx%13+1,idx%4)) for idx in np.arange(52)]
dict_idx_to_card=dict((elt[0], elt[1]) for elt in idx_to_card)
dict_card_to_idx=dict((elt[1], elt[0]) for elt in idx_to_card)