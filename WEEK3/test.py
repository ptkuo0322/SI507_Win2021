
import sqlite3 

def print_query_result(raw_query_result):
    '''Pretty prints raw query result
    
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
Who_is_in_charge_of_the_order()


#usr_input = input("Please enter a Order Date and a Ship Country (e.g. 2012-07-04 France) or exit to quit ")
#a = usr_input[:10]
#b = usr_input[11:]

#print(a)
#print(b) elif usr_input != "exit" and usr_input[4] != "-" and usr_input[7] != "-" and usr_input[10] != " " :