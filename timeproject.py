'''Scenario: A film company asks you to write a function called readable_time_fun() that turns the number 
of minutes into a str displaying the duration in hours and minutes. print(readable_time_fun(651)) should return 
'10 hour(s) and 51 minute(s)' as the output. Use the function with the following numbers of minutes and store 
the different function outputs in the str variable readable_time_str and then print that variable.

1
60
122
651
1000
10000
'''

def readable_time_fun(minutes): #defining the function
    #converting the minutes into hours
    hours = minutes // 60 
    # Get additional minutes with modulus
    minutes = minutes % 60
    # Create time as a string
    time_string = "{} hour(s) and {} minute(s)".format(hours, minutes)
    return time_string

readable_time_str = readable_time_fun(1)
print(readable_time_str)
readable_time_str = readable_time_fun(60)
print(readable_time_str)
readable_time_str = readable_time_fun(122)
print(readable_time_str)
readable_time_str = readable_time_fun(651)
print(readable_time_str)
readable_time_str = readable_time_fun(1000)
print(readable_time_str)
readable_time_str = readable_time_fun(10000)

