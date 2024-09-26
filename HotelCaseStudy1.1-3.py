# Options code by Jna, taga ayos Rhey Mark~

def main():
    costs = [[6000, 6300,6600],
             [8000, 8300, 8600],
             [10000, 13000, 10600],
             [12000, 12300, 12600]]
    type = []
    day = []
    res_fee = 250
    unavailable_room = [[],[]]
    print('\t\t\t\t    █   █   █ █████ ███    ███   ████    █   █  ███ █████ █████ █ ')
    print('\t\t\t\t    █   █  █ █  █   █  █  █   █ █        █   █ █   █  █   █     █ ')
    print('\t\t\t\t    █████ █   █ █   █   █ █   █ █ ███    █████ █   █  █   ████  █ ')
    print('\t\t\t\t    █   █ █████ █   █   █ █   █ █   █    █   █ █   █  █   █     █ ')
    print('\t\t\t\t    █   █ █   █ █   ████   ███   ███     █   █  ███   █   █████ █████')
    print("\t\t\t\t\t    --IT'S CHEEZY HOTDOGGY RELAXING IN OUR HOTEL!--")
                       
    while True:
        print("\n\t\t<<<" + "-" * 37 + "MAIN MENU" + "-" * 37 + ">>>")
        print("\t\t\t\t[0] - EXIT")
        print("\t\t\t\t[1] - ROOM INFORMATION LIST")
        print("\t\t\t\t[2] - ROOM AVAILABILITY")
        print("\t\t\t\t[3] - CHECK - IN")
        print("\t\t-" + "-" * 88)
        try:
            choice = int(input("\t\tPlace your choice here: "))
        except ValueError:
            print("\t\t\t> Please enter a valid value in the given options.\n")
            continue
        if choice == 0:
            print("> Program Terminated.")
            exit()
        elif choice == 1:
            prices(costs,res_fee)
        elif choice == 2:
            rooms(type,day,unavailable_room)
        elif choice == 3:
            check_in(costs,res_fee,unavailable_room)
        else:
            print("\t\t\t> Please choose between 0 - 3 only.\n")


# Price List code by Jna, Info by Trix, taga ayos by all~
def prices(costs,res_fee):
    print("\n\t\t" + "-" * 34 + "ROOM INFORMATION LIST" + "-" * 34)
    print("\n\t\t\t***Reservation Fee : ", res_fee)
    print("\n\t\t||--------------------------------------------------------------------------------------||    ")
    print("\t\t||    EXECUTIVE QUEEN ROOM (Type '1')      ||    EXECUTIVE DOUBLE ROOM (Type '2')       ||    ")
    print("\t\t||--------------------------------------------------------------------------------------||    ")
    print("\t\t||    2 adults                             ||    2-3 adults                             ||    ")
    print("\t\t||    35-square meter                      ||    35-square meter                        ||    ")
    print("\t\t||    Queen-size bed                       ||    Two (2) double beds                    ||    ")
    print("\t\t||    32-inch flat screen cable TV         ||    32-inch flat screen cable TV           ||    ")
    print("\t\t||    Coffee and tea station               ||    Coffee and tea station                 ||    ")
    print("\t\t||    Mini-refrigerator                    ||    Mini-refrigerator                      ||    ")
    print("\t\t||    Bathroom                             ||    Bathroom                               ||    ")
    print("\t\t||--------------------------------------------------------------------------------------||    ")
    print("\n\t\t||--------------------------------------------------------------------------------------||    ")
    print("\t\t||    FAMILY JUNIOR SUITE (Type '3')       ||    ONE BEDROOM SUITE (Type '4')           ||    ")
    print("\t\t||--------------------------------------------------------------------------------------||    ")
    print("\t\t||    2 adults 3 kids                      ||    1-2 adults                             ||    ")
    print("\t\t||    43-square meter                      ||    57-square meter                        ||    ")
    print("\t\t||    King-sized bed                       ||    King-sized bed and trundle bed         ||    ")
    print("\t\t||    Single and trundle bed               ||    32-inch flat screen inside bedroom     ||    ")
    print("\t\t||    32-inch flat screen cable TV         ||    32-inch flat screen inside living r.   ||    ")
    print("\t\t||    Coffee and tea station               ||    Coffee and tea station                 ||    ")
    print("\t\t||    Living Room(can accomodate 6 people) ||    Living Room(can accomodate 8 people)   ||    ")
    print("\t\t||    Mini-kitchen                         ||    Mini-kitchen                           ||    ")
    print("\t\t||    Bathroom with bathtub                ||    Bathroom with bathtub                  ||    ")
    print("\t\t||--------------------------------------------------------------------------------------||    ")

    print("\n\t\t||--------------------------------------------------------------------------------------||    ")
    print("\t\t||                                ROOM PRICE LIST                                       ||    ")
    print("\t\t||--------------------------------------------------------------------------------------||    ")
    for row in range(len(costs)):
        for col in range(len(costs[row])):
            print(f"\t\t||   Type {row + 1} \tAdditional Day: {col} \tCheck-in cost (with reservation fee): Php {costs[row][col] + res_fee} %4s" %"||")
        print("\t\t||++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++||    ")
    print()


