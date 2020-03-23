""" importing the module random and math
    it is calculate using some feature of probability
    and it is good to get idea of it but we can improve
    the accuracy
"""
import random , math
def calculatePi(n=10000): #n is 10000 by default but you can change it and it is the number of random choice inside the square
    points = [(random.uniform(-1,1), random.uniform(-1,1)) for _ in range(n)] #we are getting the x , y coordinates of points inside the square
    points_inside_circle = [(x,y) for(x,y) in points if x**2 + y **2 <=1] #now we are seperating the points that are inside the circle if their distance is less than 1 because that is the radius
    PI = 4* len(points_inside_circle) / len(points) #calculating pi using formula
    return PI #returning pi

if __name__ == "__main__": #running the function
    results = [] #storing the result of pi in results list
    avg_pi_value = 0 #the average value of pi initiallly it is 0
    
    for _ in range(100): #doing calculatePi function 100 times
        results.append(calculatePi()) #storing the value in results lists
    avg_pi_value = sum(results) / len(results) #storing the pi value for more accuracy
    print(avg_pi_value) #printing it in the screen
    avg_error = (math.pi - avg_pi_value)/ math.pi * 100 # the percentage of error in calculation
    print("average error in the value of pi is %s"%avg_error + "%")