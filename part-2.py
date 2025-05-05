# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
        
    if array[0] == query:
        return True
        
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    
    if text[0] != text[-1]:
        return False
        
    return is_palindrome(text[1:-1])


# digit_match

def digit_match(apples, oranges):
    
    def helper (apples, oranges):
        if(apples == 0 or oranges == 0):
            return 0
        match_count = 1 if (apples%10 == oranges%10) else 0
            
        return match_count + helper(apples//10, oranges//10)
        
    
    if(apples == 0 and oranges == 0):
        return 1
    
    return helper(apples, oranges)


# def digit_match(apples, oranges):
#     if(apples == 0 and oranges == 0):
#         return 1
#     if(apples == 0 or oranges == 0):
#         return 0
#     match_count = 1 if (apples%10 == oranges%10) else 0
        
#     return match_count + digit_match(apples//10, oranges//10)

