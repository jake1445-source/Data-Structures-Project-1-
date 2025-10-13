# define class 

class Events_List: 

    '''Array based list of event details 

    This class allows the user to create a list of events. Each element in the array is a dictionary 
    ----------------------------------
    Functions: 

    insert: insert an event at the end of the list 
    
    delete: Delete the event based on the ID 
    
    search_by_id: Returns event dictionary with matching id 

    list_all: Returns a copy of all events 

    
    '''
    # initialize array of event dictionaries 
    def __init__(self):
        self.data = []

    # Insert function
    def insert(self, event):
        self.data.append(event)

    # Delete 
    def delete(self, event_id):
        for i in range(len(self.data)): 
            if self.data[i]["id"] == event_id: 
                del self.data[i]
                return print(f'Event {event_id} deleted.')
        return print('Event not found, delete unsuccessful.')

    # Search for an event 
    def search_by_id(self, event_id): 

        for i in self.data: 
            if i['id'] == event_id:
                return i 

        return 'Event not found'
        
    # List all events 
    def list_all(self): 
        return self.data



'''Sorting Algorithms
-------------------------------------------------
Below are the sorting algorithms. These are to be called as any other method of the class, and will re-define the event
array to be the sorted list. 

Algorithms: 

1. insertion_sort
2. merge_sort 
3. quick_sort 

'''

def insertion_sort(events, sort_by1, sort_by2=None):
    '''Parameters: 
    
    sort_by1 (str): Name of the dictionary key by which the list is to be sorted. To sort by date, 
                    call insertion_sort(events, 'date')
    sort_by2 (str): Default None, secondary sorting parameter to sort by time of day. Call 
                    insertion_sort(events, 'date', 'time')

    '''
    
    for i in range(1, len(events)):
        key = events[i]
        j = i - 1

        while j >= 0 and (events[j][sort_by1], events[j][sort_by2]) > (key[sort_by1], key[sort_by2]):
            events[j + 1] = events[j]
            j -= 1

        events[j + 1] = key

    return events



# Merge sort
def merge_sort(events, sort_by1, sort_by2):
    '''
    Note: When calling this function with an instance of the Events_List class, events parameter 
          must be events.data

    Parameters: 
        events: events.data 
        sort_by1 (str): Name of the dictionary key by which the list is to be sorted. To sort by date, 
                    call insertion_sort(events, 'date')
        sort_by2 (str): Default None, secondary sorting parameter to sort by time of day. Call 
                    insertion_sort(events, 'date', 'time') 
    
    '''
    #splits events into individual arrays each with length 1.
    if len(events)>1:
      mid = len(events) // 2
      left = events[:mid]
      right = events[mid:]

      left_sorted = merge_sort(left,sort_by1,sort_by2)
      right_sorted = merge_sort(right,sort_by1,sort_by2)

      i = j = k = 0

      #compare each array and place back into events
      while i < len(left) and j < len(right):
        if (left[i][sort_by1],left[i][sort_by2]) <=(right[j][sort_by1],right[j][sort_by2]):
          events[k]=left[i]
          i+=1

        else:
          events[k]=right[j]
          j+=1

        k+=1

      while i < len(left):
        events[k]=left[i]
        i+=1
        k+=1

      while j < len(right):
        events[k]=right[j]
        j+=1
        k+=1

    return events

# #Quick Sort

def quick_sort(events, sort_by1, sort_by2):
  
  def partition(events,low,high):

    pivot = (events[high][sort_by1],events[high].get(sort_by2,""))
    i = low -1
    for j in range(low,high):
      current = (events[j][sort_by1],events[j].get(sort_by2,""))
      if current <=pivot:
        i +=1
        events[i],events[j] = events[j],events[i]

    (events[i+1],events[high]) = (events[high],events[i+1])
    return i+1


  def _quick_sort(events,low,high):
    if low < high:
      new = partition(events,low,high)
      _quick_sort(events,low,new-1)
      _quick_sort(events,new+1,high)

  _quick_sort(events,0,len(events)-1)
  return events




'''
Time Testing 
-------------------------------------
Contains code to populate the list of events, and test the time elapsed for various sorting algorithms 

'''

#Generate n events:

def generate_events(n):
  '''
  Generates a list of n events. Note that this only generates dates and times, not location, ID, or title. This is because we only care       about the sorting performance, and the sorting is only based on date and time 
  
  '''
  
  import random
  

  events = Events_List()
  for i in range(n):
    events.insert({"date": f"2025-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
                   "time": f"{random.randint(0,23):02d}:{random.randint(0,59):02d}"})
  return events



#Test runtime - Insertion:

def runtime(n, sort):
  import time 
    
  events = generate_events(n)
  begin = time.time()
  sort(events.data,'date','time')
  end = time.time()
  return end-begin



