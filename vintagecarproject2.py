'''Scenario: As mentioned in the previous lesson, 32 cars were tested in 1974 in Motor Trend magazine. 
After you were able to answer their first three questions, the magazine has come back again to ask you the following:

How powerful were the two least fuel-efficient cars from 1974?
How powerful were the two most fuel-efficient cars from 1974?
How many cylinders did most of the 1974 Mercedes models have?
After detailed research and a little cleaning, the data looks like this. Run the following cell so that the data is stored the workspace.'''

# car model names:
name = ['Mazda RX4', 'Mazda RX4 Wag', 'Datsun 710',
        'Hornet 4 Drive', 'Hornet Sportabout', 'Valiant',
        'Duster 360', 'Merc 240D', 'Merc 230', 'Merc 280',
        'Merc 280C', 'Merc 450SE', 'Merc 450SL', 'Merc 450SLC',
        'Cadillac Fleetwood', 'Lincoln Continental',
        'Chrysler Imperial', 'Fiat 128', 'Honda Civic',
        'Toyota Corolla', 'Toyota Corona', 'Dodge Challenger',
        'AMC Javelin', 'Camaro Z28', 'Pontiac Firebird',
        'Fiat X1-9', 'Porsche 914-2', 'Lotus Europa',
        'Ford Pantera L', 'Ferrari Dino', 'Maserati Bora',
        'Volvo 142E']

# miles per gallon
mpg = [21.0, 21.0, 22.8, 21.4, 18.7, 18.1, 14.3, 24.4, 22.8,
       19.2, 17.8, 16.4, 17.3, 15.2, 10.3, 10.4, 14.7, 32.4,
       30.4, 33.9, 21.5, 15.5, 15.2, 13.3, 19.2, 27.3, 26.0,
       30.4, 15.8, 19.7, 15.0, 21.4]

# number of cylinders (NA = missing value)
cyl = [6, 6, 4, 6, 8, 6, 8, 4, 4, 6, 6, 8, 8, 8, 8, 8, 8, 4, 4, 4,
       4, 8, 8, 8, 8, 4, 4, 4, 8, 'NA', 'NA', 'NA']

# gross horsepower
hp = [110, 110, 93, 110, 175, 105, 245, 62, 95, 123, 123, 180, 180,
      180, 205, 215, 230, 66, 52, 65, 97, 150, 150, 245, 175, 66,
      91, 113, 264, 175, 335, 109]

# transmission (0 = automatic, 1 = manual)
am = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0,
      0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]


'''As you can see, the values are no longer sorted by manufacturer. There is also a new variable cyl, 
the number of cylinders a car model has. Unfortunately this variable is missing for three models. 
These positions have been identified with 'NA'. After asking several experts, it turns out that the missing values 
are 6, 8, and 4. Update the list accordingly.'''
cyl.index('NA') #replacing the NA with the correct values
cyl[29] = 6
cyl[30] = 8
cyl[31] = 4
print(cyl)


'''The first question is:
How powerful were the two least fuel-efficient cars from 1974?

Let's look at the possible sub-problems.
Identifying the least fuel-efficient cars, which are the ones with the lowest mpg values
Identifying the horsepower value for the least fuel-efficient car.
Important: A higher value for miles per gallon indicates a lower consumption. A lower value for miles per gallon indicates a higher consumption.'''
print(sorted(mpg)) #sorts out the mpg in alphabetical order
mpg_lowest = [10.3, 10.4] #the 2 lowest values
mpg_lowest_idx = [mpg.index(10.3), mpg.index(10.4)] #finds the index of the values in the original list
print(mpg_lowest_idx)
#You have solved the first sub-problem. Now you can move onto the second sub-problem. 
#What is the value in hp that corresponds to the index stored in mpg_lowest_idx? 
#Calculate the average of these two values and assign it to the variable mpg_lowest_hp_mean.
hp_lowest = hp[14] + hp[15] #adds the hp of the index
mpg_lowest_hp_mean = hp_lowest / 2 #finds average of both of them
print(mpg_lowest_hp_mean)


'''The second question is: How powerful were the two most fuel-efficient cars from 1974?
Try again to divide the question into sub-problems and then to solve the sub-problems step by step. 
Assign the average horsepower value of the two most fuel-efficient cars in the variable mpg_highest_hp_mean.'''
print(sorted(mpg))
mpg_highest_idx = [mpg.index(32.4), mpg.index(33.9)]
print(mpg_highest_idx)

mpg_highest_hp_mean = (hp[17] + hp[19]) / 2
print(mpg_highest_hp_mean)


'''The third question is:
How many cylinders did most of the 1974 Mercedes models have?
Consider what kind of sub-problems you could divide this into. Assign the answer in the variable merc_cyl_mode.'''
#indexes 7 to 14 is the list of merc cars
print(cyl[7:14].count(4)) 
print(cyl[7:14].count(6))
print(cyl[7:14].count(8))

merc_cyl_mode = 8

