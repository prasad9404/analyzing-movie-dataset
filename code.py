# --------------
from csv import reader
import csv

review_max={}
movies_clean=[]
def explore_data(dataset, start, end, rows_and_columns=False):
    """Explore the elements of a list.
    
    Print the elements of a list starting from the index 'start'(included) upto the index 'end'         (excluded).
    
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes binary          values, either True or False. If true, print the dimension of the list, else dont.
    """
    for i in range(start,end):
        print(dataset[i],end="\n")

def duplicate_and_unique_movies(dataset, index_):
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or duplicated based     on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for duplicacy 
    
    """
    for row in dataset.values():
        
        key=row[index_]
        if key in review_max.keys():
            num=review_max[key]
            num+=1
            review_max[key]=num
        else:
            review_max[key]=1
    
    movies_clean=[num for num in review_max.values() if num>1]

def movies_lang(dataset, index_, lang_):
    """Extract the movies of a particular language.
    
    Of all the movies available in all languages, this function extracts all the movies in a            particular laguage.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    
    """
    movies_=[]
    for row in dataset.values():
        if(row[index_] == lang_):
            movies_.append(row[13])
    explore_data(movies_,0,5,False)
    return movies_
    
def rate_bucket(dataset, rate_low, rate_high):
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.
    
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """
    rated_movies=[]
    for row in dataset.values():
        rate = float(row[11]) 
        if((rate >= rate_low and rate <= rate_high) and row[3] == "en"):
            rated_movies.append(row)  
    explore_data(rated_movies,0,5,False)
    #del rated_movies[0]
    return rated_movies

# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)

mydict={}
with open(path, 'r') as file:
    csv_file = csv.reader(file)
    i=0
    for row in csv_file:
        mydict[i]=row
        i+=1;


# The first row is header. Extract and store it in 'movies_header'.
movies_header = mydict[0]

# Subset the movies dataset such that the header is removed from the list and store it back in movies
del mydict[0]
del movies[0]



# Delete wrong data

# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.

del movies[4553]

# Using explore_data() with appropriate parameters, view the details of the first 5 movies.

#explore_data(mydict,1,6,False)



# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.



# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.



# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 
#duplicate_and_unique_movies(mydict,13)



# Calling movies_lang(), extract all the english movies and store it in movies_en.
#movies_en =  movies_lang(mydict,3,"en")



# Call the rate_bucket function to see the movies with rating higher than 8.
high_rated_movies = rate_bucket(mydict,8.0,10.0)
print(high_rated_movies)


