from game_one import Node, ConwayGame

def test_init():
    game = ConwayGame(board=[Node(top_left=None, top_center=None, top_right=None, left=None, right=None, bottom_left=None, bottom_center=None, bottom_right=None)])
    
    assert len(game.board) == 1
    assert game.board[0].get_living_neighbors() == []
    
    
def test_get_living_neighbors():
    node1 = Node()
    node2 = Node()
    node1.top_center = node2
    node2.bottom_center = node1

    assert len(node1.get_living_neighbors()) == 1
    assert len(node2.get_living_neighbors()) == 1

def test_play_round_rule1():
    node1 = Node()
    node2 = Node()
    node1.top_center = node2
    node2.bottom_center = node1
    game = ConwayGame([node1, node2])
    
    
    node3 = Node()
    node4 = Node()
    node5 = Node()
    
    node3.top_center = node4
    node3.top_right = node5
    
    node4.bottom_center = node3
    node4.right = node5
    
    node5.left = node4
    node5.bottom_left = node3
    
    game2 = ConwayGame([node3,node4,node5])
    
    game.play_round()
    game2.play_round()
    
    assert game.board == []
    assert len(game2.board) == 3


    
    
    
    