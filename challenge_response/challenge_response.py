import globalvars

def create_sim_map():
    '''Map of the network with information about which flashlights are on or off'''
        
    #define data structure for the map maintained by the simulator
    globalvars.sim_map = [{'agent_id':i, 'flash_light':0} for i in range(globalvars.number_of_nodes)]
    print("This is the current map:",globalvars.sim_map)
