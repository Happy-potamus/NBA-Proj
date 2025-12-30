from nn_training import w
import torch

age=input("Enter opponent average age: ")
height=input("Enter opponent average height (inches): ")
weight=input("Enter opponent average weight (lbs): ")
guard_def_rating=input("Enter opponent average guard defensive rating: ")
cen_def_rating=input("Enter opponent average center defensive rating: ")
guards=input("Enter number of guards on opponent team: ")

cols =1, 7
data_input=[cols]
data_input[6]=1
data_input[0]=float(age)
data_input[1]=float(height)
data_input[2]=float(weight)
data_input[3]=float(guard_def_rating)
data_input[4]=float(cen_def_rating)
data_input[5]=float(guards)

x=torch.tensor(data_input,dtype=torch.float32)
w=torch.tensor([0.8451, 2.3796, -1.7607,-0.3706, -1.6352, 0.2413, 0.6434],dtype=torch.float32)
y_pred=torch.matmul(x,w)
print(f'Predicted long attempts by Luka: {y_pred.item()}')
