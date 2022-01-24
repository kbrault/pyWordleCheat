# pyWordleCheat
A simple Wordle solver with no real intelligence nor complexity optimization

# TODO : 
* Guest words based on letters appearance percentage
* Optimize complexity
* Colorization of the script to make it more user friendly

# Usage :
```shell
Launch ./python main.go
```

```shell
./python main.py
--------------------------------------------------------------------------------------
--                                  Wordle Solver                                   --
--------------------------------------------------------------------------------------
There is  5757 five letters words in my dictionary (words.txt)
Hint the first word (how about "ADIEU" to find a maximum of vowels ?) :
Your hint  1 /5 :
adieu
Your hint is : adieu
What is the result (example : "__X_O" where "_" doesn't exist, "X" exist, "O" is correct) :
_____
486 possible words.
['story', 'known', 'short', 'shown', 'front', 'shows', 'color', 'forms', 'floor', 'books', 'north', 'looks', 'wrong', 'rocks', 'works', 'songs', 'knows', 'brown', 'forth', 'month', 'cross', 'grown', 'crops', 'roots', 'shook', 'cloth', 'worth', 'towns', 'tools', 'block', 'clock', 'grows', 'storm', 'stock', 'sorry', 'throw', 'costs', 'honor', 'worry' [...]
Your hint  2 /5 :
howls
Your hint is : howls
What is the result (example : "__X_O" where "_" doesn't exist, "X" exist, "O" is correct) :
_O__O
76 possible words.
['forms', 'books', 'rocks', 'songs', 'roots', 'costs', 'rooms', 'boots', 'sorts', 'posts', 'ports', 'socks', 'roofs', 'moons', 'bombs', 'cooks', 'fonts', 'tombs', 'forts', 'corps', 'forks', 'combs', 'tongs', 'cocks', 'booms', 'monks', 'moors', 'mocks', 'toots', 'zooms', 'morns', 'nooks', 'corks', 'corns', 'coops', 'bongs', 'cocos', 'rooks', 'romps', 'noons', 'soots', 'goons', 'norms', 'coons', 'gongs', 'coots', 'kooks', 'boors', 'bozos', 'jocks', 'toons', 'torts', 'comps', 'goofs', 'yoyos', 'boobs', 'boons', 'conks', 'toffs', 'morts', 'corms', 'foots', 'bocks', 'softs', 'pocks', 'poops', 'boffs', 'mosts', 'porks', 'bonks', 'zonks', 'pomps', 'topos', 'moots', 'zooks', 'gooks']
Your hint  3 /5 :
jocks 
Your hint is : jocks
What is the result (example : "__X_O" where "_" doesn't exist, "X" exist, "O" is correct) :
_O_OO
11 possible words.
['books', 'forks', 'monks', 'nooks', 'rooks', 'kooks', 'porks', 'bonks', 'zonks', 'zooks', 'gooks']
Your hint  4 /5 :
porks
Your hint is : porks
What is the result (example : "__X_O" where "_" doesn't exist, "X" exist, "O" is correct) :
_O_OO
8 possible words.
['books', 'monks', 'nooks', 'kooks', 'bonks', 'zonks', 'zooks', 'gooks']
Your hint  5 /5 :
monks
Your hint is : monks
What is the result (example : "__X_O" where "_" doesn't exist, "X" exist, "O" is correct) :
OOOOO
1 possible words.
['monks']
```