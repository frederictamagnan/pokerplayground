import torch
from scipy.sparse import load_npz
import numpy as np
class EquityDataset(torch.utils.data.Dataset):

  def __init__(self,bypath=True,x_boards=None,x_cards=None,y_winrates=None):
      if bypath:
          x_boards = load_npz("../data/x_boards.npz").toarray()
          x_cards = load_npz("../data/x_cards.npz").toarray()
          y_winrates = load_npz("../data/y_winrates.npz").toarray()



      x_cards = x_cards.reshape((-1,6, 2, 15,4)).astype(np.float32)
      x_boards = x_boards.reshape((-1, 5, 15,4)).astype(np.float32)
      self.y = y_winrates.reshape((-1, 6,3)).astype(np.float32) / 1000

      sum_cards_boards=[]
      board = np.sum(x_boards, axis=1)
      for i in range (6):
          current_hand=np.sum(x_cards[:,i,:,:,:],axis=1)
          non_padded_array=np.add(current_hand,board)
          # print("non padded shape",non_padded_array.shape)
          padded_array=np.zeros((non_padded_array.shape[0],17,17))
          padded_array[:,:15,:4]=non_padded_array
          sum_cards_boards.append(padded_array)
      self.x_cards_plus_boards=np.stack(sum_cards_boards,axis=1).astype(np.float32)

      #3d
      # self.x_cards_plus_boards=np.zeros((x_cards_plus_boards.shape[0],17,17,17))
      # self.x_cards_plus_boards[:,:6,:,:]=x_cards_plus_boards
      # self.x_cards_plus_boards=np.expand_dims(self.x_cards_plus_boards,axis=1).astype(np.float32)

      print("global size", self.x_cards_plus_boards.shape[0])



      # am=np.argmax(self.y,axis=2)
      # y=np.zeros(self.y.shape)
      # y[am]=1
      # self.y=am

      # self.x_cards = np.concatenate((x_cards, x_boards), axis=2).astype(np.float32)
      # print(self.x.shape)


  def __len__(self):
        assert len(self.x_cards_plus_boards)==len(self.y)
        return len(self.x_cards_plus_boards)

  def __getitem__(self, index):
        # X_c=self.x_cards[index]
        # X_b=self.x_boards[index]
        # y=self.y[index][0,:]
        X=self.x_cards_plus_boards[index]
        y = self.y[index,:,0]
        # y=self.y[index][0]


        return X, y