# Bayesian Posterior Probability

Calculates a posterior probability based on the prior conditional probabilities.

## Purpose

Bayes' rule can be described as a way to improve a prior belief by incorporating observed data, related to this belief (like test data or sensor measurements). The rule is written as: 

P(A|B) = P(B|A) * P(A) / P(B)

Where A is the event and B is some observed, related data.

Given only three probabilities: `p_A`, `p_B_given_A`, and `p_notB_given_notA`, which can be written in notation as: 

P(A), P(B|A) 
P(notB|notA)

This function calculates the posterior probability:
P(A|B)

## Instructions

To use bayes.py, install this code base and run the following command:

      python bayes.py --pA <float> --pBgivenA <float> --pnotBgivennotA <float>

