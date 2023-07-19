if __name__ == '__main__':

    # Importing Modules
    import os
    import random

    # Adding Or Removing Customers

    add = int(input("Enter 1 to add a person \n2 to remove\n3 if you are a existing Customer :\n"))

    if add == 1:
        nme = input("Enter Your Name :")
        Blc = random.randint(1, 10000)

        f = open(f"{nme}.txt", 'w')
        f.write(f"{nme}\n")
        f.write(str(Blc))
        f.close()
        print("Success , Customer added !")

    elif add == 2:
        bc = str(input("Enter Your Name :"))
        b1 = list(os.listdir())
        if f"{bc}.txt" in b1:
            os.remove(f"{bc}.txt")
            print("Customer Removed !")

    # If customer is already in the bank

    elif add == 3:
        name = str(input("Enter Your Name to access bank :"))
        b = list(os.listdir())
        for i in b:
            if f"{name.lower()}.txt" == i.lower():
                with open(i, 'r') as f:
                    user = f.readline()
                    Balance = f.readline()

                    # Here are some things that you can do in bank .... :D
                    print("                     As_Bank                     ")
                    inp = int(input('''Enter 1 to Check Balance Money 
Enter 2 to Widrawl Money
Enter 3 to Deposit Money
Enter 4 to Exit \n'''))

                    Balance = int(Balance)

                    if inp == 1:  # To check balance
                        print(f"Your Balance is {Balance}")

                    elif inp == 2:  # To Widrawl Money
                        wid_mny = int(input(f"Enter the amount to widrawl (current available amount is {Balance}):"))
                        if wid_mny > Balance:
                            print("Your Account doesn't have enough money ")

                        else:
                            res = Balance - wid_mny
                            f = open(f"{name}.txt", 'r')
                            content = f.readline()
                            content2 = f.readline()
                            content2 = content2.replace(str(Balance), str(res))
                            f.close()

                            with open(f"{name}.txt", 'w') as fi:
                                fi.write("Ashmit \n")
                                fi.write(content2)
                            print(f"Your Money is Widrawled and Available balance is {res} ")

                    elif inp == 3:  # To deposit Money
                        dip_mny = int(input(f"Enter the amount to diposit (current available amount is {Balance}) :"))
                        if dip_mny > 100000:
                            print("money Deposit Limit exceeded , You cannot deposit more than 100000")

                        else:
                            res = Balance + dip_mny
                            f = open(f"{name}.txt", 'r')
                            content = f.readline()
                            content2 = f.readline()
                            content2 = content2.replace(str(Balance), str(res))
                            f.close()

                            with open(f"{name}.txt", 'w') as fi:
                                fi.write(f"{name} \n")
                                fi.write(content2)
                            print(f"Your Money is Deposited and Available balance is {res} ")

                    elif inp == 4:  # To Exit Bank
                        pass

                    elif inp != 1 and 2 and 3 and 4:
                        print("Enter Valid Input ")

#### Special Note : Currently I'm Learning Python..... and I'm not that much familiar with Files I\O, So Please Forgive me if there anything wrong
