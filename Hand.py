from Card import Card
import numpy as np
class Hand:

    def __init__(self,cards,tensor=None):
        if tensor is None:
            self.cards=cards
            self.tensor,self.tensor_straight=self.cards_to_tensor()
        else:
            self.tensor=tensor

    def __repr__(self):
        repr=str()

        for card in self.cards:
            repr+=card.__repr__()
        return repr


    def cards_to_tensor(self):

        tensor = np.zeros((len(self.cards), 15, 4))
        for i_card,card in enumerate(self.cards):
            tensor[i_card,card.height,card.suit]=1
            tensor[i_card,card.height,card.suit]=1
            if card.height==1:
                tensor[i_card,14,card.suit]=1
        tensor_straight=tensor
        tensor[:,1,:]=0
        return tensor,tensor_straight

    def search_for_x_of_a_kind(self,x,nb_top):
        sum_height=np.sum(self.tensor,axis=(0,2))
        x_of_a_kind=np.argwhere(sum_height>=x).reshape(-1)
        if x_of_a_kind.size<nb_top:
            return -1
        return -np.sort(-x_of_a_kind)[:nb_top]

    def search_for_flush(self):
        sum_suit = np.sum(self.tensor, axis=(0, 1))
        suit_index = np.argwhere(sum_suit >= 5).reshape(-1)
        if len(list(suit_index))==0:
            return -1,-1
        return np.argmax(self.tensor[:,:,suit_index]),suit_index

    def highest_pair(self):
        index_highest=self.search_for_x_of_a_kind(x=2,nb_top=1)
        remaining_tensor=self.tensor
        remaining_tensor[:,index_highest,:]=0

        return index_highest,self.kickers(remaining_tensor,4)
    def two_pairs(self):
        index_highest = self.search_for_x_of_a_kind(x=2, nb_top=2)
        if type(index_highest).__module__ != np.__name__:
            return -1,-1
        remaining_tensor = self.tensor
        remaining_tensor[:, index_highest, :] = 0
        return -np.sort(-index_highest), self.kickers(remaining_tensor,1)

    def three_of_a_kind(self):
        index_highest = self.search_for_x_of_a_kind(x=3, nb_top=1)
        if type(index_highest).__module__ != np.__name__:
            return -1,-1
        remaining_tensor=self.tensor
        remaining_tensor[:,index_highest,:]=0
        return index_highest, self.kickers(remaining_tensor,2)

    def four_of_a_kind(self):
        index_highest = self.search_for_x_of_a_kind(x=4, nb_top=1)
        if type(index_highest).__module__ != np.__name__:
            return -1,-1
        remaining_tensor = self.tensor
        remaining_tensor[:, index_highest, :] = 0
        return index_highest, self.kickers(remaining_tensor,1)

    def flush(self):
        max_index_flush,index_suit=self.search_for_flush()
        if type(max_index_flush).__module__ != np.__name__:
            return -1
        return max_index_flush,index_suit

    def straight(self):
        sum_height = np.sum(self.tensor_straight, axis=(0, 2))
        # sum_height_ace=np.zeros(15)
        # sum_height_ace[:14]=sum_height
        # sum_height_ace[14] = sum_height[1]
        sum_height_ace_max=(sum_height>=1).astype(int)
        search_seq=np.ones(5)
        straight_indexes=Hand.search_sequence_numpy(sum_height_ace_max,search_seq)
        if len(straight_indexes)==0:
            return -1
        max_straight=np.max(straight_indexes)


        return max_straight

    def straight_flush(self):
        max_index_flush,suit_index=self.search_for_flush()
        if max_index_flush != -1 and self.straight() !=-1:
            tensor=self.tensor_straight[:, :, suit_index].reshape(-1,15,4)
            tensor=Hand(tensor)
            return tensor.straigth()

        return None



    def kickers(self,remaining_tensor,nb_kickers):
        sum_height = np.sum(remaining_tensor, axis=(0, 2))
        kicker = np.argwhere(sum_height >= 1).reshape(-1)
        kicker_list=list(kicker)
        if kicker.size == 0:
            return -1
        return (-np.sort(-kicker))[:nb_kickers]

    def all(self):
        self.search_for_flush()
        self.highest_pair()
        self.three_of_a_kind()
        self.four_of_a_kind()
        self.straight()
        self.flush()

    @staticmethod
    def search_sequence_numpy(arr, seq):
        """ Find sequence in an array using NumPy only.

        Parameters
        ----------
        arr    : input 1D array
        seq    : input 1D array

        Output
        ------
        Output : 1D Array of indices in the input array that satisfy the
        matching of input sequence in the input array.
        In case of no match, an empty list is returned.
        """

        # Store sizes of input array and sequence
        Na, Nseq = arr.size, seq.size

        # Range of sequence
        r_seq = np.arange(Nseq)

        # Create a 2D array of sliding indices across the entire length of input array.
        # Match up with the input sequence & get the matching starting indices.
        M = (arr[np.arange(Na - Nseq + 1)[:, None] + r_seq] == seq).all(1)

        # Get the range of those indices as final output
        if M.any() > 0:
            return np.where(np.convolve(M, np.ones((Nseq), dtype=int)) > 0)[0]
        else:
            return []  # No match found








