
from EquityNHands import EquityNHands
import numpy as np
from tqdm import tqdm
from scipy.sparse import csr_matrix
from scipy.sparse import vstack
from scipy.sparse import save_npz
class GenerateEquityDataset:

    def __init__(self,n_rows=10000,n_sim=1000):
        self.inputs=[]
        self.boards=[]
        self.winrates=[]
        self.n_rows=n_rows
        self.n_sim=n_sim

    def generate_dataset(self,suffix):
        for i in tqdm(range(self.n_rows)):
            n_h=np.random.randint(2,6)
            nb_c=np.random.choice([0,3,4,5],1)
            e = EquityNHands(random=True, n_hands=n_h,n_simulation=self.n_sim)
            hands=e.list_hands
            board,winrate=e.monte_carlo_simulation(nb_card_initial_board=nb_c,to_print=False)
            input=np.zeros((6,2,15,4))
            for i_h,h in enumerate(hands):
                input[i_h,:,:]=h.tensor


            self.inputs.append(csr_matrix(input.reshape(6*2*15*4)))
            self.boards.append(csr_matrix(board.tensor.reshape(5*15*4)))
            self.winrates.append(csr_matrix(winrate))
        # if i % 1000 == 0:
        #     save_npz(filepath + 'x_cards_' + str(i) + '.npz', self.inputs)
        #     save_npz(filepath + 'x_boards_' + str(i) + '.npz', self.boards)
        #     save_npz(filepath + 'y_winrates_' + str(i) + '.npz', self.winrates)
        # self.inputs=np.stack(self.inputs)
        # self.boards=np.stack(self.boards)
        # self.winrates=np.stack(self.winrates)
        self.inputs=vstack(self.inputs)
        self.boards=vstack(self.boards)
        self.winrates=vstack(self.winrates)
        
        filename='./data/'
        save_npz(filename+'x_cards_'+suffix+'.npz',self.inputs)
        save_npz(filename +'x_boards_'+suffix+'.npz',self.boards)
        save_npz(filename+'y_winrates_'+suffix+'.npz',self.winrates)
        # np.savez('./data/dataset.npz',x_cards=self.inputs,x_boards=self.boards,y_winrates=self.winrates)


if __name__=='__main__':
    for i in range(100):
        g=GenerateEquityDataset()
        g.generate_dataset(suffix=str(i))