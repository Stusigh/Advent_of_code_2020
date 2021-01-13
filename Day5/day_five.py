with open('input.txt', 'r') as f:
    data = f.readlines()
boarding_passes = []
for line in data:
    line = line.rstrip()
    boarding_passes.append(line)

all_seat_ids = []
all_seats = []


class Seat(object):
    def __init__(self, row, column, seatID):
        self.row = row
        self.column = column
        self.seatID = seatID
    def __str__(self):
        return str(self.row) + ' is the row' + str(self.column) + ' is the column' + str(self.seatID) + ' is the seat ID.'

for boarding_pass in boarding_passes:

    potential_rows = []
    for i in range(128):
        potential_rows.append(i)
    potential_columns = [0, 1, 2, 3, 4, 5, 6, 7]
    number_of_potential_columns = len(potential_columns)
    number_of_potential_rows = len(potential_rows)




    for character in boarding_pass:
        if character == 'F':
            potential_rows = potential_rows[:number_of_potential_rows//2]
            number_of_potential_rows = len(potential_rows)
        if character == 'B':
            potential_rows = potential_rows[number_of_potential_rows//2:]
            number_of_potential_rows = len(potential_rows)
        if character == 'L':
            potential_columns = potential_columns[:number_of_potential_columns//2]
            number_of_potential_columns = len(potential_columns)
        if character == 'R':
            potential_columns = potential_columns[number_of_potential_columns//2:]
            number_of_potential_columns = len(potential_columns)

    seat_column = int(potential_columns[0])
    seat_row = int(potential_rows[0])
    seat_id = (seat_row*8) + seat_column
    seat = Seat(seat_row, seat_column, seat_id)
    all_seat_ids.append(seat_id)
    all_seats.append(seat)


all_seat_ids.sort()
# 594 is what we are looking for
for seat in all_seats:
    if seat.seatID == 593:
        print(seat)
    if seat.seatID == 595:
        print(seat)
# 74 is the row, 2 is the column