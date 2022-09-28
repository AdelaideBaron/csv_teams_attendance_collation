import csv

import pandas as pd

def create_csv(name):
    csv_name = "{}.csv".format(name)
    created_file = open(csv_name, "x")

def read_original_csv_date(file_to_read):
    og_file = open(file_to_read, "r")

    desired_row_name = 'Start time'
    row_entries = csv.reader(og_file)

    for row in row_entries:
        if row[0] == desired_row_name:
            start_time = row[1]
            date_and_time = start_time.split(",")
            date = date_and_time[0]
            break
    return date

def get_attendees(file):
    og_file = open(file, "r")
    desired_row_name = 'Name'
    row_entries = csv.reader(og_file)
    attendees = []
    read_next_line = False
    empty_row = False

    for row in row_entries:
        if (read_next_line == False):
            if row[0] == desired_row_name:
                read_next_line = True
        else:
            attendees.append(row[0])
            if row[0] == '':
                break

    if '' in attendees:
        attendees.remove('')

    return attendees

def remove_duplicate_attendees(attendees):
    attendees_no_dupe = list(dict.fromkeys(attendees))
    return attendees_no_dupe

def remove_guest_title(attendees):
    #split at spaces, then make individual words
    for attendee in attendees:
        seperated_strings = attendee.split(" ")
        if "(Guest)" in seperated_strings:
            attendees.remove(attendee)
            seperated_strings.remove("(Guest)")
            string_to_add = ' '.join(seperated_strings)
            attendees.append(string_to_add)
        elif "(guest)" in seperated_strings:
            attendees.remove(attendee)
            seperated_strings.remove("(guest)")
            string_to_add = ' '.join(seperated_strings)
            attendees.append(string_to_add)
            # print(attendees)

    return attendees

def create_list_of_date_and_attendees(file):
    date = read_original_csv_date(file)
    attendees = get_attendees(file)
    attendees = remove_guest_title(attendees)
    attendees = remove_duplicate_attendees(attendees)
    attendees.sort()
    newest_list = [date] + attendees
    newest_list = [*set(newest_list)] 
    return newest_list

def add_attendance_to_csv():
    global df
    df = pd.DataFrame(data)
    for file in list_of_attendance_files:
        this_header = read_original_csv_date(file)
        these_attendees = get_attendees(file)
        attendees = remove_guest_title(these_attendees)
        best_attendees = remove_duplicate_attendees(attendees)

        for i in range(len(best_attendees)):
            best_attendees[i] = best_attendees[i].lower()
        best_attendees.sort()

        best_attendees = remove_guest_title(best_attendees)
        if (len(best_attendees) < 50): #this is the amount of attendees max
            to_add = 50 - len(best_attendees)
            i = 0
            while i < to_add:
                best_attendees.append('')
                i += 1
        df[this_header] = best_attendees

if __name__ == '__main__':

    list_of_attendance_files = [#insert here 
    ]

    csv_name = input("Enter name for new CSV (must not exist already): ")

    data = {}
    add_attendance_to_csv()
    create_csv("{}".format(csv_name))

   
    df.to_csv('{}.csv'.format(csv_name))



