from email.header import Header
from flask import Flask, render_template
from flask import request
from flask import Response
from lxml import etree

from datetime import datetime
import random
import json

app = Flask(__name__)

@app.route('/inventory')
def getInventory():
    inventory = json.load(open('inventory.json'))
    return app.response_class(json.dumps(inventory), mimetype='application/json')

@app.route('/inventory/cpus')
def getInventoryCPUs():
    inventory = json.load(open('inventory.json'))
    partslist = inventory['cpus']
    return app.response_class(json.dumps(partslist), mimetype='application/json')

@app.route('/inventory/cpus/<cpu>')
def getInventoryPartCPUs(cpu):
    inventory = json.load(open('inventory.json'))
    partslist = inventory['cpus']
    cpuCount = partslist.get(cpu, -1)
    response = {
        f"amount: {cpuCount}"
    }
    return app.response_class(response, mimetype='application/json')

@app.route('/inventory/cpucoolers')
def getInventoryCPUCoolers():
    inventory = json.load(open('inventory.json'))
    partslist = inventory['cpu_coolers']
    return app.response_class(json.dumps(partslist), mimetype='application/json')

@app.route('/inventory/cpucoolers/<cpucooler>', methods=['GET', 'PUT'])
def getInventoryPartCPUCoolers(cpucooler):
    with open('inventory.json', 'r+') as data: 
        inventory = json.load(data)
        if request.method == 'PUT':
            requestBody = request.get_json()
            newAmount = requestBody['amount']
            inventory['cpu_coolers'][cpucooler] = newAmount
            data.seek(0)
            json.dump(inventory, data, indent=4)
        partslist = inventory['cpu_coolers']
        cpuCoolerCount = partslist.get(cpucooler, -1)
        response = {
            f"amount: {cpuCoolerCount}"
        }
        data.close()
    return app.response_class(response, mimetype='application/json')

@app.route('/inventory/ram')
def getInventoryRAMs():
    inventory = json.load(open('inventory.json'))
    partslist = inventory['ram']
    return app.response_class(json.dumps(partslist), mimetype='application/json')

@app.route('/inventory/ram/<ram>')
def getInventoryPartRAMs(ram):
    inventory = json.load(open('inventory.json'))
    partslist = inventory['ram']
    ramCount = partslist.get(ram, -1)
    response = {
        f"amount: {ramCount}"
    }
    return app.response_class(response, mimetype='application/json')

@app.route('/inventory/gpus')
def getInventoryGPUs():
    inventory = json.load(open('inventory.json'))
    partslist = inventory['gpus']
    return app.response_class(json.dumps(partslist), mimetype='application/json')

@app.route('/inventory/gpus/<gpu>')
def getInventoryPartGPUs(gpu):
    inventory = json.load(open('inventory.json'))
    partslist = inventory['gpus']
    gpuCount = partslist.get(gpu, -1)
    response = {
        f"amount: {gpuCount}"
    }
    return app.response_class(response, mimetype='application/json')

@app.route('/inventory/createOrder')
def createOrder():
    inventory = json.load(open('inventory.json'))
    cpus = inventory['cpus']
    cpuCoolers = inventory['cpu_coolers']
    gpus = inventory['gpus']
    ram = inventory['ram']
    response = {
        "cpu": random.choice(list(cpus.keys())),
        "cpu cooler": random.choice(list(cpuCoolers.keys())),
        "memory": random.choice(list(ram.keys())),
        "gpu": random.choice(list(gpus.keys()))
    }
    return app.response_class(json.dumps(response), mimetype='application/json')

@app.route('/inventory/status')
def getStatus():
    response = {
        "status": "idk tbh"
    }
    return app.response_class(json.dumps(response), mimetype='application/json')

@app.route('/correlator', methods=['GET', 'POST', 'PUT'])
def base():
    
    headers = dict(request.headers)
    body = request.get_json()

    with open('log.txt', 'a') as logfile:
        timestamp = datetime.now()
        logfile.write(f"COMING IN HOT | {timestamp.strftime('%d/%m/%Y %H:%M:%S')} | HEADERS {headers} | BODY | {body}\n")
    logfile.close()    
    return app.response_class("kid named finger")

@app.route('/testXML', methods=['GET', 'POST', 'PUT'])
def test():
    tree = etree.parse("production.xml")
    print (tree.xpath("//*[name()='teil2']"))
    return app.response_class('Kid named finger')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9301, debug=True)