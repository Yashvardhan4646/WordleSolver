
def search():
    with open('words.txt', 'r') as file:
        l1 = input('Enter first letter: ')
        l2 = input('Enter second letter: ')
        l3 = input('Enter third letter: ')
        l4 = input('Enter fourth letter: ')
        l5 = input('Enter fifth letter: ')

        data = file.readline()

        while data:
            data = data.strip()

            if len(data) >= 5:
                if (data[0] == l1 or l1 == '') and \
                   (data[1] == l2 or l2 == '') and \
                   (data[2] == l3 or l3 == '') and \
                   (data[3] == l4 or l4 == '') and \
                   (data[4] == l5 or l5 == ''):
                    print(data)

            data = file.readline()

search()
