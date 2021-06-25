
def check_doc_string_len(fn):
    """
    This function is used to check the docstring count for each fucntion, it checks 
    if the doc string is of minimum 50 characters and returns True or False

    #clouser
        check_doc_string_len_inner:
            This function uses two free varibales i.e. free_var_local  and mydoc. It then checks if mydoc is not 
            empty and then checks its lenght, 
            if the condition is satisfied it returns a bool
    """
    free_var_local_count = 50
    def check_doc_string_len_inner():
        '''This function returns True, if the docstring has minimum 
            50 characters else it returns false'''
        nonlocal free_var_local_count
        if len(fn.__doc__) >= free_var_local_count:
            return True
        else:
            return False
    return check_doc_string_len_inner
	
	
def myfibonacci():
    '''Function to generate the next fibonacci number
    
    Input:
        first and sencond number has been initiated with difualt value

    output:
    generate the next fibonacci number
     '''
    first = 0
    second = 1
    def generate_my_next_number():
        ''' This function to generate sum of previous number and returns the genarated numbers
        
        '''
        nonlocal first,second
        temp = second
        second = first + second
        first = temp
        return second
    return generate_my_next_number



def add(a, b):
    '''Function adds the two elements
    Input : a,b int object
    '''
    return a + b

def mult(a, b, c):
    '''Function which return the product of the numbres
    Inputs: a,b,c int object
    '''
    return a * b * c

def div(a,b):
    ''' Div of two numbers 
    a : int
    b : int
    '''   
    if b==0:
        raise ValueError("denomnetor should not be zero")
    else:
        return a/b

def my_counter(fn):
    '''This function used to calcualte how many times a funtion is called
    '''
    cnt = 0
    def inner(*args,**kwargs):
        nonlocal cnt
        cnt+=1
        return cnt
    return inner

counters = dict()
def global_dictionary_variable_with_the_counts(fn):
    '''Function which keep tracks the how many times a function were called
    Input:
    count: initialze 
    
    '''
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner


	
# my_dict = {'add':0,'mult':0,'div':0}
# def global_dictionary_variable_with_the_counts_2(fn):
#     ''' Function which counts the different dictionary variables to
#      update different dictionaries
#      Input: 
#         fn: function to be counted
#         my_dict : dict objects to counts the fuction count values differently     
#      '''
  
#     cnt = 0
#     def inner(*args, **kwargs):
#         nonlocal cnt
#         cnt += 1
#         my_dict[fn.__name__] = cnt
#         return fn(*args, **kwargs)
#     return inner
def counter(fn, counters):
  """This function useses a closure to passdifferent dictionary variables
    to update different dictionaries.
  """

  cnt = 0
  def inner(*args, **kwargs):
    nonlocal cnt
    cnt += 1
    counters[fn.__name__] = cnt
    return fn(*args, **kwargs)
  return inner

c = dict()
m = dict()
d = dict()