# Availability of Rooms code by Brent n Trix, taga ayos slight palang Rhey Mark~
def rooms(type,day,unavailable_room):
    print("\n\t\t" + "-" * 36 + "ROOM AVAILABILITY" + "-" * 36)
    print("\t\t\t\tUnavailable rooms:")

    print("\t\tType number {} with Additional {} day/s is unavailable".format(type,day))

    print("\t\t" + "-" * 88 + "\n")
    main()

# Check-in code by Jna, taga ayos Rhey Mark~
def check_in(costs,res_fee,unavailable_room):
    print("\n\t\t" + "-" * 41 + "CHECK-IN" + "-" * 40)
    while True:
        try:
            type = int(input("\t\t>> Which Type of room you'd like to book? [Choose from 1-4]: "))
            day = int(input("\t\t>> How many days you would like to extend? [Choose from 0-2]: "))

        except ValueError:
            print("\t\t\t\t>> Invalid Input.\n")
            continue
        if 5 > type > 0 and 3 > day > -1:
            while True:
                choice2 = input("\t\t>> Would you like to book a reservation?[Y/N]: ")
                if choice2.upper() == "Y":
                    reservation_sign_up(costs, type, day, unavailable_room, res_fee)
                elif choice2.upper() == "N":
                    print("\t\t>> Alright, we'll be bringing you back to the menu")
                    print("\t" + "-" * 58 + "\n")
                    main()
                else:
                    print("\t\t>> Please input Y or N only.\n")
        else:
            print("\t\t\t> Please enter a valid value in the given options.\n")


# reservation_account() method code by Trixie, taga ayos Mar Brent n Rhey~
def reservation_sign_up(costs, type, day,unavailable_room,res_fee):
    print("\n\t\t>> Sign up to verify identity")
    username = input("\t\t\t>> Enter your username:")
    while True:
        passwd = input("\t\t\t>> Enter Password (should be at least 6 characters containing alphanumeric):")
        if password_check(passwd):
            hello(username, passwd, costs, type, day,unavailable_room,res_fee)
        else:
            print("\t\t\t\t> Input another password")


# log-in code by Trixie, taga ayos Mar Brent taga lagay ng tab Rhey~~
def password_check(passwd):
    val = True

    if len(passwd) < 6:
        print('\t\t\t\t> length should be at least 6')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('\t\t\t\t> Password should have at least one numeric value.')
        val = False

    if val:
        return val

# hello code by Trxie n Mar Brent modified by Rhey~
def hello(username, passwd, costs, type, day,unavailable_room,res_fee):
    tel_number = 0
    while True:
        print("\n\t\t>> Hello Ma'am/Sir, Please fill up the following information:")
        f_name = input("\t\t\t>> First Name      : ")
        m_name = input('\t\t\t>> Middle Initial  : ')
        l_name = input('\t\t\t>> Last Name       : ')
        c_info = input('\t\t\t>> Card number     : ')
        while True:
            try:
                tel_number = int(input('\t\t\t>> Cellphone Number: '))
            except ValueError:
                print("\t\t\t\tPlease Enter a Numeric Value")
                continue
            if len(str(tel_number)) == 10:
                break
            else:
                print('\t\t\t\tPlease enter your 11 digit number')
                continue
        print('\n\t\t>> Hello, please double check the following information:')
        print('\t\t\t> First Name      : ', f_name.upper())
        print('\t\t\t> Middle Initial  : ', m_name[0].upper() + '.')
        print('\t\t\t> Last Name       : ', l_name.upper())
        print('\t\t\t> Card Number     : ', c_info)
        print('\t\t\t> Cellphone Number: ', tel_number)
        answer = ''
        while answer.upper() != 'Y':
            answer = input('\t\t>> Do you want to re-enter your information? [Y/N]: ')
            if answer.upper() == "N":
                break
            elif answer.upper() != 'Y':
                print("\t\t\t> Please input Y or N only.\n")
        if answer.upper() == 'N':
            break
    print("\n\t\t> " + f_name.title(), "Please re-log in")
    loop(username, passwd, costs, type, day,unavailable_room,res_fee)


# loop code by Brent, taga lagay ng tab Rhey~
def loop(username, passwd, costs, type, day,unavailable_room, res_fee):
    log_in_un = input("\t\t\t>> Username:")
    if log_in_un == username:
        log_in_pw = 0
        while log_in_pw != passwd:
            log_in_pw = input("\t\t\t>> Password:")
            if log_in_pw != passwd:
                print("\t\t\t> Wrong password, try again")
            elif log_in_pw == passwd:
                check_out(costs, type, day,unavailable_room,res_fee)
    else:
        print("\t\t\t> Invalid username, try again")
        loop(username, passwd, costs, type, day, unavailable_room, res_fee)


# Check-out code by Trix kinalikut ng slight Rheyyyyy~
def check_out(costs, type, day, unavailable_room,res_fee):
    print("\n\t\t> Check-out")
    print("\t\t\t> Reservation Fee: ", res_fee)
    print(f"\t\t\t> Confirmation: Hotel room type {type} with Additional {day} day/s \n\n"
          f"\t\t\t\t\tTotal: Php {costs[type - 1][day] + res_fee}")
    print("\n\t\t" + "-" * 88 + "\n")
    unavailable_room.append([type, day])
    rooms(type, day, unavailable_room)


main()
