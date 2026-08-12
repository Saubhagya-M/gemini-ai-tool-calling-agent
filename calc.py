def calculator(a:float,b:float,operation:str)->float:
    '''
    Perform a mathemetical operation.

    Args:
    a. First Number
    b. Second Number
    operation: add, subtract,multiply or divide.
    Returns:
    Result of the Calculation        
    '''
    if operation=="add":
        return a+b
    elif operation=="subtract":
        return a-b
    elif operation=="multiply":
        return a*b
    elif operation=="divide":
        if b==0:
            return "Can Not Divide by ZERO!!!!"
        return a/b
    else:
        return 'UNKNOWN OPERATION!!!!'