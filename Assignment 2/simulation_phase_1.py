import random

random_list = []
q1 = []
q2 = []
q3 = []

total_numbers_to_be_generated = 10
generated = 1


while generated <= total_numbers_to_be_generated:
    random_generated_number = random.randint(1, 100)
    random_list.append(random_generated_number)

    if random_generated_number % 2 == 0:
        if random_generated_number % 7 == 0:
            q1.append(random_generated_number)
    else:
        if random_generated_number % 9 == 0:
            q2.append(random_generated_number)

    if generated % 8 == 0:
        q3.append(random_generated_number)

    generated += 1

print('Random 100 elements list: ', random_list, end='\n\n')

print('List of even numbers and divisible by 7: ', q1, end='\n\n')

print('List of odd numbers and divisible by 9: ', q2, end='\n\n')

print('Every 8th element of random_list:', q3, end='\n\n')
