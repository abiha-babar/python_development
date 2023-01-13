class FileContext:
    def __init__(self, file_name, file_mode='r'):
        self.file_name = file_name
        self.file_mode = file_mode

    def __enter__(self):
        self.file = open(self.file_name, self.file_mode)
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()


if __name__ == '__main__':

    print('------------------------------------------------------------------------------------------------')
    print('A S S I G N M E N T                5                C O N T E X T                M A N A G E R S')
    print('------------------------------------------------------------------------------------------------\n')

    with FileContext('w_plus_mode_example.txt', 'w+') as file:
        file.write("This is content for w_plus_mode file.\n")

    with FileContext('a_plus_mode_example.txt', 'a+') as file:
        file.write("This is content for a_plus_mode file.\n")

    with FileContext('r_mode_example.txt', 'r') as file:
        print(file.read())
        
    with FileContext('default_mode_example.txt') as file:
        print(file.read())

    with FileContext('w_mode_example.txt', 'w') as file:
        file.write("This is content for w_mode file.\n")

    with FileContext('r_plus_mode.txt', 'r+') as file:
        file.write("This is content for r_plus_mode file.\n")
    
    print(end="\n\n\n")
    print('------------------------------------------------------------------------------------------------')
    print('E N D                       O F                       A S S I G N M E N T                      5')
    print('------------------------------------------------------------------------------------------------\n')
