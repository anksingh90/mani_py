#Write a program using a user defined function myMean() to calculate the mean of floating values stored in a list.
#Function to calculate mean
#The requirements are listed below:
	#1. The function should have 1 parameter (list containing floating 
	    #point values)
	#2. To calculate mean by adding all the numbers and dividing by  
	    #total number of elements

def myMean(lst):
    sum = 0
    for i in lst:
        sum = sum + i
    print('Mean : ',sum/len(lst))


lst = [1.1, 2.1, 3.4, 5.2, 6.5]
myMean(lst)