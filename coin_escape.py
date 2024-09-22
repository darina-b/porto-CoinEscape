'''
$ PROJECT NAME: CoinEscape, game

$ IDEA: Build a Pygame shooter using only the given images: coin, robot, monster, door.

$ CODE BASICS: Each object has its own class: Coin, Robot, Monster, Door, Text - with assigned attributes and functionality. These individual classes are inherited by the main game class CoinEscape, which contains methods for handling all of the above classes.

$ GAME INSTRUCTIONS:

Start: Run the code
Start screen: You will see the screen with 12 coins and the door, into which you should shoot as many coins, as you can. Charging and shooting happens below the horizontal line. Everything above the line is out of your direct control.
Actions: Click below the horizontal line to pick up a coin from the stack, then click again to shoot it into the door when you find the right moment for it. Beware of monsters and robots, your coin should not touch any of them on its way to the door.
If you hit a monster >> the door moves. If you hit a robot >> a new monster appears.

$ CONTROL KEYS:

start == run the code
play == use cursor (one click: charge, two clicks: shoot)
end == close the game window by pressing the 'X' button
Enjoy!
'''
import pygame
import random
import itertools

# COIN - class and related methods:
class Coin: 
    c_map=[[1,2,3,4], 
          [5,6,7,8],
          [9,10,11,12]]

    available_coins=[]     
    next_coin= []
    tossed_coins=[]

    def __init__(self):
        self.coin=pygame.image.load("coin.png")
        self.w=self.coin.get_width()
        self.h=self.coin.get_height()
        self.nr=00
        self.tossed=False
        self.next=False
        self.velocity=0
        self.x=550
        self.y=1050
    
    def all_coins (self):
        return list(itertools.chain.from_iterable([self.available_coins,self.tossed_coins,self.next_coin]))
    
    def create_coins(self):       
        for i in range(len(self.c_map)):
            for ii in range(len(self.c_map[i])):
                if self.c_map[i][ii]!=0: 
                    c=Coin()
                    c.nr=self.c_map[i][ii]          
                    c.x=(ii+1)*100-c.w/2
                    c.y=840+(i+1)*20
                    self.c_map[i][ii]=c
                    self.available_coins.append(c)                   
                else:
                    pass

    def choose_a_coin (self):
        if self.attempts_left()>0:
            for i in self.c_map:
                for ii in i:
                    if type(ii) is Coin:
                        ii.next=True   
                        self.next_coin.append(ii)                     
                        self.available_coins.remove(ii)                        
                        i[i.index(ii)]=0
                        return                        
        else:
            pass 

    def pick_coin(self,x,y):
        try:
            self.hit=False
            self.next_coin[-1].x = x-self.next_coin[-1].w/2
            self.next_coin[-1].y = y-self.next_coin[-1].h/2   
        except:
            raise IndexError("NOT WORKING! (pick_coin)!")
        
    def toss_coin(self):
        try:
            self.tossed_coins.append(self.next_coin[-1])                 
            self.tossed_coins[-1].next=False
            self.tossed_coins[-1].tossed=True
            self.next_coin=[]
        except:
            raise IndexError("NOT WORKING! (toss_coin)")
        
    def off_you_go(self):
        for c in self.tossed_coins:
            if c.tossed:
                c.velocity = 9
                c.y -= c.velocity
            else:
                self.tossed_coins.remove(c)
        
    def clean_tossed(self):
        for c in self.tossed_coins:
            if c.y < -c.h:
                c.tossed=False

    def attempts_left(self):
        return len(self.available_coins) + len(self.next_coin)
    
# MONSTER - class and related methods:
class Monster:
    all_monsters=[]
    def __init__(self):
        self.monster=pygame.image.load("monster.png")
        self.w=self.monster.get_width()
        self.h=self.monster.get_height()
        self.nr=len(self.all_monsters)+1
        self.x=600
        self.y=1100
        self.velocity=0
        
    def add_monster(self,x,y,velocity):       
        m=Monster()
        m.x=x
        m.y=y
        m.velocity=velocity
        self.all_monsters.append(m)
        return m

# ROBOT - class and related methods:
class Robot:    
    range_x=[]
    range_y=[]

    all_robots=[]
        
    def __init__(self):
        self.robot=pygame.image.load("robot.png")
        self.w=self.robot.get_width()
        self.h=self.robot.get_height()
        self.nr=len(self.all_robots)+1
        self.x=600
        self.y=1100
        self.velocity=0        
    
    def robot_xy(self, range_1, range_2):
        return (random.choice(range_1),260+random.choice(range_2))
        
    def add_robot(self, range_1, range_2):
        r=Robot()
        r.x=self.robot_xy(range_1,range_2)[0]
        r.y=self.robot_xy(range_1,range_2)[1]
        self.all_robots.append(r)
        self.range_x.append(range_1)
        self.range_y.append(range_2)
        return r

# DOOR - class and related methods:
class Door:
    all_doors=[]
    def __init__(self):
        self.door = pygame.image.load("door.png")
        self.w=self.door.get_width()
        self.h=self.door.get_height()
        self.nr=len(self.all_doors)+1
        self.x=600
        self.y=1100
        self.velocity=0
        
    def add_door(self, x, y):
        d=Door()
        d.x=x
        d.y=y
        self.all_doors.append(d)
        return d

