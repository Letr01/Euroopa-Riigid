import random
slovar = {'Estonia': 'Tallinn', 'Russia' : 'Moscow', 'Tallinn' : 'Estonia', 'Moscow' : 'Russia', 'Riga': 'Latvia', 'Latvia': 'Riga', 'Finland': 'Helsinki', 'Helsinki': 'Finland', 'Sweden': 'Stockholm', 'Stockholm': 'Sweden', 'Germany': 'Berlin', 'Berlin': 'Germany', 'France': 'Paris', 'Paris': 'France','Italy': 'Rome', 'Rome': 'Italy','Belarus': 'Minsk','Minsk': 'Belarus','China': 'Pekin','Pekin': 'China','Japan': 'Tokyo','Tokyo': 'Japan','USA': 'Washington', 'Wasgington':'USA','Brasilia': 'Brasilia','Portugal': 'Lissabon', 'Lissabon': 'Portugal'}
def add_to_slovar():
    riik = input('Add country: ')
    linn = input('Add city: ')
    slovar[riik] = linn
    slovar[linn] = riik
def change(town):
    del slovar[town]
    new_slovar_value=input('Change your word: ')
    slovar[town] = new_slovar_value
    slovar[new_slovar_value] = town
def test():
    count = 0
    listik=[]
    for element in slovar.keys():
        listik.append(element)
    for i in range(10):
        random_element = random.sample(listik, 1)[0]
        print(random_element)
        test_write = input('Write: ')
        i += 1
        if test_write == slovar[random_element]:
            print('Correct!')
            count=count+1
        else:
            print('Incorrect')
    print('You finished your test with',count*10,'%.')

while True:
    print('Type "1" if you want to write country or city')
    print('Type "2" if you want to control your knowledge')
    choose=input()
    if choose=='1':
        town = input('Write country or city: ')
        if town in slovar.keys():
            output = slovar[town]
            print(output)  
            print('If it is wrong, do you want to change it?\nYes or No?')
            a=input()
            while True:
                if a=='Yes':
                    change(town)
                    break
                elif a == 'No':
                    break
                else:
                    print('Wrong input!')
                    a=input('Sisestage uuesti: ')
        else:
            print('Does not exist.')
            print('Type "1" if you want to add it')
            print('Type "2" if you do not want to add it')
            valik=input()
            while True:
                if valik=='1':
                    add_to_slovar()
                    break
                elif valik=='2':
                    break
                else:
                    print('Wrong input!')
                    valik=input('Sisestage uuesti: ')
                    break
    elif choose=='2':
        test()
    else:
        print('Wrong input!')
        choose=input('Sisestage uuesti: ')