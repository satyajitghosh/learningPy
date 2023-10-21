from abc import ABC,abstractmethod

class Orders(ABC):
    '''Interface or Abstract class that is used to implement classes
    that help retrieve historical orders data. Hence, the implementing
    classes must have the method getOrders()'''
    @abstractmethod
    def getOrders(self):
        pass

class RainstorOrders(Orders):
    '''Implements functionality to get data from Rainstor database.
    Must follow the pattern set out in Orders.'''
    def getOrders(self):
        print('Get Orders from Rainstor')

class IQOrders(Orders):
    '''Implements functionality to get data from IQ database.
    Must follow the pattern set out in Orders.'''
    def getOrders(self):
        print('Get Orders from IQ')

def client_code(ord:Orders):
    '''The client code receives an object of tye Orders and calls getOrders()
    The client code expects the object to have a getOrders function.'''
    ord.getOrders()


'''The application was working fine. Then came a requirement to onboard intraday orders.
The process to retrieve intraday orders war written by another team and therefore did not 
have the getOrders function which the client_code was expecting.'''

class IntradayOrders(ABC):
    @abstractmethod
    def fetchOrders():
        pass
class MongoIntradayOrders(IntradayOrders):
    def fetchOrders():
        print('Fetching orders from MongoDB.')


'''Therefore, we need to write an Adapter class that will allow us to fetch orders from an
Intraday source into the client code.'''

class IntradayOrdersAdapter(Orders):
    def __init__(self,intradaysource:IntradayOrders):
        self.intradaysource = intradaysource
    def getOrders(self):
        self.intradaysource.fetchOrders()

def client_code(ord:Orders):
    '''The client code which remains unchanged can now also retrieve Intraday Orders.'''
    ord.getOrders()

'''All we need to do is pass the appropriate object of type Orders.'''

mongoOrders = MongoIntradayOrders()
mongoadapter = IntradayOrdersAdapter(mongoOrders)
'''Note that mongoadapter is of type Orders,
because the IntradayOrdersAdapter inherits Orders,
and will therefore have the getOrders() function.'''
client_code(mongoadapter)
