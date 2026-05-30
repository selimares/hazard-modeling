import numpy as np

N=20
state=np.zeros(N)

state[10]=1 # initial failure
 
for t in range(5): 
    new_state=state.copy()
    for i in range(1,N-1):
        if state[i]>0:
            new_state[i-1]+=0.3
            new_state[i+1]+=0.3
    state=new_state
    print(f"Step {t}: {state}")        
