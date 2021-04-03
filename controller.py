

import pygame


class controller(object):
    def __init__(self):
        
        #self.trust=0.0;
        #self.x=0.0
        #self.y=0.0
        #self.z=0.0
        self.good=0

        try:
            pygame.init()
            pygame.joystick.init()

            if(pygame.joystick.get_init()): self.good = 1
            else:self.good = 0

            if (2 == pygame.joystick.get_count()): self.good = 1

            else :self.good = 0

        

            self.trust = pygame.joystick.Joystick(1)
            self.handle = pygame.joystick.Joystick(0)

            self.trust.init()
            self.handle.init()

            if(self.handle.get_name() == 'T.A320 Pilot'): self.good = 1
            else:self.good = 0
            'TCA Q-Eng 1&2'
            if(self.trust.get_name() == 'TCA Q-Eng 1&2'): self.good = 1
            else:self.good = 0
            if(self.good):print('控制器一切连接就绪')
            else: print('连接错误')

        except:
            print('控制器未能成功连接')


    def get_val(self):
        pygame.event.get()
        out=[]#x：左负右正,y：上负下正,z左手定则 ,trust上负下正
        for a in range(3):
            out.append(self.handle.get_axis(a))
        out.append(self.trust.get_axis(1))
        out.append(self.trust.get_button(7))#按键号-1
        return out
            


        #print(pygame.joystick.Joystick.get_name(0))



rocket= controller();

clock = pygame.time.Clock()


#测试代码
#while(1):
    
#    print(rocket.get_val())
#    clock.tick(30)
