import sys
from ringgit import format_ringgit

def to_ringgit(amount):
    '''
    Returns the amount as a ringgit string.

    Usage:
    to_ringgit(100) ->

    Ringgit Malaysia One Hundred Only
	(RM100.00)
    '''
    return format_ringgit('@text\n\t(@amount)', amount)


# Assumes that the first argument passed is
# the rental amount.
rental = float(sys.argv[1])

# The deposit is usally twice the rental.
deposit = rental * 2

# Prints the rental amount.
print('Rental: ')
print(to_ringgit(rental))

# Prints the deposit amount.
print('Deposit: ')
print(to_ringgit(deposit))