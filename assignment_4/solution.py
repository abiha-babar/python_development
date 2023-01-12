class MyCollection:
    def __init__(self):
        self.name_of_collection = None
        self.container = []
    
    def __lt__(self, other_collection):
        return len(self.container) < len(other_collection.container)

    def __eq__(self, other_collection):
        return self.container == other_collection.container

class MyStack(MyCollection):
    def push(self, element):
        self.container.append(element)

    def pop(self):
        if len(self.container) > 0:
            self.container.pop()

    def isEmpty(self):
        return len(self.container) == 0

    @staticmethod
    def get_stack_string(container):
        top_bottom = '==================\n'
        mid = ''
        total_elements = len(container)
        mid_created = 0
        if total_elements > 0:
            for element in container[::-1]:
                mid += str(element)
                if not mid_created:
                    mid += ' -----> stack top'
                if mid_created != total_elements - 1:
                    mid += '\n-----\n'
                else:
                    mid += '\n'
                mid_created += 1

        return top_bottom + mid + top_bottom

    def __str__(self):
        return self.get_stack_string(self.container)
    
    def __repr__(self):
        return self.get_stack_string(self.container)

class MyQueue(MyCollection):
    def enqueue(self, element):
        self.container.append(element)

    def dequeue(self):
        if len(self.container) > 0:
            self.container.pop(0)

    def isEmpty(self):
        return len(self.container) == 0
    
    @staticmethod
    def get_queue_string(container):
        container_length = len(container)
        if container_length == 0:
            return 'Queue is empty'
        elif container_length == 1:
            return f'{container[0]} --- Head/Tail of Queue'
        else:
            final_string = ''
            elements_processed = 0
            for element in container:
                final_string += str(element)
                if not elements_processed:
                    final_string += ' --- Head of Queue\n'
                elif elements_processed == container_length - 1:
                    final_string += ' --- Tail of Queue'
                else:
                    final_string += '\n'
                elements_processed += 1
            return final_string

    def __str__(self):
        return self.get_queue_string(self.container)
    
    def __repr__(self):
        return self.get_queue_string(self.container)




if __name__ == "__main__":
    print('------------------------------------------------------------------------------------------------')
    print('Q U E U E                                  P A R T                                   O U T P U T')
    print('------------------------------------------------------------------------------------------------\n')
    q1 = MyQueue()
    q2 = MyQueue()

    print(q1)
    print(q2)
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)

    q2.enqueue(1)
    q2.enqueue(2)
    q2.enqueue(3)
    q2.enqueue(4)

    if q1 == q2:
        print('Both queues are equal')
    else:
        print('Queues are not equal')

    if q1 < q2:
        print('Queues q1 is smaller than q2')
    else:
        print('Queues q1 is bigger than q2')

    print(q1)
    q1.dequeue()
    q1.dequeue()
    print(q1)
    q1 = MyQueue()
    print(q1)

    print(end="\n\n\n")
    print('------------------------------------------------------------------------------------------------')
    print('S T A C K                                  P A R T                                   O U T P U T')
    print('------------------------------------------------------------------------------------------------\n')

    st0 = MyStack()

    st0.push(1)
    st0.push(2)
    st0.push(3)
    st0.push(4)
    st0.push(5)
    print(st0)
    st0.pop()
    st0.pop()
    st0.pop()
    st0.pop()
    st0.pop()
    st0.push('a')
    print(st0)
    st1 = MyStack()
    st1.push(1)
    st1.push(2)
    st1.push(3)
    print(st1)
    st2 = MyStack()
    st2.push(1)
    st2.push(2)
    st2.push(3)
    print(st2)
    if st1==st2:
        print('Both stacks are equal')
    else:
        print('Stacks are not equal')

    st2.push(4)
    if st1==st2:
        print('Both stacks are equal')
    else:
        print('Stacks are not equal')

    print(end="\n\n\n")
    print('------------------------------------------------------------------------------------------------')
    print('E N D                       O F                       A S S I G N M E N T                      4')
    print('------------------------------------------------------------------------------------------------\n')
