import unittest
from Card import Card

class TestCard(unittest.TestCase):


    def test_repr_card(self):
        self.assertEqual(Card(1,0).__repr__(),"A♠")

    def test_execute_generate_hand(self):
        hand=Card.generate_hand(10)
        self.assertEqual(len(hand),10)
if __name__ == '__main__':
    unittest.main()
