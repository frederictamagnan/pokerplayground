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
        self.arrayEqual(best_kicker,[3])

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
        self.arrayEqual(best_kicker,[3])

    def test_two_pairs_seven_cards_hand_with_aces(self):
        a = Card(1, 1)
        b = Card(1, 2)
        c = Card(4, 1)
        d = Card(5, 1)
        e = Card(5, 3)
        f = Card(7, 1)
        g = Card(7, 3)

        hh = [a, b, c, d, e, f, g]

        hh = Hand(hh)
        index_highest_pairs, best_kicker = hh.two_pairs()

        self.arrayEqual(index_highest_pairs, [14, 7])
        self.arrayEqual(best_kicker,[5])


    def test_two_pairs_omaha_hand_with_aces(self):
        a = Card(1, 1)
        b = Card(1, 2)
        c = Card(3, 1)
        d = Card(5, 1)
        e = Card(5, 3)
        f = Card(7, 1)
        g = Card(7, 3)
        h = Card(8, 1)
        i = Card(8, 3)

        hh = [a, b, c, d, e, f, g,h,i]

        hh = Hand(hh)
        index_highest_pairs, best_kicker = hh.two_pairs()

        self.arrayEqual(index_highest_pairs,[14,8])
        self.arrayEqual(best_kicker,[7])

    def test_two_pairs_omaha_hand_with_aces(self):
        a = Card(1, 1)
        b = Card(1, 2)
        c = Card(2, 1)
        d = Card(3, 1)
        e = Card(4, 3)
        f = Card(5, 1)
        g = Card(6, 3)
        h = Card(7, 1)
        i = Card(8, 3)

        hh = [a, b, c, d, e, f, g,h,i]

        hh = Hand(hh)
        index_highest_pairs, best_kicker = hh.two_pairs()

        self.assertEqual(index_highest_pairs,-1)
        self.assertEqual(best_kicker,-1)


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


    def test_four_of_a_kind_omaha_hand(self):
        a = Card(1, 1)
        b = Card(1, 2)
        c = Card(1, 3)
        d = Card(1, 0)
        e = Card(4, 3)
        f = Card(5, 1)
        g = Card(6, 3)
        h = Card(7, 1)
        i = Card(8, 3)

        hh = [a, b, c, d, e, f, g, h, i]

        hh = Hand(hh)
        index_four_of_a_kind, best_kicker = hh.four_of_a_kind()
        self.arrayEqual(index_four_of_a_kind, [14])
        self.arrayEqual(best_kicker, [8])


    def test_three_of_a_kind_omaha_hand(self):
        a = Card(1, 1)
        b = Card(1, 2)
        c = Card(1, 3)
        d = Card(9, 0)
        e = Card(4, 3)
        f = Card(5, 1)
        g = Card(6, 3)
        h = Card(7, 1)
        i = Card(8, 3)

        hh = [a, b, c, d, e, f, g, h, i]

        hh = Hand(hh)
        index_three_of_a_kind, best_kicker = hh.three_of_a_kind()
        self.arrayEqual(index_three_of_a_kind, [14])
        self.arrayEqual(best_kicker, [9,8])

    def test_flush_omaha_hand(self):
        a = Card(1, 1)
        b = Card(1, 2)
        c = Card(1, 3)
        d = Card(9, 1)
        e = Card(4, 1)
        f = Card(5, 1)
        g = Card(6, 3)
        h = Card(7, 1)
        i = Card(8, 3)

        hh = [a, b, c, d, e, f, g, h, i]

        hh = Hand(hh)
        flush,index_suit = hh.flush()
        self.arrayEqual(flush, [14])
        self.arrayEqual(index_suit,[1])

    def test_straight_omaha_hand(self):
        a = Card(1, 1)
        b = Card(2, 2)
        c = Card(3, 3)
        d = Card(4, 1)
        e = Card(5, 1)
        f = Card(6, 1)
        g = Card(8, 3)
        h = Card(9, 1)
        i = Card(8, 1)

        hh = [a, b, c, d, e, f, g, h, i]

        hh = Hand(hh)
        max_straight=hh.straight()
        self.arrayEqual(max_straight,[6])





    def arrayEqual(self,array,list_):
        assert_array_equal(array,np.array(list_))

    def arrayNotEqual(self,array,list_):
        assert_raises(AssertionError, assert_array_equal, array, np.array(list_))


if __name__ == '__main__':
    unittest.main()
