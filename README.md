PROJECT: **CoinEscape**  

AUTHOR: **Darina Bunak**  

TECHNOLOGIES: **Python (OOP, Pygame)**  

##  

**TASK**  

*This project was made as a part of a course, so some restrictions were imposed by the course assignment.*  
Build a game in Pygame using only the given images (how many - by choice):
* coin  
* robot
* monster
* door  
![pic_07](https://github.com/user-attachments/assets/81d92b10-c67a-4aaf-b078-08225e9f79cf)
##  

**IDEA**  

***'CoinEscape'** = you have to **help coins escape through the door** while avoiding collisions with anyone/enything*

**1.** Build a shooter game that incorporates all the given assets.   
**2.** Make it visually stimulating through colours and effects to encourage more scores.  
**3.** The game-over statistics should have some personal touch - based on the final score.  
##  

**SOLUTION**  

The game is coded in Python (Pygame) using the principles of Object-Oriented Programming (OOP).  
Each game asset has its **own class** - Coin, Robot, Monster, Door, Text - with relevant attributes and functionality.
These individual classes are **inherited by the main game class** CoinEscape, which contains methods
for handling all of the above classes.   
Coin placement is based on a **matrix**. Direction- and coulour changes are based on **random** distribution.  



![001-2](https://github.com/user-attachments/assets/d2040c21-3512-40d9-9708-7fce4312a8d2)
Every new score changes the **background colour** and enlarges the **score font** to emphasise the achievement.
##  

**FUNCTIONALITY**  

- *Start:* Run the code
- *Start screen:* You will see the screen with 12 coins and the door, into which you should shoot as many coins, as you can.
**Charging and shooting happens below the horizontal line.** Everything above the line is out of your direct control.
- *Actions:* Click below the horizontal line to pick up a coin from the stack, then click again to shoot it into the door
when you find the right moment for it. Beware of monsters and robots, your coin should not touch any of them on its way to the door.

If you hit a *monster* >> the door moves.  
If you hit a *robot* >> a new monster appears.  
If you *hit a robot too many times* >> it turns into a monster too.

![002](https://github.com/user-attachments/assets/4824accc-faeb-4e9e-b5be-5c9a84df4857)
##  

**CONTROL KEYS**

- *start* == run the code
- *play* == use cursor (one click: charge, two clicks: shoot)
- *end* == close the game window by pressing the 'X' button

***Enjoy!***
