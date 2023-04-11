"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

# open file 
f = open('sales-report.txt')

# loop over each line in file
for line in f:
    # remove trailing whitespace
    line = line.rstrip()
    # create list with data from line 
    # Ann Jacobs|219.59|77
    # salesperson's name|total amount of the order|total number of melons sold
    entries = line.split('|')
    # get salesperson's name
    salesperson = entries[0]
    # get total number of melons sold
    melons = int(entries[2])

    # get person's id if them is already in the salespeople list
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        # update total number of melons sold by this salesperson
        melons_sold[position] += melons
        
    else:
        # if this person is not in the list yet, add them
        salespeople.append(salesperson)
        # and add the info about the total number of melons sold by this salesperson
        melons_sold.append(melons)

# print report formed from the two lists data
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')