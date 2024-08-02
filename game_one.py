class Node:
    def __init__(self,top_center=None, top_right=None, top_left=None, right=None, left=None, bottom_center=None, bottom_right=None, bottom_left=None):
        self.top_center=top_center
        self.top_left=top_left
        self.top_right=top_right
        self.bottom_center=bottom_center
        self.bottom_left=bottom_left
        self.bottom_right=bottom_right
        self.right=right
        self.left=left

    def get_neighbors(self):
        return list(filter(lambda val: val is not None, [self.top_center, self.top_right, self.top_left, self.right, self.left, self.bottom_center, self.bottom_right, self.bottom_left]))


class ConwayGame:
    def __init__(self, board):
        self.board = board
        
    def next_turn(self):
        for i in range(len(self.board)):
            node = self.board[i]
            if len(node.get_neighbors()) < 2:
                self.board[i] = None
        self.board = list(filter(lambda val: val is not None, self.board))
        return self.board

                
                
