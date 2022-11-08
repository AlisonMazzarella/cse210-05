# cse210-05
Cycle Game 


# **Overview:**

- Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

## **Rules:**

- Players can move up, down, left, and right. 
- Player 1 moves using the W, S, A and D keys. 
- Player 2 moves using the I, K, J and L keys. 
- Each player's trail grows as they move.
- Players try to maneuver so the opponent collides with their trail.
- If a player collides with their opponent's trail: A "game over" message is displayed in the middle of the screen, the cycles turn white, players keep moving and turning but don’t run into each other. 

**Requirements:**

- The program includes a README file.
- The program includes class and method comments.  
- The program contains 16 classes.
- The game remains true to game play described in the overview.

**Project Structure:**
_The project files are the following:_

- +-- keyboard_input.py 
- +-- video_input.py
- +-- player_one_movement.py 
- +-- player_two_movement.py 
- +-- player_one.py 
- +-- player_two.py 
- +-- director.py 
- +-- draw_screen.py 
- +-- draw_players.py 
- +-- color.py 
- +-- sound.py 
- +-- handle_collision.py 
- +-- score.py
- +-- main.py 
- +-- action.py
- +-- background.py 
- +-- point.py
- +-- cycle1.png
- +-- cycle2.png 
- +-- background.png
- +-- pycache
- +-- README.md

---

_The project files are organized in folders as follows:_

```
root                               
+-- images                         
+-- sound                           
+-- casting
+-- directing
+-- scripting 
+-- services 
+-- shared
+-- pycache
+-- game
+-- cycle                      
+-- README.md                       
```

**Required Technologies:**

- Python 3.8 or greater
- Pygame

## **Authors: (Team E)**

- Mazzarella-Woelzl, Alison Reed (maz12005@byui.edu)
- Saenz, Paula (sae21002@byui.edu)
- Ogboanoh, Richard Oshiomole Ephraim (ogb22001@byui.edu)
- Diab, Garren Mark (dia22004@byui.edu)
