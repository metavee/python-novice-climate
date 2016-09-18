import sys
import numpy

def main():
    script = sys.argv[0]
    for filename in sys.argv[1:]:
        data = numpy.loadtxt(filename, delimiter=',', skiprows=1)
        for m in numpy.mean(data, axis=0):
            print(m)

if __name__ == '__main__':
   main()
