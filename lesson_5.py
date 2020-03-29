from copy import copy
# 2) выводит список всех делителей числа;
def all_divisor (number):
    all_divisor_number = []
    counter = 1
    while counter!= (number+1):
        if number % counter == 0:
            all_divisor_number.append(counter)
            counter +=1
        else:
            counter += 1
    print("Всего делителей числа:",len(all_divisor_number), all_divisor_number)
    return all_divisor_number
# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
def prime_number (p_number):
    all_divisor_number = all_divisor(p_number)
    print(all_divisor(p_number))
    if len(all_divisor_number)>2:
        print (p_number, "- не простое число т.к. имеет больше 2х делителей")
        return False
    else:
        print(p_number, "- действительно простое число")
        return True
# 3) выводит самый большой простой делитель числа.
def biggest_devider (devider):
    all_prime_divisor = [1]
    job_list=[]
    job_list=copy(all_divisor(devider))
    for i in job_list:
        if (len(all_divisor(i))==2):
            all_prime_divisor.append(i)
        else:
            continue
    print("Все простые делители числа", devider, all_prime_divisor, "Наибольший из них:", max(all_prime_divisor))
    return max(all_prime_divisor)
# 4) функция выводит каноническое разложение числа
def prime_factorization(f_number):
    job_number=copy(f_number)
    if prime_number(job_number) == True:
        print("Агрументом выбрано простое чило, его нельзя разделить на простые множители.")
    else:
        i = 2
        prime_factorization_list = []
        while i * i <= job_number:
            while job_number % i == 0:
                prime_factorization_list.append(i)
                job_number = job_number / i
            i = i + 1
        if job_number > 1:
            prime_factorization_list.append(int(job_number))
        print("Результат разложения числа",f_number,"на простые множители: ",prime_factorization_list)
        return prime_factorization_list

# 5)функция выводит самый большой делитель (не обязательно простой) числа.
def most_devider(m_number):
    if prime_number(m_number) == True:
        print("Агрументом выбрано простое чило, его делителями будет 1 или оно само. Какое из них считать самым большим?")
    else:
        devider_list= all_divisor(m_number)
        devider_list= sorted(devider_list,reverse=True)
        print(devider_list[1])
        return devider_list[1]




