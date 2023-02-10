from collections import deque
from copy import deepcopy
from petal import *
import globalvars
import re
import sys

def update_packet(action,loc):
    '''This method is for creating a packet. It is called by each source node'''

    if action == "INITIATE_BROADCAST":
        globalvars.packet['tLoc'] = loc #intermediate node
        globalvars.packet['myLoc'] = loc #intermediate node

    if action == "INITIATE_TRANSMISSION":
        globalvars.packet['tLoc'] = loc #source node
        globalvars.packet['myLoc'] = loc #source node, that broadcast the packet
    
    if action == "INITIATE_RECEIVE":
        #whoever received, myLoc would change, but transmitter location would not
        globalvars.packet['myLoc'] = loc #receiver, that received the packet

    
    globalvars.packet['eccentricity'] = globalvars.e
    if globalvars.zone == 1 and action == "INITIATE_RECEIVE":
        globalvars.packet['zoneType'] = "MULTI"
        globalvars.packet['sLoc'] = loc



def create_event(eventid,nodeid,timeofevent,packetdetails):
    event = {'event_id':"DEFAULT", 'node':0,'time':0, 'details':"Packet details"}
    event['event_id'] = eventid
    event['node'] = nodeid
    event['time'] = timeofevent
    event['details'] = packetdetails

    return event


