#Coffee Beverage with milk

coffee_mug = """
      (  )   (   )  
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ /
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    /
\_____________________/
"""
Espresso_drinks={"Espresso":1.68,"Espresso_Macchiato":3.24,"Espresso_Con_Panna":1.05,"Caffe_Americano":3.75,"Cappucino":4.20,"Latte_Macchiato":5.85}
Mocha_Beverages={"Caffe_Mocha":4.90,"White_Chocolate_Mocha":5.45}
Iced_Coffees_Cold={"Iced_Caffe_Latte":3.38,"Iced_Caffe_Mocha":4.90,"Iced_Caramel_Macchiato":5.10,"Iced_Caffe_Americano":3.75}
Frappuccino={"Caramel_Waffle_Creme":5.95,"Toffee_Nut":5.95}

final_menu={}
final_menu.update(Espresso_drinks)
final_menu.update(Mocha_Beverages)
final_menu.update(Iced_Coffees_Cold)
final_menu.update(Frappuccino)
#print(final_menu)



