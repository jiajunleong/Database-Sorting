#!/usr/bin/env python
# coding: utf-8

title_of_package = [
    "Sentosa Package",
    "MBS Package",
    "CityHall Package",
    "Jurong Package",
    "Woodlands Package",
    "Yishun Package",
    "Clementi Package",
    "Tuas Package",
    "Bedok Package",
    "Tampines Package",
]  # initialize the package list.

price_of_package = {
    "Sentosa Package": 100,
    "MBS Package": 200,
    "CityHall Package": 3000,
    "Jurong Package": 400,
    "Woodlands Package": 500,
    "Yishun Package": 600,
    "Clementi Package": 700,
    "Tuas Package": 800,
    "Bedok Package": 1200,
    "Tampines Package": 1900,
}  # initialize the package costs dictionary.

name_of_customer = [
    "John Cena",
    "Jia Jun",
    "Zoey Teo",
    "Alicia Tan",
    "Derrick Lim",
    "Adriel Wong",
    "Edwin Neo",
    "Zi Jun",
    "Michael Tan",
    "Elton Neo",
]  # initialize the customers name list.

booked_details = {
    "Michael Tan": ["Sentosa Package", 2],
    "Edwin Neo": ["Clementi Package", 1],
    "Elton Neo": ["Bedok Package", 5],
    "John Cena": ["MBS Package", 6],
    "Alicia Tan": ["Yishun Package", 7],
    "Zi Jun": ["Tuas Package", 4],
    "Jia Jun": ["Jurong Package", 3],
    "Adriel Wong": ["Tampines Package", 1],
    "Zoey Teo": ["CityHall Package", 54],
    "Derrick Lim": ["Woodlands Package", 20],
}  # initialize the booked details dictionary.

customerSort = [
    ["Michael Tan", "Sentosa Package", "2 pax", "$100/pax"],
    ["Edwin Neo", "Clementi Package", "1 pax", "$700/pax"],
    ["Elton Neo", "Bedok Package", "5 pax", "$1200/pax"],
    ["John Cena", "MBS Package", "6 pax", "$200/pax"],
    ["Alicia Tan", "Yishun Package", "7 pax", "$600/pax"],
    ["Zi Jun", "Tuas Package", "4 pax", "$800/pax"],
    ["Jia Jun", "Jurong Package", "3 pax", "$400/pax"],
    ["Adriel Wong", "Tampines Package", "1 pax", "$1900/pax"],
    ["Zoey Teo", "CityHall Package", "54 pax", "$3000/pax"],
    ["Derrick Lim", "Woodlands Package", "20 pax", "$500/pax"],
]

packageSort = [
    ["Sentosa Package", "2 pax", "$100/pax", "Michael Tan"],
    ["Clementi Package", "1 pax", "$700/pax", "Edwin Neo"],
    ["Bedok Package", "5 pax", "$1200/pax", "Elton Neo"],
    ["MBS Package", "6 pax", "$200/pax", "John Cena"],
    ["Yishun Package", "7 pax", "$600/pax", "Alicia Tan"],
    ["Tuas Package", "4 pax", "$800/pax", "Zi Jun"],
    ["Jurong Package", "3 pax", "$400/pax", "Jia Jun"],
    ["Tampines Package", "1 pax", "$1900/pax", "Adriel Wong"],
    ["CityHall Package", "54 pax", "$3000/pax", "Zoey Teo"],
    ["Woodlands Package", "20 pax", "$500/pax", "Derrick Lim"],
]



