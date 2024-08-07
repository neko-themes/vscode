import collections

def queue():
    d = collections.deque([9,8,7,6,5,4]) 
    return d 

d = queue()
print("Deque",d) 

def insertQueue(): 
    d.append(1) 
    d.append(2)
    d.append(3)

def removeQueue():
    d.popleft()

insert = insertQueue()
print("Adding 3, 2, 1",d)

remove = removeQueue()
print("Removing 9 from deque", d)