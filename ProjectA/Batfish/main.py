#!/usr/bin/env python

'''
bf_session is used to provide details for communication with the batfish application (IP address, API token etc)
bf_init_snapshot is used to upload your configuration files into the batfish application.
load_questions is used to initialise the Batfish questions
bfq is used to ask the question and receive the response
OS standard lib, which allow us to work with directories at linux host

Create Variable, which we need to for our python script to work:
    bf_address : IP address we are using to connect to Batfish
    As it is running in the Docker container and its TCP ports are NATed to all interfaces, we can use localhost (127.0.0.1) to connect to it. 

Body Part : 
    connectivity data from bf_address to bf_session.host property
    load confiiguration using bf_init_snapshot() using argument snapshot_path
    Initialising Batfish questions without arguments using load_questions()
    Collect the answer() to the question nodeProperties() sent via bfq class, which is converted to Pandas Dataframe using Frame() method and stored in a variable r.
    printing the answer r in the STDOUT with print() function
'''

from pybatfish.client.commands import bf_init_snapshot, bf_session
from pybatfish.question.question import load_questions
from pybatfish.question import bfq
import os

bf_address = "127.0.0.1"
snapshot_path = "./snapshot"
output_dir = "./output"

if __name__ == "__main__":
    
    # Setting host to connect
    bf_session.host = bf_address
    
    # Loading configs and questions
    bf_init_snapshot(snapshot_path, overwrite=True)
    load_questions()

    # Running Questions
    r = bfq.nodeProperties().answer().frame()
    print(r)

    # Saving output
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    r.to_csv(f"{output_dir}/results.csv")

