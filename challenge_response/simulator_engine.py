from collections import deque
from copy import deepcopy
import sys

import globalvars
from challenge_response import *



def create_event(eventid,nodeid,packetdetails,timeofevent):
    event = {'event_id':"DEFAULT", 'agent':0,'time':0}
    event['event_id'] = eventid
    event['agent'] = nodeid
    event['time'] = timeofevent
    event['details'] = packetdetails
    
    

    return event


def update_claim(id,pos,timeofevent):
    
    claim = {'sender':"DEFAULT", 'position':(0,0,0),'time':0}
    claim['sender'] = id
    claim['position'] = pos
    claim['time'] = timeofevent
    
    return claim

def update_challenge(prover,challenger,timeofchallenge,task):
    
    challenge = {'prover':"DEFAULT", 'challenger':0,'time':0, 'challenge':"default challenge"}
    
    challenge['prover'] = prover
    challenge['challenger'] = challenger
    challenge['time'] = timeofchallenge
    challenge['challenge'] = task
    
    return challenge
    


def start_timer(prover,node_id,timeofchallenge,duration):
    
    timer = {'prover':"DEFAULT", 'challenger':0,'time':0, 'challenge':"default challenge"}
    
    timer['timer_started_for'] = prover
    timer['timer_started_by'] = node_id
    timer['time'] = timeofchallenge
    timer['duration'] = duration
    
    return timer

  
def node_handler(node_id,action,e):


    if action == "SEND_POSITION-CLAIM":
        #node_id is sending position claim
       # print("Agent ",node_id," is creating the packet for position claim at",globalvars.now, "seconds." )
               
        claim = update_claim(node_id,globalvars.sim_map[node_id]['position'],globalvars.now)

        event_id = "CLAIM_%03d" % (globalvars.idn)
        globalvars.idn += 1

        e = create_event(event_id,node_id,claim,globalvars.now)
        globalvars.event_queue.append(deepcopy(e))

        #sort queue according to the simulated real time (time of event happening)
        globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])
        
        
    if action == "SEND_CHALLENGE":
        #node_id is sending challenge
       # print("Agent ",node_id," is challenging e['details']['sender'] and creating the packet for challenge at",globalvars.now, "seconds." )
       
        
        challenge = update_challenge(e['details']['sender'],node_id,globalvars.now,"TURN ON FLASHLIGHT")
        event_id = "CHALLENGE_%03d" % (globalvars.idn)
        globalvars.idn += 1

        e = create_event(event_id,node_id,challenge,globalvars.now)
        globalvars.event_queue.append(deepcopy(e))

        #start timer event
        timer = start_timer(e['details']['prover'],node_id,globalvars.now,3*globalvars.e_now)
        event_id = "TIMERSTART_%03d" % (globalvars.idn)
        globalvars.idn += 1
        e = create_event(event_id,node_id,timer,globalvars.now)
        globalvars.event_queue.append(deepcopy(e))
        
        
        #sort queue according to the simulated real time (time of event happening)
        globalvars.event_queue = sorted(globalvars.event_queue, key=lambda x: x['time'])
        
        
    if action == "FLASHLIGHT_ON":
        #node_id will turn on flashlight
        turn_on_flashlight(node_id)
        
    if action == "TIMER_EXPIRY":
        #node_id will do actions because of its own timer expiry
        #it verifies response, i.e., checks if prover's light is on and then increases/decreases confidence
        ret = is_flashlight_on(e['details']['timer_started_for'])
        if ret == 1:
            update_confidence(1,e['details']['timer_started_for'],node_id)
        else:
            update_confidence(-1,e['details']['timer_started_for'],node_id)
        
        
  
        

def turn_on_flashlight(agent):
    globalvars.sim_map[agent]['flashlight'] = 1

def is_flashlight_on(agent):
    if globalvars.sim_map[agent]['flashlight'] == 1:
        return 1


def update_confidence(c,prover,agent):
    #maintained by each agent
    print("g")

        
    
   
def process_event(e):

    if "CLAIM" in e['event_id']:
        #send challenge for each position claim from each agent that received the claim
        #increment simulation time
        globalvars.now += globalvars.e_now  
        for i in range(globalvars.number_of_nodes): #everyone received because wireless communication is infinite
            node_handler(i,"SEND_CHALLENGE",e)



    if "CHALLENGE" in e['event_id']:
        #turn on flashlight for all the agents who got the challenge
        globalvars.now += globalvars.e_now
        
        for i in range(globalvars.number_of_nodes):
            if e['details']['prover'] == i:
                node_handler(i,"FLASHLIGHT_ON",e)
                
                
    if "TIMERSTART" in e['event_id']:
        #create a timer expiry event for every timerstart event
        node_handler(e['details']['timer_started_by'],"TIMER_EXPIRY",e)
        

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
    
    
    #create confidence table
   # globalvars.sim_map = [{'agent_id':i, 'position':(0,0,0), 'flash_light':0} for i in range(globalvars.number_of_nodes)]
   
    conf = [{'agent_id':i, 'value':0} for i in range(globalvars.number_of_nodes)]

        
        
    confidence_table = [{'my_id':i, 'confidence':conf} for i in range(globalvars.number_of_nodes)]
    
    
    print(confidence_table[1]['my_id'])
  #  print(confidence_table[1]['confidence'][1]['value'])
 #   print(confidence_table[1]['confidence'][2]['agent_id'])
 #   print(confidence_table[2]['confidence'][2]['agent_id'])
    print("CONFIDENCE TABLE")
    print(confidence_table)
    i=0
    
    while i < globalvars.number_of_nodes: 
       # print(confidence_table[i]['my_id'])
       # print(confidence_table[i]['confidence'])
        if confidence_table[i]['my_id'] == confidence_table[i]['confidence'][i]['agent_id']:
            confidence_table[i]['confidence'][i]['value'] = 99
        i=i+1;
                
     #   for j in range(globalvars.number_of_nodes): 
      #      if confidence_table[i]['my_id'] == confidence_table[i]['confidence'][i]['agent_id']:
       #         confidence_table[i]['confidence'][j]['value'] = 1 
            
    print("CONFIDENCE TABLE")
    print(confidence_table)

    sys.exit()
    #add first event(s) to the event_queue
    e = {'event_id':"DEFAULT", 'agent':0,'time':0}
    for i in range(globalvars.number_of_nodes):
        node_handler(i,"SEND_POSITION-CLAIM",e);
        
    print("Initial events:")
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
