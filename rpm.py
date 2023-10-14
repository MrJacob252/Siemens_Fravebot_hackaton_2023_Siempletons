from math import pi

# R = 200 #path radius
# wheel_diameter = 1

# wheel_rpm = [0.0] * 4
# K = []

# R = wheel_diameter*0.5

# L = 250 #Wheel base

# T = 30 #time to complete

# V = 2*pi*(R/T)

# om = V/R

# for i in range(len(wheel_rpm)):
    
rpm = [0.0]*4
    
D = 500

o_min = 2*pi*D*0.5

delta = 310

o_max = 2*pi*(D+(2*delta))*0.5

k = o_min/o_max

print(k)
