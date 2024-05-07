#Summary:
#OOP in Python allows developers to model real-world concepts and entities using classes and objects,encapsulate data, reuse code through inheritance, and write more flexible code through polymorphism.


#Example of Object oriented Program:
 
# RailwayForm   ---> Class [blueprint]
# harry --> harry ki info wala form --> Object [entity]
# tom --> tom ki info wala form --> Object [entity]
# shubham -- shubham ki info wala form --> Object [entity]

class RailwayForm:

    def name1(self):
        name = "Ritesh"
        surname="Pathak"
        age = 20
        print(name,surname,age)
    def name2(self):
        name = "Shubham"
        surname="Pathak"
        age = 20
        print(name,surname,age)

obj1 = RailwayForm()
obj1.name1() 
obj1.name2() 