from BankAccount import BankAccount
from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount

def main():
    currentobject=CurrentAccount(722, "bosco", 10000, 10 )
    savingsobject=SavingsAccount(7234, "john", 90000, 15 )

    while True:
        print("1.current account")
        print("2.saving account")
        menu_option=int(input())

        if menu_option==1:
            print("1.deposit funds")
            print("2.withdraw funds")
            submenu_option=int(input())
            if submenu_option==1:
                value=int(input("how much would you like to deposit"))
                currentobject.deposit(value)
            elif submenu_option==2:
                value=int(input("how much would you like to withdraw"))
                currentobject.withdraw(value)
            else:
                print("wrong menu choice")
        elif menu_option==2:
            print("1.deposit funds")
            print("2.withdraw funds")
            submenu_option=int(input())
            if submenu_option==1:
                value=int(input("how much would you like to deposit"))
                currentobject.deposit(value)
            elif submenu_option==2:
                value=int(input("how much would you like to withdraw"))
                currentobject.withdraw(value)
            else:
                print("wrong menu choice")


if __name__ =="__main__":

    main()


