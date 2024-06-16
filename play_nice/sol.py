#!/home/maxime/.pyvenv/bin/python3

SQUARE_SIZE = 6

def generate_square(alphabet):
    assert len(alphabet) == pow(SQUARE_SIZE, 2)
    m = []
    for i, letter in enumerate(alphabet):
	    if i % SQUARE_SIZE == 0:
		    row = []
	    row.append(letter)
	    if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
		    m.append(row)
    return m

def get_index(letter, m):
	for row in range(SQUARE_SIZE):
		for col in range(SQUARE_SIZE):
			if m[row][col] == letter:
				return (row, col)
	print("letter not found in m.")
	exit()

def decode_pair(m, pair):
    p1 = get_index(pair[0], m)
    p2 = get_index(pair[1], m)

    if p1[0] == p2[0]:
	    return m[p1[0]][(p1[1] - 1)  % SQUARE_SIZE] + m[p2[0]][(p2[1] - 1)  % SQUARE_SIZE]
    elif p1[1] == p2[1]:
	    return m[(p1[0] - 1)  % SQUARE_SIZE][p1[1]] + m[(p2[0] - 1)  % SQUARE_SIZE][p2[1]]
    else:
	    return m[p1[0]][p2[1]] + m[p2[0]][p1[1]]


with open("alphabet", 'r') as a, open("flag_enc", 'r') as e:
    m = generate_square(a.read().strip())
    enc = e.read().strip()
    assert len(enc) % 2 == 0

    msg = ""
    for i in range(0, len(enc), 2):
        msg += decode_pair(m, enc[i:i+2])

    print(msg)

