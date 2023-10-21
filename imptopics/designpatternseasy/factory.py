#https://github.com/satyajitghosh/learningPy/blob/main/imptopics/designpatterns/factorypattern

'''Explained well here.
The main point here is to separate the creation of the object from the usage.
Essentially there will be logical classes that implement the logic.
In addiional there will be factory classes that create and return objects of the relevant logical classes
based on certain logic.
The returned objects from the factory classes are used.
Essetially, the factory class contains the logic to decide which class will be appropriate
for the given situation and then creates an object and returns the object.
'''