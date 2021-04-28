import time

def search_condition():
    instruction = '''What kind of filtering condition would you like?
    1. filtered by Rating first and ordered by ReviewCount.
    2. filtered by Rating first and ordered by Price.
    3. filtered by ReviewCount first and ordered by Rating.
    4. filtered by ReviewCount first and ordered by Price.
    5. filtered by Price first and ordered by Rating.
    6. filtered by Price first and ordered by ReviewCount.
    '''
    option_list = ['1','2','3','4','5','6']
    rating_list = ["0", '0.5','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0']
    price_list = ["0", '1','2','3','4','5']
    while True:
        print(instruction)
        usr_input = input("what's your choice? from 1 to 6 ")
        if usr_input in option_list:
            if usr_input == "1":
                query_list = ["R.Rating", "R.ReviewCount"]
                print("Rating range:", rating_list)
                usr_input2 =input("Enter the number, please! ")
                if usr_input2 in rating_list:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")
            elif usr_input == "2":
                query_list = ["R.Rating", "R.Price"]
                print("Rating range:", rating_list)
                usr_input2 =input("Enter the number, please! ")
                if usr_input2 in rating_list:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")
            elif usr_input == "3":
                query_list = ["R.ReviewCount", "R.Rating"]
                print("ReviewCount range: at least 1")
                usr_input2 =input("Enter the number, please! ")
                if bool(int(usr_input2))==True and int(usr_input2) > 0:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")

            elif usr_input == "4":
                query_list = ["R.ReviewCount", "R.Price"]
                print("ReviewCount range: at least 1")
                usr_input2 =input("Enter the number, please! ")
                if bool(int(usr_input2))==True and int(usr_input2) > 0:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")

            elif usr_input == "5":
                query_list = ["R.Price", "R.Rating"]
                print("Price range:", price_list)
                usr_input2 =input("Enter the number, please! ")
                if usr_input2 in price_list:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")
            elif usr_input == "6":
                query_list = ["R.Price", "R.ReviewCount"]
                print("Price range:", price_list)
                usr_input2 =input("Enter the number, please! ")
                if usr_input2 in price_list:
                    query_list.append(usr_input2)
                    break
                else:
                    print("invalid input!, please try again!")
        else:
            print("invalid input!, please try again!")
    return query_list

def search_order():
    instruction = '''which order would you like?
    1, in ascending order.
    2, in descending order.
    '''
    option_list = ['1','2']
    print(instruction)
    while True:
        usr_input = input("what's your choice? from 1 to 2 ")
        if usr_input in option_list:
            if usr_input == "1":
                query_word = "ASC"
                break
            elif usr_input == "2":
                query_word = "DESC"
                break
        else:
            print("invalid input!, please try again!")
    return query_word

def search_number():
    instruction = '''How many data do you want to search?
    ranging for 1 to 20
    '''
    print(instruction)
    option_list  = ["1",'2','3','4','5','6','7','8','9','10','11',"12",'13','14','15','16','17','18','19','20']
    while True:
        usr_input = input("what's your choice? from 1 to 20 ")
        if usr_input in option_list:       
            query_word = usr_input
            break
        else:
            print("invalid input!, please try again!")
    return query_word

def sql_query():
    query_string1 = '''SELECT F.RestaurantName, F.PhoneNumber, F.Rating, F.ReviewCount, F.Price FROM FOOD_RESULT 
    AS F JOIN RESTAURANT_RESULT AS R  ON F.RefId = R.RefId 
    '''
    init_list = search_condition()
    b_word = search_order()
    c_word = search_number()
    init_list.append(b_word) 
    init_list.append(c_word) 
    query_string2 = f'WHERE {init_list[0]} > {init_list[2]} ORDER BY {init_list[1]} {init_list[3]} LIMIT {init_list[4]}'
    
    return query_string1 + query_string2

    search_cond = ["Rating", "ReviewCount", "Price"]
    while True:
        usr_answer1 = input("w")



def decide_sql_query():
    rating_scale  = ["0", '0.5','1.0','1.5','2.0','2.5','3.0','3.5','4.0','4.5','5.0']
    price_scale  = ["0", '1','2','3','4','5']
    order_scale  = ["ASC", "DESC"]
    num_scale = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    default_list = ['A','B','C','DESC','10']
    

SELECT F.RestaurantName, F.PhoneNumber, F.Rating, F.ReviewCount, F.Price FROM FOOD_RESULT AS F JOIN RESTAURANT_RESULT AS R  ON F.RefId = R.RefId 
WHERE R.Rating > 4.0 ORDER BY R. ReviewCount DESC LIMIT 15
print(decide_sql_query())