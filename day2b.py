f = open("day2input.txt",'r')

inputs = f.readlines()

f.close()

#print(inputs)

inputs2 = [x.replace("\n","") for x in inputs]

#print(inputs2)

x = 0
aim = 0
y = 0

for i in inputs2:
    #print(i.split())
    j = i.split()
    if j[0] == "forward":
        x += int(j[1])
        if aim != 0:
            y += int(j[1])*aim
    elif j[0] == "up":
        aim -= int(j[1])
    elif j[0] == "down":
        aim += int(j[1])
    print(x,y,aim)


print(x*y)