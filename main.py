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
    # mylist = ["a", "b", "a", "c", "c"]
    attendees_no_dupe = list(dict.fromkeys(attendees))
    # print(attendees_no_dupe)
    return attendees_no_dupe

def remove_guest_title(attendees):
    #split at spaces, then make individual words
    for attendee in attendees:
        seperated_strings = attendee.split(" ")
        # print(seperated_strings)
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
    new_list = [date] + attendees
    new_list = [*set(new_list)] # https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
    return new_list

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

def get_expected_attendees(expected_attendees): #to do
    #read the file of expected
    expected_attendees_file = open(expected_attendees, "r")
    row_entries = csv.reader(expected_attendees_file)
    expected_attendees = []
    for row in row_entries:
        name = row[0]
        expected_attendees.append(name)

    return expected_attendees

def check_expected_attendees(list_of_attendance_files, expected_attendees_file):
    expected_attendees = get_expected_attendees(expected_attendees_file)
    for file in list_of_attendance_files:
        this_header = read_original_csv_date(file)
        these_attendees = get_attendees(file)
        attendees = remove_guest_title(these_attendees)
        best_attendees = remove_duplicate_attendees(attendees)

        for i in range(len(best_attendees)):
            best_attendees[i] = best_attendees[i].lower()
        best_attendees.sort()

        best_attendees = remove_guest_title(best_attendees)

        attendence = []
        person_attendance = {}
        for person in expected_attendees:
            person = person.lower()
            expected_names = person.split(" ")
            for attendee in best_attendees:
                attendee_names = attendee.split(" ")
                for name in expected_names:
                    if name in attendee_names:
                        attendence.append(person)
                        break

            amount_of_attendance = attendence.count(person)
            person_attendance[person] = amount_of_attendance

        output = pd.DataFrame()
        output = output.append(person_attendance, ignore_index=True)

        return output


if __name__ == '__main__':

    check_attendance = input("Would you like to check attendance too? Enter 'YES' or 'NO'")
    if check_attendance == "NO":
        list_of_attendance_files = [ "attendance_files/Weds/Intro to Python - Attendance report 21-09-22 - Intro to Python - Attendance report 21-09-22.csv"
         ]
        csv_name = input("Enter name for new CSV (must not exist already): ")

        data = {}
        add_attendance_to_csv()
        create_csv("{}".format(csv_name))

        df.to_csv('{}.csv'.format(csv_name))
    elif check_attendance == "YES":
        list_of_attendance_files = [
            "attendance_files/Weds/Intro to Python - Attendance report 21-09-22 - Intro to Python - Attendance report 21-09-22.csv"
            ]
        csv_name = input("Enter name for new CSV (must not exist already): ")

        expected_attendance_files = "attendance_files/Weds/expected_attendance - Sheet1 (1).csv"

        data = {}
        add_attendance_to_csv()
        create_csv("{}".format(csv_name))

        df.to_csv('{}.csv'.format(csv_name))

        print(get_expected_attendees(expected_attendance_files))

        attendance_figure_df = check_expected_attendees(list_of_attendance_files, expected_attendance_files)

        attendance_file_csv_name = input("Input name of attendance file: ")
        attendance_figure_df.to_csv('{}.csv'.format(attendance_file_csv_name))

    else:
        print("Invalid response, please restart.")


