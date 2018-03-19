
import requests
import jsonpickle

# TODO: make this as library
# TODO: note, libraries should be local dependencies
# TODO: docuemnt, accroding to pyhton style

class HypnoLog:
    def __init__(self):
        pass

    # Simple HypnoLog logging funciton
    def log(obj, objType='object'):

        # some const settings
        serverURL = 'http://localhost:7000/logger/in';

        # prase the log request in a valid HypnoLog-data object
        hypnologObj = { "data": obj, "type": objType };

        # encode the whole object to JSON
        postData = jsonpickle.encode(hypnologObj)

        # send the request to HypnoLog server
        r = requests.post(serverURL, headers={'Content-Type': 'application/json'}, data=postData);
        if r.status_code == 200:
            return True;
        return False;

def log(obj, objType='object'):
    HypnoLog.log(obj, objType);
