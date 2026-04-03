"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seats_list = ["A", "B", "C", "D"]
    
    for i in range(number):
        yield seats_list[i % len(seats_list)]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    counter = 0
    
    for row in range(1, number+1):
        for seat in ["A", "B", "C", "D"]:
            if counter == number: return
                
            if row != 13:
                yield f'{row}{seat}'
                counter+=1
            else:
                continue
        
            
def assign_seats(passengers):  
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    my_dict = {}
    seat_number = generate_seats(len(passengers))
    for i in passengers:
        my_dict[i] = next(seat_number)

    return my_dict

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    

    for i in seat_numbers:
        if len(i+flight_id) == 12:
            yield i+flight_id
        else:
            yield (i+flight_id).ljust(12, "0")
            
        
