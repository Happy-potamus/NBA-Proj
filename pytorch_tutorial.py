import torch
import torch.nn as nn
from execute import result



rows, cols =1,4
data_input=[[0]*cols for a in range(rows)]
for i in range(rows):
    data_input[i][0]=float(result[i].opponent_height)
    data_input[i][1]=float(result[i].opponent_weight)
    data_input[i][2]=float(result[i].opponent_age)
    data_input[i][3]=float(result[i].opponent_def_rating)

data_output=[0]*rows
for i in range(rows):
    data_output[i]=float(result[i].shot_stats["long_attempt"])
x=torch.tensor(data_input,dtype=torch.float32)
y=torch.tensor(data_output,dtype=torch.float32)
w=torch.tensor([0.0,0.0,0.0,0.0],dtype=torch.float32,requires_grad=True)

loss=nn.MSELoss()
optimizer=torch.optim.SGD([w],lr=0.000001)

iterations=1000



for epoch in range(10):
    y_pred=torch.matmul(x,w)
    l=loss(y,y_pred)
    l.backward()
    optimizer.step()
    optimizer.zero_grad()
    print(w)
    print(f'epoch:{epoch},loss={l.item()}')
print(x)