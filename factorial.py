def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))

if __name__ == '__main__':
    print factorial(3)