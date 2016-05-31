from __future__ import print_function

# For later prime functions, a primelist and a twinprimelist is needed. I know some primes, and I put them here,
# But the list gets longer as you run algorithms.

primelist = [2,3,5,7,11,13,17,19,23,29,31,37]
twinprimelist = []

def factor_v2(a,b,c):
    '''Remember, adding a negative number is subtracting a positive, and
    subtracting a negative number is adding a positive.
    If you get decimals, it's probably not easily factorable.'''
    
    discriminant = (b ** 2) - (4 * a * c)
    
    if discriminant < 0:
    
        return print('This equation has no real solutions, meaning it is prime.')
    
    cringe1 = (-b + sqrt(discriminant)) / (2 * a)
    cringe2 = (-b - sqrt(discriminant)) / (2 * a)
    
    # When the discriminant is 0, there is only one x-int.
    if discriminant == 0:
    
        return print('(x + ', cringe1, ')^2', sep='')
    
    # Just lots of factoring conditionals.
    elif a == 1:
    
        return print('(x + ', cringe1, ')(x + ', cringe2, ')', sep = '')
    
    elif a > 1:
    
        if cringe1 % a == 0:
    
            return print('(x + ', cringe1/a, ')(x + ', cringe2, ')', sep = '')
    
        elif cringe2 % a == 0:
    
            return print('(x + ', cringe1, ')(x + ', cringe2/a, ')', sep = '')
    
    elif a == -1:
    
        return print('-1*(x + ', cringe1, ')(x + ', cringe2, ')', sep = '')
    
    elif a < -1:
    
        if cringe1 % a == 0:
    
            return print('(x + ', cringe1/a, ')(', a, 'x + ', cringe2, ')', sep = '')
    
        elif cringe2 % a == 0:
    
            return print('(x + ', cringe1, ')(', a, 'x + ', cringe2/a, ')', sep = '')
    
    else:
    
        return print('Dude, you try this one yourself.')
        
def sqrt(number):
    
    return number ** .5

def prime_factor(number,human=True):
    '''Get the prime factorization of a number! Pretty neat, except not recommended
    to exceed 100,000,000.'''
    
    # I think the whole human thing is before I did a test_prime
    
    factors = []
    num2 = number
    
    def is_prime(composite):
        possible_factor = 2
    
        while possible_factor <= composite ** .5 + 1:
    
            if composite % possible_factor == 0:
    
                return False
    
            else:
    
                possible_factor += 1
    
        return True
    
    for factor in range(2,number):
    
        while num2 % factor == 0:
    
            if is_prime(factor):
    
                factors.append(factor)
                num2 /= factor
    
        if is_prime(num2) and not num2 == 1:
    
            factors.append(num2)
    
            if human and len(factors) > 1:
    
                return factors
    
            elif human and len(factors) == 1:
    
                factors.append(1)
                return factors
    
            else:
    
                return True
    
    if human and len(factors) > 1:
    
        return factors
    
    elif human and len(factors) == 1:
    
        factors.append(1)
    
        return factors
    
    else:
    
        return True
        
def test_is_prime(number):
    
    global primelist
    prime = True
    
    for factor in primelist:
    
        if number % factor != 0 and prime:
    
            prime = True
    
        else:
    
            prime = False            
    
    if number == 1:
    
        prime = False
    
    if prime:
    
        primelist.append(number)
    
    return prime


def find_primes(I_accept=False, maxi = 1000):
    '''Warning!!!! This could eventually crash things. I'm not responsible.
    There is an argument, the maximum number, that comes after True if you
    accept that I am not liable for damages.
    Set the priority to high or real-time in Task Manager!'''
    
    # I do need to warn people that this could crash things.
    warning = 'Warning!!!! This could crash things. I am not held liable for any damages. Type \'find_primes(True)\' (caps matters) to run. True means that you accept these terms.'
    
    if not I_accept:
    
        return print(warning)
    
    number = 3
    
    while number < maxi:
    
        if test_is_prime(number):
    
            print(number)
            number += 2
    
        else:
    
            number += 2
    
    return print(primelist, ' are the primes you found! There are ', len(primelist),
                 ' primes between 1 and ', maxi, '.', sep = '')
        
def find_twin_primes(I_accept=False, maxi = 1000):
    '''Warning!!!! This could eventually crash things. I'm not responsible.
    There is an argument, the maximum number, that comes after True if you
    accept that I am not liable for damages.
    Set the priority to high or real-time in Task Manager!'''
    
    # I do need to warn people that this could crash things
    warning = 'Warning!!!! This could eventually crash things. I am not held liable for any damages. Type \'find_primes(True)\' (caps matters) to run. True means that you accept these terms.'
    
    if not I_accept: 
    
        return print(warning)
    
    # Twin primes are defined as primes that have a difference of 2.
    # I set number2 to -10 every time just because I don't want anything
    # weird to happen.
    
    number = 1
    number2 = -10
    
    while number < maxi:
    
        if test_is_prime(number):
    
            if number2 != number - 2:

                number2 = number
    
            elif number2 == number - 2:

                print(number2,'and', number, 'are twin primes!')
                twinprimelist.append(number2)
                twinprimelist.append(number)
                number2 = -10

            # There are no even twin primes, or even primes excluding 2 for that matter.
            # This avoids unnecessary calculations.
            number += 2
        
        else:
            
            number += 2
    
    return print(twinprimelist, ' are the twin primes you found! There are ', len(twinprimelist),
                 ' twin primes between 1 and ', maxi, '.', sep = '')