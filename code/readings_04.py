import sys
import numpy

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    for f in filenames:
        data = numpy.loadtxt(f, delimiter=',', skiprows=1)

        if action == '--min':
            values = numpy.min(data, axis=0)
        elif action == '--mean':
            values = numpy.mean(data, axis=0)
        elif action == '--max':
            values = numpy.max(data, axis=0)

        for m in values:
            print(m)

if __name__ == '__main__':
   main()
