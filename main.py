print("""
Welcome 
Food order option:
------------------
1: Add item
2: Remove item
3: View item
4: Exit
""")
order = {}
option = int(input("Enter a option:  "))
while option != 0:
    if option == 1:
        print("1.Add item\n")
        item = input("Enter a item: ")
        qty = int(input("Enter quantity: "))
        order[item] = qty
    elif option == 2:
        print("2.Remove item\n")
        item = input("Enter a item to remove: ")
        del (order[item])  # revisa el arreglo con la palabra ingresada
        print("Se ha borrado: " + item + " Satisfactoriamente\n")
    elif option == 3:
        print("3.View item\n")
        for item in order:
            print(item, ":", order[item])  # imprime nombre item y cantidad del item...
    elif option == 4:
        print("4.Thank you for visit us...\n")
        break
    else:
        print("Enter a correct option between 1 to 4...\n ")
    option = int(input("Enter a option:  "))
