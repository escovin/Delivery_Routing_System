import csv
import datetime

# Reads distances between locations from csv file
with open('WGUDistanceData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    readCSV = list(readCSV)

# Reads the names of all possible delivery locations from csv file
with open('WGUDistanceNameData.csv') as csv_name_file:
    name_readCSV = csv.reader(csv_name_file, delimiter=',')
    name_readCSV = list(name_readCSV)

    # Row/Column values are inserted into this function. This function then calculates the total distance.
    # The distance is returned and each iteration represents a distance between two locations.
    # Space-time complexity is O(1)
    def check_distance(row_value, column_value, sum_of_distance):
        distance = readCSV[row_value][column_value]
        if distance == '':
            distance = readCSV[column_value][row_value]

        sum_of_distance += float(distance)
        return sum_of_distance

    # This function returns the current distance, and functions much in the same was as check_distance.
    # Space-time complexity is O(1)
    def check_current_distance(row_value, column_value):
        distance = readCSV[row_value][column_value]
        if distance == '':
            distance = readCSV[column_value][row_value]
        return float(distance)
    # Truck leaving hub times
    first_time_list = ['8:00:00']
    second_time_list = ['9:10:00']
    third_time_list = ['11:00:00']

    # This function takes a distance and divides it by 18. It then uses divmod to display a time and appends 00.
    # This string being a timestamp is then turned into a datetime timedelta object
    # The object is then added to sum which is the total distance for a particular truck
    # Runtime of function is O(N)
    def check_time_first_truck(distance):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        first_time_list.append(final_time)
        sum = datetime.timedelta()
        for i in first_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum
    # Function repeated for second truck
    def check_time_second_truck(distance):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        second_time_list.append(final_time)
        sum = datetime.timedelta()
        for i in second_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum
    # Function repeated for the third truck
    def check_time_third_truck(distance):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        third_time_list.append(final_time)
        sum = datetime.timedelta()
        for i in third_time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum

    # Function returns the time objects for use in Packages.py
    # Space-time complexity is O(1)
    def check_address():
        return name_readCSV
    # Sorted truck lists that are put in order of efficiency in the following function
    first_optimized_truck = []
    first_optimized_truck_index_list = []
    second_optimized_truck = []
    second_optimized_truck_index_list = []
    third_optimized_truck = []
    third_optimized_truck_index_list = []

    # This sorting algorithm uses a greedy approach to automate optimization of each truck's delivery route.
    # There are three parameters for this function:
    # First parameter is the list of packages on an unoptimized truck.
    # Second parameter is the truck number.
    # Third parameter is the current location which is updated each time a truck moves.

    # The base case of the algorithm is len(truck_distance_list) == 0. This breaks recursion
    # once the input list has a size of 0.
    # A "lowest value" of 50.0 is set on initialization and uses the check current distance function to iterate through
    # every possible point that is currently available to determine if there is a lesser value.
    # If one exists, the lowest value is updated and the search proceeds. Once finished cycling through all
    # possible routes, the truck can proceed given the available packages, it then adds that package object
    # and associated index to new lists. To guarantee that the right truck packages are being associated, the
    # second parameter is checked. If the truck is being sorted than the optimized delivery path will be associated
    # to the lists first_optimized_truck and first_optimized_truck_index. Each time these lists are updated, the lowest
    # value is dropped from the truck_distance_list. This allows updating the current location and recursively
    # calling the function. Once the argument list is empty, it will return the empty list and the function call
    # will end.

    # The space-time complexity of this algorithm is O(N^2).

    def calculate_shortest_distance(truck_distance_list, truck_number, current_location):  # section 1
        if len(truck_distance_list) == 0:  # section 2
            return truck_distance_list
        else:  #
            try:
                lowest_value = 50.0
                new_location = 0
                for index in truck_distance_list:
                    if check_current_distance(current_location, int(index[1])) <= lowest_value:
                        lowest_value = check_current_distance(current_location, int(index[1]))  # section 3
                        new_location = int(index[1])
                for index in truck_distance_list:  # section 4
                    if check_current_distance(current_location, int(index[1])) == lowest_value:
                        if truck_number == 1:
                            first_optimized_truck.append(index)
                            first_optimized_truck_index_list.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            calculate_shortest_distance(truck_distance_list, 1, current_location)
                        elif truck_number == 2:
                            second_optimized_truck.append(index)
                            second_optimized_truck_index_list.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            calculate_shortest_distance(truck_distance_list, 2, current_location)
                        elif truck_number == 3:
                            third_optimized_truck.append(index)
                            third_optimized_truck_index_list.append(index[1])
                            pop_value = truck_distance_list.index(index)
                            truck_distance_list.pop(pop_value)
                            current_location = new_location
                            calculate_shortest_distance(truck_distance_list, 3, current_location)
            except IndexError:
                pass

    first_optimized_truck_index_list.insert(0, '0')

    # Space-time complexity is O(1)
    def first_optimized_truck_index():
        return first_optimized_truck_index_list

    # Space-time complexity is O(1)
    def first_optimized_truck_list():
        return first_optimized_truck
    second_optimized_truck_index_list.insert(0, '0')

    # Space-time complexity is O(1)
    def second_optimized_truck_index():
        return second_optimized_truck_index_list



    # Space-time complexity is O(1)
    def second_optimized_truck_list():
        second_optimized_truck.insert(0, second_optimized_truck.pop(13))
        return second_optimized_truck


    third_optimized_truck_index_list.insert(0, '0')


    # Space-time complexity is O(1)
    def third_optimized_truck_index():
        return third_optimized_truck_index_list

    # Space-time complexity is O(1)
    def third_optimized_truck_list():
        return third_optimized_truck