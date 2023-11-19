import matplotlib.pyplot as plt
import time
positionx=[]#для координат
positiony=[]
class Robot:
    type="Flight"
    def __init__(self,vx,vy,mas):
        self.vx = 0
        self.vxold = vx
        self.vy = 0
        self.vyold = vy
        self.mas = mas
    def move(self,t):
        if (self.vxold and self.vyold and self.mas) >= 0:
            self.vx = self.vxold * t
            self.vy = self.vyold * t - (9.8 * t * t /2)
            positionx.append(self.vx)
            positiony.append(self.vy)
        else:
            print("Mistakes data")
            exit()
    def show(self):
        if self.vx >= 0 and self.vy >= 0:
            x = [positionx]
            y = [positiony]
            print("X:", "[", self.vx, "]", "Y:", "[", self.vy, "]")
            plt.scatter(x, y, color='blue')
            plt.xlabel('Meter')
            plt.ylabel('Height')
            plt.title('Rocket flight')
        else:
            print("Rocket Crash")
            plt.show()
            exit()

print("Задайте массу корабля в кг")
mas=int (input())
print("Задайте vx корабля в м/с")
vx=int (input())
print("Задайте vy корабля в м/с")
vy=int (input())
moon33=Robot(vx,vy,mas)
for i in range (0,100):
    time.sleep(0.9)
    moon33.move(i)
    moon33.show()