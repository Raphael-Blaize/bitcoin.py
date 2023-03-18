#Getting http requests
import requests
#for command line arguments
import sys

#defining a function to check weather a number is a float or not
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
'''
1. checking if the argument at location 1 is a float using the function
2. try and except statement for errors
3. fetching the json file using requests.get
4. storing the json file in a usd variable
5. getting the location of rate_float which is where the value of bitcoin in USD is
6. mulitplying that rate with the amount of bitcoin we want to buy
7. printing to 4 decimal places
8. Exiting if the conditions are not met
'''

if isfloat(sys.argv[1]) == True:
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        usd = response.json()
        bitcoin = usd["bpi"]["USD"]["rate_float"]
        amount = bitcoin * float(sys.argv[1])
        print(f"${amount:,.4f}")
    except requests.RequestException:
        pass
elif isfloat(sys.argv[1]) == False:
    sys.exit("Command-line argument is not a number")

else:
    sys.exit("Missing command-line argument")
