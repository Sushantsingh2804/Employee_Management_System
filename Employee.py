import sqlite3
from prettytable import PrettyTable
# connecting to database
connection = sqlite3.connect("Employee.db")
# checking if table exists
if len(connection.execute(
        "SELECT name from sqlite_master WHERE type='table' AND name='EMPLOYEE_DATA'").fetchall()) != 0:
    print("Table already exist")
else:
    connection.execute('''CREATE TABLE EMPLOYEE_DATA (
                        EMPLOYEE_CODE INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME TEXT,
                        MOBILE_NUMBER TEXT,
                        DESIGNATION TEXT,
                        SALARY INTEGER,
                        COMPANY_NAME TEXT
                        );
                        ''')
    print("Table created Successfully")

# menu part
while True:
    print("Select an option from the menu")
    print("1.Add an Employees ")
    print("2.View All employees ")
    print("3.Search an employee using employee name ")
    print("4.Update an employee details using employee Code")
    print("5.Delete an employee using employee Code ")
    print("6.Display all the details of employees whose salary is greater than 50000 ")
    print("7.Display the count of total number of employees in the company")
    print("8.Display all the employee details in alphabetical order, within the specific salary range ")
    print("9.Display all the employees data, whose salary is less than the average salary of all the employees")
    print("10.Exit ")

    choice = int(input("Enter a choice: "))
    # Add the Employees
    if choice == 1:
        getName = input("Enter the Name-")
        getDes = input("Enter the Designation-")
        getSal = input("Enter the Salary-")
        getComp = input("Enter the Company Name-")
        getMob = input("Enter the Mobile Number-")

        connection.execute(
            "INSERT INTO EMPLOYEE_DATA (NAME,DESIGNATION,SALARY,COMPANY_NAME,MOBILE_NUMBER) VALUES('" + getName + "','" + getDes + "'," + getSal + ",'" + getComp + "','" + getMob + "')")
        connection.commit()
        print("Entry successful")
        print("======================================================================================================================\n\n")

    # View All employees
    elif choice == 2:
        result = connection.execute("SELECT * FROM EMPLOYEE_DATA ORDER BY NAME")
        table = PrettyTable(
            ["EMPLOYEE_CODE", "NAME", "MOBILE_NUMBER", "DESIGNATION", "SALARY", "COMPANY_NAME"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])
        print(table)
        print("======================================================================================================================\n\n")

    # Search an employee using employee name
    elif choice == 3:
        getname = input("Enter Employee Name (Single Letter or multiple letters): ")
        result = connection.execute("SELECT * FROM EMPLOYEE_DATA WHERE NAME LIKE '%" + getname + "%'")
        table = PrettyTable(
            ["EMPLOYEE_CODE", "NAME", "MOBILE_NUMBER", "DESIGNATION", "SALARY", "COMPANY_NAME"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])
        print(table)
        print("======================================================================================================================\n\n")

    # Update an employee details using employee Code
    elif choice == 4:
        getEmp = input("Enter the Employee code- ")
        getName = input("Enter the Name-")
        getDes = input("Enter the Designation-")
        getSal = input("Enter the Salary-")
        getComp = input("Enter the Company Name-")
        getMob = input("Enter the Mobile Number-")
        connection.execute(
            "UPDATE EMPLOYEE_DATA SET NAME='" + getName + "',DESIGNATION='" + getDes + "',SALARY=" + getSal + ",COMPANY_NAME='" + getComp + "',MOBILE_NUMBER='" + getMob + "' WHERE EMPLOYEE_CODE=" + getEmp)
        connection.commit()
        print("Record Updated successfully")
        result = connection.execute("SELECT * FROM EMPLOYEE_DATA WHERE EMPLOYEE_CODE=" + getEmp)
        table = PrettyTable(
            ["EMPLOYEE_CODE", "NAME", "MOBILE_NUMBER", "DESIGNATION", "SALARY", "COMPANY_NAME"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])
        print(table)
        print("======================================================================================================================\n\n")

    # Delete an employee using employee Code
    elif choice == 5:
        getEmp = input("Enter the Employee code- ")
        connection.execute("DELETE FROM EMPLOYEE_DATA WHERE EMPLOYEE_CODE=" + getEmp)
        connection.commit()
        print("Record deleted successfully")
        result = connection.execute("SELECT EMPLOYEE_CODE,NAME FROM EMPLOYEE_DATA ORDER BY EMPLOYEE_CODE")
        table = PrettyTable(
            ["EMPLOYEE_CODE", "NAME"])
        for i in result:
            table.add_row([i[0], i[1]])
        print(table)
        print("======================================================================================================================\n\n")

    # Display all the details of employees whose salary is greater than 50000
    elif choice == 6:
        result = connection.execute("SELECT * FROM EMPLOYEE_DATA WHERE SALARY>50000 ORDER BY SALARY")
        table = PrettyTable(
            ["EMPLOYEE_CODE", "NAME", "MOBILE_NUMBER", "DESIGNATION", "SALARY", "COMPANY_NAME"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])
        print(table)
        print("======================================================================================================================\n\n")

    # Display the count of total number of employees in the company
    elif choice == 7:
        result = connection.execute("SELECT COUNT(*) as count FROM EMPLOYEE_DATA")
        table = PrettyTable(
            ["Count"])
        for i in result:
            table.add_row([i[0]])
        print(table)
        print("======================================================================================================================\n\n")

    # Display all the employee details in alphabetical order, within the specific salary range
    elif choice == 8:
        lb = input("Enter the lower salary range- ")
        ub = input("Enter the higher salary range- ")
        result = connection.execute("SELECT * FROM EMPLOYEE_DATA WHERE SALARY BETWEEN "+lb+" AND "+ub+" ORDER BY SALARY")
        table = PrettyTable(
            ["EMPLOYEE_CODE", "NAME", "MOBILE_NUMBER", "DESIGNATION", "SALARY", "COMPANY_NAME"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])
        print(table)
        print("======================================================================================================================\n\n")

    # Display all the employees data, whose salary is less than the average salary of all the employees
    elif choice == 9:
        result = connection.execute("SELECT * FROM EMPLOYEE_DATA WHERE SALARY <(SELECT AVG(SALARY) as avgsal FROM EMPLOYEE_DATA) ORDER BY SALARY")
        table = PrettyTable(
            ["EMPLOYEE_CODE", "NAME", "MOBILE_NUMBER", "DESIGNATION", "SALARY", "COMPANY_NAME"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])
        print(table)
        print("======================================================================================================================\n\n")

    # EXIT
    elif choice == 10:
        connection.close()
        print("successfully closed the application")
        break
        print("======================================================================================================================\n\n")

    # wrong selection
    else:
        print("INVALID CHOICE!!!!!!!")
        print(
            "======================================================================================================================\n\n")
