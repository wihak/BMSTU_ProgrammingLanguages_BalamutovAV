from math import sin, cos

def calculate_z1(a):
    return 1 - 1 / 4 * sin(2 * a) ** 2  + cos(2 * a)

def calculate_z2(a):
    return cos(a) ** 2 + cos(a) ** 4

fi = open("lab1_in.txt", "rt")
fo = open("lab1_ou.txt", "wt")

fi.readline()
fi.readline()


fo.write("+=========+=========+=========+\n")
fo.write("I    A    I   Z1    I   Z2    I\n")
fo.write("+=========+=========+=========+\n")


for line in fi:
    if line == "\n":
        continue
    
    a = float(line.split()[0])
    z1 = calculate_z1(a)
    z2 = calculate_z2(a)
    
    fo.write("I {0:7.2f} I {1:7.4f} I {2:7.4f} I\n".format(a, z1, z2))
    fo.write("+=========+=========+=========+\n")

fi.close()
fo.close()