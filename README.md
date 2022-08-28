# Teams Attendance to CSV 

A simple program to collate attendee, and date, information from multiple teams attendance reports. For example, attendance across multiple sessions of a course. Used for tracking purposes whilst teaching CFG courses.

### Conditions: 
- Teams attendance report with the first column containing the following rows (roughly rows 3 and 9: 
  - Start time
  - Name


### How to use: 
1. Delete any output.csv files, or rename, prior to each run
2. Import all seperate attendance files, as CSV (please ensure this is comma seperated) into project directory 
3. In list_of_attendance_files (~line 77, main.py) place the path names (copy from content root) of each file
4. Adjust `if (len(these_attendees) < 50):` to less than the max register length (e.g. 50 here 
3. Run main 
4. See the generated output.csv file 
