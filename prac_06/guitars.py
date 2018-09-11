from prac_06.guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: $"))
    #     add_guitar = Guitar(name, year, cost)
    #     guitars.append(add_guitar)
    #     print(add_guitar, "added.")
    #     name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    guitars.sort()
    if len(guitars) > 0:
        print("These are my guitars:")
        # for i, guitar in enumerate(guitars):
        for i in range(len(guitars)):
            vintage_string = ""
            if guitars[i].is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f} "
                  "{2:>15}".format(i + 1, guitars[i], vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")


main()
