import time
start = input('Press enter to start the timer')
print('The timer has started.....')
start_time = time.time()
end = input('Press enter to stop the timer')
end_time = time.time()
elapsed_time = end_time-start_time
elapsed = int(elapsed_time)
print('The elapsed time is:', elapsed,'s')
