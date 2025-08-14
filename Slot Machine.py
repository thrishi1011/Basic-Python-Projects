import random

bal = 100
symbols = ['🍒', '🍉', '🥥', '🍊']

def selection():
    return [random.choice(symbols) for _ in range(3)]
def rows(result):
    print("*******************")
    print(' | '.join(result))
    if result[0] == result[1] == result[2]:
        print("*******************")
        print('You win!🥳🥳!')
    else:
        print("*******************")
        print('You lose😞')
        print("*******************************")


while True:
    print('welcome to python solt machine')
    print('symbols: 🍒, 🍉, 🥥, 🍊')
    print(f'The balance of your account is {bal} ')
    bet = int(input('Enter the bet amount or enter 0 to exit: '))
    if bet < 0:
        print('The amount of the bet should be greater than zero')
        continue
    elif bet > bal:
        print('Insufficient funds')
        break
    elif bet == 0:
        break

    result = selection()
    rows(result)


    if result[0] == result[1] == result[2]:
        bal += bet * 2
    else:
        bal -= bet
