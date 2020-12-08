from Card import Card
from Hand import Hand
import numpy as np


class Evaluate:
    """
    Straight Flush
    Four of a kind
    Full
    Flush
    Straight
    Three of a kind
    Two pairs
    One Pair
    High Card




    """
    def __init__(self,hand):
        assert isinstance(hand, Hand)
        self.hand=hand

    def check_force_hand(self):
        pass


if __name__=='__main__':
    a = Card(1, 0)
    b = Card(9, 3)
    c = Card(10, 0)
    d = Card(11, 0)
    e = Card(12, 0)
    f = Card(13, 0)
    g = Card(7, 0)

    hh = [a, b, c, d, e, f, g]
    hh=Hand(hh)
    check_list=[hh.straight_flush,hh.four_of_a_kind,hh.full,hh.flush,hh.straight,hh.three_of_a_kind,hh.two_pairs,hh.one_pair,hh.high_card]
    for function in check_list:
        res,kicker=function()
        if type(res).__module__ == np.__name__ and res!=-1 :
            break




