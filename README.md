HypnoLog Python Library
============================

## What is HypnoLog?
*Get Hypnotized While Logging*

*HypnoLog* allows you to fast and easily visualize your application data/objects while debugging. From any environment, in any language. Forget about those black text-based console debug-printing back from the 70's. 

**See [HypnoLog main repo](https://github.com/SimonLdj/hypnolog-server).**

What it looks like, visualizing your data in the browser:
![alt text](/doc/images/screenshot_hypnolog-python-example.png "HypnoLog UI screenshot")

## About HypnoLog Python Library
Logging using *HypnoLog* means sending you data as JSON HTTP request to HypnoLog server. This library wraps all of those into simple easy to use functions.
<!--TODO: To use *HypnoLog* in your Python script ... -->

## Usage Examples
Really simple. Import HypnoLog:
```python
import hypnolog as HL
```
Log:
```python
// Log a string
HL.log('Hello HypnoLog from Pyhton!');

// log list of numbers as a graph (plot)
HL.log([1,2,3], 'plot');
```

For more examples, see [Basic Example](/examples.py) and [Advanced Example](advancedExample.py) code files.

Read how to view the log and more about *HypnoLog* in [HypnoLog main repo page](https://github.com/SimonLdj/hypnolog-server).

