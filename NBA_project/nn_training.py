import torch
import torch.nn as nn
from execute import result



rows, cols =6,7
data_input=[[0]*cols for a in range(rows)]
for i in range(rows):
    data_input[i][6]=1
    data_input[i][0]=float(result[i].opponent_age)
    data_input[i][1]=float(result[i].opponent_height)
    data_input[i][2]=float(result[i].opponent_weight)
    data_input[i][3]=float(result[i].opponent_gdef_rating)
    data_input[i][4]=float(result[i].opponent_cdef_rating)
    data_input[i][5]=float(result[i].guards)
print(data_input)
data_output=[12,15, 7, 8, 15,11]
for i in range(rows):
    data_output[i]=float(result[i].shot_stats["long_attempt"])
x=torch.tensor(data_input,dtype=torch.float32)
y=torch.tensor(data_output,dtype=torch.float32)
w=torch.tensor([0.0,0.0,0.0,0.0,0.0,0.0,0.0],dtype=torch.float32,requires_grad=True)
print('\n')
loss=nn.MSELoss()
optimizer=torch.optim.SGD([w],lr=0.00021)

iterations=10000


lowest_lost=1

for epoch in range(10000):
    y_pred=torch.matmul(x,w)
    l=loss(y,y_pred)
    l.backward()
    optimizer.step()
    optimizer.zero_grad()
    print(w)
    if l.item()<lowest_lost:
        lowest_lost=l.item()
    print(f'epoch:{epoch},loss={l.item()}')

print("lowest loss so far:",lowest_lost)

'''
final_w=torch.tensor([1.8304, 6.0040, -1.6630,-1.5967, 5.0365],dtype=torch.float32)
for i in range(rows):
    print(f'predicted long attempts:{torch.matmul(x[i],final_w).item()}, actual long attempts:{data_output[i]}')
'''