class PackageDealsInventory:

    def __init__(self, name_of_customer, title_of_package, price_of_package, booked_details, customerSort, packageSort):

        self.name_of_customer = name_of_customer
        self.title_of_package = title_of_package
        self.price_of_package = price_of_package
        self.booked_details = booked_details
        self.customerSort = customerSort
        self.packageSort = packageSort

    def display_all_records(self):

        print("\nLIST OF CUSTOMERS: ")
        for items in self.name_of_customer:
            print(items)

        print("\nLIST OF PACKAGES: ")
        for items in self.title_of_package:
            print(items)

        print("\nLIST OF PACKAGE COSTS: ")
        for items, integer in self.price_of_package.items():
            print(f"{items}: ${integer}")

        print("\nLIST OF BOOKED DETAILS: ")
        for items, integer in self.booked_details.items():
            if integer[1] == 1:
                print(f"{items}: {integer[0]} for {integer[1]} pax")
            else:     #f-string formatting, faster than normal str.formatting
                print(f"{items}: {integer[0]} for {integer[1]} pax")

    def bubble_sort_customer(self):    #not suitable for large data sets ; easiest

        list_scale = len(self.customerSort)
        for s in range(list_scale - 1):
            reversed_list = False  # list items positions have not been reversed yet
            for j in range(list_scale - 1 - s):
                # if second range item is greater than first range item, list has been reversed
                if self.customerSort[j] > self.customerSort[j + 1]:
                    reversed_list = True
                    self.customerSort[j], self.customerSort[j + 1] = (
                        self.customerSort[j + 1], self.customerSort[j], )
            if not reversed_list:
                break  # halt the iteration once the items have been sorted
        print("Customer names sorted using bubble sort: \n")
        for item in self.customerSort:
            print(item[0] + ":", ": ".join(map(str, item[1:])))

    def selection_sort_package(self):    #finds lowest value first

        list_scale = len(self.packageSort)  # create variable for size of title_of_package list
        for s in range(list_scale - 1):  # for loop to get minimum value in the list
            minimum_value = s
            for k in range(s + 1, list_scale):
                if self.packageSort[k] < self.packageSort[minimum_value]:
                    minimum_value = k  # keep finding the minimum value
            if (
                minimum_value != s
            ):  # if statement to make sure each preceding value is less than the next
                self.packageSort[minimum_value], self.packageSort[s] = (
                    self.packageSort[s],
                    self.packageSort[minimum_value],
                )
        print("Package Names Sorted using Selection sort: ")
        for item in self.packageSort:
            print(item[0] + ":", ": ".join(map(str, item[1:])))
        #print(*self.customerSort, sep="\n")  # print sorted items


    def insertion_sort_price_of_package(self):    #compare 2 values all the time

        price_list = []  # initialize empty list
        k = {}  # initialize empty dictionary
        for (
            item, price,
        ) in (
            self.price_of_package.items()
        ):  # for loop to store the dictionary values in price_list
            price_list.append(price)

        # insertion sort process
        for placement, price in enumerate(price_list[1:]):
            holdingIndex = placement
            while placement >= 0 and price < price_list[placement]:
                price_list[placement + 1] = price_list[placement]
                placement -= 1
            if placement != holdingIndex:
                price_list[placement + 1] = price

        for (price) in (price_list):  # for loop to add data to empty dictionary using sorted data as key value pairs
            for item, val in self.price_of_package.items():
                if price == val:
                    k[item] = val
        print("Package Cost Sorted using Insertion sort: \n")
        for item, price in k.items():
            print(f"{item}: ${price}")  # print sorted data

    def linear_search_customer(self, searched_name):   #0(n) time complexity

        # for loop to search the given input linearly
        for placement, name in enumerate(self.name_of_customer):
            name = name.lower()
            if name == searched_name:
                return placement

        return -1

    def stooge_package(self, unsortedList, firstElement, lastElement):
        """
        Bonus feature is a function that uses the stooge sort algorithm to sort the 
        package name list and return it to be used in the binary search function for
        the package name list.
        """

        if firstElement >= lastElement:
            return None

        if unsortedList[firstElement] > unsortedList[lastElement]:
            unsortedList[firstElement], unsortedList[lastElement] = (unsortedList[lastElement], unsortedList[firstElement],)

        if lastElement - firstElement + 1 > 2:
            two_thirds = (int)((lastElement - firstElement + 1) / 3)

            # sort two third of the elements
            self.stooge_package(unsortedList, firstElement, (lastElement - two_thirds))

            # sort two third of the elements
            self.stooge_package(unsortedList, firstElement + two_thirds, (lastElement))

            self.stooge_package(unsortedList, firstElement, (lastElement - two_thirds))

        return unsortedList

    def binary_search_package(self, sorted_title_of_package, searched_title_of_package):  #0(Log n) time complexity

        start = 0  # placement of first item
        end = len(sorted_title_of_package) - 1  # placement of last item

        # while loop to search for the item using binary search
        while start <= end:
            middle = start + (end - start) // 2
            current_item = sorted_title_of_package[middle]
            current_item = current_item.lower()
            if current_item == searched_title_of_package:
                return middle

            elif searched_title_of_package < current_item:
                end = middle - 1

            else:
                start = middle + 1

        return None

    def record_range(self):
        x = 0
        print("We have affordable to expensive packages.")
        while x == 0:
            lower = int(input("Enter lower value: "))
            upper = int(input("Enter upper value: "))
            validate_lower = isinstance(lower, int)
            validate_upper = isinstance(upper, int)
            if validate_lower and validate_upper == False:
                continue
            else:
                x = 1

            # for loop to get all items in that range
            for items, value in self.price_of_package.items():
                if value >= lower and value <= upper:
                    print(f"{items} : ${value}")


