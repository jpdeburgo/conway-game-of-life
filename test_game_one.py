from game_one import Node, ConwayGame

def test_init():
    game = ConwayGame(board=[Node(top_center=None, top_right=None, top_left=None, right=None, left=None, bottom_center=None, bottom_right=None, bottom_left=None)])
    
    assert len(game.board) == 1
    assert game.board[0].top_right is None
    assert len(game.board[0].get_neighbors()) == 0
    
def test_rule1():
    game = ConwayGame(board=[Node()])
    game2 = ConwayGame(board=[Node(top_center=Node())])
    
    assert game.next_turn() == []
    assert game2.next_turn() == []
    
def test_rule2():
    game = ConwayGame(board=[Node(top_center=Node(), top_right=Node())])

    

