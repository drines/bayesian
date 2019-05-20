#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.20
# REVISED DATE:     2019.05.20
# PURPOSE:  Function for calculating a Bayesian posterior probablity.
#
# NOTES:    Program takes in three probabilities:
#               1. P(A)
#               2. P(B | A)
#               3. P(notB | notA).
#
#   Example call:
#      python bayes.py --pA <value> --pBgivenA <value> --pnotBgivennotA <value>
##

import argparse


def get_input_args():
    """
    Retrieves and parses the command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's
    argparse module to created and defined these command line arguments. If
    the user fails to provide some or all of the arguments, then the default
    values are used for the missing arguments. 
    Command Line Arguments:
      1. P(A) --pA <float> 
      2. P(B | A) --pBgivenA <float> 
      3. P(notB | notA) --pnotBgivennotA <float>
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - using argparse module to store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser(description='Calcs Bayesian posterior prob P(A | B).')
    # Create the command line arguments as mentioned above
    parser.add_argument('--pA,
                        type=float,
                        default= 0.3,
                        help='P(A): (default: 0.3).')
    parser.add_argument('--pBgivenA',
                        type=float,
                        default= 0.7',
                        help='P(B | A): (default: 0.7).')
    parser.add_argument('--pnotBgivennotA',
                        type=float,
                        default= 0.9,
                        help='P(notA | notB): (default: 0.9).')

    # Return the parsed arguments back to the calling function
    return parser.parse_args()