def node_handler(node_id, action,e):
    '''This handles everything that a node is supposed to do:
        1. Find if it is inside a petal
        2. Calculate the back off time
        3. Adds future events that should be triggered from an action
        4. Deletes future events, if encounters a transmission from another node that is closer to the source-destination line
        
        Input(s): Node ID (because this is a common handler for all nodes)
        action: what the node is supposed to do at first
        NOTE: memory for each node will be separate, maintained by the simulator'''

    loc = (0,0,0)
    #find the location of the node corresponding to node_id
    for i in range(globalvars.number_of_nodes):
        if globalvars.node[i]['nodeID'] == node_id:
            loc = globalvars.node[i]['loc']
    

    if action == "INITIATE_TRANSMISSION":
        #This is the first node, src
        print("Source ",node_id," is creating the packet, ", globalvars.packet['pID']," at",globalvars.now, "seconds." )
        update_packet(action,loc)
        #pid is incremented the only after a source creates a packet
        #in the next round of petal routing, this new pid will be used
        globalvars.pid += 1
        event_id = "BROADCAST_%03d" % (globalvars.idn)
        globalvars.idn += 1

        e = create_event(event_id,node_id,globalvars.now,globalvars.packet)
        globalvars.event_queue.append(deepcopy(e))

        #sort queue according to the simulated real time (time of event happening)
        globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])


        #Update state vector of the source
        for i in range(globalvars.number_of_nodes):
            if globalvars.state_vector[i]['node_id'] == node_id:
                globalvars.state_vector[i]['pid'] = globalvars.packet['pID']
                globalvars.state_vector[i]['packet_seen'] = 1
                globalvars.state_vector[i]['transmitted'] = 1 #source is transmittn=ing
                globalvars.state_vector[i]['time_of_state_update'] = globalvars.now
                break
        
        #Read adjacency list and create receive events
        for s, nbrs in globalvars.G.adjacency():
            if s == node_id:
                for t, data in nbrs.items():
                    event_id = "RECEIVE_%03d" % (globalvars.idn)
                    globalvars.idn += 1
                    
                    receiverloc = (0,0,0)
                    #find the location of the node corresponding that is receiving this packet
                    for i in range(globalvars.number_of_nodes):
                        if globalvars.node[i]['nodeID'] == t:
                            receiverloc = globalvars.node[i]['loc']
                            break
                    #update_packet(action,receiverloc)#TODO check
                    dist = distance(s, t)
                    #convert distance to m
                    dist = 0.3048*dist
                    propagation_delay = dist/globalvars.speed
                    time = globalvars.transmission_delay + propagation_delay 
                    globalvars.now = globalvars.now + time
                    
                    #s['node'] is the node id where event receive is happening, is it is "t" here
                    e = create_event(event_id,t,globalvars.now,globalvars.packet)
                    globalvars.event_queue.append(deepcopy(e))
                    globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])

    

    if action == "START_BACKOFF":
        
        #check if the node is inside petal or not
        inside = insideOrNot(loc)
        #inside = insideOrNot(e['details']['myLoc'])
        if inside == 1:
            globalvars.node[node_id]['packet'] += 1
            #it is inside the petal
            print("it is inside petal")

            ##backoff timer start 
            bofftime = calculate_backoff(loc)
            #bofftime = calculate_backoff(e['details']['myLoc'])
            print("Back off time =",bofftime, "seconds")
            globalvars.now = globalvars.now + bofftime
            event_id = "BACKOFFTIMEREXPIRY_%03d" % (globalvars.idn)
            globalvars.idn += 1

            e = create_event(event_id,node_id,globalvars.now,globalvars.packet)
            globalvars.event_queue.append(deepcopy(e))
            globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])

        else:
            print("it is outside petal")



    if action == "INITIATE_BROADCAST":

        print("checking for broadcast")
        print("node id is ",node_id)
        print("state is:")
        for i in range(globalvars.number_of_nodes):
            if globalvars.state_vector[i]['node_id'] == node_id:
                print("PID: ",globalvars.state_vector[i]['pid'])
                print("packet seen? ",globalvars.state_vector[i]['packet_seen'])
                print("transmitted? ",globalvars.state_vector[i]['transmitted'])
                print("receive_count: ",globalvars.state_vector[i]['receive_count'])
                print("received_from_location: ",globalvars.state_vector[i]['received_from_location'])
                print("time of state update: ",globalvars.state_vector[i]['time_of_state_update'])


        #check the receive count
        for i in range(globalvars.number_of_nodes):
            if globalvars.state_vector[i]['node_id'] == node_id:
                if globalvars.state_vector[i]['transmitted'] == 0: #transmission is pending
                    if globalvars.protocol == 1:#if petal protocol
                        print("receive count is ",globalvars.state_vector[i]['receive_count'])
                        if globalvars.state_vector[i]['receive_count'] > 1:
                            centroid = find_centroid(globalvars.state_vector[i]['received_from_location'])
                            ret = compare_distance_to_destination(centroid,loc,globalvars.packet['dLoc'])
                            if ret == 1:
                            #my distance is closer to destination
                            #if globalvars.state_vector[i]['receive_count'] <= 2:
                                globalvars.state_vector[i]['transmitted'] = 1 #it should be transmitted
                                globalvars.state_vector[i]['time_of_state_update'] = globalvars.now
                                


                                print("Initializing broadcast")
                                #Everytime a packet is broadcast, it should be updated with tLoc (of the node broadcasting), myLoc (of the node broadcasting), 
                                update_packet(action,loc)


                                globalvars.broadcast += 1
                                event_id = "BROADCAST_%03d" % (globalvars.idn)
                                globalvars.idn += 1
                                e = create_event(event_id,node_id,globalvars.now,globalvars.packet)
                                globalvars.event_queue.append(deepcopy(e))
                                globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])
                            else:
                                print("My distance is farther away from destination")
                               # print("receive count is ",globalvars.state_vector[i]['receive_count'])
                        if globalvars.state_vector[i]['receive_count'] <= 1:
                            globalvars.state_vector[i]['transmitted'] = 1 #it should be transmitted
                            globalvars.state_vector[i]['time_of_state_update'] = globalvars.now
                                
                            print("Initializing broadcast")
                            update_packet(action,loc)
                            globalvars.broadcast += 1
                            event_id = "BROADCAST_%03d" % (globalvars.idn)
                            globalvars.idn += 1
                            e = create_event(event_id,node_id,globalvars.now,globalvars.packet)
                            globalvars.event_queue.append(deepcopy(e))
                            globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])


                    if globalvars.protocol == 0:
                        #if flooding
                        globalvars.state_vector[i]['transmitted'] = 1 #it should be transmitted
                        globalvars.state_vector[i]['time_of_state_update'] = globalvars.now
        
                        print("Initializing broadcast")
                        globalvars.broadcast += 1
                        event_id = "BROADCAST_%03d" % (globalvars.idn)
                        globalvars.idn += 1
                        e = create_event(event_id,node_id,globalvars.now,globalvars.packet)
                        globalvars.event_queue.append(deepcopy(e))
                        globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])
                break


    if action == "INITIATE_RECEIVE":

        #update petal if multi zone
        #if yes, update source node as own location, recalculate the petal
        if globalvars.zone == 1:
            #for s in range(globalvars.number_of_nodes):
            #    if globalvars.node[s]['loc'] == loc:
            #        globalvars.focus1_key = s
            #        #whoever is broadcasting will be the new source (NOT the ones that are receiving
            #        break
            globalvars.focus1_key = node_id
            print("Now the source for new petal is ",node_id)
            initiate_petal_parameters()
        ##Look for all neighboring nodes and add events for receive
        #Read adjacency list and create receive events
        for s, nbrs in globalvars.G.adjacency():
            if s == node_id:
                for t, data in nbrs.items():
                    event_id = "RECEIVE_%03d" % (globalvars.idn)
                    globalvars.idn += 1
                    
                    receiverloc = (0,0,0)
                    #find the location of the node corresponding that is receiving this packet
                    for i in range(globalvars.number_of_nodes):
                        if globalvars.node[i]['nodeID'] == t:
                            receiverloc = globalvars.node[i]['loc']
                            break
                    update_packet(action,receiverloc)
                    dist = distance(s, t)
                    print("DISTANCE = ", dist)
                    #convert distance to m
                    dist = 0.3048*dist
                    propagation_delay = dist/globalvars.speed
                    time = globalvars.transmission_delay + propagation_delay 
                    globalvars.now = globalvars.now + time
                    e = create_event(event_id,t,globalvars.now,globalvars.packet)
                    globalvars.event_queue.append(deepcopy(e))
                    globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])




