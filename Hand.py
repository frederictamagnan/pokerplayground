
import numpy as np
class Hand:
    """
     Straight Flush : 0
     Four of a kind : 1
     Full : 2
     Flush :3
     Straight: 4
     Three of a kind : 5
     Two pairs : 6
     One Pair : 7
     High Card :8
     Kickers :9,11,12,13
     """
    def __init__(self,cards,tensor=None):
        if tensor is None:
            self.cards=cards
            self.tensor,self.tensor_straight=self.cards_to_tensor()
        self.force_array=np.zeros(14)


    def __repr__(self):
        repr=str()

        for card in self.cards:
            repr+=card.__repr__()
        return repr

    @property
    def force(self):
        self.all()
        # force =int(''.join(map(str, list(self.force_array.astype(int)))))
        base=np.full((14),16).astype(np.dtype('int64'))
        power=-np.sort(-np.arange(14).astype(np.dtype('int64')))
        powerbase=np.power(base,power).astype(np.dtype('int64'))
        force=np.matmul(self.force_array,powerbase).astype(np.dtype('int64'))
        #return hex(force)
        return force

    def cards_to_tensor(self):

        tensor = np.zeros((len(self.cards), 15, 4))
        for i_card,card in enumerate(self.cards):
            tensor[i_card,card.height,card.suit]=1
            tensor[i_card,card.height,card.suit]=1
            if card.height==1:
                tensor[i_card,14,card.suit]=1
        tensor_straight=np.copy(tensor)
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

    def high_card(self):
        kickers=self.kickers(self.tensor,5)

        self.force_array[-5:]=kickers
        return kickers,-1

    def one_pair(self):
        index_highest=self.search_for_x_of_a_kind(x=2,nb_top=1)
        if type(index_highest).__module__ != np.__name__ and index_highest==-1:
            return -1,-1
        remaining_tensor=np.copy(self.tensor)
        remaining_tensor[:,index_highest,:]=0
        kickers=self.kickers(remaining_tensor,4)
        self.force_array[7]=index_highest
        self.force_array[-5:]=kickers
        return index_highest,kickers

    def two_pairs(self):
        index_highest = self.search_for_x_of_a_kind(x=2, nb_top=2)
        if type(index_highest).__module__ != np.__name__ and index_highest==-1:
            return -1,-1
        remaining_tensor = np.copy(self.tensor)
        remaining_tensor[:, index_highest, :] = 0
        kickers=self.kickers(remaining_tensor,1)
        self.force_array[6:8]=index_highest
        self.force_array[-5:]=kickers


        return -np.sort(-index_highest), kickers

    def three_of_a_kind(self):
        index_highest = self.search_for_x_of_a_kind(x=3, nb_top=1)
        if type(index_highest).__module__ != np.__name__ and index_highest==-1:
            return -1,-1
        remaining_tensor=np.copy(self.tensor)
        remaining_tensor[:,index_highest,:]=0
        kickers= self.kickers(remaining_tensor,2)
        self.force_array[5]=index_highest
        self.force_array[-5:]=kickers
        return index_highest,kickers

    def four_of_a_kind(self):
        index_highest = self.search_for_x_of_a_kind(x=4, nb_top=1)
        if type(index_highest).__module__ != np.__name__ and index_highest==-1 :
            return -1,-1
        remaining_tensor = np.copy(self.tensor)
        remaining_tensor[:, index_highest, :] = 0
        kickers=self.kickers(remaining_tensor,1)
        self.force_array[4]=index_highest
        self.force_array[-5:]=kickers
        return index_highest,kickers

    def flush(self):
        max_index_flush,index_suit=self.search_for_flush()
        if type(max_index_flush).__module__ != np.__name__ and max_index_flush==-1 :
            return -1,-1
        self.force_array[2]=max_index_flush
        return max_index_flush,-1

    def straight(self):
        sum_height = np.sum(self.tensor_straight, axis=(0, 2))
        sum_height_ace_max=(sum_height>=1).astype(int)
        search_seq=np.ones(5)
        straight_indexes=Hand.search_sequence_numpy(sum_height_ace_max,search_seq)
        if len(straight_indexes)==0:
            return -1,-1
        max_straight=np.max(straight_indexes)
        self.force_array[3]=max_straight
        return max_straight,-1

    def straight_flush(self):
        max_index_flush,suit_index=self.search_for_flush()
        is_straight=self.straight()

        if max_index_flush != -1 and is_straight!=-1:
            # tensor=np.zeros((self.tensor_straight.shape[0],15,4))
            # tensor[:,:,suit_index]=self.tensor_straight[:, :, suit_index]
            # sum_height = np.sum(tensor, axis=(0, 2))
            # print(self.tensor_straight)

            tensor=np.squeeze(self.tensor_straight[:,:,suit_index])

            sum_height=np.sum(tensor,axis=0)

            sum_height_ace_max = (sum_height >= 1).astype(int)
            search_seq = np.ones(5)
            straight_indexes = Hand.search_sequence_numpy(sum_height_ace_max, search_seq)
            if len(straight_indexes) == 0:
                return -1,-1
            max_straight = np.max(straight_indexes)
            self.force_array[0] = max_straight
            return max_straight,-1


        return -1,-1



    def full(self):
        three_of_a_kind_index,kickers=self.three_of_a_kind()
        if three_of_a_kind_index==-1:
            return -1,-1
        remaining_tensor=np.copy(self.tensor)
        remaining_tensor[:,three_of_a_kind_index,:]=0

        x=2
        nb_top=1
        sum_height = np.sum(remaining_tensor, axis=(0, 2))
        x_of_a_kind = np.argwhere(sum_height >= x).reshape(-1)
        if x_of_a_kind.size < nb_top:
            return -1,-1
        highest_pair_indice=-np.sort(-x_of_a_kind)[:nb_top]
        self.force_array[1]=three_of_a_kind_index
        self.force_array[7]=highest_pair_indice
        return (three_of_a_kind_index,highest_pair_indice),-1



    def kickers(self,remaining_tensor,nb_kickers):
        nb_kickers=min(nb_kickers,int((np.sum(self.tensor))))
        sum_height = np.sum(remaining_tensor, axis=(0, 2))
        kicker = np.argwhere(sum_height >= 1).reshape(-1)
        kicker_list=list(kicker)
        if kicker.size == 0:
            return -1
        kickers_fill=np.zeros(5)
        kickers_fill[:nb_kickers]=(-np.sort(-kicker))[:nb_kickers]
        return kickers_fill

    def all(self):
        funcs=[self.straight_flush,self.full,self.four_of_a_kind,self.full,self.flush,self.straight,self.three_of_a_kind,self.two_pairs,self.one_pair,self.high_card]
        for function in funcs:
            res,kicker=function()
            if type(res).__module__ == np.__name__:
                break

    def __cmp__(self, other):
        if self.force>other.force:
            return 1
        elif self.force==other.force:
            return 0
        else :
            return -1

    @staticmethod
    def merge(hand1,hand2):
        return Hand(hand1.cards+hand2.cards)
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









