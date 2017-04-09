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

    import numpy as np

    ### your code goes here

    data = np.hstack((ages, net_worths, abs(net_worths - predictions)))
    data = data[np.argsort(data[:, 2])]

    cleaned_data = data

    print len(data)
    print len(cleaned_data)

   # for n in range(len(ages)):
        #print net_worths - predictions

    #    print n, ages[n], net_worths[n], predictions[n], abs(predictions[n] - net_worths[n])


    return cleaned_data

