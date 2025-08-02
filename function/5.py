def median(lst):
    if len(lst)%2==0:
        middle_value = len(lst)/2
    else:
        middle_value = (len(lst)+1)/2

    lst.sort()
    print(lst)
    print("The middle value of the list",int (middle_value) -1)
    lst[middle_value]



# Main Program
lst=[1.4,2.4,3.5,6.9,7.3,1.4]
median(lst)
