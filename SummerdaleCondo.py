
run = True

while run:

    print("1.Park View at $150,000")

    print("2.Golf Course View at $170,000")

    print("3.Lake View at $210,000")

    print("4.Exit")

    print("")

    choice = input("Please enter choice for accomodation: ")

    if choice == "4":
        break

    numb = input("Would you like a 1.garage for an extra $5000 or just a 2.parking space for $0: ")


    if choice == "1" and numb == "1":
        print(f"Park View at ${(150000 + 5000):.2f}")
        break

    elif choice == "1" and numb == "2":
        print(f"Park View at ${150000:.2f}")
        break

    elif choice == "2" and numb == "1":
        print(f"Golf Course View at ${(170000 + 5000):.2f}")
        break

    elif choice == "2" and numb == "2":
        print(f"Golf Course View at ${170000:.2f}")
        break

    elif choice == "3" and numb == "1":
        print(f"Lake View at ${(210000 + 5000):.2f}")
        break

    elif choice == "3" and numb == "2":
        print(f"Lake View at ${210000:.2f}")
        break

    else:
        print("Please enter valid choice")
