from Card import Card
from Hand import Hand
from utils import split
from tqdm import tqdm
from time import time

class Equity2Hands:

    def __init__(self):

        self.hero_hand,self.villain_hand=Card.generate_hand(4,split_bool=True,chunk_length=2)
        self.hero_hand, self.villain_hand = [Hand([Card(11, 0), Card(10, 0)]), Hand([Card(7, 3), Card(6, 3)])]
        print(self.hero_hand,self.villain_hand,sep='\n')

    def monte_carlo_simulation(self):
        start=time()
        n=10000
        win=0
        loose=0
        tie=0
        for i in tqdm(range(n)):
            board=Card.generate_hand(5)
            hero_board=Hand.merge(self.hero_hand,board)
            villain_board = Hand.merge(self.villain_hand, board)
            if hero_board.force>villain_board.force:
                win+=1
            elif hero_board.force<villain_board.force:
                loose+=1
            else:
                tie+=1

        print("win : "+str(win*100/n)+", tie : "+str(tie*100/n)+" loose : "+str(loose*100/n))
        end=time()
        print(str(end-start)+" second elapsed")
if __name__=='__main__':
    e=Equity2Hands()
    e.monte_carlo_simulation()