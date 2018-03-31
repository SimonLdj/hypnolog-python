import requests
import jsonpickle

# TODO: make this as library
# TODO: note, libraries should be local dependencies
# TODO: docuemnt, accroding to pyhton style

_errorHandler = None;
_host = 'localhost';
_port = 7000;

# Init
def initialize(host=None, port=None, errorHandler=None):
    global _host, _port, _errorHandler;
    if host != None:
        _host = host;
    if port != None:
        _port = port;
    if errorHandler != None:
        _errorHandler = errorHandler;

# Simple HypnoLog logging funciton
def log(obj, objType=None):
    try:
        if objType == None:
            objType = _determineType(obj);

        # some const settings
        serverURL = 'http://{host}:{port}/logger/in'.format(host=_host, port=_port);

        # prase the log request in a valid HypnoLog-data object
        hypnologObj = { "data": obj, "type": objType };

        # encode the whole object to JSON
        postData = jsonpickle.encode(hypnologObj)

        # send the request to HypnoLog server
        r = requests.post(serverURL, headers={'Content-Type': 'application/json'}, data=postData);
        if r.status_code == 200:
            return True;

        # bad status code, raise exception
        raise Exception("Server response code is not 200. status code: {0}".format(r.status_code));

    except Exception as e:
        _onError(e);
        return False;

    return False;

def _onError(e):
    if _errorHandler != None:
        _errorHandler(e);
    else:
        print("HypnoLog error:\n{0}".format(e));
        # raise e;

def _determineType(obj):
    if isinstance(obj, str):
        return 'string';
    return 'object';

