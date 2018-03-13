# TODO: make this as library
# TODO: note, libraries should be local dependencies
###############################################################################

import requests
import jsonpickle

# # support numpy serialization
# import jsonpickle.ext.numpy as jsonpickle_numpy
# jsonpickle_numpy.register_handlers()

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

###############################################################################


# Hypnolog-python usage examples:

# log a string
someString = "Hello HypnoLog from Pyhton!";
log(someString, "string");

# log numbers list as single line graph
numbers = [1,2,3];
log("Example of logging list of numbers:", "string");
log(numbers, "plot");

# log numpy arrays
import numpy
npArray = 1 + numpy.sin(2 * numpy.pi * numpy.arange(0.0, 2.0, 0.01))
npArrayAsList = npArray.tolist();
log("Example of logging numpy array:", "string");
log(npArrayAsList, "plot");

# TODO: log multi line graph

# log 2d array as heatmap
a = numpy.arange(-50, 50, 1).reshape(10,10); 
a = a.tolist();
log(a, "heatmap");

# TODO: log histogram

# log Lat-Long Geo locations using Google maps
locations = [
    ['Lat', 'Long', 'Name'],
    [37.4232, -122.0853, 'Work'],
    [37.4289, -122.1697, 'University'],
    [37.6153, -122.3900, 'Airport'],
    [37.4422, -122.1731, 'Shopping']
];
log("Example of logging Lat-Long Geo locations using Google maps:", "string");
log(locations, "GoogleMaps");


# log custom object
class Rectangle:
    pass
rect = Rectangle();
rect.higth = 20;
rect.width = 10;
rect.color = "green";
log("Example of logging custom object:", "string");
log(rect, 'object');

# log custom object with nested custom objects
class Car:
    pass
class Engine:
    pass
car = Car();
car.brand = "Seat";
car.model = "Mii";
car.engine = Engine();
car.engine.numberOfCylinders = 3;
car.engine.acceleration = 14.4;
car.color = "red";
log("Example of logging custom object with nested custom objects:", "string");
# note, default logging type is "object"
log(car);

