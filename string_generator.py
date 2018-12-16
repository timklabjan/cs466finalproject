import numpy as np
import random
chars = ["A","C","T","G"]

for i in range(1,11):
    f_name = "input_" + str(i) + ".txt"
    with open(f_name,'w+') as f:
        f.write("1\n")
        f.write("-1\n")
        f.write("-1\n")

with open("input_1.txt","a") as f:
    for i in range(2):
        rand_s = np.random.choice(chars,5,replace=True)
        s = ""
        for x in rand_s:
            s += x
        s += "\n"
        f.write(s)

with open("input_2.txt","a") as f:
    for i in range(2):
        rand_s = np.random.choice(chars,10,replace=True)
        s = ""
        for x in rand_s:
            s += x
        s += "\n"
        f.write(s)

with open("input_3.txt","a") as f:
    for i in range(2):
        rand_s = np.random.choice(chars,100,replace=True)
        s = ""
        for x in rand_s:
            s += x
        s += "\n"
        f.write(s)

with open("input_4.txt","a") as f:
    for i in range(2):
        rand_s = np.random.choice(chars,500,replace=True)
        s = ""
        for x in rand_s:
            s += x
        s += "\n"
        f.write(s)

with open("input_5.txt","a") as f:
    for i in range(2):
        rand_s = np.random.choice(chars,1000,replace=True)
        s = ""
        for x in rand_s:
            s += x
        s += "\n"
        f.write(s)

with open("input_6.txt","a") as f:
    for i in range(2):
        rand_s = np.random.choice(chars,5000,replace=True)
        s = ""
        for x in rand_s:
            s += x
        s += "\n"
        f.write(s)

with open("input_7.txt","a") as f:
    for i in range(2):
        rand_s = np.random.choice(chars,10000,replace=True)
        s = ""
        for x in rand_s:
            s += x
        s += "\n"
        f.write(s)

with open("input_8.txt","a") as f:
    for i in range(2):
        rand_s = np.random.choice(chars,50,replace=True)
        s = ""
        for x in rand_s:
            s += x
        s += "\n"
        f.write(s)

with open("input_9.txt","a") as f:
    for i in range(2):
        rand_s = np.random.choice(chars,200,replace=True)
        s = ""
        for x in rand_s:
            s += x
        s += "\n"
        f.write(s)

with open("input_10.txt","a") as f:
    for i in range(2):
        rand_s = np.random.choice(chars,2000,replace=True)
        s = ""
        for x in rand_s:
            s += x
        s += "\n"
        f.write(s)

with open("input_11.txt","w+") as f:
    f.write("2\n")
    f.write("-1\n")
    f.write("-3\n")
    rand_s = np.random.choice(chars, 10, replace=True)
    s = ""
    for x in rand_s:
        s += x
    s += "\n"
    f.write(s)
    rand_s = np.random.choice(chars, 5, replace=True)
    s = ""
    for x in rand_s:
        s += x
    s += "\n"
    f.write(s)