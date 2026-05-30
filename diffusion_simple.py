import numpy as np
import matplotlib.pyplot as plt

N=100
grid=np.zeros(N)
grid[N//2]=1

for t in range(50):
    new_grid=grid.copy()
    for i in range(1,N-1):
        new_grid[i]=(grid[i]+0.1*(grid[i-1]-2*grid[i]+grid[i-1]))

    grid=new_grid

plt.plot(grid)
plt.title("Simple Diffusion Model (Hazard analogy)")
plt.show()        