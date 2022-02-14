from traceback import print_exception
import precize_time
from datetime import datetime
import pickle

global actions_counter
actions_counter = None

def getCurrentDateAndTime() -> str:
    currentTimeDate = datetime.now()
    return f"{currentTimeDate} ({precize_time.millis()})"

# def readActionsCounterFromShared() -> int:
#         try:
#             fp = open("shared.pkl")
#             shared = pickle.load(fp)
#             actions_counter = shared["actions_counter"]
#         except:
#             pass
            
#         return actions_counter


def getActionsCounter(seed = 1) -> str:
    return getCurrentDateAndTime()
    # global actions_counter
    # actions_counter +=1
    # return actions_counter
#     if actions_counter == None:

#         shared = {"actions_counter":"1"}
#         fp = open("shared.pkl","w")
#         pickle.dump(shared, fp)

#         actions_counter = seed
#     else:
#         actions_counter +=1

#     return f"{actions_counter}".zfill(6)

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

if __name__ == "__main__": #if running this module as a stand-alone program
    # for i in range(0):
    #     print(getActionsCounter())

    print(make_pos((10,10)))

