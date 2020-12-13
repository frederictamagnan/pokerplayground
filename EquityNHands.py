from Card import Card
from Hand import Hand
from utils import get_list_maximum_values
from tqdm import tqdm
from time import time
import numpy as np

class EquityNHands:

    def __init__(self,random=True,n_hands=3,n_simulation=100):
        if random:

            self.list_hands=Card.generate_hand(n_hands*2,split_bool=True,chunk_length=n_hands)

        else:
            self.list_hands = [Hand([Card(1, 0), Card(2, 1)]), Hand([Card(11, 2), Card(13, 3)]),Hand([Card(4, 0), Card(9, 3)])]

        self.n_hands = len(self.list_hands)

        self.n_simuation=n_simulation


    def monte_carlo_simulation(self,nb_card_initial_board=0,to_print=False):
        winrate = np.zeros((6, 3))
        start = time()

        board = Card.generate_hand(nb_card_initial_board,previous=Hand.id_of_list_of_hands(self.list_hands))
        if to_print:
            print(board)

        hands_board_with_flop = list()
        for hand in self.list_hands:
            hands_board_with_flop.append(Hand.merge(hand, board))

        for i in range(self.n_simuation):

            post_board = Card.generate_hand(5-nb_card_initial_board,previous=Hand.id_of_list_of_hands(hands_board_with_flop))
            hands_board_post_flop = list()
            for i_hand,hand in enumerate(hands_board_with_flop):
                hands_board_post_flop.append(Hand.merge(hand, post_board))
            # print(hands_board_post_flop)
            listforce=[hand.force for hand in hands_board_post_flop]
            indices_max=get_list_maximum_values(listforce)
            all_indices=np.arange(self.n_hands)
            if len(indices_max)==1:
                winrate[indices_max,0]+=1
                remaining_indices=np.delete(all_indices,indices_max)
            elif len(indices_max)>1:
                winrate[indices_max,1]+=1
                remaining_indices = np.delete(all_indices, indices_max)
            winrate[remaining_indices,2]+=1
        if to_print:
            print("      W  T  L")
            for i,line in enumerate(winrate):
                if i>=len(self.list_hands):
                    break
                print(self.list_hands[i],line*100/self.n_simuation)

            end = time()
            print(str(end - start) + " second elapsed")
        complete_board=Hand.merge(board,post_board)
        return complete_board,winrate

if __name__ == '__main__':
    # e = EquityNHands(random=False)
    # e.monte_carlo_simulation()
    e = EquityNHands(random=True,n_hands=2)
    e.monte_carlo_simulation(nb_card_initial_board=5)