HypnoLog Python Library
============================

## What is HypnoLog?
*Get Hypnotized While Logging*

*HypnoLog* allows you to fast and easily visualize your application data/objects while debugging. From any environment, in any language. Forget about those black text-based console debug-printing back from the 70's. 

**See [HypnoLog main repo](https://github.com/SimonLdj/hypnolog-server).**

What it looks like, visualizing your data in the browser:
![alt text](/doc/images/screenshot_hypnolog-python-example.png "HypnoLog UI screenshot")

## About HypnoLog-Python Library
Logging using *HypnoLog* means sending you data as JSON HTTP request to HypnoLog server. This library wraps all of those into simple easy to use functions.

## Installation
The easiest way to get *HypnoLog* is via [PyPi](https://pypi.org/) with `pip` command
```bash
pip install hypnolog
```

If you haven't use *HypnoLog* before, [setup HypnoLog server](https://github.com/SimonLdj/hypnolog-server#setup-hypnolog-server) on your machine:
```bash
npm install -g hypnolog-server
```
*Note:* you will need [Node.js](https://nodejs.org/en/) installed on your machine first.

## Usage
1. Start *HypnoLog* server:
    ```bash
    hypnolog-server
    ```
2. View output: open [`http://127.0.0.1:7000/client.html`](http://127.0.0.1:7000/client.html) in your browser.
3. Import HypnoLog into your script:
   ```python
   import hypnolog as HL
   ```
4. Log:
   ```python
   // Log a string
   HL.log('Hello HypnoLog from Pyhton!');

   // log list of numbers as a graph (plot)
   HL.log([1,2,3], 'plot');
   ```

For more examples, see [Basic Example](hypnolog-python/examples.py) and [Advanced Example](hypnolog-pythona/dvancedExamples.py) code files.

Read how to view the log and more about *HypnoLog* in [HypnoLog main repo page](https://github.com/SimonLdj/hypnolog-server).

