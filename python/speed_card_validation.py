"""
Validation of the CB number .

The first function is the fastest.

print('', file=sys.stderr, flush=True)
"""
ITERATION = 5000
STMT_TMPL = "$f()"

CARD = C = "4556 7375 8689 9855"  # input

S = (
    0,  # 0 * 2 = 0
    2,  # 1 * 2 = 2
    4,  # 2 * 2 = 4
    6,  # 3 * 2 = 6
    8,  # 4 * 2 = 8
    1,  # 5 * 2 = 10, 10 - 9 = 1
    3,  # 6 * 2 = 12, 12 - 9 = 3
    5,  # 7 * 2 = 14, 14 - 9 = 5
    7,  # 8 * 2 = 16, 16 - 9 = 7
    9,  # 9 * 2 = 18, 18 - 9 = 9
)

A = {'0': 0, '1': 2, '2': 4, '3': 6, '4': 8,
     '5': 1, '6': 3, '7': 5, '8': 7, '9': 9}

B = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
     '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def fastest():  # no respect
    is_valid = (
        A[CARD[0]] + A[CARD[2]] + A[CARD[5]] + A[CARD[7]]
        + A[CARD[10]] + A[CARD[12]] + A[CARD[15]] + A[CARD[17]]
        + B[CARD[1]] + B[CARD[3]] + B[CARD[6]] + B[CARD[8]]
        + B[CARD[11]] + B[CARD[13]] + B[CARD[16]] + B[CARD[18]]
    ) % 10 == 0
    return "YES" if is_valid else "NO"


def no_respect_bis():
    return "NO" if sum(
        A[CARD[a + b]] + B[CARD[a + b + 1]]
        for a in (0, 5, 10, 15) for b in (0, 2)
    ) % 10 else "YES"


def monster():
    t = (
        S[int(C[0])] + S[int(C[2])] + S[int(C[5])] + S[int(C[7])]
        + S[int(C[10])] + S[int(C[12])] + S[int(C[15])] + S[int(C[17])]
        + int(C[1]) + int(C[3]) + int(C[6]) + int(C[8])
        + int(C[11]) + int(C[13]) + int(C[16]) + int(C[18])
    )
    return "NO" if t % 10 else "YES"


def dev():  # direct modulo without lambda
    card = CARD.replace(' ', '')
    odd = (S[int(d)] for d in card[::2])
    even = (int(d) for d in card[1::2])
    return "NO" if (sum(odd) + sum(even)) % 10 else "YES"


def original():
    _is_divisible_by10 = lambda x: x % 10 == 0

    card = CARD.replace(' ', '')
    odd = (S[int(d)] for d in card[::2])
    even = (int(d) for d in card[1::2])
    return "YES" if _is_divisible_by10(sum(odd)+sum(even)) else "NO"


def most_vote_on_codingame():
    card = [int(i) for i in CARD if i.isdigit()]
    tot = sum(card) + sum(i if i < 5 else i - 9 for i in card[::2])
    return "NO" if tot % 10 else "YES"


def dev3():
    def compute(x):
        double = int(x) * 2
        if double < 10:
            return double
        else:
            return double - 9

    card = CARD.replace(' ', '')

    odd = (compute(d) for d in card[::2])
    even = (int(d) for d in card[1::2])
    return "NO" if (sum(odd) + sum(even)) % 10 else "YES"


def dev2():
    card = CARD.replace(' ', '')
    odd = (
        int(d) * 2
        if (int(d) * 2) < 10 else (int(d) * 2) - 9
        for d in card[::2]
    )
    even = (
        int(d)
        for d in card[1::2]
    )
    return "NO" if (sum(odd) + sum(even)) % 10 else "YES"
