import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
# here i put 2 A, 4 B, 6 C, 8 D


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # right a for loop to add how many symbols we have here  into the all_symbols list
    for symbol, symbol_count in symbols.items():
        # symbols.items give me the key and the value in the dict
        # i wanna add this symboles to the all_symbols
        # symbol the key, and symbole_count the value
        for _ in range(symbol_count):
            # i am looping in range of the symbole_count which is the value of the key
            all_symbols.append(symbol)
            # msln bi awal whde l A l value 2 ye3ne bade hota marten bl list all_symbole
            # y3ne l khoulasa bmsk l symbol w bzido bl all_symbol 3a add ma l value tab3o bl dict (symbol_count)
            # for example
            # ['A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D']

    columns = []
    for _ in range(cols):
        # for every col we want to generate a certain number of symbols
        column = []
        current_symbols = all_symbols[:]
        # hek bkoun 3mlt copy lal allsymbols
        # kermel bade kel ma na2e symbol shil 3adad menno
        # msln na2et A ken 3nde tnen A bshil whde
        for _ in range(rows):
            # we loop throw the number of values that we need to generate
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            # get the first value in the list and remove it
            column.append(value)
        columns.append(column)

    return columns


"""
this is an example of the list columns
[
    ['B', 'A', 'D'],  # Column 1
    ['C', 'C', 'B'],  # Column 2
    ['A', 'D', 'B'],  # Column 3
]
"""


def print_slot_machine(columns):
    """
    [
        ['A', 'B', 'C'],  # Column 1
        ['D', 'E', 'F'],  # Column 2
        ['G', 'H', 'I'],  # Column 3
    ]
    ma3e yeha hek bade yeha:

    A | D | G
    B | E | H
    C | F | I
    """
    for row in range(len(columns[0])):
        # the first column ['A', 'B', 'C'] l len taba3o
        # gives the num of rows in each col
        # loops through the row indices from 0 to len(columns[0]- 1)
        for i, column in enumerate(columns):
            # now i'm looping in all of the items inside of column
            # it gives me every individual column
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
    # we loop for every single row we have
    # for every single row we loop for every single column
    # and for every col we print the current row
    # we print masln row 0 kello byrja3 row 1 ...


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:

        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You don't have enough to bet the amount, your current balance:${balance}")

        else:
            break

    print(f"You are betting ${bet} on {
          lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()
