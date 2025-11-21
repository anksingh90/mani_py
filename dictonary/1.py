#stu{key:value}

#accessing dic.values
stu={"alto":"maruti",'safari':'tata', 'xuv':'mahindra'}
print(stu)
print(stu["alto"])
stu.get("alto")
print(stu)

#editing dic. values

stu['alto'] = 'suzuki'
print(stu)

# Adding new entry

stu['xyz'] = 'abc'
print(stu)

#deletion 
#"deleting value"/pop()
stu.pop('xuv')
print(stu)
 #accessing value
print(stu.keys())
print(stu.values())
print(stu.items())