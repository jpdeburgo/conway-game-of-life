class Node:
    def __init__(self, top_left=None, top_center=None, top_right=None, left=None, right=None, bottom_left=None, bottom_center=None, bottom_right=None) -> None:
        self.top_left = top_left
        self.top_center = top_center
        self.top_right = top_right
        self.left = left
        self.right = right
        self.bottom_left = bottom_left
        self.bottom_center = bottom_center
        self.bottom_right = bottom_right
        
    def get_living_neighbors(self):
        neighbors = [self.top_left, self.top_center, self.top_right, self.left, self.right, self.bottom_left, self.bottom_center, self.bottom_right]
        neighbors = list(filter(lambda val: val is not None, neighbors))
        return neighbors
    
    
class ConwayGame:
    def __init__(self, board) -> None:
        self.board = board

    def next_round(self):
        self.board = []