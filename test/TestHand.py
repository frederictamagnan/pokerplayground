import unittest
from Card import Card
from Hand import Hand
import numpy as np
from numpy.testing import assert_array_equal,assert_raises

class TestHand(unittest.TestCase):

    def test_two_pairs_one(self):
        a = Card(2, 1)
        b = Card(2, 2)
        c = Card(3, 1)
        d = Card(5, 1)
        e = Card(5, 3)
        hh = [a, b, c, d, e]

        hh = Hand(hh)
        index_highest_pairs,best_kicker=hh.two_pairs()

        self.arrayEqual(index_highest_pairs,[5,2])

    def test_two_pairs_seven_cards_hand(self):
        a = Card(2, 1)
        b = Card(2, 2)
        c = Card(3, 1)
        d = Card(5, 1)
        e = Card(5, 3)
        f= Card(7,1)
        g=Card(7,3)


        hh = [a, b, c, d, e,f,g]

        hh = Hand(hh)
        index_highest_pairs,best_kicker=hh.two_pairs()

        self.arrayEqual(index_highest_pairs,[7,5])

    def test_two_pairs_seven_cards_hand_with_aces(self):
        a = Card(1, 1)
        b = Card(1, 2)
        c = Card(3, 1)
        d = Card(5, 1)
        e = Card(5, 3)
        f = Card(7, 1)
        g = Card(7, 3)

        hh = [a, b, c, d, e, f, g]

        hh = Hand(hh)
        index_highest_pairs, best_kicker = hh.two_pairs()

        self.arrayEqual(index_highest_pairs, [14, 7])

    def test_two_pairs_false(self):
        a = Card(2, 1)
        b = Card(2, 2)
        c = Card(3, 1)
        d = Card(5, 1)
        e = Card(5, 3)
        h = [a, b, c, d, e]

        h = Hand(h)
        index_highest_pairs,best_kicker=h.two_pairs()

        self.arrayNotEqual(index_highest_pairs,[5,3])

    def test_two_pairs_best_kicker(self):
        a = Card(2, 1)
        b = Card(2, 2)
        c = Card(3, 1)
        d = Card(5, 1)
        e = Card(5, 3)
        h = [a, b, c, d, e]

        h = Hand(h)
        index_highest_pairs, best_kicker = h.two_pairs()

        self.arrayEqual(best_kicker, [3])

    def arrayEqual(self,array,list_):
        assert_array_equal(array,np.array(list_))

    def arrayNotEqual(self,array,list_):
        assert_raises(AssertionError, assert_array_equal, array, np.array(list_))


if __name__ == '__main__':
    unittest.main()
