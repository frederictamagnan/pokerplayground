import numpy as np
class Card:

    def __init__(self,height,suit):
        assert 0<height<14,"height must be between 1 and 13"
        assert -1<suit<4, "suit must be between 1 and 4"
        self.height=height
        self.suit=suit

    def __repr__(self):
        height_dict={
            1:"A",
            2:"2",
            3:"3",
            4:"4",
            5:"5",
            6:"6",
            7:"7",
            8:"8",
            9:"9",
            10:"T",
            11:"J",
            12:"Q",
            13:"K"
        }
        suit_dict={
            0:"♠",
            1:"♥",
            2:"♦",
            3:"♣ "
        }
        card_repr=height_dict[self.height]+suit_dict[self.suit]
        return card_repr

    @staticmethod
    def generate_hand(length=7):
        random_card=list(np.random.choice(52,length,replace=False))
        return [Card(height=x%13+1,suit=x%4) for x in random_card]
