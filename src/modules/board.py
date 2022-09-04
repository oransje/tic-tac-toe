current = []

def init():
    global current
    current = [' ', ' ', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']

def write(pos, char):
    global current
    current[pos] = char

def is_available(pos):
    global current
    return current[pos] == ' '

def display():
    global current

    for i in range(0, 9, 3):
        print(current[0+i] + '|' + current[1+i] + '|' + current[2+i])
        if i < 6:
            print('-+-+-')