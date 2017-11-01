## 3. Bikesharing distribution ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

prob_over_5000 = bikes[bikes["cnt"] > 5000].shape[0]/bikes.shape[0]

## 4. Computing the distribution ##

import math

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))

def combin(N ,k ):
    son = math.factorial(N)
    mon = math.factorial(k) * math.factorial(N-k)
    return son / mon

def com_pro(p,q,days,total):
    
    return p**days * q**(total-days)

p = .39
q = 1 - .39
outcome_probs = []
for i in outcome_counts:
    outcome_probs.append(combin(30 , i) * com_pro(p,q,i,30))
    


## 5. Plotting the distribution ##

import matplotlib.pyplot as plt

# The most likely number of days is between 10 and 15.
plt.bar(outcome_counts, outcome_probs)
plt.show()

## 6. Simplifying the computation ##

import scipy
from scipy import linspace
from scipy.stats import binom

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)
outcome_probs = binom.pmf(outcome_counts,30,0.39)
plt.bar(outcome_counts, outcome_probs)
plt.show()

print(outcome_probs.mean())

## 8. Computing the mean of a probability distribution ##

dist_mean = None
dist_mean = 30 * .39

## 9. Computing the standard deviation ##

dist_stdev = None

dist_stdev = (30*.39*.61)**(1/2)

## 10. A different plot ##

# Enter your answer here.
from scipy.stats import binom
from scipy import linspace

outcome = linspace(0,10,11)

outcome_probs = binom.pmf(outcome, 10 ,.39)
plt.bar(outcome, outcome_probs)
plt.show()

outcome_counts = linspace(0,100,101)
outcome_probs = binom.pmf(outcome_counts,100,0.39)
plt.bar(outcome_counts, outcome_probs)
plt.show()

## 11. The normal distribution ##

# Create a range of numbers from 0 to 100, with 101 elements (each number has one entry).
outcome_counts = scipy.linspace(0,100,101)

# Create a probability mass function along the outcome_counts.
outcome_probs = binom.pmf(outcome_counts,100,0.39)

# Plot a line, not a bar chart.
plt.plot(outcome_counts, outcome_probs)
plt.show()

## 12. Cumulative density function ##

outcome_counts = linspace(0,30,31)
outcome_probs = binom.cdf(outcome_counts,30,0.39)
plt.plot(outcome_counts, outcome_probs)
plt.show()

## 14. Faster way to calculate likelihood ##

left_16 = None
right_16 = None

left_16 = binom.cdf(16 , 30 , .39)
right_16 = 1- left_16