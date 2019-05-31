from num2words import num2words


def to_decimal(number, decimal=2):
    '''
    to_decimal returns the given number as a string 
    with the given decimal places.

    number is a number
    decimal is a number (default: 2)

    Usage:
    to_decimal(1) -> "1.00"
    '''
    format_string = "{:." + str(decimal) + "f}"
    return format_string.format(number)


def to_ringgit_word(amount):
    '''
    to_ringgit_word return the amount of ringgit as text.
    The text will be formatted in title case.

    amount is a number

    Usage:
    to_ringgit_word(1100) -> "Ringgit Malaysia One Thousand One Hundred Only"
    '''
    text = num2words(amount)
    without_comma = text.replace(',', '')
    title_case = without_comma.title()

    return 'Ringgit Malaysia ' + title_case + ' Only'


def to_ringgit(amount):
    '''
    to_ringgit returns the amount as a ringgit string.

    amount is a number

    Usage:
    to_ringgit(100) -> "RM100.00"
    '''
    amount_str = to_decimal(amount)
    return f'RM{amount_str}'


def format_ringgit(format, amount):
    '''
    Format ringgit returns a string that is formatted
    using the format string and amount passed into the function.

    There are 2 variables usable in the format string.
    1.  @amount
        This represents the amount as ringgit in number format 
        "RM100.00"        

    2.  @text
        This represents the amount of ringgit in text format
        "RINGGIT MALAYSIA ONE HUNDRED ONLY"

    format is a string
    amount is a number

    Usage:
    format_ringgit("@text\n\t(@amount)", 100)

    returns:
    Ringgit Malaysia One Hundred Only
    (RM100.00)
    '''
    with_amount = format.replace('@amount', to_ringgit(amount))
    with_text = with_amount.replace('@text', to_ringgit_word(amount))

    return with_text


if __name__ == "__main__":
    import sys

    amount = float(sys.argv[1])
    amount_text = format_ringgit('@text\n\t(@amount)', amount)

    print(amount_text)