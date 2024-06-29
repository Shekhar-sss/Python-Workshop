name='shekhar'
if name == 'shinde':
    print('name is shinde')
else: print('name is shekhar')

dic = {}
dic['name']='shekhar'
dic['adhar card']= 523016176814
print(dic)

for i in range(10,20):
    if i%2 ==0:
        print(f'{i} Given no is even')
    else:print(f'{i} Given no is odd')

# For Loop
li =[1,2,22,32,12,23]
k=0
for i in li:
    k+=i
print('k value is',k)

#while loop
i =4
while(i!=0):
    print(f'i am in while loop with counter no {i}')
    i=i-1

# write programe to skip 3 and 7 in loop and break print to 13
i=1
while(i>0):
    if i==3:
        i=i+1
        continue
    if i==7:
        i=i+1
        continue
    if i==13:
        break
    print(f'Values of i is {i}')
    i=i+1

