import Car as car


def main():
    # Create an instance of Car.

    my_car = car.Car('2008', 'Honda Accord')

    # Accelerate 5 times.

    print('car is accelerating: ')

    for i in range(5):
        my_car.accelerate()

        print('Current speed: ', my_car.get_speed())

    print()

    # Brake 5 times.

    print('car is braking: ')

    for i in range(5):
        my_car.brake()

        print('Current speed: ', my_car.get_speed())


# Call the main function.

main()
