import time

# Display initial live time
print("Starting at:", time.strftime("%H:%M:%S"))

# First delay
time.sleep(3)
print("After 3 seconds, current time:", time.strftime("%H:%M:%S"))

# Second delay
time.sleep(4)
print("After 4 more seconds, current time:", time.strftime("%H:%M:%S"))

# Third delay
time.sleep(5)
print("After 5 more seconds, current time:", time.strftime("%H:%M:%S"))
print("Done!")