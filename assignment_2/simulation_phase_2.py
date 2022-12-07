import random
import time


def generate_random_size():
    min = random.randint(5, 10)
    max = random.randint(min, min + 10)
    return random.randint(min, max)


def get_random_index():
    return random.randint(0, 2)


def populate_list(size):
    list = random.sample(range(1, 100), size)

    return list


def enqueue(q1, q2, q3):
    lengths = [len(q1), len(q2), len(q3)]
    len_q1, len_q2, len_q3 = lengths
    temp = []

    if len_q1 == len_q2 == len_q3:
        return q1, q2, q3
    else:
        min_length = min(lengths)
        temp.append(q1[min_length:])
        q1 = q1[:min_length]
        temp.append(q2[min_length:])
        q2 = q2[:min_length]
        temp.append(q3[min_length:])
        q3 = q3[:min_length]
        temp = sum(temp, [])  # flatten list
        return q1, q2, q3, temp


def dequeue(q1, q2, q3, temp):
    print('***********************************')
    print('APPLYING                    DEQUEUE')
    print('***********************************')

    lists = [q1, q2, q3, temp]
    while sum(lists, []):
        picked_list = get_random_index()
        if lists[picked_list]:
            poped = lists[picked_list].pop()
            print(
                f'Customer with No. {poped} has served from list, Status of list after removal{lists[picked_list]}')
            time.sleep(0.5)
            if lists[-1]:
                temp_poped = lists[-1].pop(random.randint(0,
                                           len(lists[-1]) - 1))
                lists[picked_list].insert(0, temp_poped)
    print('All customers Served ... Bank Closing')


print('Generating random sizes 3 lists...')
time.sleep(2)

random_size = [generate_random_size(), generate_random_size(),
               generate_random_size()]
print('Random sizes are: ', random_size)
print()

print('Generating 3 lists with random number of sizes', random_size, '...')
time.sleep(2)
q1, q2, q3 = populate_list(random_size[0]), populate_list(
    random_size[1]), populate_list(random_size[2])
print('Generated lists are: ', q1, q2, q3)
print()

print('Enqueuing generated lists...')
time.sleep(2)
q1, q2, q3, temp = enqueue(q1, q2, q3)
print('Enqueued lists are')
print('Q1', q1)
print('Q2', q2)
print('Q3', q3)
print('temp_queue_elements: ', temp)
dequeue(q1, q2, q3, temp)
