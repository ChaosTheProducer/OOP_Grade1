# Q6
def ifprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    value = int(input('Enter an interger: '))
    if ifprime(value):
        print(value, 'is prime.')
    else:
        print(value, 'is not prime.')
