import os, shutil, calendar


months = [x for x in calendar.month_name][1:]
years = [x for x in os.listdir("./")][1:-1]

for i in years:
    ind_yr = 0
    for j in months:
        ind_mon = 0
        des = f"{i}\{j}" + "\\"
        src = f"{i}" + "\\"
        dir = os.listdir(i)
        for files in dir:
            file = files.split(".")
            if len(file) > 1 and files[4:6] == "20":  # Clue for identifing
                if months[int(files[8:10]) - 1] == j:  # Mapping to folder
                    ind_yr += 1
                    ind_mon += 1
                    source = src + files
                    destination = des + files
                    if os.path.isfile(source):
                        shutil.move(source, destination)
        print(i, j, ind_mon)
    print(i, ind_yr)
    print()
