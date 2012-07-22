# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3

def convert_seconds(number):
    hours = int(number/(60*60))
    if hours!=1:
        output_hours = str(hours)+" "+"hours"
    else:
        output_hours = str(hours)+" "+"hour"
    minutes = int((number - hours*60*60)/60)
    if minutes!=1:
        output_minutes = str(minutes)+" "+"minutes"
    else:
        output_minutes = str(minutes)+" "+"minute"
    seconds = number-hours*60*60-minutes*60
    if seconds!=1:
        output_seconds = str(seconds)+" "+"seconds"
    else:
        output_seconds = str(seconds)+" "+"second"
    return output_hours+", "+output_minutes+", "+output_seconds
    
print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second
print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds
print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds
print convert_seconds(3600)