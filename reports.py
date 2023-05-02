#import send_to_email
import os
import csv

# Uncomment either of these files to send report via email and/or slack
#import send_to_slack
#import send_to_email


# This dictionary will be prepolulated Based on active == True
active_dict = {"jnb_active": 0, "acc_active": 0, "add_active": 0, "afr_active": 0,
               "abj_active": 0, "kgl_active": 0, "los_active": 0, "nbo_active": 0}

# This dictionary will be prepopulated base on score > 70
above_70_dict = {"jnb_above70": 0, "acc_above70": 0, "add_above70": 0, "afr_above70": 0,
               "abj_above70": 0, "kgl_above70": 0, "los_above70": 0, "nbo_above70": 0}

active_total = 0
above_70_total = 0

# CSV files assumed to be stored in current directory
for filename in os.listdir("."):
    if filename.endswith(".csv"):
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            # Avoid reading the header column
            next(reader, None)
            for row in reader:
                if (row[4] == "true" and len(row) >= 4):
                    if filename.startswith("JNB"):
                        active_dict["jnb_active"] += 1

                    elif filename.startswith("ACC"):
                        active_dict["acc_active"] += 1

                    elif filename.startswith("ADD"):
                        active_dict["add_active"] += 1

                    elif filename.startswith("AFR"):
                        active_dict["afr_active"] += 1

                    elif filename.startswith("ABJ"):
                        active_dict["abj_active"] += 1

                    elif filename.startswith("KGL"):
                        active_dict["kgl_active"] += 1
                    
                    elif filename.startswith("LOS"):
                        active_dict["los_active"] += 1
                    
                    elif filename.startswith("NBO"):
                        active_dict["nbo_active"] += 1

                if (float(row[7]) >= 70 and len(row) >= 7):
                    if filename.startswith("JNB"):
                        above_70_dict["jnb_above70"] += 1

                    elif filename.startswith("ACC"):
                        above_70_dict["acc_above70"] += 1

                    elif filename.startswith("ADD"):
                        above_70_dict["add_above70"] += 1

                    elif filename.startswith("AFR"):
                        above_70_dict["afr_above70"] += 1

                    elif filename.startswith("ABJ"):
                        above_70_dict["abj_above70"] += 1

                    elif filename.startswith("KGL"):
                        above_70_dict["kgl_above70"] += 1
                    
                    elif filename.startswith("LOS"):
                        above_70_dict["los_above70"] += 1
                    
                    elif filename.startswith("NBO"):
                        above_70_dict["nbo_above70"] += 1

for key in active_dict:
    active_total += active_dict[key]
for key in above_70_dict:
    above_70_total += above_70_dict[key]

with open("active.txt", "w") as file:                
    file.write("Hi Manager. This is the number of active students for Cohort 11 (Based on Active = True)\n\nJNB-: {}\nACC-: {}\nADD-: {}\nAFR-: {}\nABJ-: {}\nKGL-: {}\nLOS-: {}\nNBO-: {}\n\nTotal active = {}\n\n".format(active_dict["jnb_active"], active_dict["acc_active"], active_dict["add_active"], active_dict["afr_active"], active_dict["abj_active"], active_dict["kgl_active"], active_dict["los_active"], active_dict["nbo_active"], active_total))
    file.write("\nStudents with scores Higher than Seventy for C11\n\nJNB-: {}\nACC-: {}\nADD-: {}\nAFR-: {}\nABJ-: {}\nKGL-: {}\nLOS-: {}\nNBO-: {}\n\nTotal Above Seventy = {}".format(above_70_dict["jnb_above70"], above_70_dict["acc_above70"], above_70_dict["add_above70"], above_70_dict["afr_above70"], above_70_dict["abj_above70"], above_70_dict["kgl_above70"], above_70_dict["los_above70"], above_70_dict["nbo_above70"], above_70_total))
