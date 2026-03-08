# Author: A.K.E.M Perera
# Date:30/11/2024
# Student ID:20240017

#Referances 
    # W3schools.com(1998) W3schools Online Web Tutorials. Available at:https://www.w3schools.com/ (Accessed: 30 November 2024)
    # Where developers learn,share,& build careers(2008) Stack Overflow. Available at: https://stackoverflow.com/ (Accessed: 30 November 2024)

import datetime
import os
import csv

# Task A: Input Validation
def validate_date_input():
    """
    Prompts the user for a date in DD MM YYYY format, validates the input for:
    - Correct data type
    - Correct range for day, month, and year
    """ 
    
    try:
        while True:
            global inputDate
            inputDate = input("Enter the survey date with the format of (DD MM YYYY) to select the file: ")
            inputDate=inputDate.replace(" ", "")
            if len(inputDate) == 8 :
                if inputDate.isnumeric():
                    if (1 <= int(inputDate[0:2]) <= 31) and (int(inputDate[2:4]) in [1,3,5,7,8,10,12]):
                        pass
                    elif (1 <= int(inputDate[0:2]) <= 30) and (int(inputDate[2:4]) in [4,6,9,11]):
                        pass
                    elif ( int(inputDate[2:4]) ==2 ):
                        if ( int(inputDate[4:8])%4 == 0 and int(inputDate[4:8])%100 != 0) or(int(inputDate[4:8])%400 == 0):
                           if (1 <= int(inputDate[0:2]) <= 29):
                             pass
                           else:
                             print ( "Invalid input DD for february in a leap year..!" )
                             continue
                          
                        else:
                            if ( 1 <= int(inputDate[0:2]) <= 28 ):
                             pass
                            else:
                             print ( "Invalid input DD for fabruary in a non leap year.. !")
                             continue
                    else :
                        print("Input date is out of range. please enter a valid DD for the related MM..")
                        continue   
                    if ((int(inputDate[2:4]) >= 1) and (int(inputDate[2:4]) <= 12)):
                        pass
                    else :
                        print("Input month is out of range. Month (MM) should between 1 to 12..!")  
                        continue

                    if ((int(inputDate[4:8]) >= 2000) and (int(inputDate[4:8]) <= 2024)):
                        pass
                    else :
                        print("Input date is out of range. Year (YYYY) should between 2000 to 2024..!")
                        continue        
                else:
                    print("Input date should contain only numerics with the format of (DD MM YYYY)..!")
                    continue
            else:
                print("Input date is out of range. Input date should contain only numerics with the format of (DD MM YYYY)..!")
                continue
            break
        
        return True
        
    except Exception as e:
        raise ValueError(f"Input date is: {inputDate} invalid due to {str(e)}")
    

   


def validate_continue_input():
    """
    Prompts the user to decide whether to load another dataset:
    - Validates "Y" or "N" input
    """   

    try:
        inputNewDataSet=input("Do you want to load a new dataset? (Y/N): ")
        if inputNewDataSet.upper() == "Y":
            if validate_date_input():
                file_path=input("Please enter the file path: ")
                if not os.path.exists(os.path.dirname(file_path)):
                    print(f"Entered file path is incorrect: {file_path}")
                else:
                    process_csv_data(file_path)
            else:
                exit() 
        elif inputNewDataSet.upper() == "N":
            exit
        else:
            print("Invalid")
            exit
    except Exception as e:
        raise ValueError(f"Input value is: {inputNewDataSet} invalid due to {str(e)}")
    
