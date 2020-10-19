
temprature = 0
temprature = eval(input('Please enter your body temprature'))
if (temprature >= 39.5):
    print("Your body temprature ", temprature, "is in the RED zone! you have a high fever!")
elif (temprature >= 37.6):
    print("Your body temprature ", temprature, "is in the YELLOE zone! you have a moderate fever!")
else:
    print("Your body temprature ", temprature, "is in the GREEN zone! you have a normal temprature!")
