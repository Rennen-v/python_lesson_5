all_divisor_number = []
def all_divisor (number):
    counter = 1
    while counter!= (number+1):
        if number % counter == 0:
            all_divisor_number.append(counter)
            counter +=1
        else:
            counter += 1
    print("Всего делителей числа:",len(all_divisor_number), all_divisor_number)

# all_divisor(1000)

def prime_number (p_number):
    print(all_divisor(p_number))
    if len(all_divisor_number)>2:
        print (p_number, "- не простое число т.к. имеет больше 2х делителей")
    else:
        print(p_number, "- действительно простое число")
# prime_number(11)
all_prime_divisor = []

def biggest_devider (devider):
    all_divisor(devider)
    for i in all_divisor_number:
        # if len(prime_number(i))>2:
        prime_number(i)
        if len(all_prime_divisor)==2:
            all_prime_divisor.append(i)
        else:
            break
    print(all_prime_divisor)

    # all_divisor_number.sort(reverse=True)
    # print(all_divisor_number[:1])

biggest_devider(775)