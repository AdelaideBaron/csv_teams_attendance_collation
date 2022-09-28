# Teams Attendance to CSV 

A simple program to collate attendee, and date, information from multiple teams attendance reports. For example, attendance across multiple sessions of a course. Used for tracking purposes whilst teaching CFG courses.

### Conditions: 
- Teams attendance report with the first column containing the following rows (roughly rows 3 and 9: 
  - Start time
  - Name
  - People must join with the same name each week, otherwise it won't recognise that they're the same person 
- must not have anything but names in expected attendance, no headers 

### How to use: 
1. Import all seperate attendance files, as seperate CSVs (please double check) into project directory 
2. In list_of_attendance_files (~line 77, main.py) place the path names (copy from content root) of each file in the array within " " , e.g. 
``` 
list_of_attendance_files = ["fileone_path.csv", "filetwo_path.csv"] 
```
3. Adjust `if (len(these_attendees) < 50):` to less than the max register length (e.g. 50 here)
4. Run main 
5. Input the name of CSV you'd like to create
6. See the generated output.csv file 


### WIP 
- Count for each person 
