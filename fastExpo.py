'''The purpose of this scripts is to illustrate
   implementations of Fast Exponentiation Algorithm
   for CSCI 3330 Algorithms class.
   
   Dr. Chenyi Hu in 2017.
   Last edit: January 27, 2023
'''

def fastExpo_recursive(a, p, n):
    ''' Returns a^p mod n '''
    if p == 0:
        return 1
    if p%2 == 0:
        t = fastExpo_recursive(a, p//2, n)
        return (t*t)%n
    else:
        t = fastExpo_recursive(a, p//2, n)
        return a *(t**2%n)%n

a = fastExpo_recursive(12345, 6789, 8765)
print('fastExpo_recursive(12345, 6789, 8765)', a)

def fastExpo_iterative(a,p,n):
    Y = 1
    while p > 0:
        if p % 2 == 0:
            a = (a * a) % n
            p = p/2
        else:
            Y = (a * Y) % n
            p = p - 1
    return Y

b = fastExpo_iterative(12345, 6789, 8765)
print('fastExpo_iterative(12345, 6789, 8765)', b)

print('pow(12345, 6789, 8765)', pow(12345, 6789, 8765))

