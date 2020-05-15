import time

# formatting for date a time variables
time_format = '%I:%M'
date_format = '%A, %B %d, %Y'

# Pulls time
def tick():
    s = time.strftime(time_format)
    # label_clock.after(200, tick)
    return s

# Pulls date
def date():
	d = time.strftime(date_format)
	return d


# why did i make this god damn waste of time
