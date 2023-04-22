# take a look at the process_tickets function - it has a lot to do.
# It has to check the strategy and reorder the list, and then process tickets accordingly.
# That's low cohesion.
# Also, if we have to add a new ordering strategy, the function will grow further.
# That's high coupling.
# Also, the processing part of the code should not ideally know 
# what exactly goes behing ordering tickets.


import string
import random
from typing import List
from abc import ABC,abstractmethod

def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self,list:List[SupportTicket])->List[SupportTicket]:
        pass

class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self,list:List[SupportTicket])->List[SupportTicket]:
        return list
    
class LIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self,list:List[SupportTicket])->List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy

class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self,list:List[SupportTicket])->List[SupportTicket]:
        list_copy = list.copy()
        return random.shuffle(list_copy)

class BlackHoleOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self,list:List[SupportTicket])->List[SupportTicket]:
        return []
    
class CustomerSupport:

    def __init__(self, processing_strategy: str = "fifo"):
        self.tickets = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self,ticket_ordering_strategy:TicketOrderingStrategy):
        # if it's empty, don't do anything

        tickets_list = ticket_ordering_strategy.create_ordering(self.tickets)

        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!")
            return

        for ticket in tickets_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = CustomerSupport()

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets(LIFOOrderingStrategy())