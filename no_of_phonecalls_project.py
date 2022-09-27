'''
Scenario: A German telecommunications company has asked you to help them analyze some data. 
Until now an employee has had to go through data relating to phone calls and manually sort 
it into three countries: Germany, the UK and the USA.
The aim is to determine how often phone calls were made and the total duration of calls made to each country.

You receive the data in the variable calls.
'''

calls = [['+49-123456', 12.8], ['+1-123456', 1.6], ['+44-123456', 0.1],
        ['+49-0101010', 22.1], ['+49-12121', 2.8], ['+49-44335', 0.3],
        ['+49-1111111', 2.3], ['+1-121229', 9.2], ['+49-44355', 45],
        ['+44-1111110', 0.2], ['+44-12222', 1.8], ['+44-44555', 0.3],
        ['+49-0111110', 45], ['+44-22222', 0.5], ['+49-44336', 12],
        ['+1-01111009', 0.1], ['+49-32222', 4.2], ['+1-443667', 0.2],
        ['+49-0111000', 0.3], ['+49-33222', 0.3], ['+49-44666', 0.1],
        ['+49-0110000', 0.3], ['+44-33322', 9.7], ['+49-44337', 0.1],
        ['+49-0100000', 45], ['+44-33332', 11.9], ['+49-44377', 0.6],
        ['+49-0000000', 4.2], ['+49-33333', 33.5], ['+49-44777', 77.2],
        ['+44-1200000', 3.1], ['+1-433334', 0.3], ['+44-44338', 12],
        ['+49-1230000', 11.9], ['+49-44333', 4.2], ['+49-44339', 4.2],
        ['+49-1234000', 13.0], ['+49-44433', 0.2], ['+49-44310', 45],
        ['+49-1234500', 61.2], ['+49-44443', 0.1], ['+44-44311', 0.1],
        ['+1-12345601', 8.8], ['+49-44444', 0.2], ['+49-43312', 0.1],
        ['+49-0123456', 1.2], ['+44-54333', 13.7], ['+44-41233', 0.2]]

'''
Number of calls per country'''
#naming the variables
calls_count_d = 0
calls_count_uk = 0
calls_count_us = 0
calls_count_others = 0

#finding the calls using a combination of for loops and if statements
for call in calls:
    if '+49' in call[0]:
        calls_count_d = calls_count_d + 1
    elif '+44' in call[0]:
        calls_count_uk = calls_count_uk + 1 
    elif '+1' in call[0]:
        calls_count_us = calls_count_us + 1 
    else:
        calls_count_others = calls_count_others + 1

#prints out the results of all the calculations        
print(calls_count_d)
print(calls_count_uk)
print(calls_count_us)
print(calls_count_others)

'''
Total duration of all calls per country'''
#defining variables
calls_duration_ger = 0
calls_duration_uk = 0
calls_duration_us = 0
calls_duration_others = 0

#combining for loops and if statements
for call in calls:
    if '+49' in call[0]:
        calls_duration_ger = calls_duration_ger + call[1]
    elif '+44' in call[0]:
        calls_duration_uk = calls_duration_uk + call[1]
    elif '+1' in call[0]:
        calls_duration_us = calls_duration_us + call[1]
    else:
        calls_duration_others = calls_duration_others + call[1]
       
#prints the statements
print(calls_duration_ger)
print(calls_duration_uk)
print(calls_duration_us)
print(calls_duration_others)

