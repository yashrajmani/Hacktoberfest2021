'''hello everyone!!! I am Pratyush and this is a basic pybullet project to visualize Fibonacci numbers using simulation.''' 

import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


x=[]                
ball=[]              

for i in range(1000):

    planeId = p.loadURDF("plane.urdf")     #loading the plane
    p.setGravity(0,0,-10)                  #setting the gravity
    
    
    if(i==0 or i==1):                       #storing Fibonacci numbers
       x.append(1)                  
    else:
        x.append(x[i-1]+x[i-2])
        
                
    print(i+1,"th wave , no of spheres=",x[i])

    ball.clear()
    for z in range(x[i]):         
        ball.append(p.loadURDF("sphere.urdf",[z,0,5]))         #appending the number of balls and their coordinates
    
    for y in range(1000):                                      #running the simulation
        p.stepSimulation()
        time.sleep(1./240.)
        pos,_ = p.getBasePositionAndOrientation(ball[0])
        if pos[2]<=0.05: 
            time.sleep(1)
            break
            
    
p.resetSimulation()
