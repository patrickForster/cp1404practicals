from prac_08.taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
my_taxi.drive(40)
print(my_taxi)
print('The fare for this trip is ${:.2f}'.format(my_taxi.get_fare()))
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)
print('The fare for this trip is ${:.2f}'.format(my_taxi.get_fare()))
