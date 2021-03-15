import json


with open("HW4_dict.json", "r") as fin:
    thisDict = json.load(fin)
#print(thisDict["Holc_Grade"])


#step 6

def mean_income(grade_category):
    Total_income =0
    num_of_grade=0
    total_num_of_income_data=0
    for grade in thisDict["Holc_Grade"]:
        
        if grade == grade_category:
            income = thisDict["median_income"][num_of_grade]
            for j in income:
                if int(j) > 0:
                    Total_income +=int(j)
                    total_num_of_income_data+=1
        num_of_grade+=1
    mean_income = Total_income/total_num_of_income_data
    return mean_income

def median_income(grade_category):
    list_income = []
    num_of_grade = 0
    total_num_of_income_data = 0
    for grade in thisDict["Holc_Grade"]:
            if grade == grade_category:
                income = thisDict["median_income"][num_of_grade]
                for j in income:
                    if int(j) > 0:
                        list_income.append(int(j))
                        total_num_of_income_data+=1
            num_of_grade +=1
    
    list_income.sort()
    print(list_income)
    if total_num_of_income_data % 2 == 0:
        medain_income = 0.5*float((int(list_income[total_num_of_income_data//2]) + int(list_income[1+(total_num_of_income_data//2)])))
    else:
        medain_income = list_income[total_num_of_income_data//2]
    
    return medain_income


#A_mean_income = mean_income("A")
#B_mean_income = mean_income("B")
#C_mean_income = mean_income("C")
#D_mean_income = mean_income("D")

A_median_income = median_income("A")
#B_median_income = median_income("B")
#C_median_income = median_income("C")
#D_median_income = median_income("D")

'''
print(A_mean_income)
print(A_median_income)
print(B_mean_income)
print(B_median_income)
print(C_mean_income)
print(C_median_income)
print(D_mean_income)
print(D_median_income)
'''

print(thisDict['median_income'][25])
print(thisDict['median_income'][225])
#       self.assertTrue(thisDict['median_income'][25]=='127634')

#       self.assertTrue(thisDict['median_income'][225]=='23558')
Alist = thisDict["median_income"][0:15]
print(Alist.sort())
'''

Alist.sort()
print(Alist)
y = 0
for x in Blist:
    y = y + x
print(y/15)
'''