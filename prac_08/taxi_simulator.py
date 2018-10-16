from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    print("Let's Drive!")
    print(MENU)
    total_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'C':
            print('Taxis available:')
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, str(taxi)))
            taxi_choice = int(input("Choose Taxi: "))
            selected_taxi = taxis[taxi_choice]
        elif choice == 'D':
            travel_distance = int(input("How far are you driving? "))
            selected_taxi.start_fare()
            selected_taxi.drive(travel_distance)
            cost_of_trip = selected_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(selected_taxi.name, cost_of_trip))
            total_cost += cost_of_trip
        else:
            print("Invalid option")
            print("Bill to date: ${:.2f}".format(total_cost))
        print(MENU)
        choice = input(">>> ").upper()

    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))


main()
