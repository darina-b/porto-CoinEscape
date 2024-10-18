PROJECT: **CoinEscape**  

AUTHOR: **Darina Bunak**  

TECHNOLOGIES: **Python (OOP, Pygame)**  

##  

**TASK**  
*[This project was made as a part of Advanced Python course, so some restrictions were imposed by the assignment.]*
Build a game in Pygame using only the given images (how many - by choice):
* coin  
* robot
* monster
* door  
##  

![pic_07](https://github.com/user-attachments/assets/81d92b10-c67a-4aaf-b078-08225e9f79cf)
##  

**IDEA**  
Build a shooter game that incorporates all the given assets.  
The
##  

**SOLUTION**  

Each object has its own class: Coin, Robot, Monster, Door, Text - with assigned attributes and functionality.
These individual classes are inherited by the main game class CoinEscape, which contains methods
for handling all of the above classes.
##  


##  

**FUNCTIONALITY**  

- *Start:* Run the code
- *Start screen:* You will see the screen with 12 coins and the door, into which you should shoot as many coins, as you can.
Charging and shooting happens below the horizontal line. Everything above the line is out of your direct control.
- *Actions:* Click below the horizontal line to pick up a coin from the stack, then click again to shoot it into the door
when you find the right moment for it. Beware of monsters and robots, your coin should not touch any of them on its way to the door.

If you hit a *monster* >> the door moves.
If you hit a *robot* >> a new monster appears.

$ CONTROL KEYS:
- *start* == run the code
- *play* == use cursor (one click: charge, two clicks: shoot)
- *end* == close the game window by pressing the 'X' button

Enjoy!
