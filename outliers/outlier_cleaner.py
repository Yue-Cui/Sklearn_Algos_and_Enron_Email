#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    original_data=zip(ages, net_worths, predictions)
    errors=[pred-real for pred, real in zip(predictions, net_worths)]
    processed_data=zip(ages, networths, errors)
    processed_data.sort(key=errors)
    cleaned_data=processed_data[:len(predictions)*0.9]


    return cleaned_data
