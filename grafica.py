#importamos las librerias
import numpy as np
import matplotlib.pyplot as plt

#definimos el intervalo de x
x = np.linspace(-np.pi, 2*np.pi, 100)

#calculamos los valores de y
y1=np.cos(x)
y2=np.sin(x)

#creamos la grafica
fig=plt.figure(figsize=(10,8))
ax=plt.axes()

#ponemos los colores de fondo
fig.set_facecolor('#34495e')
ax.set_facecolor('#ECF0F1')

#graficamos la curva
ax.plot(x,y1, color = 'blue',
    linewidth = 2,label='sin(x)')
ax.plot(x,y2, color = 'red',
    linewidth = 3,label='cos(x)')

#mostarmos los nombres de las curvas
ax.legend(loc='upper left', fontsize = 12)

#mostramos el nombre de la grafica
plt.title('Grafica de funciones', fontsize = 20, fontweight = 'bold',color = 'white')

#Poner cuadricula
plt.grid(color = 'black',
        linestyle = 'dashed',
        linewidth = 0.5,
        alpha = 0.5,)

#cambiar la pocicion de los ejes x e y

ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.spines['bottom'].set_color('black')
ax.spines['bottom'].set_linewidth(2)
ax.spines['left'].set_color('black')
ax.spines['left'].set_linewidth(2)

ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
              [r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\cdot\pi}{2}$', r'$2\cdot\pi$'],
             fontsize = 14)
ax.set_yticks(np.arange(-1.5, 1.5, 0.5))
plt.show()