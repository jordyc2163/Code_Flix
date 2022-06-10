# Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a grade for the exam and a number of completed projects.

# This function should take two arguments: exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above);

# This function should return a number (final grade). There are four types of final grades:

# 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# 0, in other cases


# Example 1: 
# Input: final_grade(100, 12)
# Output: 100

# Example 2:
# Input: final_grade(85, 5) 
# Output: 90

def finalGrade(grade, projects):
    if grade > 90 or projects > 10:
        return 100
    elif grade > 75 and projects >= 5:
        return 90
    elif grade > 50 and projects >= 2:
        return 75
    else:
        return 0

print(finalGrade(75, 0))

# Lucky Numbers
# Given an array of integers arr, a lucky integer is an integer which has a frequency in the array equal to its value.
# Return a lucky integer in the array. If there are multiple lucky integers return the largest of them. If there is no lucky integer return -1.
# Example 1:
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

def luckynum(array):
    from collections import Counter
    c = dict(Counter(array))
    max_num = -1
    for k,v in c.items():
        if k == v:
            if k > max_num:
                max_num = k
        else:
            return -1
    return max_num

print(luckynum([1,1,2,3,3]))