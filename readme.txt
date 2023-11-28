class MasterMind is the backend class, which allows to play logic game Master Mind. In the Czech republic is this game known under the name Logic.

Rules of game:

It is game for 2 players. One player is codemaker. Second player is codebreaker. Target of the game is to break secret code.
Standard version: 
There are code pegs in 8 different colors. They have round head. There are 5 holes. Guessing player inserts into each hole one code peg. The colors of code pegs can be repeated in any way.
There are key pegs, which are black and white. Key pegs are fleat-headed and are smaller than code pegs.
On the beginning, codemaker create secret combination and coverd it by the shield. The secret combination is visible for codemaker, but not for codebreaker.
Codebreaker try to quess the pattern. He inserts code pegs into holes. When he finished his attempt, codemaker check and evaluate it. He inserts key pegs into small holes on the left from code pegs.
On the beginning, he insert black key pegs into holes, then white key pegs. He insert key pegs from left to right, independently on position of code pegs.
Black peg means good value on good place. White peg means good value, but on bad position.
The game continue until codemaker break the secret code or all attempts are exhausted.

The old variation:
There ist 6 different colors. There are 4 holes. There is usually also 10 attempts. Rest of the rules is the same as by standard version.

Stuff in if __name__ == "__main__":

Class MasterMind is primarily intended as frontend for larger projects. It should be imported in this case.
But for testing purposes and to allow play game in single command line, this code snippet is used.
It is also tutorial for better understanding for using of class MasterMind.

    attempt = 10 # you have 10 attempts
    value = 6 # value can be 1 , 2, 3, 4, 5, 6
    digit = 4 # 4 digits of secret code
    time = 5  #5 minutes to break code
    the_game = MasterMind(attempt, value, digit, time)
Initiate class MasterMind as the_game.


print(repr(the_game))
generate report about actual state of current game.


while the_game.is_running():
  .....
Pooling of the flag for game running.
Until the game is active, you can try to break the secret code.
print(repr(the_game)) inform you about actual state of current game.
When the game is over, this flag is cleared.

When game is over, final game report is generated and saved to the file.

Description of class MasterMind and how to use it:
class Attempt:
class Attempt is part of class MasterMind. For each attempt to break code, one object of class MasterMind.

def __init__(
        self, att_no, your_code=[], white=0, black=0, duration=datetime.time(0)
    ):
For new attempt is new object initialised. Its attributes are:
 att_no  ... index of attempt
 your_code ... value of quessed code
 white = number of white code pegs
 white = number of black code pegs
 duration = time per attempt

def __repr__(self):
Return text string with values of this attempt.
