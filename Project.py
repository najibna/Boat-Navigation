# Import necessary libraries
import math
import random


# Constants for latitude and longitude bounds and Earth radius
MIN_LAT = -90
MAX_LAT = 90
MIN_LONG = -180
MAX_LONG = 180
EARTH_RADIUS = 6371


# Define the coordinates for the restricted zone and hazardous area
restricted_latitude = 25.0
restricted_longitude = -71.0
hazardous_latitude_min = 40.0
hazardous_latitude_max = 41.0
hazardous_longitude_min = -71.0
hazardous_longitude_max = -70.0


#Set global variables to 0 to start
num_passengers = 0
vessel_length = 0
vessel_width = 0
latitude = 0
longitude = 0
vessel_length = 0
vessel_width = 0
choice = 0
new_latitude = 0
new_longitude = 0






def meter_to_feet(distance):
    """
    Function to convert meters to feet
    """
    return round ((distance) * 3.28, 2)


def degrees_to_radians(angle):
    """
    Function to convert degrees to radians
    """
    radian_angle = round(( angle * ( math.pi / 180) ),2)

    return radian_angle


def get_vessel_dimensions():
    """
    Function to get vessel dimensions from the user
    """ 
    vessel_length = float(input('Enter the vessel length (in meter): '))
    vessel_width = float(input('Enter the vessel width (in meter): '))
    

    vessel_length = meter_to_feet(vessel_length)
    vessel_width = meter_to_feet(vessel_width)

    return (vessel_length, vessel_width)



def get_valid_coordinate(val_name, min_float, max_float):
    """
    Function to get a valid coordinate within specified bounds
    """
    val = float(input (f'What is your {val_name} ?'))

    while float(min_float) > val or float(max_float) < val:
        print(f'Invalid {val_name}')
        val = float(input (f'What is your {val_name} ?'))
            
    return val  


def get_gps_location():
    """
    Function to get GPS location from the user
    """    
    global latitude
    global longitude
    latitude = get_valid_coordinate('latitude',MIN_LAT,MAX_LAT)
    longitude = get_valid_coordinate('longitude',MIN_LONG,MAX_LONG)
    return latitude, longitude



def distance_two_points(latitude_1, longitude_1, latitude_2, longitude_2) :
    """
    Function to calculate the distance between two points on Earth
    """    
    #conversion to radians
    latitude_1 = degrees_to_radians(latitude_1)
    longitude_1 = degrees_to_radians(longitude_1)
    latitude_2 = degrees_to_radians(latitude_2)
    longitude_2 = degrees_to_radians(longitude_2)

    # Calculate the differences in latitude and longitude
    delta_latitude = latitude_2 - latitude_1
    delta_longitude = longitude_2 - longitude_1
        
    #Haversine formula
    part1 = math.sin(delta_latitude / 2) ** 2
    part2 = math.cos((latitude_1)) * math.cos((latitude_2))
    part3 = math.sin(delta_longitude / 2) ** 2

    a = part1 + part2 * part3
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = EARTH_RADIUS * c

    return round(distance, 2)


def check_safety(vessel_latitude, vessel_longitude) :
    """
    Function to check the safety of the vessel's location
    """
    # Calculate the distance between the vessel's location
    # and the restricted zone
    distance_to_restricted_zone = distance_two_points(
        vessel_latitude, vessel_longitude,
        restricted_latitude, restricted_longitude
    )

    # Check if the vessel is close to the restricted zone
    if distance_to_restricted_zone <= 400.0:
        print("Error: Restricted zone!")



    # Check if the vessel is in the hazardous area
    elif (
        hazardous_latitude_min 
        <= vessel_latitude <= hazardous_latitude_max and
        hazardous_longitude_min <= vessel_longitude 
        <= hazardous_longitude_max
    ):
        print("Warning: Hazardous area! Navigate with caution.")
    
    else:
        print("Safe navigation.")

def get_max_capacity(length, width):
    """
    Function to calculate the maximum capacity of the vessel
    """
    if length <= 26:
        capacity = (length * width) / 15
    else:
        capacity = (length * width) / 15 + ((length - 26) * 3)
    
    # Round down the capacity to the nearest integer
    capacity = int(capacity)
    
    return capacity


def passengers_on_boat(vessel_length, vessel_width, num_passengers):
    """
    Function to check the number of passengers on the boat
    """    
    max_capacity = get_max_capacity(vessel_length, vessel_width)

    # Check if the number of passengers exceeds the maximum capacity
    if num_passengers > max_capacity:
        return False

    # Check if the number of passengers can be distributed equally
    if num_passengers % 4 == 0:
        return True
    else:
        return False


def update_coordinate(position, min_float, max_float):
    """
    Function to update the boat's coordinate due to waves
    """  
    random.seed(123)
    
    while True:
        # Generate a random number between -10 and 10
        random_step = random.uniform(-10, 10)
        
        # Calculate the new position by adding the random step
        new_position = position + random_step
        
        # Check if the new position is within 
        # the (min_float, max_float) interval
        if min_float < new_position < max_float:
            return round(new_position, 2)
        

def wave_hit_vessel(vessel_latitude, vessel_longitude):
    """
    Function to simulate waves hitting the vessel and update its position
    """
    global new_latitude
    global new_longitude
    global latitude
    global longitude

    # Update latitude and longitude separately 
    # while ensuring they stay within bounds
    new_latitude = update_coordinate(vessel_latitude, MIN_LAT, MAX_LAT)
    new_longitude = update_coordinate(vessel_longitude, MIN_LONG, MAX_LONG)
    
    # Check safety of the new location
    check_safety(new_latitude, new_longitude)
    
    # Return the updated coordinates as a tuple
    return new_latitude, new_longitude

def vessel_menu():
    """
    Displays a menu for the user to interact with vessel-related functions.
    
    The menu allows the user to:
    1. Check the safety of the boat's current location.
    2. Check the maximum number of people that can fit on the boat.
    3. Update the position of the boat due to waves.
    4. Exit the boat menu.
    
    The function will repeatedly display the menu until the user 
    chooses to exit (option 4).
    """
    global choice
    global latitude
    global longitude

    global new_latitude
    global new_longitude
    global latitude
    global longitude
    global num_passengers

    # Initialize choice to a value outside the range of 0-3
    choice = 10


    print('Welcome to the boat menu!')
    
    get_gps_location()

    print('Your current position is at latitude', 
          latitude, 'and longitude',longitude)

    (vessel_length, vessel_width) = get_vessel_dimensions()

    print('Your boat measures', vessel_length, 'feet by',vessel_width,
           'feet')

    while choice != '4' :
        
        print("Please select an option below: ")
        print("1. Check the safety of your boat")
        print("2. Check the maximum number of people" + 
              " that can fit on the boat")
        print("3. Update the position of your boat")
        print("4. Exit boat menu")

        choice = (input("Your selection: "))

        if choice == '1':
                check_safety(latitude, longitude)
        elif choice == '2':
                num_passengers = int(input("Enter the number of" 
                + " adults to go on the boat: "))
                if passengers_on_boat(vessel_length, 
                                      vessel_width, 
                                      num_passengers):
                    print('Your boat can hold', num_passengers,
                           'adults')
                else:
                    print("The boat cannot hold ", num_passengers,
                           "adults")
        elif choice == '3':
                latitude, longitude = wave_hit_vessel(latitude, 
                                                      longitude)
                print("Your new position is latitude of", latitude, 
                      "and longitude of",longitude)

        elif choice == '4' :
            print("End of boat menu.")
