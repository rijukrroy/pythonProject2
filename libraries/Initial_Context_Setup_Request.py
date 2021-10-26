import re
import sys
import os
import shutil

sys.path.insert(0,r"C:\Users\40015321\PycharmProjects\pythonProject2\config") # What this line is performing???
import Config_Test
'''
    Initial_Context_Setup_Request Message Format (from new AMF --- gNB)
'''
class Initial_Context_Setup_Request:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    endoded_msg=[]

    def __init__(self):
        pass
'''
   Encoding of the initial_context_setup_request_encoding 
'''
    def initial_context_setup_request_encoding(self):
        global endoded_msg
        Message_Type = 1
        AMF_UE_NGAP_ID = 237
        RAN_UE_NGAP_ID = 212
        Old_AMF = 56    # AMF name
        UE_Aggregate_Maximum_Bit_Rate = 45  # 45 Kbps
        Core_Network_Assistance_Information = 87 # "his morning"
        GUAMI = 57

        endoded_msg = [Message_Type, AMF_UE_NGAP_ID, RAN_UE_NGAP_ID, Old_AMF,
                       UE_Aggregate_Maximum_Bit_Rate, Core_Network_Assistance_Information, GUAMI]

        fob=open(Config_Test.UE_src_path, "w+")
        fob.write(str(endoded_msg))

    def initial_context_setup_response_encoding(self):


'''
   Send the initial_context_setup_request Message from new AMF to gNB
'''
    def move_msg(self):
        src = Config_Test.UE_src_path
        dest = Config_Test.dest_path

        #dst= shutil.copy(src,dest)

        if shutil.copy(src,dest) == True:
            print(" Moved the message successfully")

    def validation(self):
        global endoded_msg
        count =0
        msg_dict={}

        fob = open(Config_Test.log_path, "r")
        print("Inside Validation")
        for elem in fob:

            data = elem.rstrip("\n").split(" ")
            msg_dict[data[3]]=data[-1]


        for elem in msg_dict:
            print(msg_dict[elem])
            print(endoded_msg[count])

            if str(msg_dict[elem]) == str(endoded_msg[count]):
                 print("Passed")
            count+=1
        print(msg_dict)


class_instance = Initial_Context_Setup_Request()
class_instance.initial_context_setup_request_encoding()
class_instance.move_msg()
class_instance.validation()