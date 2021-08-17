def func():
    lists = ['No Time is 0', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    return lists


x = round(float(input('Enter the time currently: ')))

if 2 < x <= 6:
    print(str(func()[x]) + ', it is early morning')
elif x < 12 and x < 12 and x != 2 and x != 1:
    print((str(func()[x])) + ', it is morning.')
elif x == 12 and x != 11:
    print(str(func()[x]) + ', it is noon.')
elif not x == 12 and x <= 17.00 and x != 2 and x != 1:
    print(str(func()[x]) + ', it is afternoon.')
elif x <= 20 and x != 2 and x != 1:
    print(str(func()[x]) + ', it is evening.')
elif x <= 24 or x <= 2:
    print(str(func()[x]) + ', it is night time.')