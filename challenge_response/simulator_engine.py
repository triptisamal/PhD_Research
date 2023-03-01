from collections import deque
from copy import deepcopy
import sys

import globalvars
from challenge_response import *



def create_event(eventid,nodeid,timeofevent):
    event = {'event_id':"DEFAULT", 'node':0,'time':0, 'details':"Packet details"}
    event['event_id'] = eventid
    event['node'] = nodeid
    event['time'] = timeofevent
   # event['details'] = packetdetails

    return event

def node_handler(node_id,action):


    if action == "SEND_POSITION-CLAIM":
        print("Event is position-claim.")
        #This is the first node, src
        print("Source ",node_id," is creating the packet for position claim at",globalvars.now, "seconds." )
       # update_packet(action,loc)
        #pid is incremented the only after a source creates a packet
        #in the next round of petal routing, this new pid will be used
    #    globalvars.pid += 1
       # if globalvars.packet_reached_dest == 0:
        #    globalvars.broadcast += 1
        event_id = "CLAIM_%03d" % (globalvars.idn)
        globalvars.idn += 1

        e = create_event(event_id,node_id,globalvars.now)
        globalvars.event_queue.append(deepcopy(e))

        #sort queue according to the simulated real time (time of event happening)
        globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])




def process_event(e):

    if "CLAIM" in e['event_id']:
        print("claim");

def main():
    '''Simulation engine'''
    
    #parse arguments
    if len(sys.argv) < 2:
        print("Usage: simulator_engine.py <number of nodes>")
        sys.exit();
    
    globalvars.init()
    globalvars.number_of_nodes = int(sys.argv[1])
    #print("Number of nodes = ", globalvars.number_of_nodes)

    #create map maintained by the simulator
    #used to check if the flashlight is on or off
    create_sim_map();

    #add first event to the event_queue
    node_handler(1,"SEND_POSITION-CLAIM");
    print(*globalvars.event_queue,sep="\n")
    #process event queue
    while globalvars.event_queue:
        item = globalvars.event_queue.pop(0)
        print("\nEvent occuring: ",item)
        process_event(item)
        print("\nEVENT QUEUE:\n")
        print("-----------------")
        print(*globalvars.event_queue,sep="\n")







if __name__=="__main__":
    main()
