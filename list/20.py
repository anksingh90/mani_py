var=7
while var>0:
    print('current value:',var)
    var=var-1
    if var==3:
        break
    else:
        if var==6:
            var=var-1
            continue
    print("good bye")