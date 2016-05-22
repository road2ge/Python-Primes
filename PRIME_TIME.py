'''Let's find some primes!!!'''
MINI = 1
MAXI = 100
num = MINI
primelist = []
composite_list = []

def min_max(mini, maxi):
    if mini % 2 == 0:
        mini -= 1
    global MINI
    MINI = mini
    global MAXI
    MAXI = maxi
    global num
    num = MINI + 1

def find_primes():
    global num
    global prime_list
    global MINI
    global MAXI
    while num >= MINI and num <= MAXI:
        if num % 2 != 0 and num != 2:
            if num % 3 != 0 and num != 3:
                if num % 5 != 0 and num != 5:
                    if num % 7 != 0 and num != 7:
                        primelist.append(num)
        num += 1
    print primelist
    
def find_primes2():
    global num
    primelist2 = []
    global composite_list
    global MINI
    global MAXI
    while num >= MINI and num <= MAXI:
        if num % 2 == 0 and num != 2:
            if not num in composite_list:
                composite_list.append(num)
        if num % 3 == 0 and num != 3:
            if not num in composite_list:
                composite_list.append(num)
        if num % 5 == 0 and num != 5:
            if not num in composite_list:
                composite_list.append(num)
        if num % 7 == 0 and num != 7:
            if not num in composite_list:
                composite_list.append(num)
        num += 1
    print composite_list
    p_prime = MINI
    while p_prime <= MAXI:
        if not p_prime in composite_list:
             primelist2.append(p_prime)
        p_prime += 1
    print primelist2