# ********* In The Nmae Of God ***********
#  Student ID: 401130443
#  Student Name: Mohammad Saleh Sohrabi
#  Fundamental of Computers and Programming (python)
#  Hamedan University of Technology, Hamedan, Iran.

from classSaleh import *

def Management_menu():
    print('******************* Management menu ******************* ')
    print('1) CRUD Packs')
    print('2) CRUD Continers')
    print('3) CRUD Cars')
    print('4) Loading')
    print('5) Send and Receive load')
    print('6) Exit')
    
    print("#_Admin---> Enter number")
    choose = eval(input("User: "))
    return choose


filename = ''

def login():

    global filename

    print("#_Admin-----> Hello! welcome to Local transportation system")
    an = int(input("Do you have any Account? [1/0]"))
    if an == 0:
        print("#_Admin-----> Fill information")
        UserName = input("UserName: ")
        phone_number = input("PhoneNumber: ")

        filename = UserName + ".txt"

        f = open(filename,'w')
        f.write(phone_number)
        f.write('')
        f.close()

    else :
        print("#_Admin -----> Fill information")
        UserName = input("UserName: ")

        filename = UserName + ".txt"

        f = open(filename, 'r')
        print("#_Admin -----> Your Letter load ")
        print(f.read())

def Loading_menu():
    print('*************** Loading menu  *************** ')
    print('1.Diplay Package')
    print('2.Display Continers')
    print('3.Display Cars')
    print('4.loading Package to continer')
    print('5.Connection continer to CarContiner')
    print('6.loding Simple_Package to CarRoom')
    print('7.Exit')
    
    print()
    print("#_Admin---> Enter number")
    choose = eval(input("User: "))
    return choose

def Send_Receive_menu():
    print('******************* Send_Receive_menu  ******************* ')
    print('1) Display load waiting to be received  ')
    print('2) Send Letter load and save letter load')

    print()
    print("#_Admin---> Enter number")
    choose = eval(input("User: "))
    return choose

# ************** Smaling **************
list_Package = []
count_Package = 0 

list_continers = []
count_continer = 0 

list_cars = []
count_car = 0

warehous = []

# ************** menu_CRUD **************
def menu_CRUD_Package():
    print('******************* CRUD Package menu *******************')
    print('1) Insert Package')
    print('2) Update Package')
    print('3) Delete Package')

    print("#_Admin---> Enter number")
    choose = eval(input("User: "))
    return choose

def menu_CRUD_continer():
    print('******************* CRUD Continer menu *******************')
    print('1) Insert Continer')
    print('2) Update Continer')
    print('3) Delete Continer')

    print("#_Admin---> Enter number")
    choose = eval(input("User: "))
    return choose

def menu_CRUD_Car():
    print('******************* CRUD Car menu *******************')
    print('1) Insert Car')
    print('2) Update Car')
    print('3) Delete Car')

    print("#_Admin---> Enter number")
    choose = eval(input("User: "))
    return choose

# ************** get Name **************
def Name_Package():
    print('******************* Name Packages *******************')
    print('1) Simple_Package')
    print('2) Breakable_package')
    print('3) Cold_Package')

    print("#_Admin---> Enter number")
    choose = eval(input("User: "))
    return choose

def Name_Continer():
    print('******************* Name Continers *******************')
    print('1) Breakable_Package_Container')
    print('2) FreezerContainer')

    print("#_Admin---> Enter number")
    choose = eval(input("User: "))
    return choose

def Name_Car():
    print('******************* Name Cars *******************')
    print('1) CarRoom')
    print('2) CarContiner')

    print("#_Admin---> Enter number")
    choose = eval(input("User: "))
    return choose

