 while True:

        if rating_sca not in rating_scale:
            print("invalid value! Please try again1111")
            rating_sca = input("What is the lowest rating would you like to search? sacle from 0 to 5, separate by 0.5")
        else:
            default_list[0] = rating_sca
            break
    price_sca = input("What is the lowest price range would you like to search? sacle from 0 to 5, separate by 1")
    while True:
        if price_sca not in price_scale:
            print("invalid value! Please try again2222")
            price_sca = input("What is the lowest price range would you like to search? sacle from 0 to 5, separate by 1")
        else:
            default_list[1] = price_sca
            break
    review_sca = input("What is the lowest number of revuew would you like to search? must be a integer")
    while True:
        if bool(int(review_sca.isdigit())) == False:
            print("invalid value! Please try again3333333")
            review_sca = input("What is the lowest number of revuew would you like to search? must be a integer")
        else:
            default_list[2] = review_sca
            break
    num_scl = ("How much data do you wnat?, from 1 to 20, default value = 10")
    while True:
        if num_scl not in num_scale:
            print("invalid value! Please try again44444")
            num_scl = ("How much data do you wnat?, from 1 to 20, default value = 10")
        else:
            default_list[4] = num_scl
            break     
    return default_list


print("Rating: scale from 0 to 5, separate by 0.5")
    print("Price range: sacle from 0 to 5, separate by 1")
    print("Number of Review count: at least 1, muust be integer")
    print("Data order: ASC(ascending) or DESC(descebding)")
    print("value of data: scale from 1 to 20, default value is 10")
    usr_input = input("Rating, Price_range, Number_of_Review, Data_order, Number_of_data, please separate by ,")
    parsed_list = usr_input.strip(" ").split(",")
    for idx in range(len(parsed_list)):
        if parsed_list
