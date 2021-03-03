# POMODORO VIRTUAL TIMER

import time
from playsound import playsound
from os import system, name 

#status_str = ""
mp3_file = "Alarm.mp3"
proceed_var = "y"
total_wcycle = 0

def cycle(Time, cycle_name):
	# btn.destroy()
	# btn2.pack()
	# global pval
	# global mp3_file
	global total_wcycle
	t_time = Time * 60
	curr_time = 0
	s_time = time.time()

	while True:
		# progress['value'] = pval
		global proceed_var
		# pval += 1
		# window.update_idletasks()
		time.sleep(1)
		now = time.time()

		curr_time = int(now - s_time)
		t_left = [0, 0]
		t_left[0] = int((t_time - curr_time) / 60)
		t_left[1] = t_time - (60 * t_left[0]) - curr_time
		system('cls')

		print("Time Elapsed: " + str(curr_time))
		# print((t_time - curr_time))
		print("Time Left in " + cycle_name + ": " + str(t_left[0]) + "  " + str(t_left[1]))

		# stop timer condition
		if curr_time >= t_time:
			#total_wcycle += 1
			playsound(mp3_file)
			# print("Proceed to Break?......")
			if cycle_name == "Work Cycle":
				total_wcycle += 1
				print("Work Cycle " + str(total_wcycle) + " Completed")
				proceed_var = (input("Proceed to " + "Break" + "?......"))

			else:
				proceed_var = (input("Proceed to " + "Work Cycle" + "?......"))

			break
		# if stopval:
		# 	break

input("....Enter any key to Start Timer....")
while True:
	if proceed_var == "y":
		cycle(25, "Work Cycle")
	if proceed_var == "y":
		cycle(5, "Break")
	if proceed_var == "n":
		break

print("End of Execution - completed " + str(total_wcycle) + " Work cycles")
input()