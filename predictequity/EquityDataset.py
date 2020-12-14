import torch
from scipy.sparse import load_npz
import numpy as np
class EquityDataset(torch.utils.data.Dataset):

  def __init__(self,bypath=True,x_boards=None,x_cards=None,y_winrates=None):
      if bypath:
          x_boards = load_npz("../data/x_boards.npz").toarray()
          x_cards = load_npz("../data/x_cards.npz").toarray()
          y_winrates = load_npz("../data/y_winrates.npz").toarray()


      self.x_cards = x_cards.reshape((-1,1, 6 * 2, 15,4)).astype(np.float32)
      self.x_boards = x_boards.reshape((-1,1, 5, 15,4)).astype(np.float32)
      self.y = y_winrates.reshape((-1, 6, 3)).astype(np.float32) / 1000



      # self.x_cards = np.concatenate((x_cards, x_boards), axis=2).astype(np.float32)
      # print(self.x.shape)


  def __len__(self):
        assert len(self.x_boards)==len(self.y)
        return len(self.x_boards)

  def __getitem__(self, index):
        X_c=self.x_cards[index]
        X_b=self.x_boards[index]
        y=self.y[index][0,:]



        return X_c,X_b, y