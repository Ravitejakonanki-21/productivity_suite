def converter_menu():
    print("""
Unit Converter:
1. KM to Miles
2. Miles to KM
""")
    choice = input("Enter choice: ")

    if choice == "1":
        km = float(input("Enter km: "))
        print("Miles:", km * 0.621371)

    elif choice == "2":
        miles = float(input("Enter miles: "))
        print("KM:", miles / 0.621371)
