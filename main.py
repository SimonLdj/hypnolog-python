import hypnolog as HL

# Hypnolog-python usage examples:

# log a string
someString = "Hello HypnoLog from Pyhton!";
HL.log(someString, "string");

# log numbers list as single line graph
numbers = [1,2,3];
HL.log("Example of logging list of numbers:", "string");
HL.log(numbers, "plot");

# log numpy arrays
import numpy
npArray = 1 + numpy.sin(2 * numpy.pi * numpy.arange(0.0, 2.0, 0.01))
npArrayAsList = npArray.tolist();
HL.log("Example of logging numpy array:", "string");
HL.log(npArrayAsList, "plot");

# TODO: log multi line graph

# log 2d array as heatmap
a = numpy.arange(-50, 50, 1).reshape(10,10); 
a = a.tolist();
HL.log(a, "heatmap");

# TODO: log histogram

# log Lat-Long Geo locations using Google maps
locations = [
    ['Lat', 'Long', 'Name'],
    [37.4232, -122.0853, 'Work'],
    [37.4289, -122.1697, 'University'],
    [37.6153, -122.3900, 'Airport'],
    [37.4422, -122.1731, 'Shopping']
];
HL.log("Example of logging Lat-Long Geo locations using Google maps:", "string");
HL.log(locations, "GoogleMaps");


# log custom object
class Rectangle:
    pass
rect = Rectangle();
rect.higth = 20;
rect.width = 10;
rect.color = "green";
HL.log("Example of logging custom object:", "string");
HL.log(rect, 'object');

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
HL.log("Example of logging custom object with nested custom objects:", "string");
# note, default logging type is "object"
HL.log(car);

