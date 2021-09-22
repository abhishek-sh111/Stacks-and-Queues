class stack:
    def __init__(self):
        #initialise list
        self.list1=[]

    def push(self,num):
        self.list1.append(num)
    
    def pop(self):
        return self.list1.pop()
    
    def top(self):
        return self.list1[-1]


    def empty(self):
        return not self.list1

obj = stack()
obj.push(5)
obj.push(6)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
rint(param_2)
print(param_3)
print(param_4)
