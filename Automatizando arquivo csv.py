import csv

with open('wecodeinpython.csv', 'w') as csvfile:
    fieldsnames = ['first_name', 'last_name', 'Role']
    writer = csv,DictWriter(csvfile, fieldsnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'Role': 'Developer',
                    'first_name': 'Demetrius',
                    'last_name': 'Da mata'})
    writer.writerow({'Role', 'Tester',
                     'first_name', 'Jhon',
                     'last_name', 'De'})
    writer_writerow({'Role', 'Alanyst',
                     'first_name', 'Shin',
                     'last_name', 'Chan'})
    
print('data inserted')