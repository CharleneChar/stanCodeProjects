"""
File: weather_master.py
Name: Charlene
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


EXIT = -1


def main():
	"""
	Let user enter temperatures and help determine the highest and lowest one as well as the average of them all.
	Also, calculate the number of cold days defined by temperature value which is below 16 degree (not inclusive).
	(quit and result anytime when entering a specific value)
	"""
	print('stanCode \"Weather Master 4.0\"!')
	# Remember to use var. name (e.g. EXIT in this case) for inconstant exit number below
	data = float(input('Initial Temperature (or ' + str(EXIT) + ' to quit): '))
	maximum = data
	minimum = data
	total = data
	count = 1
	if data < 16:
		cold_count = 1
	else:
		cold_count = 0
	if data == EXIT:
		print('No temperatures were entered.')
	else:
		while True:
			data = float(input('Next Temperature (or -100 to quit): '))
			if data == EXIT:
				break
			if data >= maximum:
				maximum = data
			elif data <= minimum:
				minimum = data
			total += data
			count += 1
			if data < 16:
				cold_count += 1
		average = total / count
		print('Highest Temperature = '+str(maximum))
		print('Lowest Temperature = '+str(minimum))
		print('Average = '+str(average))
		print(str(cold_count)+' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
