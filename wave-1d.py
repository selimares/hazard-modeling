import numpy as np
import matplotlib.pyplot as plt 

N=200
u_prev=np.zeros(N)
u_curr=np.zeros(N)
u_next=np.zeros(N)

u_curr[N//2]=1

r=0.2

plt.ion()
fig,ax=plt.subplots()
line,=ax.plot(u_curr)
ax.set_ylim(-1,1)

for t in range(300):
    for i in range(1,N-1):
        u_next[i]=(2*u_curr[i]-u_prev[i]+
                   r*(u_curr[i+1]-2*u_curr[i]+u_curr[i-1]))
        
    u_prev=u_curr.copy()
    u_curr=u_next.copy()

    line.set_ydata(u_curr)
    plt.pause(0.01)

plt.ioff()
plt.show()