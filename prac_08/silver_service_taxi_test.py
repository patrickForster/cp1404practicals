from prac_08.silver_service_taxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi("Hummer", 0, 2)
my_taxi.start_fare()
my_taxi.drive(18)
print(my_taxi)
print('Your fare is {:.2f}'.format(my_taxi.get_fare()))
