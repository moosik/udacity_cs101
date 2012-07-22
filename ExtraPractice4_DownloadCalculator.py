# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth and returns the time taken to download the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) whereas file size is given in
# megabytes (MB).
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
    seconds = number-hours*60*60-minutes*60.
    if seconds!=1:
        output_seconds = str(seconds)+" "+"seconds"
    else:
        output_seconds = str(seconds)+" "+"second"
    return output_hours+", "+output_minutes+", "+output_seconds


def download_time(file_size,file_unit,bw_size,bw_unit):
    if file_unit=="kB":
        file_size = file_size*2**10*8.
    elif file_unit == "kb":
        file_size = file_size*2**10*1.
    elif file_unit=="MB":
        file_size = file_size*2**20*8.
    elif file_unit == "Mb":
        file_size = file_size*2**20*1.
    elif file_unit=="GB":
        file_size = file_size*2**30*8.
    elif file_unit == "Gb":
        file_size = file_size*2**30*1.
    elif file_unit=="TB":
        file_size = file_size*2**40*8.
    else:
        file_size = file_size*2**40*1.
    if bw_unit=="kB":
        bw_size = bw_size*2**10*8.
    elif bw_unit == "kb":
        bw_size = bw_size*2**10*1.
    elif bw_unit=="MB":
        bw_size = bw_size*2**20*8.
    elif bw_unit == "Mb":
        bw_size = bw_size*2**20*1.
    elif bw_unit=="GB":
        bw_size = bw_size*2**30*8.
    elif bw_unit == "Gb":
        bw_size = bw_size*2**30*1.
    elif bw_unit=="TB":
        bw_size = bw_size*2**40*8.
    else:
        bw_size = bw_size*2**40*1. 
    
    return convert_seconds(file_size/bw_size)


print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')
