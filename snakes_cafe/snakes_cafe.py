print("""
    python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

menu=["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears"]
menu_count=[0,0,0,0,0,0,0,0,0,0,0,0,0]
order=input('enter your order ').lower()
newarr=[]
[newarr.append(element.lower()) for element in menu]

def ordering(menu_count,order,menu):
 while order!="quit":
    
  if order in newarr:
      menu_count[newarr.index(order)]+=1
      print(f"{menu_count[newarr.index(order)]} order of {menu[newarr.index(order)]} have been added to your meal ")
  else:
      print("Please Choose Something From The Menu ")
  order=input('enter your order ').lower()

 for i in range(len(menu_count)):
    if menu_count[i]!=0:
     print (f"{menu[i]}:{menu_count[i]} ")

ordering(menu_count,order,menu)