# TEXT - class and related methods (font settings for different use cases):        
class Text:
    all_texts=[]
    
    def __init__(self):
        pygame.font.init()
        self.game_font = pygame.font.SysFont("Arial", 18,bold=False, italic=False)
        self.bold_font=pygame.font.SysFont("Arial", 32,bold=True, italic=False)
        self.big_font=pygame.font.SysFont("Arial", 28,bold=False, italic=False)
        self.colour=(0, 0, 0)
        self.bold_colour=(255, 249, 51)
        self.antialias=True
        self.background=None
        self.nr=len(self.all_texts)+1
        self.message=""
        self.x=600
        self.y=1100
        
    def create_text(self, message: str, x: int, y: int, bold=False, big=False):
        if big==True:
            t=Text()
            t.message=message
            t.x=x
            t.y=y       
            tt=self.big_font.render(message, self.antialias, self.bold_colour)
            self.all_texts.append((tt,t)) 
        if bold==True:
            t=Text()
            t.message=message
            t.x=x
            t.y=y       
            tt=self.bold_font.render(message, self.antialias, self.bold_colour,(0, 0, 0))
            self.all_texts.append((tt,t)) 
        else:
            t=Text()
            t.message=message
            t.x=x
            t.y=y       
            tt=self.game_font.render(message, self.antialias, self.colour)
            self.all_texts.append((tt,t)) 
        
