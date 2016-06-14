list_name = ['Jones', 'Peter', 'Julie', 'Bob', 'Natasha', 'Drake']

try:
    for n in list_name:
        if len(n) > 5:
            raise Exception('Length too much')
            continue
        else:
            print(n)

except:
    pass
