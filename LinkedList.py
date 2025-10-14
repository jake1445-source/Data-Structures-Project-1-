class Event:
    def __init__(self, id, title, date, time, location):
        self.id = id
        self.title = title
        self.date = date
        self.time = time
        self.location = location
        self.next = None

class LinkedEvents:
    def __init__(self):
        self.head = None
        self.total = 0


    def append(self, id, title, date, time, location):
        new_event = Event(id, title, date, time, location)
        self.total +=1
        if self.head == None:
            self.head = new_event
        else:
            current_event = new_event
            event = self.head
            while event.next != None:
                event = event.next
            event.next = current_event


    def show_events(self):
        event = self.head
        while event:
            print(event.title, event.location, event.date, event.time, event.id)
            event = event.next


    def delete_event(self, attribute, value):
        delete_count = 0
        if self.head is None:
            print("No list found")
            return
        while getattr(self.head, attribute) == value:
            self.head = self.head.next
        current_event = self.head
        next_event = self.head.next
        while next_event:
            if getattr(next_event, attribute) != value:
                current_event = next_event
                next_event = next_event.next
            else:
                current_event.next = next_event.next
                next_event = next_event.next
                self.total -= 1
                delete_count += 1
        if delete_count == 0:
            print("No events deleted")
        else:
            print(f"{delete_count} events deleted with {attribute}: {value}")


    def find_event(self, attribute, value):
        match_count = 0
        if self.head is None:
            print("No list found")
            return
        event = self.head
        while event:
            if getattr(event, attribute) != value:
                event = event.next
            else:
                match_count +=1
                print(event.title, event.location, event.date, event.time, event.id)
                event = event.next
        if match_count == 0:
            print("No events found")
        else:
            print(f"{match_count} events found with {attribute}: {value}")


    def list_all(self):
        if self.head is None:
            print("No list found")
            return
        event = self.head
        while event:
            print(event.title, event.location, event.date, event.time, event.id)
            event = event.next
        print(f"All {self.total} events listed")

    def event_count(self):
        print(self.total)

    def insert_sort(self, attribute1):
        if self.head is None:
            print("No list found")
            return
        sorted_event_head = None #placeholder
        current_event = self.head

        while current_event:
            next_event = current_event.next
            if sorted_event_head == None or getattr(current_event, attribute1) < getattr(sorted_event_head, attribute1): # if current is smaller than the sorted head
                current_event.next = sorted_event_head # previous head becomes the next, point towards head
                sorted_event_head = current_event  # current is now the sorted head

            else:  # if current is larger than sorted head
                inserted_event = sorted_event_head  #start at sorted head
                while inserted_event.next and getattr(inserted_event, attribute1) < getattr(current_event, attribute1): # index through events until current
                  inserted_event = inserted_event.next  # move key through sorted while attribute is smaller, assigning next
                current_event.next = inserted_event.next # assign next to first larger attribute next
                inserted_event = current_event  #
            current_event = next_event
        self.head = sorted_event_head
        print(f"Events sorted by {attribute1}")


def generate_linked_events(n):
  '''
  Generates a list of n events. Note that this only generates dates and times, not location, ID, or title. This is because we only care       about the sorting performance, and the sorting is only based on date and time 
  
  '''
  
  import random
  

  events = LinkedEvents()
  for i in range(n):
    events.append(id = random.randint(0, 50000), title = 'title', date = f"2025-{random.randint(1,12):02d}-{random.randint(1,28):02d}", 
                  time = f"{random.randint(0,23):02d}:{random.randint(0,59):02d}", 
                  location = 'location')
  return events

def runtime(n, sort):
    import time 
    if sort == LinkedEvents.insert_sort:   
        events = generate_linked_events(n)
        begin = time.time()
        events.insert_sort('date')
        end = time.time()
        return end-begin

    elif sort == LinkedEvents.merge_sort: 
        events = generate_linked_events(n)
        begin = time.time()
        events.merge_sort('date')
        end = time.time()
        return end-begin
    else: 
        events = generate_linked_events(n)
        begin = time.time()
        events.quick_sort('date')
        end = time.time()
        return end-begin
        









    