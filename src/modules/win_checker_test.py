from . import win_checker

def test_min_moves():
    b = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']
    c = 4

    w = win_checker.run(c, b, 'O')

    assert w == False

def test_no_win():
    b = ['X', 'X', ' ',
         'O', 'X', ' ',
         ' ', ' ', 'O']
    c = 5

    w = win_checker.run(c, b, 'X')
    v = win_checker.run(c, b, 'O')

    assert w == False
    assert v == False

def test_tie(capfd):
    b = ['X', 'X', ' ',
         'O', 'X', ' ',
         ' ', ' ', 'O']
    c = 9

    w = win_checker.run(c, b, 'X')
    out, err = capfd.readouterr()

    assert w == False
    assert out == 'Tie! No one wins\n'


def test_vertical_0(capfd):
    b = ['O', 'O', 'O',
         ' ', ' ', ' ',
         ' ', ' ', ' ']
    c = 5

    w = win_checker.run(c, b, 'O')
    out, err = capfd.readouterr()

    assert w == True
    assert out == 'O WINS\n'

def test_vertical_1(capfd):
    b = [' ', ' ', ' ',
         'O', 'O', 'O',
         ' ', ' ', ' ']
    c = 5

    w = win_checker.run(c, b, 'O')
    out, err = capfd.readouterr()

    assert w == True
    assert out == 'O WINS\n'

def test_vertical_2(capfd):
    b = [' ', ' ', ' ',
         ' ', ' ', ' ',
         'X', 'X', 'X']
    c = 5

    w = win_checker.run(c, b, 'X')
    out, err = capfd.readouterr()

    assert w == True
    assert out == 'X WINS\n'

def test_horizontal_0(capfd):
    b = ['X', ' ', ' ',
         'X', ' ', ' ',
         'X', ' ', ' ']
    c = 5

    w = win_checker.run(c, b, 'X')
    out, err = capfd.readouterr()

    assert w == True
    assert out == 'X WINS\n'

def test_horizontal_1(capfd):
    b = [' ', 'X', ' ',
         ' ', 'X', ' ',
         ' ', 'X', ' ']
    c = 5

    w = win_checker.run(c, b, 'X')
    out, err = capfd.readouterr()

    assert w == True
    assert out == 'X WINS\n'

def test_horizontal_2(capfd):
    b = [' ', ' ', 'X',
         ' ', ' ', 'X',
         ' ', ' ', 'X']
    c = 5

    w = win_checker.run(c, b, 'X')
    out, err = capfd.readouterr()

    assert w == True
    assert out == 'X WINS\n'

def test_diagonal_0(capfd):
    b = ['A', ' ', ' ',
         ' ', 'A', ' ',
         ' ', ' ', 'A']
    c = 5

    w = win_checker.run(c, b, 'A')
    out, err = capfd.readouterr()

    assert w == True
    assert out == 'A WINS\n'

def test_horizontal_1(capfd):
    b = [' ', ' ', 'C',
         ' ', 'C', ' ',
         'C', ' ', ' ']
    c = 5

    w = win_checker.run(c, b, 'C')
    out, err = capfd.readouterr()

    assert w == True
    assert out == 'C WINS\n'
