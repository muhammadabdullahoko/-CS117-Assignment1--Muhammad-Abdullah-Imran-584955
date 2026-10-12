#RESISTOR COLOUR CODE
colour=input("Enter you colour : ").lower()
colour_code={"black":0,
             "brown":1,
             "red":2,
             "orange":3,
             "yellow":4,
             "green":5,
             "blue":6,
             "violet":7,
             "grey":8,
             "white":9}
if colour in colour_code:
    print(f"Your Digit is :{colour_code[colour]}")
else:
    print("Invalid colour")
