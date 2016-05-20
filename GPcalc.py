#the user enters the number of courses he offers
number_of_courses = input("Enter number of courses here: ")
#a counter is used to count how many courses have been entered
counter = 0
#a "sum of units" variable is used to sum the units of all the entered courses
sum_of_units = 0
#A "sum of scores" variable is used to sum the scores obtained in each course
sum_of_scores = 0
grades = {"A":5, "B":4, "C":3, "D":2, "E":1, "F":0}
while counter != number_of_courses:
	course = raw_input("Enter name of course: ")
	unit = input("Enter course unit: ")
	score = input("Enter score: ")
	if score >= 70:
		score = grades["A"]
	elif score >= 60:
		score = grades["B"]
	elif score >= 50:
		score = grades["C"]
	elif score >= 45:
		score = grades["D"]
	elif score >= 40:
		score = grades["E"]
	else:
		score = grades["F"] 
	counter += 1
	product = score*unit
	sum_of_scores += product
	sum_of_units += unit
	if counter == number_of_courses:
		break
grade_point = float(sum_of_scores)/float(sum_of_units)
print "Your GP is %.2f" % grade_point