# ************** Display **************
def Display_Package():
    
    print("#_Admin------> Your Package: ")

    for i in list_Package:

        if i.name == "Simple_Package" :
            line1 = "Simple Package" + str(i.numPackage) + ':'
            line2 = "weight: " + str(i.weight) + " ||| " +"destination: " + i.destination + " ||| " + "beginning: " + i.beginning +'\n'
            print(line1)   
            print(line2)

        elif i.name == "Breakable_package" :
            line1 = "Breakable package" + str(i.numPackage) + ':'
            line2="weight: " + str(i.weight) + " ||| " +"destination: " + i.destination + " ||| " + "beginning: " + i.beginning +'\n'
            print(line1) 
            print(line2)

        elif i.name == "Cold_Package" :
            line1 = "Cold Package" + str(i.numPackage) + ':'
            line2 = "weight: " + str(i.weight) + " ||| " +"destination: " + i.destination + " ||| " + "beginning: " + i.beginning + " ||| " + "min_temperature: " + i.min_temperature +'\n'
            print(line1)
            print(line2)

def Display_continer():
    for i in list_continers:

        if i.name == "Breakable_Package_Container" :
            line1 = "Continer breakable" + str(i.numContiner) + ':' 
            line2 =  "weight: " + str(i.weight) + " ||| " +"max_pack: " + str(i.max_pack) + " ||| "  + 'max_speed: ' + i.max_speed +'\n'
            print(line1)  
            print(line2) 

        elif i.name == "FreezerContainer" :
            line1 = "Continer Freezer" + str(i.numContiner) + ':' 
            line2 = "weight: " + str(i.weight) + " ||| " +"max_pack: " + str(i.max_pack) + " ||| "  + 'refrigerator_min_temperature: ' + i.refrigerator_min_temperature +'\n'
            print(line1) 
            print(line2)

def Display_car():
    for i in list_cars:

        if i.name == "CarRoom" :
            line1 = "CarRoom" + str(i.numCar) + ':' 
            line2 =  "weight: " + str(i.weight) + " ||| " +"max_pack: " + str(i.max_pack) + '\n'
            print(line1)  
            print(line2) 

        elif i.name == "CarContiner" :
            line1 = "CarContiner " + str(i.numCar) + ':' 
            line2 = "weight: " + str(i.weight) + " ||| " +"max_Continer: " + str(i.max_Continer) + '\n'
            print(line1) 
            print(line2)

# ************** Insert **************
def Insert_Package():

    choose_Name_Package = Name_Package()

    global count_Package

    count_Package = count_Package + 1

    print("#_Admin-----> Fill information ")
    weight = int(input('weight: '))
    destination = input('destination: ')
    beginning = input('beginning: ')

    if choose_Name_Package ==1 :

        p = Simple_Package(count_Package, weight, destination, beginning)
        
        list_Package.append(p)

    elif choose_Name_Package == 2:

        p = Breakable_package(count_Package, weight, destination, beginning)

        list_Package.append(p)

    elif choose_Name_Package == 3:

        min_temperature = input('min_temperature: ')

        p = Cold_Package(count_Package, weight, destination, beginning, min_temperature)

        list_Package.append(p)

def Insert_Contine():

    choose_Name_Continer = Name_Continer()

    global count_continer

    count_continer = count_continer + 1

    print("#_Admin-----> Fill information ")
    weight = int(input('weight: '))
    max_pack = int(input('max_pack: '))

    if choose_Name_Continer ==1 :

        max_speed = input('max_speed: ')
        c = Breakable_Package_Container(count_continer, weight, max_pack, max_speed)
        
        list_continers.append(c)

    elif choose_Name_Continer == 2:

        refrigerator_min_temperature = input('refrigerator_min_temperature: ')
        c = FreezerContainer(count_continer, weight, max_pack, refrigerator_min_temperature)

        list_continers.append(c)

def Insert_Car():

    choose_Name_Car = Name_Car()

    global count_car

    count_car = count_car + 1

    print("#_Admin-----> Fill information ")
    weight = int(input('weight: '))

    if choose_Name_Car ==1 :

        max_pack = int(input('max_pack: '))

        car = CarRoom(count_car, weight, max_pack)
        
        list_cars.append(car)

    elif choose_Name_Car == 2:

        max_Continer = int(input('max_Continer: '))
        car = CarContiner(count_car, weight, max_Continer)

        list_cars.append(car)

