class InvalidPassException(Exception):
    pass


code = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num != code:
        raise InvalidPassException
    else:
        print("Passcode Accepted")

except InvalidPassException:
    print("Exception occurred: Invalid Passcode!")
