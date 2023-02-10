from collections import deque
from copy import deepcopy


def create_event(a,b,c,d):
    event = {'event_id':"DEFAULT", 'node':0,'time':0, 'details':"Packet details"}
    event['event_id'] = a
    event['node'] = b
    event['time'] = c
    event['details'] = d

    return event


event_queue = deque()

e = create_event("event001",12,3,"pid is 1")
event_queue.append(deepcopy(e))
#event_queue = sorted(event_queue, key=lambda x: x['time'])
print(event_queue)
e = create_event("event002",12,5,"pid is 1")
event_queue.append(deepcopy(e))
#event_queue = sorted(event_queue, key=lambda x: x['time'])

print(event_queue)
e = create_event("event001",12,4,"pid is 1")
event_queue.append(deepcopy(e))
#event_queue = sorted(event_queue, key=lambda x: x['time'])

print(event_queue)

event_queue = sorted(event_queue, key=lambda x: x['time'])
print(event_queue)
item = event_queue.pop(0)
print(event_queue)
