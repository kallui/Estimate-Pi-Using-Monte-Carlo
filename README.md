# Monte Carlo Pi Estimation

Monte Carlo methods are a versatile class of computational algorithms that leverage repeated random sampling to derive numerical results. This Python program visualizes the Monte Carlo method in action, specifically for estimating the value of Pi. Users can control the number of points used in the estimation process.

## Overview

The Monte Carlo Pi estimation operates on a simple principle:

1. Visualize a 2x2 square with a perfectly fitting circle of radius 1.
2. Randomly place points within the square and count how many fall inside the circle.
3. The estimation of Pi is calculated as Pi ≈ 4 * (points inside the circle / total points inside the square).

The accuracy of the estimation improves as more points are used in the calculation.

## Usage

To use this program, follow these steps:

1. Download the `EstimatePi.py` file.
2. Make sure you have `pygame` library installed. You can install by ```pip install pygame```
3. Run the Python script.

```bash
python EstimatePi.py
```

## More information:
- https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/,
- https://en.wikipedia.org/wiki/Monte_Carlo_method

## Preview

![image](https://github.com/kallui/Estimate-Pi-Using-Monte-Carlo/assets/90471072/132bc3f0-60fa-4aeb-bd2e-c24645577829)

![image](https://github.com/kallui/Estimate-Pi-Using-Monte-Carlo/assets/90471072/0e432653-68f7-44f1-a209-b8899fa2ceb1)



