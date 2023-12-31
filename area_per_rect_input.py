#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: September 25th, 2023
# This program asks the user for the length and
# width of the rectangle in cm. It then 
# calculates and displays the area and 
# perimeter.
import math

def main():
    # input
    print("We are going to calculate the area and")
    print("perimeter of a rectangle")
    length = int(input("Enter the length (cm): "))
    width = int(input("Enter the width (cm): "))
    
    # process
    area = length * width
    perimeter = 2*(length + width)

    # output
    print("")
    print ("Area = {} cm^2". format (area))
    print ("Perimeter = {} cm". format (perimeter))


if __name__ == "__main__":
  main()