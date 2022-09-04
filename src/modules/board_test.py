from . import board

def test_init_board():
    board.init()

    assert board.current == [' ', ' ', ' ',
                             ' ', ' ', ' ', 
                             ' ', ' ', ' ']

def test_write():
    board.init()

    board.write(0, 'X')

    assert board.current == ['X', ' ', ' ',
                             ' ', ' ', ' ', 
                             ' ', ' ', ' ']

def test_is_available():
    board.init()

    board.write(0, 'X')
    zero_pos = board.is_available(0)
    one_pos = board.is_available(1)

    assert zero_pos == False
    assert one_pos == True


def test_empty_display_board(capfd):
    board.init()

    board.display()
    out, err = capfd.readouterr()
    
    assert out == ' | | \n-+-+-\n | | \n-+-+-\n | | \n'

def test_write_diplay_board(capfd):
    board.init()
    board.write(0, 'X')

    board.display()
    out, err = capfd.readouterr()
    
    assert out == 'X| | \n-+-+-\n | | \n-+-+-\n | | \n'

def test_full_board_truthy():
    board.init()

    board.current = ['X'] * 9

    assert board.full_board() == True

def test_full_board_falsey():
    board.init()

    assert board.full_board() == False
