print("Hello In The Programe")

name = input("May you enter your name pls: \n")
age = int(input("May you enter your age pls: \n"))


match age:
    case age if age < 18:
        print("Age is young for entery")
    case age if age >= 18 and age <= 25:
        print("You may enter the club " + name)
    case age if age > 25:
        print("are you a memebr / with a memebr ")
        choice = input("yes / no \nyour choice: ")
        if choice == "yes":
            print("You may enter the club " + name)
        else:
            print("You arent permeted to enter the club")
