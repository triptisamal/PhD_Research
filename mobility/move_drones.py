from create_pos import *
import temp.globalvars

def reads_velocity():
    
    if move == 1:
        #Do something
        print("All drones have the same velocity")
    else:
        #Do something
        print("All drones have the same velocity")
        
    return velocity


def init_position(velocity):
    

#creating drone start position
    create_drones_startpos()  

#Update start and end positions of the drones

    if velocity == 0:
        read_pos_from_file()
    else:
        calc_new_position(velocity)

def create_drones_network(velocity):
    init_position(velocity)
    display_position()

def generate_final_position():
    
    velocity = reads_velocity(globalvars.move)
    create_drones_network(velocity)

def main():

    #parse arguments
    if len(sys.argv) < 2:
        print("Usage: move_drones.py <type of motion>")
        print("type of motion = All drones moving from point A to B with same velocity = 1 ")
        print("type of motion = A subset of drones moving from point A to B with same velocity = 2 ")

    globalvars.init()
    globalvars.move = int(sys.argv[1])

    create_drones_network(0)

    #this is the time at which the simulator notes how much each drone has moved
    time_blocks = [] #seconds
    for t in range(10):
        time_blocks[t] = t+5 #TODO change 5 according to what measurement you got in petal algo; it is the time in which appreciable amount of movement happens for a drone

    for time in time_blocks:
        generate_final_position()
        display_final_position()



if __name__=="__main__":
    main()
