# Ringgit Text

This is python package written to, translate a given amount into a Ringgit string.

A Ringgit string can be in 2 formats:

1. RM100.00
2. RINGGIT MALAYSIA ONE HUNDRED ONLY

## Requirements

The num2words package is required:

    pip install num2words

## Usage

The package can be used in 3 ways:

1. You can import **ringgit.py** to use the main functions
2. You can call the **ringgit.py** file directly with an argument. This will print the given number as a ringgit string in the default format
3. You can call the **rental.py** file directly with an argument. This will print the given number and the predicted deposit as a ringgit string in the default format.

<!-->

    python3 ringgit.py 100

returns:

    Ringgit Malaysia One Hundred Only
    (RM100.00)

**Note:**  
 If you are importing **ringgit.py** directly you can use the format_ringgit function to determine the format of the ringgit string.