# The Snake Pit

* This is a straightforward Python terminal-based game. Taking inspiration from a five-point grid-based game, similar to something like BattleShips.
* You play the game crushing the snakes that the opposition has placed in their board.
* This means that you will try and guess where the code computer has placed their randomized points snakes on a 5x5 gird board which you, as the user, cannot see. 


PHOTO

## How To Play 

1. Guess where the computer has their snakes placed in their board.
2. The rows are labeled 1 through 5 
3. Type in two spaced-out digits e.g: "2 3". 
4. See if you were able to guess correctly and have crushed the computer snakes
5. Repeat until a winner is declared!

PHOTO

## Features 

This is based off the popular Battle Ships game, but with an added twist. Here a few images for you to get a feel of the game.

PHOTO

###  Features - Exisiting Features

* Randomly generated board.
 - The board is a 5 by 5 grid but.
 - The user cannot see where the computer has generated the position of their snakes (obviously, as it would be much fun otherwise).

PHOTO 

* The user plays against the comuputer.
* The python code therefor accepts data input from the user.
* The computer also keeps track of the socres. 
* It will not let you enter same data twice. 
* It will not let you enter erronious data, out side the digits of 1 thgroug 5 and the word 'yes' or 'no'. 

PHOTO

PHOTO

###  Features - Future Features 

* The board could be extended to bigger than it currently is. 
* Allow the user to decide where they place their snakes. 

## Testing 

I used the manual testing methods for checking my code: 

- PEP8 
- Feeding it invalid data, outside the previosly stated bounds, to see how it responds. 
- Use my local terminal in my IDE
- Deploying via Heroku to see final product 

### Bugs deteced

- PEP8 informed of many indentation errors, most of which were resolved.
- Í previoulsy tried to add command which I had forgotten to define, therefor sending back an error.

### Bug resolved 

- Fixed indent errors with PEP8
- Made sure I had all required "def" 

## Deployment 

1. Go to Heroku dash board 
2. Click on 'Create a new Heroku app'
3. Set the buildbacks to Python and NodeJS in that order
4. Link you GitHub repo to Heroku app 
5. Click on Deploy!

## Credits 

I used materials for writing game code from online source such as: 
* Code Institute 
* Geeks For Geeks 
* Stack Overflow
* Code Review Stack Exchange  
* Tutorials Point