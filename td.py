import random
import pandas as pd
class GridWorld():
    def __init__(self):
        self.x=0
        self.y=0
        
    def step(self,a):
        if a==0:
            self.move_right()
            
        elif a==1:
            self.move_left()
            
        elif a==2:
            self.move_up()
        
        elif a==3:
            self.move_down()
        
        reward=-1
        done=self.is_done()
        
        return reward,done
    
    def move_right(self):
        self.y+=1
        
        if self.y>3:
            self.y=3
            
    def move_left(self):
        self.y-=1
        
        if self.y<0:
            self.y=0
            
    def move_up(self):
        self.x-=1
        
        if self.x<0:
            self.x=0
            
    def move_down(self):
        self.x+=1
        
        if self.x>3:
            self.x=3
            
    def is_done(self):
        if self.x==3 and self.y==3:
            return True
        
        else:
            return False
    
    def get_state(self):
        return (self.x,self.y) 
    
    def reset(self):
        self.x=0
        self.y=0
        return (self.x,self.y)
    
class Agent ():
    def __init__ (self):
        pass
    
    def select_action(self):
        coin=random.random()
        
        if coin<0.25:
            action=0
            
        elif coin<0.5:
            action=1
        
        elif coin<0.75:
            action=2
            
        else:
            action=3
       
        return action
    
    
def main():
    env=GridWorld()
    agent=Agent()
    data=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    gamma=1.0
    alpha=0.01
    
    for k in range(50000):
        done=False
        while not done:
            x,y=env.get_state()
            action=agent.select_action()
            reward,done=env.step(action)
            x_prime,y_prime=env.get_state()
            data[x][y]=data[x][y]+alpha*(reward+gamma*data[x_prime][y_prime]-data[x][y])
        env.reset()
    
    df=pd.DataFrame(data)
    print(df)

main()
        