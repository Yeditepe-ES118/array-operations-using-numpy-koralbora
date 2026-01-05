import numpy as np #importing numpy

def stat(): #defining the function

    data = np.loadtxt("populations.txt") #loading the txt file as a variable called data

    hare = data[:,1] #extracting the hare counts from the greater array

    min_year_hare = data[np.argmin(hare),0] #getting the year in which the hares have the smallest population

    lynx_avg = np.mean(data[:,2]) #finding the average amount of lynx populations of the entire dataset

    sum_all_species = np.sum(data[:,1:], axis=1) #summing all data for the species
    new_data = np.column_stack((data, sum_all_species)) #adding the new sum_all_species to the end of the array which creates new_data

    new_data[new_data[:, 3] < 40000, 3] = 0 #setting all carrot values below 40000 to 0

    return data, hare, min_year_hare, lynx_avg, new_data #returning the data
