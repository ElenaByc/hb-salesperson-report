"""Generate sales report showing total melons each salesperson sold."""


def get_sales_data(input_file):
    """Construct dictionary of {salesperson_name: melons_sold} from given file"""

    sales_report = {}

    # open file
    file = open(input_file)

    # loop over each line in file
    for line in file:
        # remove trailing whitespace
        line = line.rstrip()
        # get data from line
        # Ann Jacobs|219.59|77
        # salesperson's name|total amount of the order|total number of melons sold
        salesperson_name, _, melons_sold = line.split('|')
        sales_report[salesperson_name] = sales_report.get(
            salesperson_name, 0) + int(melons_sold)

    file.close()
    return sales_report


def print_report(sales_report):
    """Print sales report formed from dictionary data"""
    for salesperson_name, melons_sold in sales_report.items():
        print(f'{salesperson_name} sold {melons_sold} melons')


print_report(get_sales_data('sales-report.txt'))
