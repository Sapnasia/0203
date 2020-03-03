file = open('teams.txt', 'r+')
sixnations = ['England' , 'Ireland' , 'Scotland' , 'Wales' , 'France' , 'Italy']
x = '' 

for i in range(6):
    x = x+ sixnations[i] + '\n'

for i in range(6):
    if i == (0): 
        print(file.readline())
    elif i == (4):
        print(file.readline())
    else: 
        file.readline()
        print ("helloworld)
