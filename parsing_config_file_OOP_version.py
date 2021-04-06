import configparser as CP
import sys

class Seria:
    name = ""
    temp = 0.0
    a = 0.0
    b = 0.0
    c = 0.0
    geo_avg = 0.0

    def __init__(self, name, temp, a, b, c, geo_avg):
        self.name = name
        self.temp = temp
        self.a = a
        self.b = b
        self.c = c
        self.geo_avg = geo_avg


if __name__ == '__main__':
    path = (sys.argv[1])
    rd = CP.ConfigParser()
    rd.read('trm.rc')
    print(type(rd.sections()), rd.sections())
    lst = sorted(rd.sections())
    print(type(lst), lst)
    x = []
    plik = open(path, 'w')

    for i in rd.sections():
        print(i)
        print(rd.items(i))
        geo_avg = abs(float(rd.get(i, "temp").split(',')[0]) * float(rd.get(i, "a")) * float(rd.get(i, "b")) * float(
            rd.get(i, "c"))) ** (1 / 4)
        obj = Seria(i, (rd.get(i, "temp").split(',')[0]), rd.get(i, "a"), rd.get(i, "b"), rd.get(i, "c"), geo_avg)
        plik.write("Parametry dla "+i+" :: temperaura :: "+str(obj.temp)+", a:: "+str(obj.a)+", b:: "+str(obj.b)+", c:: "+str(obj.c)+", srednia_geometryczna (temp, a, b, c) ::"+str(obj.geo_avg))
        plik.write("\n")
    else:
        print("======\n")
    plik.close()