def process_event(e):
    '''Checks what type of event is extracted, and what node initiated it
    Call node_handler for that node'''


    print("In PROCESS EVENT: ", e)


    if "RECEIVE" in e['event_id']:
        print("it is a receive event")
        
        initiate_backoff_or_broadcast = 0
        
        ##it is receive event, so add a future broadcast event
        ##whoever received will create the broadcast event
        
        ## find the node id of the node where the receive happened (the same will broadcast if inside petal)
        node_id = e['node']


        #Check if already transmitted
        for i in range(globalvars.number_of_nodes):
            if globalvars.state_vector[i]['node_id'] == node_id:
                if globalvars.state_vector[i]['transmitted'] == 1: #transmission already done once
                    print("Already transmitted this packet once")
                    break
                else:
                    initiate_backoff_or_broadcast = 1
                    break

        if initiate_backoff_or_broadcast == 1:
            initiate_backoff_or_broadcast = 0
            #update state vector of the pid at receiver
            globalvars.state_vector[i]['pid'] = globalvars.packet['pID']
            globalvars.state_vector[i]['packet_seen'] = 1
            globalvars.state_vector[i]['transmitted'] = 0 #transmission is pending
            globalvars.state_vector[i]['receive_count'] += 1
            globalvars.state_vector[i]['received_from_location'].append(globalvars.packet['tLoc'])
            globalvars.state_vector[i]['time_of_state_update'] = globalvars.now
            #print state
            for i in range(globalvars.number_of_nodes):
                if globalvars.state_vector[i]['node_id'] == node_id:
                    print("node id: ",globalvars.state_vector[i]['node_id'])
                    print("PID: ",globalvars.state_vector[i]['pid'])
                    print("packet seen? ",globalvars.state_vector[i]['packet_seen'])
                    print("transmitted? ",globalvars.state_vector[i]['transmitted'])
                    print("receive_count: ",globalvars.state_vector[i]['receive_count'])
                    print("time of state update: ",globalvars.state_vector[i]['time_of_state_update'])


            #find destination id
            for j in range(globalvars.number_of_nodes):
                if globalvars.node[j]['loc'] == globalvars.packet['dLoc']:
                    dest_id = globalvars.node[j]['nodeID']
                    break
            #start back off timer for future broadcast only if the receiver is not destination
            #if node_id != dest_id and globalvars.node[node_id]['packet'] == 0:
            if node_id != dest_id:
                if globalvars.protocol == 1:
                    node_handler(node_id,"START_BACKOFF",e)
                if globalvars.protocol == 0:
                    #if it is flooding, then directly broadcast
                    node_handler(node_id,"INITIATE_BROADCAST",e)
            else:
                print("THE PACKET REACHED DESTINATION")
                globalvars.copies_delivered += 1



    if "BROADCAST" in e['event_id']:
        print("it is a broadcast event")
        
        node_id = e['node']
        print(node_id)
        node_handler(node_id,"INITIATE_RECEIVE",e)

    
    if "BACKOFF" in e['event_id']:
        print("it is a back off timer expiry event")
        node_id = e['node']
        node_handler(node_id,"INITIATE_BROADCAST",e)
         

