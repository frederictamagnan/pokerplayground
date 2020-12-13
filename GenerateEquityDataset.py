
from EquityNHands import EquityNHands
import numpy as np

class GenerateEquityDataset:

    def __init__(self,n_rows=10,n_sim=10):
        self.inputs=[]
        self.boards=[]
        self.winrates=[]
        self.n_rows=n_rows
        self.n_sim=n_sim

    def generate_dataset(self):
        for i in range(self.n_rows):
            n_h=np.random.randint(2,6)
            nb_c=np.random.choice([0,3,4,5],1)
            e = EquityNHands(random=True, n_hands=n_h,n_simulation=self.n_sim)
            hands=e.list_hands
            board,winrate=e.monte_carlo_simulation(nb_card_initial_board=nb_c,to_print=True)
            input=np.zeros((6,2,15,4))
            for i_h,h in enumerate(hands):
                input[i_h,:,:]=h.tensor

            self.inputs.append(input)
            self.boards.append(board.tensor)
            self.winrates.append(winrate)

        self.inputs=np.stack(self.inputs)
        self.boards=np.stack(self.boards)
        self.winrates=np.stack(self.winrates)
        print(self.inputs.shape)
        print(self.boards.shape)
        print(self.winrates.shape)
        np.savez('./data/dataset.npz',x_cards=self.inputs,x_boards=self.boards,y_winrates=self.winrates)


if __name__=='__main__':
    g=GenerateEquityDataset()
    g.generate_dataset()