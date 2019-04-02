# Complete the matchingStrings function below.
# In this question passing the strings,queries of the main function
def matchingStrings(strings, queries):
    # l will be the list
    l = []
    # In the for loop checking
    # count the no of strings present in the queries
    for i in queries:
        count=0
        for j in strings:
        # if queries equal to the strings increase count value.
            if i==j:
                count+=1
        l.append(count)
    return l