import json
import math
import pandas as pd
df=pd.read_excel("mess_student/Mess_Menu_16_th-30th_nov_23.xlsx",engine="openpyxl")
#df=df.dropna().reset_index(drop=False) #to remove empty cells
def get_index(name,column):
    
    for index,x in column.items():
        
        if x==name:
            return index
  
d2=df['FRIDAY']
#print(d2)
last_row=len(d2)
 #to remove empty cells

#print(last_row)
#print(get_index('LUNCH',d2))
#print(get_index('DINNER',d2))
#to  check if value is a food item
def check_valid(value):
    if  value[0]=='*' or value=="NO EGG" or len(value)<1 :
        return False
    return True

breakfast_indexs=[get_index('BREAKFAST',d2)+1,get_index('LUNCH',d2)-2]
lunch_indexs=[get_index('LUNCH',d2)+1,get_index('DINNER',d2)-2]
dinner_indexs=[get_index('DINNER',d2)+1,last_row-1]
#print(lunch_indexs)


final_dict=dict()
def todict(df):
    
    
    for index,column in df.items():
        date=column[0].date()

        breakfast_items=[]
        lunch_items=[]
        dinner_items=[]
        for i in range(breakfast_indexs[0],breakfast_indexs[1]+1):
                    if(check_valid(str(column[i]))):
                        breakfast_items.append(column[i])
        for i in range(lunch_indexs[0],lunch_indexs[1]+1):
                if(check_valid(str(column[i]))):    
                   lunch_items.append(str(column[i]))

        for i in range(dinner_indexs[0],dinner_indexs[1]+1):
                if(check_valid(str(column[i]))):
                    dinner_items.append(column[i])

        final_dict[str(date)]={"BREAKFAST":breakfast_items,"LUNCH":lunch_items,"DINNER":dinner_items}
    return final_dict
    
#final_dict=todict(df)
#print(final_dict)
#with open('mess_menu.json','w',encoding='utf-8') as menu:
   # json.dump(final_dict,menu,ensure_ascii=False,indent=4)
    
 



    

            









