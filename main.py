import random


MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = { 
    "A":2,
    "B":4,
    "C":8,
    "D":10
}
symbol_value = { 
    "A":10,
    "B":7,
    "C":3,
    "D":1.4
}
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines): 
        symbol = columns[0][line] 
        for column in columns: 
            symbol_to_check = column[line]
            if(symbol != symbol_to_check):
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line+1)
    return winnings, winning_lines





# for getting the random sequence 
def get_slot_machine_spin(rows,cols,symbols) : 
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
    
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row],end = " | ")  
            else: 
                print(column[row])  



def deposit():
    while True:
        amount = input("enter the amount to be deposited: $")
        if amount.isdigit():
            amount = int(amount)
            if(amount>0):
                break
            else:
                print("please enter the amount > 0 ")
        else:
            print("please enter a number") 
    return amount
def get_number_of_lines():
    while True:
        lines = input("enter the number of lines (1-"+str(MAX_LINES)+") :")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES :
                break
            else:
                print("please enter the number of lines  > 0  and less than "+str(MAX_LINES)+")")
        else:
            print("please enter a number") 
    return lines
def get_bet():
    while True:
        amount = input("what would you like to bet on each line:  $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<=amount <=MAX_BET :
                break
            else:
                print(f"please enter the amount between ${MIN_BET} and ${MAX_BET}") 
        else:
            print("please enter a number") 
    return amount

def spin(balance):
    while True: 
        lines = get_number_of_lines()
        bet = get_bet()
        totalAmount  = bet*lines
        if(totalAmount > balance):
            print(f"you do not have enough balance \nyour balance amount is {balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines. total amount of bet is ${totalAmount}")
    
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines , bet , symbol_value)
    print(f"you have won ${winnings} on {winning_lines}" )
    return winnings - totalAmount

def main():
    balance = deposit() 
    while True:
        print(f"current Balance is ${balance} ")
        anwer = input("Press enter to play (q to quit)")
        if anwer == "q" :
            break
        else : 
            balance += spin(balance)
    print(f"you are left with {balance}")


main()