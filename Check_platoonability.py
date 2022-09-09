import csv


def No_of_lines():
    cfile = open("csv_1.csv")
    reader = csv.reader(cfile)
    lines = len(list(reader))
    cfile.close()
    if lines == 0:
        Create_csv()
        return 1
    return lines


def Create_csv():
    with open('csv_1.csv', 'w', newline='') as f:
        fieldname = ['Sl_No', 'Register_ID', 'Additional_follower', 'Location_start', 'Location_destination']
        thewriter = csv.DictWriter(f, fieldnames=fieldname)
        thewriter.writeheader()
        f.close()


def Write_to_csv(lis):
    lines_count = No_of_lines()

    with open('csv_1.csv', 'a', newline='') as f:
        fieldname = ['Sl_No', 'Register_ID', 'Additional_follower', 'Location_start', 'Location_destination']
        thewriter = csv.DictWriter(f, fieldnames=fieldname)

        thewriter.writerow(
            {'Sl_No': lines_count, 'Register_ID': lis[0], 'Additional_follower': lis[1], 'Location_start': lis[2],
             'Location_destination': lis[3]})
        f.close()


def Read_all_from_csv():
    with open('csv_1.csv', 'r', newline='') as f:
        thereader = csv.reader(f)

        for row in thereader:
            print(row)




def Read_specific_line(line_list):
    with open('csv_1.csv', 'r', newline='') as f:

        for pos, line in enumerate(f):
            if pos in line_list:
                return line


def Check_platoonable(line_no):
    l1 = Read_specific_line([1])
    print("Leader Starting point: ", l1[8])
    print("Leader Destination point: ", l1[10])
    l2 = Read_specific_line([line_no])
    print("Joining vehicle Starting point: ", l2[8])

    if ord(l1[8]) <= ord(l2[8]) <= ord(l1[10]):
        print("The vehicle is Platoonable")
    else:
        print("The vehicle is Not Platoonable")


def register():
    register_id = int(input("Enter ID [3 Digit]: "))
    additional_follower = int(input("Enter the no additional followers [0-9]: "))
    location_start = input("Location of starting [A-Z]: ")
    location_destination = input("Location of destination [A-Z]: ")
    return [register_id, additional_follower, location_start, location_destination]


if __name__ == "__main__":
    # Create_csv()
    print("Check if Platoonable ")
    print("1. Register")
    print("2. Check whether your vehicle is platoonable")
    print("3. Exit\n")

    Read_all_from_csv()

    in_option = int(input("\nEnter your option: "))

    flag = True

    while flag:
        if in_option == 1:
            lis = register()
            Write_to_csv(lis)
            break

        elif in_option == 2:
            sl_no = int(input("Enter the Serial Number"))
            Check_platoonable(sl_no)
            break

        else:
            flag = False
            print("End")

    #
    # lis = register()
    # Write_to_csv(lis)
    # Read_all_from_csv()
    # Check_platoonable(2)
