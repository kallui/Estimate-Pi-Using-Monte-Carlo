# Estimate-Pi-Using-Monte-Carlo

Monte Carlo methods are a broad class of computational algorithms that rely on repeated random sampling to obtain numerical results. One of the uses of the Monte Carlo method is to estimate Pi. I've created a Python program that visualizes the process and allows the users to control the number of points to use.

The simplified idea of the process: Imagine a 2x2 square, with a circle of radius 1 that perfectly fits inside of the square. Now randomly put points into the square and count how many point gets inside of the circle. The estimation of Pi would be Pi = 4 * (points inside of circle / points inside of the square), where the points inside the square would just be the total number of points we put. This way, generally, the more points we use to estimate Pi, the more accurate it becomes. 

Instruction: To use this program, simply download the EstimatePi.py file and run it. 

More information:
https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/,
https://en.wikipedia.org/wiki/Monte_Carlo_method


