from Card import Card
from Hand import Hand
from utils import get_list_maximum_values
from tqdm import tqdm
from time import time
import numpy as np

class EquityNHands:

    def __init__(self,random=True,n_hands=3):
        if random:

            self.list_hands=Card.generate_hand(n_hands*2,split_bool=True,chunk_length=n_hands,seed_number=0)

        else:
            self.list_hands = [Hand([Card(1, 0), Card(2, 1)]), Hand([Card(11, 2), Card(13, 3)]),Hand([Card(4, 0), Card(9, 3)])]

        self.n_hands = len(self.list_hands)
        self.winrate = np.zeros((n_hands, 3))
    def monte_carlo_simulation(self):
        start = time()
        n = 1000

        for i in range(n):

            board = Card.generate_hand(5)
            hands_board=list()
            for hand in self.list_hands:
                hands_board.append(Hand.merge(hand,board))

            listforce=[hand.force for hand in hands_board]
            indices_max=get_list_maximum_values(listforce)
            all_indices=np.arange(self.n_hands)
            if len(indices_max)==1:
                self.winrate[indices_max,0]+=1
                remaining_indices=np.delete(all_indices,indices_max)
            elif len(indices_max)>1:
                self.winrate[indices_max,1]+=1
                remaining_indices = np.delete(all_indices, indices_max)
            self.winrate[remaining_indices,2]+=1

        print("      W  T  L")
        for i,line in enumerate(self.winrate):
            print(self.list_hands[i],line*100/n)
        end = time()
        print(str(end - start) + " second elapsed")

if __name__ == '__main__':
    # e = EquityNHands(random=False)
    # e.monte_carlo_simulation()
    e = EquityNHands(random=True,n_hands=6)
    e.monte_carlo_simulation()