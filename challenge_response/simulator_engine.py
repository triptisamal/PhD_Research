import sys

import globalvars
from challenge_response import *


def main():
    '''Simulation engine'''
    
    #parse arguments
    if len(sys.argv) < 2:
        print("Usage: simulator_engine.py <number of nodes>")
        sys.exit();
    
    globalvars.init()
    globalvars.number_of_nodes = int(sys.argv[1])
    print("Number of nodes = ", globalvars.number_of_nodes)

    #create map maintained by the simulator
    #used to check if the flashlight is on or off
    create_sim_map();








if __name__=="__main__":
    main()
