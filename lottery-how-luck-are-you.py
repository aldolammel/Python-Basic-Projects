from random import randrange

_userChoices = {2, 3, 13, 28, 30, 56}   # select your numbers, min 6 numbers, max 7.
_maxMatches = 6
_midMatches = 5
_minMatches = 4
_maxPot = 100000000  # 100.000.000
_midPot = 3000000    # 3.000.000
_minPot = 50000      # 50.000
_gamesCounter = 0
_years = int(input('How many years do you want to try monthly the lottery: '))
_gameLimiter = _years * 12    # X tries!
_minWin = 0          # how many times the player won the minimal pot.
_midWin = 0          # how many times the player won the middle pot.

# Cost per game (R$):
if len(_userChoices) == 6:
    _gamesCost = 4.5
if len(_userChoices) == 7:
    _gamesCost = 31.5

# lottery system:
while True:
    _game = set()               # because set doesn't accept duplicate values.
    _NumsInGame = 0             # how much numbers the player have. If 6, the game is finished.
    _rightNums = 0              # how much numbers the player hit.

    while True:
        _num = randrange(1, 60)
        if _num not in _game:
            _game.add(_num)
            _NumsInGame += 1
            if _num in _userChoices:
                _rightNums += 1

        if _NumsInGame == 6:
            _gameTuple = tuple(_game)    # converting the result from set to tuple for avoid result changes.
            _game.clear()
            break

    if _rightNums < _maxMatches:
        print(f'Your game: {_userChoices} || ', end='')
        print('Result: {', end=' ')
        for i in _gameTuple:
            if i in _userChoices:
                print(f'\033[1;32m{i}\033[m', end=' ')
            else:
                print(i, end=' ')
        print('}', end=' ')
        print(f'|| Cost so far: R$-{_gamesCost * (_gamesCounter + 1):.2f}', end=' ')
        if _rightNums >= _minMatches:
            print('<<<----------------------------== You won: R$', end='')
            if _rightNums == _minMatches:
                _minWin += 1
                print(_minPot, end='')
            if _rightNums == _midMatches:
                _midWin += 1
                print(_midPot, end='')
        print()
    else:
        print(f'\nYOU WON !!!'
              f'\nNumbers drawn: {_gameTuple}'
              f'\nYour winner game: {_userChoices}'
              f'\nYou\'ve played {_gamesCounter} times and invest R${_gamesCost * _gamesCounter} to win R${_maxPot:.2f}.'
              f'\nThe profit was R${_maxPot - _gamesCost:.2f}.')
        break

    _gamesCounter += 1

    if _gamesCounter == _gameLimiter:
        if _minWin == 0:
            print('\n\033[1;31mSORRY!\033[m')
        else:
            if _minWin > 0:
                print(f'\nYou won the MINIMAL pot {_minWin} time(s). The total is: \033[1;32m{_minWin * _minPot:.2f}\033[m!'
                      f'\nYour prolif is: {(_minWin * _minPot) - (_gamesCost * _gameLimiter):.2f}')
            if _midWin > 0:
                print(f'\nYou won the MIDDLE pot {_midWin} time(s). The total is: \033[1;32m{_midWin * _midPot:.2f}\033[m!'
                      f'\nYour prolif is: {(_midWin * _midPot) - (_gamesCost * _gameLimiter):.2f}')
        print(f'\nYou have played {_gameLimiter} times.'
              f'\nYou already spent R${_gamesCost * _gameLimiter:.2f}')
        break
