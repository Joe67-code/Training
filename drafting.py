import datetime
import time

hasard_state_index = 0
hasard_state = ["OFF", "ON", "Undefined", "ON", "OFF"]

pseat_state = ["pos1", "pos2", "pos3", "pos1", "pos4"]
pseat_state_index = 0

# Function to get the next hazard light state
def next_hazard_light_state():
    global hasard_state_index
    hasard_state_index += 1
    if ( hasard_state_index >= len(hasard_state) ):
        hasard_state_index = 0
        return False 
    return True

def send_hazard_light_state():
    print( "Sent Hasard_state:      " + hasard_state[hasard_state_index])

def next_pseat_postion_state():
    global pseat_state_index
    pseat_state_index += 1
    if ( pseat_state_index >= len(pseat_state) ):
        pseat_state_index = 0
        return False 
    return True

def send_pseat_postion_state():
    print( "Sent pseat_state:      " + pseat_state[pseat_state_index])


def main():
    
    # Get the current time in milliseconds
    start_time_ms = int(time.time() * 1000)
    time_delta = 0
    message_package_nr = 0 

    while True:
        
        if (message_package_nr == 0):
         
         send_hazard_light_state()  # send actual hazard state with 5hz frequency
         time.sleep(0.2)  

         # change hazard light state every 1 second
         time_delta =  int(time.time() * 1000) - start_time_ms

         if ( time_delta > 1000 ):
            start_time_ms = int(time.time() * 1000) 
            # check if all hazard states have been sent
            if( next_hazard_light_state() == False ):
                print("All Hazard states have been sent - let's send the next message package")
                time.sleep(2)  # wait 0.5 seconds before sending the next message package
                message_package_nr += 1
         

        if (message_package_nr == 1):
         
         send_pseat_postion_state()  # send actual seat pos state with 5hz frequency
         time.sleep(0.2)  

         # change hactual seat pos every 1 second
         time_delta =  int(time.time() * 1000) - start_time_ms

         if ( time_delta > 1000 ):
            start_time_ms = int(time.time() * 1000) 
            # check if all seat states have been sent
            if( next_pseat_postion_state() == False ):
                print("All Seat states have been sent - let's send the next message package")
                time.sleep(2)  # wait 0.5 seconds before sending the next message package
                message_package_nr = 0
                break



if __name__ == "__main__":
        main()