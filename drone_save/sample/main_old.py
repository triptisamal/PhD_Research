import igraph as ig
import random
from collections import deque

#global variables
transmittedPktIDSet = []
coords_subgraph = []
event_queue = []
src = (0,0,0)
dest = (0,0,0)
now = 0
now_e = 0.1 #time it takes for one event (transmission time)

def spawn_drones_graph():

    global coords_subgraph
    print("Spawing drones graph")

    ##TODO Read from file specifications for graph
    total_number_of_nodes = 5
    total_number_of_edges = 5

    ##create fully connected graph 
    g = ig.Graph(n=total_number_of_nodes)
    adj = []
    adj = g.get_adjacency()
    print(adj)
    ##assign location (coordinates)
    layout = g.layout(layout='auto',dim=3)
    coords_subgraph = layout[:total_number_of_nodes]

    drone_ids = []
    drone_ids = [0 for i in range(total_number_of_nodes)] 
    for i in range(len(coords_subgraph)):
        drone_ids[i] = i
        print("Drone ",drone_ids[i],": ",coords_subgraph[i])
    
    
    ##view graph
    ig.plot(g)


#def initialize_petal_parameters():
#
#    global coords_subgraph
#    global src
#    global dest
#    print("Initializing Petal Routing parameters")
#    #radius
#    
#    #Read source and destination location from file
#    src = random.choice(coords_subgraph)
#    while True:
#        dest = random.choice(coords_subgraph)
#        if dest != src:
#            break
#
#
#    print("Source:",src)
#    print("Destination:",dest)
#
#def create_message(myloc):
#    
#    global src
#    global dest
#
#    print("Creating message")
#    pkt = {
#    ##Header
#            'pID':0,    #packet ID
#            'dLoc':dest,   #destination location
#            'tLoc':(0,0,0),    #transmitter (intermediate node) location
#            #petal parameter from Trisha's paper
#            #source location from Trisha's paper
#            #following are needed in back off time calculation
#            'sLoc':src, #source location
#            'myLoc':myloc, #my location (how is it different from sLoc?)
#            'tUB1':0.002, #seconds;tB1 -> back-off time proportional to the distance from destination. 
#                          #This is bounded above by tUb1.
#            'tUB2':0.0005, #seconds;tB2 -> back-off time proportional to the distance from the source-destination 
#                           #line. This is bounded above by tUb2.
#            'zoneType':"SINGLE"
#    } 
#    
#    #Update source and destination location
#    print(pkt)
#
#    ##Payload
#    
#
#    return pkt
#
#def calculateBoffTime(pkt):
#    TD_proj = projection of TD on SD
#    tB1 = (pkt['tUb1'] ∗ TD_proj)/SD
#    if pkt['zoneType'] == "SINGLE":
#        X = pkt['sLoc']
#    else:
#        X = pkt['tLoc']
#    XP = distance of X from XD
#    tB2 = (pkt['tUb2'] ∗ XP)/XD
#    backOff = tB1 + tB2
#
#    return backOff
#
#
#def broadcast(pkt):
#
#    #destination is a point in space
#
#    if pkt['pID'] in transmittedPktIDSet:
#        discard(pkt)
#        sys.exit()
#    else:
#        schedule(pkt)
#
#def insideTransmissionZone(pkt,myLoc):
#
#
#
#
#
#



Global data structure first check if ellipse was already calculated, if not then do and save in global data structure.


handler function acting on behalf of the node should calc boff


some handler acting behalf of node
some handler acting real world 
def schedule(pkt):

    '''Schedule received packet'''
    #if already transmitted then discard
    if pkt['pID'] in transmittedPktIDSet:
        #discard(pkt)
        event = "Packet %d discarded at %d seconds" %(pkt['pID'],now) 
        event_queue.append(event)
        sys.exit(0)

    bufWait = []

    #Here, the packet is scheduled to be received by all the nodes
    #each node will check if it is inside the petal

    for i in range(len(coords_subgraph)-1):
        #am i inside petal
        if insideTransmissionZone(pkt,coords_subgraph[i]) == True:
            #coords_subgraph[i] is the location of the node that received the packet
            #first time packet goes into buffWait, and simulataneously timer is started
            if pkt['pID'] in bufWait:
                duplicate_count[pkt['pID']] += 1
                event = "Packet %d received at %d seconds" %(pkt['pID'],now) 
                event_queue.append(event)
                #save pkt["tLoc"]
            else:
                boffTime = calculateBoffTime(pkt)
                bufWait.append(pkt['pID'])
                registerCallback(boffTime, pkt, transmitOrDrop)#system call starts the timer (how long the timer to set, name of the function that will be called upon expiry (transmitOrDrop)
#
##def registerCallback(boffTime, pkt, transmitOrDrop):
##
##     '''called if the timer expired, make a decision whether to transmit or drop'''
##
##     transmitOrDrop(pkt)
##
##def transmitOrDrop(pkt):
##
###which pkt 
##    '''Petal routing callback handler'''
##    dupCoords = duplicateTransmissionCoordinates(pkt)
##    if len(dupCoords)>nodeDensity*boundary(dupCoords):
##        centroid = centroid(dupCoords)
##        if distance(myLoc, pkt['dLoc']) < distance(centroid, pkt['dLoc']):
##Add event here 
##            discard(pkt)
##        pkt['tLoc'] = myLoc
##        transmit(pkt)
##Add event here 
##    transmittedPktIDSet.append(pkt['pID'])
#
#
#def initialize_events(pkt):
#
#    global now
#    global event_queue
#    
#    print("Creating initial events")
#    event_queue = deque()
#    event = "Packet %d created at %s at %d seconds" %(pkt['pID'],pkt['sLoc'],now) 
#    event_queue.append(event)
#    now = now + now_e
#
#
#def share_message_with_all():
#    
#    global event_queue
#
#    initialize_petal_parameters()
#    pkt = create_message(src)
#
#    initialize_events(pkt)
#    print(event_queue)
#    broadcast(pkt)

def main():

    spawn_drones_graph()
#    share_message_with_all()

if __name__=="__main__":
    main()