# ************** Update **************
def Update_Package():

    Display_Package()

    while 1:

        print("#_Admin-----> Fill information")

        numPackage = int(input("which package? "))

        update = input("What do you want to Update? ")

        amount = input(f"Enter your amount :") 

        if update == "weight":
            list_Package[numPackage-1].weight = amount

        elif update == "destination":
            list_Package[numPackage-1].destination = amount

        elif update == "beginning":
            list_Package[numPackage-1].beginning = amount

        elif update == "min_temperature":
            list_Package[numPackage-1].min_temperature = amount

        print("#_Admin-----> Do you want to change again? [1/0]")
        answer = int(input("User: "))

        if answer == 0:
            break

def Update_Contine():

    Display_continer()

    while 1:

        print("#_Admin-----> Fill information")

        numContiner = int(input("which continer? "))

        update = input("What do you want to Update? ")

        amount = input(f"Enter your amount :") 

        if update == "weight":
            list_continers[numContiner-1].weight = amount

        elif update == "max_pack":
            list_continers[numContiner-1].max_pack = amount

        elif update == "max_speed":
            list_continers[numContiner-1].max_speed = amount

        elif update == "refrigerator_min_temperature":
            list_continers[numContiner-1].refrigerator_min_temperature = amount

        print("#_Admin-----> Do you want to change again? [1/0]")
        answer = int(input("User: "))

        if answer == 0:
            break

def Update_Car():

    Display_car()

    while 1:

        print("#_Admin-----> Fill information")

        numCar = int(input("which car? "))

        update = input("What do you want to Update? ")

        amount = input(f"Enter your amount :") 

        if update == "weight":
            list_cars[numCar-1].weight = amount

        elif update == "max_pack":
            list_cars[numCar-1].max_pack = amount

        elif update == "max_Continer":
            list_cars[numCar-1].max_Continer = amount

        print("#_Admin-----> Do you want to change again? [1/0]")
        answer = int(input("User: "))

        if answer == 0:
            break

# ************** Delete **************
def Delete_Package():

    global count_Package

    Display_Package() 

    print("#_Admin---> Enter number")
    numPackage = int(input("NumPackage :"))

    list_Package.pop(numPackage -1 )

    count_Package -=1

    for i in list_Package:
        i.numPackage = list_Package.index(i) + 1

def Delete_Contine():

    global count_continer

    Display_Package() 

    print("#_Admin---> Enter number")
    numContiner = int(input("numContiner :"))

    list_continers.pop(numContiner -1 )

    count_continer -=1

    for i in list_continers:
        i.numContiner = list_continers.index(i) + 1 

def Delete_Car():

    global count_car

    Display_car() 

    print("#_Admin---> Enter number")
    numCar = int(input("numCar :"))

    list_cars.pop(numCar -1 )

    numCar -=1

    for i in list_cars:
        i.numCar = list_cars.index(i) + 1 








# ************** Main **************

