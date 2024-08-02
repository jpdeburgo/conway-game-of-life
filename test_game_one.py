from game_one import Node, ConwayGame

def test_init():
    game = ConwayGame(board=[Node(top_left=None, top_center=None, top_right=None, left=None, right=None, bottom_left=None, bottom_center=None, bottom_right=None)])
    
    assert len(game.board) == 1
    assert len(game.board[0].get_living_neighbors()) == 0

def test_get_living_neighbors():
    node1 = Node()
    node2 = Node()
    node1.top_center = node2
    node2.bottom_center = node1
    game = ConwayGame(board=[node1, node2])

    assert len(game.board[0].get_living_neighbors()) == 1
    assert len(game.board[1].get_living_neighbors()) == 1

def test_rule1_next_round():
    node1 = Node()
    game = ConwayGame(board=[node1])
    
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node1.left = node2
    node2.right = node1
    node1.top_left = node3
    
    node3.bottom_right
    node2.top_center = node3
    node3.bottom_center = node2
    game2 = ConwayGame(board=[node1])
    
    game.next_round()
    
    assert game.board == []
    
    
