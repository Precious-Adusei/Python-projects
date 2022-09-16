'''Scenario: In 1974, 32 cars were tested in Motor Trend magazine. The magazine is preparing a review of that year and has asked you, as a data analyst, to answer the following questions:

How much gas did the cars from 1974 consume per 100 km?
Which car from 1974 was the most powerful? How much gas did it consume per 100km?
What percentage of the cars from 1974 had an automatic transmission?
Before you answer the questions, you have to check the data and clean it up if necessary. Your predecessor prepared the following data. The same position in each list refers to the same car model. 
For example, the Mazda RX4 is in the first position (index 0) in mazda_name, mazda_mpg, mazda_am and mazda_hp.'''

# car model names:
mazda_name = ['Mazda RX4', 'Mazda RX4 Wag']
hornet_name = ['Hornet 4 Drive', 'Hornet Sportabout']
merc_name =  ['Merc 240D', 'Merc 230', 'Merc 280', 'Merc 280C',
             'Merc 450SE', 'Merc 450SL', 'Merc 450SLC', 'Merc 500 SL']
toyota_name = ['Toyota Corolla', 'Toyota Corona']
other_name = ['Datsun 710', 'Valiant', 'Duster 360', 'Cadillac Fleetwood',
              'Lincoln Continental', 'Chrysler Imperial', 'Fiat 128',
              'Honda Civic', 'Dodge Challenger', 'AMC Javelin', 'Camaro Z28',
              'Pontiac Firebird', 'Fiat X1-9', 'Porsche 914-2', 'Lotus Europa',
              'Ford Pantera L', 'Ferrari Dino', 'Maserati Bora', 'Volvo 142E']

# miles per gallon
mazda_mpg = [21.0, 21.0]
hornet_mpg = [21.44, 18.7]
merc_mpg = [24.4, 22.8, 19.2,
            17.8, 16.4, 17.3,
            15.2, 12.7]
toyota_mpg = [33.9, 21.5]
other_mpg = [22.8, 18.1, 14.3,
             10.3, 10.4, 14.7, 32.4,
             30.4, 15.5, 15.2, 13.3,
             19.2, 27.3, 26.0, 30.4,
             15.8, 19.7, 15.0, 21.4]

# transmission (0 = automatic, 1 = manual)
mazda_am = [1, 1]
hornet_am = [0, 0]
merc_am =  [0, 0, 0, 0, 0, 0, 0, 0]
toyota_am = [1, 0]
other_am = [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

# gross horsepower
mazda_hp = [110, 110]
hornet_hp = [110, 175]
merc_hp = [62, 95, 123, 123, 180, 180, 180, 240]
toyota_hp = [65, 97]
other_hp = [93, 105, 245, 205, 215,
            230, 66, 52, 150, 150, 
            245, 175, 66, 91, 113,
            264, 175, 335, 109]

#this is to compare if all the variables are the same or some needs to be removed/ added
print(len(mazda_name)), print(len(mazda_hp)), print(len(mazda_mpg)), print(len(mazda_am))
print(len(hornet_name)), print(len(hornet_hp)), print(len(hornet_mpg)), print(len(hornet_am))
print(len(merc_name)), print(len(merc_hp)), print(len(merc_mpg)), print(len(merc_am))
print(len(toyota_name)), print(len(toyota_hp)), print(len(toyota_mpg)), print(len(toyota_am))
print(len(other_name)), print(len(other_hp)), print(len(other_mpg)), print(len(other_am))


'''How many cars are there in total in the data set that your predecessor prepared? 
Assign the number to a new variable test_N. Is the number correct?'''
name = mazda_name + hornet_name + merc_name + toyota_name + other_name
print(name)
test_N = len(name) #finds the total number of the names of cars
print(test_N)

"""The number does not match the number of cars tested (32). There is a car in the data set that shouldn't be there 
and it needs to be removed. Some research on Google reveals that the Mercedes 500 SL was first introduced in 1980. 
Remove all entries for this car in the Mercedes lists (merc_name, merc_mpg, merc_am, merc_hp)."""
index = merc_name.index('Merc 500 SL')
print(index) #prints the index to find Merc 500 SL among all the variables
del merc_name[7]
del merc_mpg[7]
del merc_am[7]
del merc_hp[7]

'''The magazine's first question is:
How much gas did the cars from 1974 consume per 100 km?
Determine the average gas consumption value of all the cars in miles per gallon (MPG)
Convert this average value into l/100km

Tip: the formula to calculate miles per gallon into l/100km is
𝑐𝑜𝑛𝑠𝑢𝑚𝑝𝑡𝑖𝑜𝑛=100*3.785411784 / 1.609344*𝑀𝑃𝐺'''
total_mpg = mazda_mpg + hornet_mpg + merc_mpg + toyota_mpg + other_mpg
print(total_mpg)

def Average(total_mpg): #function to find the average value of the miles per gallon
    avg = sum(total_mpg) / len(total_mpg)
    return avg

average = Average(total_mpg) #variable for the average 
print('Average mpg is: ', average)

liters_per_100km = (100 * 3.785411784) / (1.609344 * average) #calc to change mpg to lpkm
print('How many lpkm: ', liters_per_100km)

'''The magazine's second question is:
Which car from 1974 was the most powerful? How much gas did it consume per 100km?
As a data analyst, you often have to narrow down questions that are fairly general. You ask the magazine what they 
mean by powerful. They tell you that they mean horsepower, which is represented by the variable hp

Now assign the answer to a new text variable answer2, using the following template:
The most powerful car from 1974 was the 'xxx'. It consumed XX.X l/100 km.
Please note the following:

Quotation marks before and after the car name
The consumption should be rounded to one decimal place'''
name = mazda_name + hornet_name + merc_name + toyota_name + other_name #will add the new list of car names
hp = mazda_hp + hornet_hp + merc_hp + toyota_hp + other_hp
print(hp)
print(max(hp)) #maximum hp among all the values
print(hp.index(335)) # finds the index of the max hp
power_name = name[30] #find the most poweful name of car with that index found from hp.index
print(power_name)

#finding liters per km of the Maserati Bora car
mpg = mazda_mpg + hornet_mpg + merc_mpg + toyota_mpg + other_mpg
print(mpg)
power_lpkm = (100 * 3.785411784) / (1.609344 * mpg[30])
power_lpkm = round(power_lpkm, 1) #the final lpkm rounded to 1 decimal number
print(power_lpkm)

answer2 = "The most powerful car from 1974 was the '{}'. It consumed {} l/100 km."
print(answer2.format(power_name, power_lpkm))

'''The magazine's third question is:
What percentage of the cars from 1974 had an automatic transmission?
It's very clear here that you need the data in the am variable. How are these encoded? 
Read the comment on the line above where the am variables are defined in the first code cell.
Round the answer off mathematically and assign it to the variable percentage_automatic as an int.'''

total_am = mazda_am + hornet_am + merc_am + toyota_am + other_am #finds the total am of all cars
print(total_am)
total_am.count(0) #0= automatic transmission, finds the occurences of 0 in the list
quotient = 19 / 32
percentage_automatic = round(quotient * 100)
print(percentage_automatic)

