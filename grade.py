def student_grade(marks:float)-> str:
    '''
    Calculate a students grade based on marks.
    Returns:
    Grade based on marks
    '''
    if marks>=90:
        return "A+"
    elif marks>=80:
        return "A"
    elif marks>=70:
        return "B"
    elif marks>=60:
        return "D"
    else:
        return "F"
    