def main():

    login()

    while 1:
        choose = Management_menu()

        if choose == 1:

            choose_CRUD_Package = menu_CRUD_Package()

            if choose_CRUD_Package == 1:
                Insert_Package()
            elif choose_CRUD_Package == 2:
                Update_Package()
            elif choose_CRUD_Package == 3:
                Delete_Package()

        elif choose == 2:
            choose_CRUD_Continer = menu_CRUD_continer()

            if choose_CRUD_Continer == 1:
                Insert_Contine()
            elif choose_CRUD_Continer == 2:
                Update_Contine()
            elif choose_CRUD_Continer == 3:
                Delete_Contine()

        elif choose == 3:
            choose_CRUD_Car = menu_CRUD_Car()

            if choose_CRUD_Car == 1:
                Insert_Car()
            elif choose_CRUD_Car == 2:
                Update_Car()
            elif choose_CRUD_Car == 3:
                Delete_Car()

        elif choose == 4:
            while 1:
                
                choose_Loading_menu = Loading_menu()

                if choose_Loading_menu == 1 :
                    Display_Package()
                
                elif choose_Loading_menu == 2 :
                    Display_continer()

                elif choose_Loading_menu == 3 :
                    Display_car()

                elif choose_Loading_menu == 4 :

                    Display_continer()

                    print("#_Admin--->  What kind of continer do you want to loading (1.Freezer / 2.Breakable)")
                    choose_kindOf_continer = int(input('User: '))

                    print("#_Admin---> Enter numContiner ")
                    numContiner = int(input('User: '))

                    if choose_kindOf_continer == 1: 

                        for i in list_continers:

                            if i.numContiner == numContiner:     #  find continer
                                
                                sum_weight_p = 0
                                
                                j = 1

                                while 1:

                                    if j<= i.max_pack and i.weight >= sum_weight_p:

                                        for k in list_Package: 

                                            if k.name == "Cold_Package" :

                                                line1 = "Cold Package" + str(k.numPackage) + ':'
                                                line2 = "weight: " + str(k.weight) + " ||| " +"destination: " + k.destination + " ||| " + "beginning: " + k.beginning + " ||| " + "min_temperature: " + k.min_temperature +'\n'
                                                print(line1)
                                                print(line2)

                                    
                                        print("#_Admin------> Do you want To load pack(packs) if you have? [1/0] ")
                                        answer = int(input('User: '))

                                        if answer == 1:

                                            print("#_Admin------> Choose the numPackage to loading: ")
                                            numPackage = int(input('User: ')) 

                                            i.list_packs_FreezerContainer.append(list_Package[numPackage-1])       

                                            sum_weight_p += list_Package[numPackage-1].weight   

                                            list_Package.pop(numPackage-1)

                                            for q in list_Package:
                                                q.numPackage = list_Package.index(q) + 1 

                                        else:

                                            break

                                    else:
                                        print("#_Admin-------> Overfllow Error : something went wrong in weight or max_pack")
                                        break

                                    j+=1

                    elif choose_kindOf_continer == 2: 

                        for i in list_continers:

                            if i.numContiner == numContiner:     #  find continer
                                
                                sum_weight_p = 0

                                while 1:
                                    
                                    j = 1

                                    if j<= i.max_pack and i.weight >= sum_weight_p:

                                        for k in list_Package: 

                                            if k.name == "Breakable_package" :
                                                line1 = "Breakable package" + str(k.numPackage) + ':'
                                                line2="weight: " + str(k.weight) + " ||| " +"destination: " + k.destination + " ||| " + "beginning: " + k.beginning +'\n'
                                                print(line1) 
                                                print(line2)

                                    
                                        print("#_Admin------> Do you want To load pack(packs) if you have? [1/0] ")
                                        answer = int(input('User: '))

                                        if answer == 1:

                                            print("#_Admin------> Choose the numPackage to loading: ")
                                            numPackage = int(input('User: ')) 

                                            i.list_packs_Breakable_Package_Container.append(list_Package[numPackage-1])       

                                            sum_weight_p += list_Package[numPackage-1].weight   

                                            list_Package.pop(numPackage-1)

                                            for q in list_Package:
                                                q.numPackage = list_Package.index(q) + 1 

                                        else:

                                            break

                                    else:
                                        print("#_Admin-------> Overfllow Error : something went wrong in weight or max_pack")
                                        break

                                    j+=1

                elif choose_Loading_menu == 5 :

                    for i in list_cars:

                        if i.name == "CarContiner" :
                            line1 = "CarContiner " + str(i.numCar) + ':' 
                            line2 = "weight: " + str(i.weight) + " ||| " +"max_Continer: " + str(i.max_Continer) + '\n'
                            print(line1) 
                            print(line2)

                    print("#_Admin---> Enter numCar ")
                    numCar = int(input('User: '))

                    for i in list_cars:

                        if i.numCar == numCar:

                            sum_weight_con = 0
                            
                            j = 1                        

                            while 1:

                                if j<= i.max_Continer and i.weight >= sum_weight_con:

                                    for k in list_continers:  

                                        if k.name == "Breakable_Package_Container" :
                                            line1 = "Continer breakable" + str(k.numContiner) + ':' 
                                            line2 =  "weight: " + str(k.weight) + " ||| " +"max_pack: " + str(k.max_pack) + " ||| "  + 'max_speed: ' + k.max_speed +'\n'
                                            print(line1)  
                                            print(line2)    

                                        elif k.name == "FreezerContainer" :
                                            line1 = "Continer Freezer" + str(k.numContiner) + ':' 
                                            line2 = "weight: " + str(k.weight) + " ||| " +"max_pack: " + str(k.max_pack) + " ||| "  + 'refrigerator_min_temperature: ' + k.refrigerator_min_temperature +'\n'
                                            print(line1) 
                                            print(line2)
                                

                                    print("#_Admin------> Do you want To load continer(continers) if you have? [1/0] ")
                                    answer = int(input('User: '))

                                    if answer == 1:

                                        print("#_Admin------> Choose the numContiner to loading: ")
                                        numContiner = int(input('User: ')) 

                                        i.list_continers_car.append(list_continers[numContiner-1])       

                                        sum_weight_con += list_Package[numContiner-1].weight

                                        list_continers.pop(numContiner-1)

                                        for q in list_continers:
                                            q.numContiner = list_continers.index(q) + 1 

                                    else:
                                        break
                                else:
                                    print("#_Admin-------> Overfllow Error : something went wrong in weight or max_Continer")
                                    break

                                j+=1    

                elif choose_Loading_menu ==  6:

                    for i in list_cars:
                        if i.name == "CarRoom" :
                            line1 = "CarRoom" + str(i.numCar) + ':' 
                            line2 =  "weight: " + str(i.weight) + " ||| " +"max_pack: " + str(i.max_pack) + '\n'
                            print(line1)  
                            print(line2)

                    print("#_Admin---> Enter numCar ")
                    numCar = int(input('User: '))

                    for i in list_cars:

                        if i.numCar == numCar:

                            sum_weight_pack_simple = 0
                            
                            j = 1                        

                            while 1:

                                if j<= i.max_pack and i.weight >= sum_weight_pack_simple:

                                    for k in list_Package:  

                                        if k.name == "Simple_Package" :
                                            line1 = "Simple Package" + str(k.numPackage) + ':'
                                            line2 = "weight: " + str(k.weight) + " ||| " +"destination: " + k.destination + " ||| " + "beginning: " + k.beginning +'\n'
                                            print(line1)   
                                            print(line2)    

                                    print("#_Admin------> Do you want To load Simple_Package(Simple_Packages) if you have? [1/0] ")
                                    answer = int(input('User: '))

                                    if answer == 1:

                                        print("#_Admin------> Choose the numPackage to loading: ")
                                        numPackage = int(input('User: ')) 

                                        i.list_packs_simple.append(list_Package[numPackage-1])       

                                        sum_weight_pack_simple += list_Package[numPackage-1].weight

                                        list_Package.pop(numPackage-1)

                                        for q in list_Package:
                                            q.numPackage = list_Package.index(q) + 1 

                                    else:
                                        break
                                
                                else:
                                    print("#_Admin-------> Overfllow Error : something went wrong in weight or max_Pack")
                                    break

                                j+=1

                elif choose_Loading_menu == 7 :
                    break

        elif choose == 5:

            choose_send_Receive = Send_Receive_menu()

            if choose_send_Receive == 1:

                for i in list_cars:

                    if i.name == "CarRoom":

                        print(f'********** Simple_Package of CarRoom {i.numCar} **********')

    
                        for j in i.list_packs_simple:
                
                            line1 = "Simple Package" + str(j.numPackage) + ':'
                            line2 = "weight: " + str(j.weight) + " ||| " +"destination: " + j.destination + " ||| " + "beginning: " + j.beginning +'\n'
                            print(line1)   
                            print(line2)

                        print(50*'*')

                    elif i.name == "CarContiner":

                        print(f'********** Carry Continers for Car {i.numCar} **********')

                        for j in i.list_continers_car:

                            if j.name == "Breakable_Package_Container" :
                                line1 = "Continer breakable" + str(j.numContiner) + ':' 
                                line2 =  "weight: " + j.weight + " ||| " +"max_pack: " + str(j.max_pack) + " ||| "  + 'max_speed: ' + j.max_speed +'\n'
                                print(line1)  
                                print(line2) 

                                for k in j.list_packs_Breakable_Package_Container:
                            
                                    line1 = "Breakable package" + str(k.numPackage) + ':'
                                    line2="weight: " + k.weight + " ||| " +"destination: " + k.destination + " ||| " + "beginning: " + k.beginning +'\n'
                                    print(line1) 
                                    print(line2)

                
                            elif j.name == "FreezerContainer" :
                                line1 = "Continer Freezer" + str(j.numContiner) + ':' 
                                line2 = "weight: " + str(j.weight) + " ||| " +"max_pack: " + str(j.max_pack) + " ||| "  + 'refrigerator_min_temperature: ' + j.refrigerator_min_temperature +'\n'
                                print(line1) 
                                print(line2)


                                for k in j.list_packs_FreezerContainer:

                                    line1 = "Cold Package" + str(k.numPackage) + ':'
                                    line2 = "weight: " + str(k.weight) + " ||| " +"destination: " + k.destination + " ||| " + "beginning: " + k.beginning + " ||| " + "min_temperature: " + k.min_temperature +'\n'
                                    print(line1)
                                    print(line2)

                        print(50*'*')


                    while 1 :

                        print('#_Admin ------> Do you want to Insert load to warehous? [1/0]')
                        answer = int(input('User: '))

                        if answer == 1:

                            choose = int(input('Enter your load :'))

                            if choose == i.numCar :

                                warehous.append(i)

                        else :
                            break



            elif choose_send_Receive == 2:

                f = open(filename, 'a')
                f.write('\n')

                for i in warehous:

                    if i.name == "CarRoom":

                        f.write(f'********** Simple_Package of CarRoom {i.numCar} **********\n')
                        f.write('\n')
                        for j in i.list_packs_simple:
                
                            line1 = "Simple Package" + str(j.numPackage) + ':'
                            line2 = "weight: " + str(j.weight) + " ||| " +"destination: " + j.destination + " ||| " + "beginning: " + j.beginning +'\n'
                            f.write(line1)
                            f.write('\n')
                            f.write(line2)
                        f.write('\n')    
                 
                    elif i.name == "CarContiner":

                        f.write(f'********** Carry Continers for Car {i.numCar} **********')
                        f.write('\n')

                        for j in i.list_continers_car:

                            if j.name == "Breakable_Package_Container" :
                                line1 = "Continer breakable" + str(j.numContiner) + ':' 
                                line2 =  "weight: " + str(j.weight) + " ||| " +"max_pack: " + str(j.max_pack) + " ||| "  + 'max_speed: ' + j.max_speed +'\n'
                                f.write(line1)  
                                f.write('\n')
                                f.write(line2) 

                                for k in j.list_packs_Breakable_Package_Container:
                            
                                    line1 = "Breakable package" + str(k.numPackage) + ':'
                                    line2="weight: " + str(k.weight) + " ||| " +"destination: " + k.destination + " ||| " + "beginning: " + k.beginning +'\n'
                                    f.write(line1)  
                                    f.write('\n')
                                    f.write(line2)

                            elif j.name == "FreezerContainer" :
                                line1 = "Continer Freezer" + str(j.numContiner) + ':' 
                                line2 = "weight: " + str(j.weight) + " ||| " +"max_pack: " + str(j.max_pack) + " ||| "  + 'refrigerator_min_temperature: ' + j.refrigerator_min_temperature +'\n'
                                f.write(line1)  
                                f.write('\n')
                                f.write(line2)


                                for k in j.list_packs_FreezerContainer:

                                    line1 = "Cold Package" + str(k.numPackage) + ':'
                                    line2 = "weight: " + str(k.weight) + " ||| " +"destination: " + k.destination + " ||| " + "beginning: " + k.beginning + " ||| " + "min_temperature: " + k.min_temperature +'\n'
                                    f.write(line1)  
                                    f.write('\n')
                                    f.write(line2)

                f.close()

main()

input()
