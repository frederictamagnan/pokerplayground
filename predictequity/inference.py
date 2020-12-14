
import torch
from predictequity.EquityDataset import EquityDataset
import torch.nn as nn
from predictequity.SimpleCNNNet import SimpleCNNNet,SimpleNet
import torch.optim as optim
from Hand import Hand
from Card import Card
import numpy as np
PATH = './model/poker_net.pth'

n_hands=2
nb_cards_board=0
hands=Card.generate_hand(n_hands*2,split_bool=True,chunk_length=n_hands)
print(hands)
boards=Card.generate_hand(nb_cards_board,previous=Hand.id_of_list_of_hands(hands))
print(boards)
x_cards=np.zeros((6,2,15,4)).astype(np.float32)
for i_h,h in enumerate(hands):
    x_cards[i_h,:,:,:]=h.tensor
x_boards=np.zeros((5,15,4)).astype(np.float32)
x_boards[:nb_cards_board,:,:]=boards.tensor

x_cards=np.expand_dims(x_cards,axis=0)
x_boards=np.expand_dims(x_boards,axis=0)
y_winrates=np.zeros((x_boards.shape[0],6,3))

full_dataset = EquityDataset(bypath=False,x_cards=x_cards,x_boards=x_boards,y_winrates=y_winrates)

infloader = torch.utils.data.DataLoader(full_dataset,batch_size=1)

net=SimpleNet()
# correct = 0
# total = 0
net.load_state_dict(torch.load(PATH))

with torch.no_grad():
    for data in infloader:
        x_c,x_b, y = data
        outputs = net(x_c,x_b)
        print(outputs.data)