# Task B: Processed Outcomes
def process_csv_data(file_path):
    """
    Processes the CSV data for the selected date and extracts:
    - Total vehicles
    - Total trucks
    - Total electric vehicles
    - Two-wheeled vehicles, and other requested metrics
    """
    # Logic for processing data goes here
    
    full_file_path=f"{file_path}/traffic_data{inputDate}.csv"
    csv_file_name=f"traffic_data{file_path}.csv"
    select_date=f"{inputDate[0:2]}/{inputDate[2:4]}/{inputDate[4:8]}"
    list_of_dict=[]
    outcomes=[]
    
    #Read the CSV file and store into a Dictionery List
    try:
        with open(full_file_path, 'r') as csvfile:
            dict_reader=csv.DictReader(csvfile)
            list_of_dict=list(dict_reader)
        outcomes.append(f"Selected data file is {os.path.basename(full_file_path)}")
    except Exception as e:
        print(f"File not found: {full_file_path}")
        validate_continue_input()
    
    #1 - The total number of vehicles passing through all junctions for the selected date.
    try:
        total_no_of_vehicles=[item for item in list_of_dict if item["Date"] == select_date]
        print(len(total_no_of_vehicles))
        outcomes.append(f"The total number of vehicles passing through all junctions for the selected date is {len(total_no_of_vehicles)}")
    except Exception as e:
        error="The total number of vehicles passing through all junctions for the selected date was failed"
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)
        
    #2 - The total number of trucks passing through all junctions for the selected date. 
    try:
        total_no_of_trucks=[item for item in list_of_dict if item["VehicleType"] == "Truck" and item["Date"] == select_date]
        print(len(total_no_of_trucks))
        outcomes.append(f"The total number of trucks passing through all junctions for the selected date is {len(total_no_of_trucks)}")
    except Exception as e:
        error="The total number of trucks passing through all junctions for the selected date was failed"
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)
    
    #3 - The total number of electric vehicles passing through all junctions for the selected date. 
    try:
        total_no_of_electric_vehicles=[item for item in list_of_dict if item["elctricHybrid"] == "True" and item["Date"] == select_date]
        print(len(total_no_of_electric_vehicles))
        outcomes.append(f"The total number of electric vehicles passing through all junctions for the selected date is {len(total_no_of_electric_vehicles)}")
    except Exception as e:
        error= "The total number of electric vehicles passing through all junctions for the selected date was failed"
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)

    #4 - The number of “two wheeled” vehicles through all junctions for the date (bikes, motorbike, scooters). 
    try:
        total_no_of_two_wheeled=[item for item in list_of_dict if item["VehicleType"] in ("Bicycle","Motorcycle","Scooter") and item["Date"] == select_date]
        print(len(total_no_of_two_wheeled))
        outcomes.append(f"The number of “two wheeled” vehicles through all junctions for the date (bikes, motorbike, scooters) is {len(total_no_of_two_wheeled)}")
    except Exception as e:
        error= "The number of “two wheeled” vehicles through all junctions for the date (bikes, motorbike, scooters) was failed"
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)
    
    #5 - The total number of busses leaving Elm Avenue/Rabbit Road junction heading north
    try:
        total_no_of_busses_earr=[item for item in list_of_dict if item["VehicleType"] == "Buss" and item["JunctionName"] == "Elm Avenue/Rabbit Road" and item["travel_Direction_in"] == "N"]
        print(len(total_no_of_busses_earr))
        outcomes.append(f"The total number of busses leaving Elm Avenue/Rabbit Road junction heading north is {len(total_no_of_busses_earr)}")
    except Exception as e:
        error= "The total number of busses leaving Elm Avenue/Rabbit Road junction heading north was failed"
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)

    #6 - The total number of vehicles passing through both junctions without turning left or right.
    try:
        total_no_of_vehicles_to_north=[item for item in list_of_dict if item["travel_Direction_in"] == "N"]
        print(len(total_no_of_vehicles_to_north))
        outcomes.append(f"The total number of vehicles passing through both junctions without turning left or right is {len(total_no_of_vehicles_to_north)}")
    except Exception as e:
        error= "The total number of vehicles passing through both junctions without turning left or right was failed"
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)

    #7 - The percentage of all vehicles recorded that are Trucks for the selected date (rounded to an integer). 
    try:
        percentage_of_trucs=[item for item in list_of_dict if item["VehicleType"] == "Truck"]
        print(f"{round((len(percentage_of_trucs)/len(total_no_of_vehicles))*100)}%")
        outcomes.append(f"The percentage of all vehicles recorded that are Trucks for the selected date (rounded to an integer) is {round((len(percentage_of_trucs)/len(total_no_of_vehicles))*100)}%")
    except Exception as e:
        error="The percentage of all vehicles recorded that are Trucks for the selected date (rounded to an integer) was failed"
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)

    #8 - The average number Bicycles per hour for the selected date (rounded to an integer). 
    try:
        average_no_of_bicycles_per_hour=[item for item in list_of_dict if item["VehicleType"] == "Bicycle"]
        print(f"{round((len(average_no_of_bicycles_per_hour)/24))}%")
        outcomes.append(f"The average number Bicycles per hour for the selected date (rounded to an integer) is {round((len(average_no_of_bicycles_per_hour)/24))}%")
    except Exception as e:
        error= "The average number Bicycles per hour for the selected date (rounded to an integer) was failed"
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)
    
    #9 - The total number of vehicles recorded as over the speed limit for the selected date. 
    try:
        total_no_of_vehicles_over_speed=[item for item in list_of_dict if item["JunctionSpeedLimit"] < item["VehicleSpeed"] and item["Date"] == select_date]
        print(len(total_no_of_vehicles_over_speed))
        outcomes.append(f"The total number of vehicles recorded as over the speed limit for the selected date is {len(total_no_of_vehicles_over_speed)}")
    except Exception as e:
        error= "The total number of vehicles recorded as over the speed limit for the selected date was failed"
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)
    

    #10 - The total number of vehicles recorded through only Elm Avenue/Rabbit Road junction for the selected date. 
    try:
        total_no_of_vehicle_only_through_earr=[item for item in list_of_dict if item["JunctionName"] == "Elm Avenue/Rabbit Road" and item["Date"] == select_date]
        print(len(total_no_of_vehicle_only_through_earr))
        outcomes.append(f"The total number of vehicles recorded through only Elm Avenue/Rabbit Road junction for the selected date is {len(total_no_of_vehicle_only_through_earr)}")
    except Exception as e:
        error= "The total number of vehicles recorded through only Elm Avenue/Rabbit Road junction for the selected date was failed"
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)
    
    #11 - The total number of vehicles recorded through only Hanley Highway/Westway junction for the selected date.
    try:
        total_no_of_vehicle_only_through_hhw=[item for item in list_of_dict if item["JunctionName"] == "Hanley Highway/Westway" and item["Date"] == select_date]
        print(len(total_no_of_vehicle_only_through_hhw))
        outcomes.append(f"The total number of vehicles recorded through only Hanley Highway/Westway junction for the selected date is {len(total_no_of_vehicle_only_through_hhw)}")
    except Exception as e:
        error= "The total number of vehicles recorded through only Hanley Highway/Westway junction for the selected date was failed" 
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)

    #12 - The percentage of vehicles through Elm Avenue/Rabbit Road that are Scooters (rounded to integer)  
    try:
        percentage_of_scooters_through_earr=[item for item in list_of_dict if item["JunctionName"] == "Elm Avenue/Rabbit Road" and item["VehicleType"] == "Scooter"]
        print(f"{round((len(percentage_of_scooters_through_earr)/len(total_no_of_vehicles))*100)}%")
        outcomes.append(f"The percentage of vehicles through Elm Avenue/Rabbit Road that are Scooters (rounded to integer) is {round((len(percentage_of_scooters_through_earr)/len(total_no_of_vehicles))*100)}%")
    except Exception as e:
        error= "The percentage of vehicles through Elm Avenue/Rabbit Road that are Scooters (rounded to integer) was failed"
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)

    #13 - The number of vehicles recorded in the peak (busiest) hour on Hanley Highway/Westway. 
    peak24h={"hour":0,
          "count":0}
    try:
        for hour in range (24):
            peak24Counter=[item for item in list_of_dict if int(item["timeOfDay"][0:2])==hour and item["JunctionName"] == "Hanley Highway/Westway"]
            if len(peak24Counter) > peak24h["count"]:
                peak24h["hour"]=hour
                peak24h["count"]=len(peak24Counter)
        print(peak24h["hour"])
        outcomes.append(f"The number of vehicles recorded in the peak (busiest) hour on Hanley Highway/Westway is {peak24h} ")
    except Exception as e:
        error= "The number of vehicles recorded in the peak (busiest) hour on Hanley Highway/Westway was failed"
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)
    

    #14 - The time or times of the peak (busiest) traffic hour (or hours) on Hanley Highway/Westway in the format Between 18:00 and 19:00. 
    peak={"hour18":0,
          "count18":0,
          "hour19":0,
          "count19":0}
    try:
        for hour in [18,19]:
            peakCounter=[item for item in list_of_dict if int(item["timeOfDay"][0:2])==hour and item["JunctionName"] == "Hanley Highway/Westway"]
            peak[f"hour{hour}"]=hour
            peak[f"count{hour}"]=len(peakCounter)
        print(peak)
        outcomes.append(f"The time or times of the peak (busiest) traffic hour (or hours) on Hanley Highway/Westway in the format Between 18:00 and 19:00 is {peak}")
    except Exception as e:
        error= "The time or times of the peak (busiest) traffic hour (or hours) on Hanley Highway/Westway was failed"
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)
    
    #15 - The total number of hours of rain on the selected date.
    try:
        total_hours=0
        total_no_of_hours_rain=[item for item in list_of_dict if "Rain" in item["Weather_Conditions"]  and item["Date"] == select_date]
        print(len(total_no_of_hours_rain))
        outcomes.append(f"The total number of hours of rain on the selected date {len(total_no_of_hours_rain)}")
    except Exception as e:
        error= "The total number of hours of rain on the selected date failed"
        print(f"{error} due to: {str(e)}")
        outcomes.append(error)
        
    display_outcomes(outcomes)
    
        
def display_outcomes(outcomes):
    """}
    Displays the calculated outcomes in a clear and formatted way.
    """
    pass  # Printing outcomes to the console
    if not outcomes:
        print("Outcome is empty")
    else:    
        for print_outcome in outcomes:
            print(print_outcome)
    save_results_to_file(outcomes)

# Task C: Save Results to Text File
def save_results_to_file(outcomes, file_name="results.txt"):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    pass  
    try:
        with open(file_name, 'w+') as f:
            for items in outcomes:
                f.write('%s\n' %items)
        print(f"File successfully saved to: {str(os.getcwd())}")
    except Exception as e:
        print(f"Saving results to a file was failes due to: {str(e)}")
    finally:
        f.close()

  

#validate_continue_input()
validate_continue_input() 

   
# if you have been contracted to do this assignment please do not remove this line