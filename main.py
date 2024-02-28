seconds = input('Enter the number of seconds (integer): ')
seconds = int(seconds)
# ... complete the code below
# hours = seconds//3600
# minutes = seconds%3600//60
# seconds = seconds%3600%60
minutes, seconds = divmod(seconds, 60)
hours, minutes = divmod(minutes, 60)


# Follow the formatting given
# e.g. The duration is X hours, X minutes, and X seconds.
print("The duration is", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")
