def init():
    global pos
    global e
    global focus1_key
    global focus2_key
    global a
    global b
    global c
    global packet
    global now
    global now_e
    global node
    global pid
    global number_of_nodes
    global G
    global idn
    global broadcast
    global transmission_delay
    global speed
    global state_vector
    global copies_transmitted
    global copies_delivered
    global protocol
    global topology
    global zone
    global sourcedestdistance
    global insidectr
    global sd_random
    global iteration
    #global reached_destination
    global formation 
    global move

    G = 0
    pos = []
    e = 0.9
    focus1_key=0
    focus2_key=0
    a=0
    b=0
    c=0
    packet = {
            'pID':0,    #packet ID
            'dLoc':(0,0,0),   #destination location
            'tLoc':(0,0,0),    #transmitter (intermediate node) location
            'sLoc':(0,0,0), #source location
            'myLoc':(0,0,0), #my location 
            
            #petal parameters 
            'eccentricity':e, #of the segment corresponding to orbital eccentricity 

            #back off time parameters
            'tUB1':20, #seconds;tB1 -> back-off time proportional to the distance from destination. 
            #'tUB1':0.002, #seconds;tB1 -> back-off time proportional to the distance from destination. 
                          #This is bounded above by tUb1.
            'tUB2':90, #seconds;tB2 -> back-off time proportional to the distance from the source-destination 
            #'tUB2':0.0005, #seconds;tB2 -> back-off time proportional to the distance from the source-destination 
                           #line. This is bounded above by tUb2.


            #SINGLE zone means petal does not change
            'zoneType':"SINGLE"

        }#message details

    event_queue = []
    now = 0
    now_e = 1
    pid = 1 #count of all packets created throughout the simulation
    number_of_nodes = 125
    idn = 0
    broadcast = 0
    transmission_delay = 3 #seconds
    speed = 299792458 #m / s
    copies_transmitted = 0
    copies_delivered = 0
    protocol = 1
    topology = 0
    zone = 0
    sourcedestdistance = 0
    insidectr = 0
    sd_random = 0
    iteration = 0
    #reached_destination = 0
    formation = 0
    move = 0