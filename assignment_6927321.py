#COMPUTER APPLICATION ASSIGNMENT 4
#import numpy as np
# list of available cars and their prices 
availableCars = {
'Honda Civic': 50000,
'Lamborghini': 1000000,
'Bugatti Chiron': 1500000,
'Ford Explorer': 150000,
'Mercedes-Benz': 1200000,
'BMW': 900000,
'Honda CR-V': 60000,
'Honda Accord': 65000,
'Honda Pilot': 55000,
'Honda Odyssey': 40000,
'Honda HR-V': 45000,
'Hyundai Tucson': 50000,
'Hyundai Santa Fe': 60000,
'Hyundai Elantra': 55000,
'Hyundai Xcent': 42000,
'Hyundai i10': 70000,
'Hyundai i20': 75000,
'Ford Escape': 70000,
'Toyota Fortuner': 120000,
'Toyota Land Cruiser': 200000,
'Toyota Tundra': 180000,
'Toyota Camry': 45000,
'Toyota Prius': 50000,
'Toyota Corolla': 35000,
'Toyota Mirai': 65000,
'Toyota Yaris': 60000,
'Toyota RAV4': 75000,
'Toyota Highlander': 130000,
'Ford Edge': 80000,
'Ford Expedition': 140000,
'Ford Explorer': 150000,
'Ford Mustang': 80000,
'Ford Maverick': 85000,
'Ford Ranger': 105000,
'Ford Super Duty': 140000
}
carName = input('Enter a carName: ')
if carName in availableCars:
    print('Available')
    carPrice = availableCars[carName]
    print(f'The price of {carName} is ${carPrice}.')
else:
    print(f'Sorry, {carName} is not available.')
    
#https://github.com/KwakuOfori/assignment4.git
#the link to my github account