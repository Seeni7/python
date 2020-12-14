#!/usr/bin/env

fahrenheit = float(input("What is the temperature (in Fahrenheit) would you like to coverted to Celsius? "))
celsius = (fahrenheit -32) * 5/9

print(fahrenheit, "F is", round(celsius, 2), "C")