import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import mpl_toolkits.mplot3d.art3d as art3d


#функция определения принадлежности области
def func(x, y):
    plt.plot(x, y, 'ro') #рисование точки
    if (25 <= x**2+y**2 <= 100 and x >= -3 and y <= 0) or (x**2+y**2 <= 25 and y >= 0 and -3 <= x <= 2):
        plt.title( "Точка принадлежит области", fontsize=15, fontweight="bold")
    else:
        plt.title("Точка не принадлежит области", fontsize=15, fontweight="bold")


'''3D реализация'''
#объект axes с поддежкой 3D
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

plt.xlabel("Ось Х", fontweight="bold") # ось абсцисс
plt.ylabel("Ось Y", fontweight="bold") # ось ординат

#2 оси x и y
x1 = [0, 0]
y1 = [-200, 200]
plt.plot(x1, y1, color = "gray")
x2 = [-200, 200]
y2 = [0, 0]
plt.plot(x2, y2 , color = "gray")

#2 заданные прямые
plt.plot([2, 2], [-100, 100], label = "x = 2")
plt.plot([-3, -3], [-100, 100], label = "x = -3")

#2 круга 
p = Circle((0, 0), 5, fill=False, label = "x**2+y**2 = 5", color = "green")
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")

p = Circle((0, 0), 10, fill=False, label = "x**2+y**2 = 10")
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")

#Легенда графика
plt.legend(loc = "upper left", shadow = True)

#выставляем длину осей
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

#задаем шаг 1
plt.xticks(np.arange(-10, 10))
plt.yticks(np.arange(-10, 10))


x, y = map(float,input().split())
func(x, y) 

plt.show()