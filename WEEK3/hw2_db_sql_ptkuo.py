"""
############################## Homework #2 ##############################

% Student Name: Po-Tsun Kuo

% Student Unique Name:ptkuo

% Lab Section 00X: 006 (Wed 4:00 PM (GSI Lea))

% I worked with the following classmates: Only discuss with GSI

%%% Please fill in the first 4 lines of this file with the appropriate information before submitting on Canvas.
"""

import sqlite3 

def question0():
    ''' Provided for example only.
    Constructs and executes SQL query to retrieve
    all fields from the Region table
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = "SELECT * FROM Region"
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question1():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
        SELECT Id, TerritoryDescription, RegionId FROM Territory
    """
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question2():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
        SELECT COUNT(*) FROM Employee
    """
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question3():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
        SELECT Id, ProductName, SupplierId, CategoryId, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued 
        FROM Product 
        ORDER BY Id DESC LIMIT 10
    """
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question4():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function 
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
        SELECT ProductName, UnitPrice 
        FROM Product 
        ORDER BY UnitPrice DESC LIMIT 3
    """
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question5():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
        SELECT ProductName, UnitPrice, UnitsInStock 
        FROM Product 
        WHERE UnitsInStock BETWEEN "60" and "100"
    """
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question6():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
        SELECT ProductName 
        FROM Product 
        WHERE (UnitsInStock < ReorderLevel)
    """
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question7():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
        SELECT Id 
        FROM [Order] 
        WHERE ShipCountry= "France" and ShipPostalCode LIKE "%04"
    """
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question8():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
        SELECT CompanyName, ContactName 
        FROM Customer 
        WHERE Country = "UK" and NOT(Fax = "Null")
    """
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question9():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
        SELECT ProductName, UnitPrice 
        FROM Product AS p 
            JOIN Category as cat 
            ON p.CategoryId = cat.Id 
        WHERE cat.CategoryName = "Beverages"
    """
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question10():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
        SELECT ProductName 
        FROM Product AS p 
            JOIN Category as cat 
            ON p.CategoryId = cat.Id 
        WHERE (p.Discontinued = 1 and cat.Id = 6)
    """
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question11():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    #TODO Implement function
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
        SELECT o.Id, FirstName, LastName  
        FROM [Order] AS o 
            JOIN Employee AS e 
            ON o.EmployeeId = e.Id  
        WHERE ShipCountry = "Germany"
    """
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

def question12():
    ''' Constructs and executes SQL query to retrieve
    data based on requirements
    
    Parameters
    ----------
    None
    
    Returns
    -------
    list
        a list of tuples that represent the query result
    '''
    
    #TODO Implement function
    
    connection = sqlite3.connect("Northwind_small.sqlite")
    cursor = connection.cursor()
    query = """
        SELECT [Order].Id,OrderDate, CompanyName 
        FROM [Order] JOIN Customer 
            ON [Order].CustomerId = Customer.Id WHERE OrderDate <= "2012-07-10"
    """
    result = cursor.execute(query).fetchall()
    connection.close()
    return result

#################################################################
########################  ECs start here  #######################
#################################################################

#########
## EC1 ##
#########

## f-string alignment
## syntax f'{string_we_want_to_align : >/</^number}'
## number represent the space we reserved
## >:Right aligned, <:Left Aligned, ^:middle All

def print_query_result(raw_query_result):
    ''' Pretty prints raw query result
    
    Parameters
    ----------
    list 
        a list of tuples that represent raw query result
    
    Returns
    -------
    None
    '''
    #TODO Implement function
    separate_sign = "|"
    words = ""

    for element in raw_query_result:
        for i in range(len(element)):
            if len(str(element[i])) <= 20:
                ele_word = separate_sign + f'{element[i]:^20}' #reserve 20 space for the string
            else:
                ele_word = separate_sign + f'{element[i][0:17]:^17}' + "..." 
            words += ele_word
        words = words + separate_sign+ "\n"
    return print(words)


if __name__ == "__main__":
    '''WHEN SUBMIT, UNCOMMENT THE TWO LINES OF CODE
    BELOW IF YOU COMPLETED EC1'''

    result = question12()
    print_query_result(result)


#########
## EC2 ##
#########
    
    #TODO Implement interactive program here
    
def Who_is_in_charge_of_the_order():
    usr_input = input("Please enter a Order Date and a Ship Country (e.g. 2012-07-04 France) or exit to quit ")
    if usr_input == "exit":
        return None 
    elif '-' not in usr_input or ' ' not in usr_input:
        return print("Invalid Input. Please enter a Order Date and a Ship Country seperated by space")
    elif usr_input.count("-") ==2 and usr_input.count(" ") == 1:
        if len(usr_input) > 11:
            if usr_input[4] != "-" or usr_input[7] != "-" or usr_input[10] != " ":  
                return print("Invalid Input. Please enter a Order Date and a Ship Country seperated by space")
        else:
            return print("Invalid Input. Please enter a Order Date and a Ship Country seperated by space")
    elif len(usr_input) == 0:
        return print("Invalid Input. Please enter a Order Date and a Ship Country seperated by space")
    else:
        connection = sqlite3.connect("Northwind_small.sqlite")
        cursor = connection.cursor()
        query = f'SELECT FirstName, LastName FROM [Order] AS o JOIN Employee AS e ON o.EmployeeId = e.Id WHERE  OrderDate = "{usr_input[:10]}" and ShipCountry = "{usr_input[11:]}"'
        result = cursor.execute(query).fetchall()
        connection.close()
        if bool(result) == 1:
            return print_query_result(result)
        else:
            return print("Sorry! Your search returns no results")



