from enum import Flag
import pytest
import random
import string
import session7
import os
import inspect
import re
import time

README_CONTENT_CHECK_FOR = [
    'generate_my_next_number',
    'min_count',
    'docstring',
    'fibonacci',
    'called',
    'closure',
    'global',
    'count',
    'dictioanry',
    'variable'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_function_name_had_cap_letter():
    """
    caps letter check in functions
    """
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
    
def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 550, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 25, 'You are not writing proper heading'


def test_session7_docstring_check():
    #check more then 50 char
    f1 = session7.check_doc_string_len(session7.myfibonacci)
    assert f1()==True, 'just do by character by character count'
   
    #less then 50
    f1 = session7.check_doc_string_len(test_function_name_had_cap_letter)
    assert f1()==False,'just do by character by character count'

def test_my_doc_string_outer_not_empty():
    assert session7.check_doc_string_len != "", "doc string can't be empty"

def test_my_doc_string_outer_exists():
    assert session7.check_doc_string_len.__doc__ is not None, "doc string can't be Type None"

def test_myfibonacii():
    my_list = [1,2,3,5,8,13]
    f1 = session7.myfibonacci()
    for i in my_list:
        assert i==f1(),'check for the value given in the my list for fib vaification'

def test_add():
    assert session7.add(10, 20) == 30, "inncorrect addtion of two numbers"
	
def test_mul():
    assert session7.mult(10, 20,1) == 200, "incorrect multification of three numbers"
	
def test_div():
    assert session7.div(100, 4) == 25.0, "inncorrect division of two numbers"

def test_global_dictionary_variable_with_the_counts():

    mydict_val = {'add':4,'mult':3,'div':2}
    fn =session7.add
    value = session7.global_dictionary_variable_with_the_counts(fn)
    value(2,4),value(2,4),value(2,4),value(2,4),
    
    fn = session7.mult
    value = session7.global_dictionary_variable_with_the_counts(fn)
    value(1,2,3),value(1,2,3),value(1,2,3),
    fn = session7.div
    value = session7.global_dictionary_variable_with_the_counts(fn)
    value(2,4),value(2,4)
   
    assert session7.counters==mydict_val,'just count how many times each funtion is called..'

def test_check_docs():
    assert bool(session7.check_doc_string_len.__doc__)==True,"Docstring missing"
    assert bool(session7.myfibonacci.__doc__)==True,"Docstring missing"
    assert bool(session7.add.__doc__)==True,"Docstring missing"
    assert bool(session7.mult.__doc__)==True,"Docstring missing"
    assert bool(session7.div.__doc__)==True,"Docstring missing"
    assert bool(session7.global_dictionary_variable_with_the_counts.__doc__)==True,"Docstring missing"
    # assert bool(session7.global_dictionary_variable_with_the_counts_2.__doc__)==True,"Docstring missing"

def test_closure():
    f1 = session7.myfibonacci()
    assert bool(f1.__closure__)==True, 'Closure is missing'
    f1 = session7.check_doc_string_len(session7.myfibonacci)
    assert bool(f1.__closure__)==True,'Closure is missing'
    fn = session7.add
    f1 = session7.global_dictionary_variable_with_the_counts(fn)
    assert bool(f1.__closure__)==True, 'Closure is missing'
    

def test_counter():
    c = dict()
    m = dict()
    d = dict()
    c_val, m_val, d_val = {'add':4},{'mult':3},{'div':2}
    fn = session7.add
    value =session7. counter(fn, c)
    value(1,2),value(1,2),value(1,2),value(1,2)
    fn = session7.mult
    value = session7.counter(fn, m)
    value(2,3,1),value(2,3,1),value(2,3,1)
    fn = session7.div
    value = session7.counter(fn, d)
    value(4, 2),value(4, 2)
    assert c == c_val,'just count how many times each funtion is called..'
    assert m == m_val,'just count how many times each funtion is called..'
    assert d == d_val,'just count how many times each funtion is called..'