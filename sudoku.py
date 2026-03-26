
oson = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

orta = [
    [0, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 0, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 0]
]

qiyin = [
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 0, 5, 0, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def korish(sudoku):
    for i, row in enumerate(sudoku):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if num != 0:
                print(num, end=" ")
            else:
                print(".", end=" ")
        print()

def tekshirish(num, row, col):
    if num in sudoku[row]:
        return False
    for i in range(9):
        if sudoku[i][col] == num:
            return False
    start_row, start_col = row // 3 * 3, col // 3 * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == num:
                return False
    return True

def son_kiritish(sudoku):
    while True:
        qator = int(input("Qatorni kiriting (0-8): "))
        ustun = int(input("Ustunni kiriting (0-8): "))
        qiymat = int(input("Qiymatni kiriting (1-9): "))
        if not (0 <= qator <= 8 and 0 <= ustun <= 8):
            print("Qator yoki ustun 0 dan 8 gacha bo'lishi kerak.")
            continue
        if not (1 <= qiymat <= 9):
            print("Qiymat 1 dan 9 gacha bo'lishi kerak.")
            continue
        if sudoku[qator][ustun] == 0 and tekshirish(qiymat, qator, ustun):
            sudoku[qator][ustun] = qiymat
            print("Qo'shildi!")
            break
        else:
            print("Bu joyda raqam bor yoki bu joyga qo'yib bo'lmaydi.")

def tanlov():
    while True:
        print("""
1. Oson.
2. O'rta.
3. Qiyin""")
        num = int(input("Tanlovni kiriting: "))
        if num == 1:
            return [row[:] for row in oson]
        elif num == 2:
            return [row[:] for row in orta]
        elif num == 3:
            return [row[:] for row in qiyin]
        else:
            print("Tanlovdigilarni kiriting. ")



sudoku = tanlov()
while True:
    print("""
1. Ko'rish.
2. Son kiritish.
3. Chiqish.
""")
    n = int(input("Tanlovingizni kiriting: "))
    print("")
    if n == 1:
        korish(sudoku)
    elif n == 2:
        son_kiritish(sudoku)
    elif n == 3:
        print("O'yin tugadi.")
        break
    else:
        print("Noto'g'ri tanlov kiritingiz.")