def main():
    
    '''Simulation engine'''
    
    #parse arguments
    if len(sys.argv) < 6:
        print("Usage: simulator_drone.py <protocol number> <number of nodes> <eccentricity> <topology> <zone>")
        print("Protocol numbers:")
        print("Flooding: 0")
        print("Petal: 1")
        print("0.1>=eccentricity<=0.9")
        print("Topology:")
        print("Lattice: 0")
        print("Perturbed lattice: 1")
        print("Single Zone: 0")
        print("Multi zone: 1")
        sys.exit();
    
    globalvars.init()
    globalvars.number_of_nodes = int(sys.argv[2])
    globalvars.e = float(sys.argv[3])
    globalvars.topology = float(sys.argv[4])
    globalvars.zone = float(sys.argv[5])
    #run = int(sys.argv[6])
    print("Number of nodes = ", globalvars.number_of_nodes)
    create_drones_network()
    initiate_source_destination()
   
    globalvars.protocol = int(sys.argv[1])

    #running = 0

   # while running < run:
       # if running >=50:
   #         globalvars.protocol = 0
         #   globalvars.zone = 1

    #print("SIMULATION RUN",running)
    print("EVENTS")
    print("-------")
    globalvars.event_queue = deque()
    

    #find the node ID of src and send to node handler
    src = 0
    for i in range(globalvars.number_of_nodes):
        if globalvars.node[i]['loc'] == (globalvars.pos[globalvars.focus1_key][0], globalvars.pos[globalvars.focus1_key][1], globalvars.pos[globalvars.focus1_key][2]):
            src = globalvars.node[i]['nodeID'] = i
            print("Source node ID: ",src)
            break
    for i in range(globalvars.number_of_nodes):
        if globalvars.node[i]['loc'] == (globalvars.pos[globalvars.focus2_key][0], globalvars.pos[globalvars.focus2_key][1], globalvars.pos[globalvars.focus2_key][2]):
            des = globalvars.node[i]['nodeID'] = i
            print("Destination node ID: ",des)
            break
    
    #define data structure for state for the packet id for each node
    globalvars.state_vector = [{'pid':0, 'node_id':i, 'packet_seen':0,'transmitted':0,'receive_count':0,'received_from_location':[],'time_of_update':0} for i in range(globalvars.number_of_nodes)]

    node_handler(src,"INITIATE_TRANSMISSION",0)
    print("\nEVENT QUEUE:\n")
    print("-----------------")
    print(*globalvars.event_queue,sep="\n")
    
    while globalvars.event_queue:
        item = globalvars.event_queue.pop(0)
        print("\nEvent occuring: ",item)
        process_event(item)
        print("\nEVENT QUEUE:\n")
        print("-----------------")
        print(*globalvars.event_queue,sep="\n")

    print("Total number of nodes = ",globalvars.number_of_nodes)
    print("Total number of broadcasts = ",globalvars.broadcast)
    print("Copy Delivery Ratio = ",globalvars.copies_delivered)

    original_stdout = sys.stdout
    if globalvars.protocol == 1:
        petal_numberofnodes = "petal_numberofnodes_%d_%f.c" % (int(sys.argv[2]),globalvars.e)
        petal_numberofbcast = "petal_numberofbcast_%d_%f_%d.c" % (int(sys.argv[2]),globalvars.e,globalvars.zone)
        petal_copies = "petal_copies_%d_%f_%d.c" % (int(sys.argv[2]),globalvars.e,globalvars.zone)
        with open(petal_numberofbcast,'a') as f:
            sys.stdout = f
            if globalvars.broadcast != 0:
                print(globalvars.broadcast,",")
        with open(petal_copies,'a') as f1:
            sys.stdout = f1
            if globalvars.broadcast != 0:
                print(globalvars.copies_delivered,",")
        with open(petal_numberofnodes,'a') as f2:
            sys.stdout = f2
            print(globalvars.number_of_nodes)
    
    


    if globalvars.protocol == 0:
        petal_numberofnodes = "flood_numberofnodes_%d.c" % (int(sys.argv[2]))
        flood_numberofbcast = "flood_numberofbcast_%d.c" % (int(sys.argv[2]))
        flood_copies = "flood_copies_%d.c" % (int(sys.argv[2]))
        with open(flood_numberofbcast,'a') as f:
            sys.stdout = f
            if globalvars.broadcast != 0:
                print(globalvars.broadcast,",")
        with open(flood_copies,'a') as f1:
            sys.stdout = f1
            print(globalvars.copies_delivered,",")
        with open(petal_numberofnodes,'a') as f2:
            sys.stdout = f2
            print(globalvars.number_of_nodes)


    sys.stdout = original_stdout
   # globalvars.broadcast = 0
   # globalvars.copies_delivered = 0
   # running +=1 


if __name__=="__main__":
    main()
