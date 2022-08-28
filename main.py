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


# https://stackoverflow.com/questions/26464567/csv-read-specific-row

def create_list_of_date_and_attendees(file):
    date = read_original_csv_date(file)
    attendees = get_attendees(file)
    attendees.sort()
    new_list = [date] + attendees
    return new_list


def add_attendance_to_csv():
    global df
    df = pd.DataFrame(data)
    for file in list_of_attendance_files:
        this_date = read_original_csv_date(file)
        these_attendees = get_attendees(file)

        for i in range(len(these_attendees)):
            these_attendees[i] = these_attendees[i].lower()
        these_attendees.sort()
        if (len(these_attendees) < 50):
            to_add = 50 - len(these_attendees)
            i = 0
            while i < to_add:
                these_attendees.append('')
                i += 1
        df[this_date] = these_attendees


if __name__ == '__main__':

    list_of_attendance_files = [ #add CSV file paths as list here
         ]
    create_csv("output")
    data = {}
    add_attendance_to_csv()
    df.to_csv('output.csv')


