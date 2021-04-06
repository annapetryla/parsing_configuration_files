import configparser as CP
import sys

if __name__ == '__main__':
    path = (sys.argv[1])
    rd = CP.ConfigParser()
    rd.read('trm.rc')
    lst = sorted(rd.sections())
    x = []
    for i in rd.sections():
        x.append(rd.get(i,"temp").split(',')[0])
        x.append(rd.get(i, "a"))
        x.append(rd.get(i, "b"))
        x.append(rd.get(i, "c"))
    else:
        print("======\n")

    xf = list(map(float, x[0:]))
    j = 0
    mult_res = 1
    plik = open(path,'w')
    for i in range(len(rd.sections())):
        case, x1, x2, x3, x4 = rd.sections()[i], xf[j], xf[j+1], xf[j+2], xf[j+3]
        print("Dla : %s, temp = %.3f, a = %.3f, b = %.3f, c = %.3f\n" % (case, x1, x2, x3,x4), "\n")
        mult_res = abs(x1 * x2 * x3 * x4)
        geo_avg = mult_res ** (1/4)
        plik.write("Dla : %s, temp = %.3f, a = %.3f, b = %.3f, c = %.3f, srednia geometryczna to:::: %.3f\n" % (case, x1, x2, x3, x4, float(geo_avg)))
        geo_avg = 1
        mult_res = 1
        j += 4
    plik.close()


