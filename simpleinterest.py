import sys

def simInt(principal, rate, time):
    return (principal * rate * time) / 100


if __name__ == "__main__":
    p = int(sys.argv[1])
    i = int(sys.argv[2])
    t = int(sys.argv[3])
    print("Simple interest:", simInt(p,i,t))