# COINESCAPE - the main game class and all related methods 
# (controls all assets and game events - based on the Objects from classes defined above):
class CoinEscape(Coin,Door,Monster,Robot,Text):
    clicks=0
    collisions_monsters=[]
    collisions_robots=[]
    hits_dirty=[]
    score=0
        
    def __init__(self):
        Coin.__init__(self)
        Door.__init__(self)
        Monster.__init__(self)
        Robot.__init__(self)
        Text.__init__(self)
        pygame.init()
        self.background=(150,150,150)
        self.window_w=500
        self.window_h=1000
        self.window = pygame.display.set_mode((self.window_w, self.window_h))
        pygame.display.set_caption("Coin Escape by D.B. for Python Programming-2024")
        self.gameover= False
        self.toss=False
        self.charge=False
        self.hit=False
        self.end=False        
        pygame.init()
        self.main_loop() # immediate start of the game
        
    def create_assets(self):
        self.create_coins()        
        door_1= self.add_door(random.choice(range(0,450)),10) 
        robot_1= self.add_robot(range(0,450),[5,45]) 
        robot_2= self.add_robot(range(0,450),[230,270])
        monster_1= self.add_monster(0,120,2)
        monster_2= self.add_monster(400,400,2.7)
        self.create_texts()

    def create_texts(self):
        self.create_text("Try to toss all the coins through the door safely",10, 955, False, False)
        self.create_text("Monsters only steal coins, but robots summon extra monsters",10, 975, False, False)
        self.create_text("TO SHOOT: CLICK ANYWHERE BELOW DOUBLE LINE",65, 725, False, False)
        self.create_text(f"Coins left:{self.attempts_left()}/12",10, 760, False, False)
        self.create_text("Score:",390, 760, False, False)
        self.create_text(f"{self.score}",420, 760, False, False)

    def check_clicks(self):            
        if self.clicks%2==0:
            self.toss=True
            self.charge=False
        else:
            self.toss=False
            self.charge=True
   
    def robots_jump(self):
        for r in self.all_robots:            
            m=self.all_monsters[0]
            if m.x==random.randrange(0,450,150) or m.x==random.randrange(0,450,90): #or m.x==random.randrange(0,450,30):

                z=self.robot_xy(self.range_x[r.nr-1],self.range_y[r.nr-1])
                r.x=z[0]
                r.y=z[1]

                if m.x+m.w>self.window_w or m.x<0:
                    z=self.robot_xy(self.range_x[r.nr-1],self.range_y[r.nr-1])
                    r.x=z[0]
                    r.y=z[1]

    def doors_jump(self):
        if self.all_doors==[]:
            pass
        elif len(self.all_doors)==1:
            self.all_doors[0].x=random.randint(0,400)  
        else:
            for d in random.choice(self.all_doors):
                d.x=random.randint(0,400)   

    def monsters_turn(self):
        for m in self.all_monsters:
            m.x += m.velocity
            if m.x+m.w>= self.window_w or m.x<=0:
                m.velocity=-m.velocity

    def hits (self):
        a=self.score
        d=self.all_doors[0]
        door_rect=d.door.get_rect(topleft = (d.x, d.y))
        for c in self.tossed_coins:
            coin_rect = c.coin.get_rect(topleft = (c.x, c.y))
            if coin_rect.colliderect(door_rect):
                self.hits_dirty.append(c)
                self.score=len(set(self.hits_dirty))
        if self.score-a>0:
            self.hit=True
            self.background=(random.choice(range(50,255)),random.choice(range(50,255)),random.choice(range(50,255)))
            self.update_window()

    def collision_monsters (self):
        for c in self.tossed_coins:
            coin_rect = c.coin.get_rect(topleft = (c.x, c.y))
            for m in self.all_monsters:
                monster_rect=m.monster.get_rect(topleft = (m.x, m.y))
                if coin_rect.colliderect(monster_rect):
                    self.tossed_coins.remove(c)
                    self.collisions_monsters.append(m)
                    self.doors_jump()
                    return True

    def collision_robots (self):
        for c in self.tossed_coins:
            coin_rect = c.coin.get_rect(topleft = (c.x, c.y))
            for r in self.all_robots:
                robot_rect=r.robot.get_rect(topleft = (r.x, r.y))
                if coin_rect.colliderect(robot_rect):
                    self.tossed_coins.remove(c)
                    self.collisions_robots.append(r)

                    if self.collisions_robots.count(r)==1:
                        monster_3= self.add_monster(400,120,3.1)
                    if self.collisions_robots.count(r)==2:
                        monster_4= self.add_monster(0,400,3.1)
                    if self.collisions_robots.count(r)==3:
                        r.robot=pygame.image.load("monster.png")
   
    def draw_lines(self):
        pygame.draw.line(self.window, (0, 0, 0), (0,755), (500, 755), 2)
        pygame.draw.line(self.window, (0, 0, 0), (0,750), (500, 750), 2)
        pygame.draw.line(self.window, (0, 0, 0), (0,950), (500, 950), 2)
          
    def check_events(self): 
        while self.end==False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end=True
                    exit()

            clock = pygame.time.Clock()
            
            while self.gameover==False:
                    
                if self.attempts_left()==0 and len (self.tossed_coins)==0:
                    self.gameover=True

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.end=True
                        exit()

                    if event.type == pygame.MOUSEMOTION and event.pos[1]>775 and event.pos[0]>=20 and event.pos[0]<=500-20:                        
                        if self.charge:
                            self.pick_coin(event.pos[0],event.pos[1])
                       
                    if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]>=20 and event.pos[0]<=500-20 and event.pos[1]>775-20:
                        self.clicks+=1
                        self.check_clicks()

                        if self.charge:
                            self.choose_a_coin() 
                            self.pick_coin(event.pos[0],event.pos[1]) 

                        if self.toss: 
                            self.toss_coin() 
                        
                self.off_you_go()                
                self.robots_jump()
                self.monsters_turn()
                self.collision_monsters()
                self.collision_robots()
                self.hits()                
                self.update_window()
                self.clean_tossed()

                clock.tick(60)
            
            if self.gameover:
                self.game_over()
       
    def blit_all_coins (self):
        for i in self.all_coins():
            self.window.blit(i.coin, (i.x, i.y))
        
    def blit_all_monsters (self): 
        for i in self.all_monsters:
            self.window.blit(i.monster, (i.x, i.y))
        
    def blit_all_robots (self): 
        for i in self.all_robots:
            self.window.blit(i.robot, (i.x, i.y))

    def blit_all_doors (self): 
        for i in self.all_doors:
            self.window.blit(i.door, (i.x, i.y))

    def update_all_texts(self):
        z=self.score
        if len(self.all_texts)>=5:
            self.all_texts=self.all_texts[:3]

        self.create_text(f"Coins left:{self.attempts_left()}/12",10, 760)
        self.create_text("Score:",390, 760)

        if self.hit==True:
            self.create_text(f"{self.score}",450, 760, True, True)
        else:
            self.create_text(f"{self.score}",450, 760)
                
        for i in self.all_texts:
            self.window.blit(i[0], (i[1].x, i[1].y))

    def update_window(self):
        self.window.fill(self.background)        
        self.draw_lines()        
        self.update_all_texts()
        self.blit_all_coins()
        self.blit_all_robots()
        self.blit_all_doors()
        self.blit_all_monsters()
        pygame.display.flip()

    def game_over (self):
        if self.gameover:
            self.window.fill((150,150,150))

            t1=self.bold_font.render("GAME OVER", True, (255, 249, 51))
            t1_x=self.window_w/2-t1.get_width()/2
            self.window.blit(t1,(t1_x,300))

            t2=self.bold_font.render(f"Your score is: {self.score} / 12", True, (255, 249, 51))
            t2_x=self.window_w/2-t2.get_width()/2
            self.window.blit(t2,(t2_x,400))

            if self.score <5:
                t3=self.big_font.render("Come on, you can do better!", True, (255, 249, 51))
                t3_x=self.window_w/2-t3.get_width()/2
                self.window.blit(t3,(t3_x,500))

            elif self.score>8:
                t4=self.big_font.render("Wow! Impressive results!", True, (255, 249, 51))
                t4_x=self.window_w/2-t4.get_width()/2
                self.window.blit(t4,(t4_x,500))
            else:
                t5=self.big_font.render("Well done!", True, (255, 249, 51))
                t5_x=self.window_w/2-t5.get_width()/2
                self.window.blit(t5,(t5_x,500))
            pygame.display.flip()

    def main_loop(self):
        self.create_assets()
        self.check_events()
        
if __name__=="__main__":
    CoinEscape()
