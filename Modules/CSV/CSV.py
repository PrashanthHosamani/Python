import os 

path = os.getcwd()
print(path)

path1 = os.chdir('/Users/apple/')
# list_all = os.listdir()
# print(list_all)

path2 = os.chdir('/Users/apple/Downloads/')
path = os.getcwd()
print(path)
# list = os.listdir()
# print(list)

import csv
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    path_change = os.chdir('/Users/apple/Library/Mobile Documents/com~apple~CloudDocs/VS code /Python,DS & ML/Modules/CSV/')

    with open('new_file.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter = '\t')
    
        for line in csv_reader:
            csv_writer.writerow(line)
    
#We confirmed that we have data in the file lets get it into vs code
