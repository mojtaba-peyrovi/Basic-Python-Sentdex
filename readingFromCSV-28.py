import csv # comma seperated variables
with open('list.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    #for row in readCSV:
        #print(row)
        #print(row[0])
        #print(row[0],row[1])


    dates = []
    colors = []

    for row in readCSV:
        color = row[3]
        date = row[0]
        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)
    '''
    try:
        whatColor = input('what color do you want?')

        coldex = colors.index(whatColor.lower())
        theDate = dates[coldex]
        print('the date is: ' , theDate)
    except Exception as a:
        print(a)
    '''
    whatColor = input('what color do you want?')
    if whatColor in colors:
        coldex = colors.index(whatColor.lower())
        theDate = dates[coldex]
        print('the date is: ' , theDate)
    else:
        print('the color is not found')

    print('continuing')