def main():

    active_class = PackageDealsInventory(
        name_of_customer, title_of_package, price_of_package, booked_details, customerSort, packageSort)
            # pass the class to the active_class object

    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    )
    # making the interface user friendly
    print("Welcome To The Singapore Cultural Hotel!")
    print(
        ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
    )

    # while loop to ensure the program is only terminated if the user types 0
    while True:
        print(
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        )

        # program menu
        print("1: Display all records")
        print("2: Sort record by Customer Name using Bubble sort")
        print("3: Sort record by Package Name using Selection sort")
        print("4: Sort record by Package Cost using Insertion sort")
        print("5: Search record by Customer Name using Linear Search and update record")
        print("6: Search record by Package Name using Binary Search and update record")
        print("7: List records range from $X to $Y. e.g $100-200")
        print("0: Exit Application ")
        print(
            ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        )

        try:  # error handling
            user_input = int(
                input("Please choose an item from the menu (or type 0 to exit): ")
            )  # ask user for input
            if user_input == 0:
                break  # end the program if user inputs 0

            elif user_input == 1:
                active_class.display_all_records()

            elif user_input == 2:
                active_class.bubble_sort_customer()

            elif user_input == 3:
                active_class.selection_sort_package()

            elif user_input == 4:
                active_class.insertion_sort_price_of_package()

            elif user_input == 5:
                searchName = input("Enter Customer name to be searched/created: ")
                # ask user for the name to be searched/created
                # create case insensitivity by converting input to lowercase
                searchName = searchName.lower()
                results = active_class.linear_search_customer(searchName)
                if results == -1:
                    update_record = input(
                        # if name is not found, prompt user for customer name to be created
                        "Name not found. Enter name to be created:"
                    )

                    update_record = update_record.lower()  # enforce case insensitivity
                    name_of_customer.append(
                        update_record.title()
                        )  # append user input to appropriate list
                    print("Record has been updated!")  # inform user the name has been updated successfully
                    print(*name_of_customer, sep="\n")  # print the new list

                else:
                    print(
                        f"\n{searchName.title()} is number {active_class.linear_search_customer(searchName) + 1} in our list."
                    )
                    for index, value in booked_details.items():
                        if index.lower() == searchName:
                            if value[1] == 1:
                                print(
                                    f"{searchName.title()} has booked for the {value[0]} package for {value[1]} person."
                                )
                            else:
                                print(
                                    f"{searchName.title()} has booked for the {value[0]} package for {value[1]} people."
                                )
                            for item, cost in price_of_package.items():
                                if value[0] == item:
                                    print(
                                        f"{searchName.title()} has paid ${value[1] * cost} for the package."
                                    )
                    update_decision = input(
                        "Type Y if you want to update customer record or N to go back: "
                    ).lower()
                    if update_decision == "y":
                        new_package = input(
                            "Sentosa Package\nMBS Package\nCityHall Package\nJurong Package\nWoodlands Package\nYishun Package\nClementi Package\nTuas Package\nBedok Package\nTampines Package\nEnter Package Name: "
                        )
                        new_package = (new_package.lower())
                        new_pax = int(input("Type new pax in figures: "))

                        booked_details[searchName.title()] = [
                            new_package.title(),
                            new_pax,
                        ]
                        print("Client's booking information has been updated.")
                        print("\nLIST OF BOOKED DETAILS: ")
                        for items, integer in active_class.booked_details.items():
                            if integer[1] == 1:

                                print(f"{items}: {integer[0]} for {integer[1]} people")
                            else:
                                print(f"{items}: {integer[0]} for {integer[1]} people")

            elif user_input == 6:
                searched_title_of_package = input(
                    "Enter package name to be searched: "
                )  # ask user for name to be searched
                searched_title_of_package = (
                    searched_title_of_package.lower()
                )  # enforce case insensitivity
                i = 0
                h = len(title_of_package) - 1
                search_results = active_class.binary_search_package(
                    active_class.stooge_package(title_of_package, i, h),    #using sorted stooge package to help with binary search
                    searched_title_of_package,
                )
                if search_results == None:
                    enter_record = input(
                        # if the while loop does not find the name, inform user and ask them to update
                        f"{searched_title_of_package.title()} was not found. Type Y to create new package or N to go back: "
                    )
                    enter_record = enter_record.lower()
                    if enter_record == "y":
                        title_of_package.append(enter_record.title())
                        new_price = int(input("Enter Price of Package: "))
                        price_of_package[searched_title_of_package.title()] = new_price

                        print("Record has been updated!")
                        for item, value in price_of_package.items():
                            print(f"{item}: ${value}")


                else:
                    print(
                        f"The {searched_title_of_package.title()} package is available in our package list."
                    )
                    for index, value in price_of_package.items():
                        if index.lower() == searched_title_of_package:
                            print(
                                f"The cost of {searched_title_of_package.title()} is ${value}"
                            )
                    update_record_decision = input(
                        "Type Y to update the package price or N to go back: "
                    ).lower()
                    if update_record_decision == "y":
                        new_price = int(input("Enter new price: "))
                        if isinstance(new_price, int):
                            price_of_package[searched_title_of_package.title()] = new_price
                            print(f"Price updated. Updated price is ${new_price}")
                            for items, integer in active_class.price_of_package.items():
                                print(f"{items}: ${integer}")


            elif user_input == 7:
                active_class.record_range()

            else:
                print("Unrecognized command, Please try again.")
        except:
            return "Wrong Input"


if __name__ == "__main__":
    main()
