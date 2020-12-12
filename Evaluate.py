from Card import Card
from Hand import Hand
import numpy as np
from time import time
from tqdm import tqdm
import csv

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
    def __init__(self):
        self.number_of_possible_boards = 311875200


    def exhaustive_boards_brute(self):
        """
        execution time : 10 min~
        :return:
        """
        n=self.number_of_possible_boards
        self.boards=[]
        for a in tqdm(range(52)):
            one=(a%13+1,a%4)
            for b in range(51):
                two=(b%13+1,b%4)
                for c in range(50):
                    three = (c % 13 + 1, c % 4)
                    for d in range(49):
                        four = (d % 13 + 1, d % 4)
                        for e in range(48):
                            five = (e % 13 + 1, e % 4)
                            self.boards.append([one,two,three,four,five])
        print(len(self.boards))
    def exhaustive_boards_numpy(self):
        self.boards=np.array(np.meshgrid(np.arange(52), np.arange(51), np.arange(50),np.arange(49),np.arange(48))).T.reshape(-1, 5)

    def exhaustive_boards_csv(self):

        i=0
        with open('boards.csv', mode='w') as board_file:
            boards_writer = csv.writer(board_file)
            for a in tqdm(range(52)):
                one = (a % 13 + 1, a % 4)
                for b in range(51):
                    two = (b % 13 + 1, b % 4)
                    for c in range(50):
                        three = (c % 13 + 1, c % 4)
                        for d in range(49):
                            four = (d % 13 + 1, d % 4)
                            for e in range(48):
                                five = (e % 13 + 1, e % 4)
                                boards_writer.writerow([one, two, three, four, five])
                                i=i+1
                                if i >1000:
                                    return 0


    def one_board_to_list_of_2_cards(self,flop):
        pass
    #todo



if __name__=='__main__':
    e=Evaluate()
    # tqdm(e.exhaustive_boards_csv())



