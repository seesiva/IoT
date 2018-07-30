from opcua import ua
from opcua import Server
import random
import os
import psutil
import datetime
import time

if __name__=="__main__":
    pid = os.getpid()
    server =  Server()                          # Instantiating the server from freeopcua python library
    url="opc.tcp://192.168.0.160:4840"          # URL string on which the server to be run with port 4840
    server.set_endpoint(url)                    # setting up the URL as the end point
    name="OPCUA_SERVER_SIMULATION"
    namespace=server.register_namespace(name)   # Register names space with the name provided
    nodes = server.get_objects_node()           # Retrieve the object and its nodes

    Param = nodes.add_object(namespace,"Parameters")         # add the "Parameters" to the nodes obtained from the server

    ## define the variables and objects which will be available under "Paramters"
    cpu_percent=Param.add_variable( namespace,"cpu_percent",0)
    mem_usage=Param.add_variable( namespace,"mem_usage",0)
    DataTime=Param.add_variable( namespace,"time",0)
    retrival_interval=Param.add_variable( namespace,"retrival_interval",2)

    # Make only retrival interval as writable 
    retrival_interval.set_writable()

    # Start the server
    server.start()
    print ("OPC UA Server started in endpoint: {}".format(url))

    while True:
        py = psutil.Process(pid)
        cp_prcnt=psutil.cpu_percent()
        memoryUse = py.memory_info()[0]/2.**30  # memory use in GB
        dttime=datetime.datetime.now()

        print(cp_prcnt,memoryUse,dttime)

        cpu_percent.set_value(cp_prcnt)
        mem_usage.set_value(memoryUse)
        DataTime.set_value(dttime)

        time.sleep(retrival_interval.get_value())