import numpy as np
import time
from controller import Controller
from screenview import Screenview

class Game:
    static_templates = {
        'Sprites/InI1.jpg', 
        'Sprites/InI1R.jpg'
    }
    def __init__(self):
        
        self.controller = Controller()
        self.screen = Screenview()
        
        

    def run_bot(self):
        print('Por quanto tempo quer que o Bot rode:')
        x= input('Insira o tempo')
        x =float(x)
        time.sleep(3)
        loop_time = time.time() + x*60
        while time.time()<loop_time:
            for img in Game.static_templates:
                print(img);
                self.find_enemy_attack(img)
            time.sleep(0.5)
            


    def find_enemy_attack(self, enemy):
        pos = self.screen.img_compare(enemy)
        #print(pos)
        if pos[0]>0:
            x=pos[1]
            y=pos[2]
            print('atacando')
            print(pos)  
            time.sleep(3)
            self.controller.move_mouse_press(x,y)
        else:
            #print('saindo')
            self.controller.leave()

    

        

   

        
        


