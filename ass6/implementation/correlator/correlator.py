import requests
from flask import Flask
from flask import request

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

@app.route('/inventory/cpus/<cpu>', methods=['GET', 'PUT'])
def getInventoryPartCPUs(cpu):
    with open('inventory.json', 'r+') as data: 
        inventory = json.load(data)
        if request.method == 'PUT':
            newAmount = request.form.get('amount')
            inventory['cpus'][cpu] = newAmount
            data.seek(0)
            json.dump(inventory, data, indent=4)
            data.truncate()
        partslist = inventory['cpus']
        cpuCount = partslist.get(cpu, -1)
        response = {
            "amount": cpuCount
        }
        data.close()
    return app.response_class(json.dumps(response), mimetype='application/json')

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
            newAmount = request.form.get('amount')
            inventory['cpu_coolers'][cpucooler] = newAmount
            data.seek(0)
            json.dump(inventory, data, indent=4)
            data.truncate()
        partslist = inventory['cpu_coolers']
        cpuCoolerCount = partslist.get(cpucooler, -1)
        response = {
            "amount": cpuCoolerCount
        }
        data.close()
    return app.response_class(json.dumps(response), mimetype='application/json')

@app.route('/inventory/ram')
def getInventoryRAMs():
    inventory = json.load(open('inventory.json'))
    partslist = inventory['ram']
    return app.response_class(json.dumps(partslist), mimetype='application/json')

@app.route('/inventory/ram/<ram>', methods=['GET', 'PUT'])
def getInventoryPartRAMs(ram):
    with open('inventory.json', 'r+') as data: 
        inventory = json.load(data)
        if request.method == 'PUT':
            newAmount = request.form.get('amount')
            inventory['ram'][ram] = newAmount
            data.seek(0)
            json.dump(inventory, data, indent=4)
            data.truncate()
        partslist = inventory['ram']
        ramCount = partslist.get(ram, -1)
        response = {
            "amount": ramCount
        }
        data.close()
    return app.response_class(json.dumps(response), mimetype='application/json')

@app.route('/inventory/gpus')
def getInventoryGPUs():
    inventory = json.load(open('inventory.json'))
    partslist = inventory['gpus']
    return app.response_class(json.dumps(partslist), mimetype='application/json')

@app.route('/inventory/gpus/<gpu>', methods=['GET', 'PUT'])
def getInventoryPartGPUs(gpu):
    with open('inventory.json', 'r+') as data: 
        inventory = json.load(data)
        if request.method == 'PUT':
            newAmount = request.form.get('amount')
            inventory['gpus'][gpu] = newAmount
            data.seek(0)
            json.dump(inventory, data, indent=4)
            data.truncate()
        partslist = inventory['gpus']
        gpuCount = partslist.get(gpu, -1)
        response = {
            "amount": gpuCount
        }
        data.close()
    return app.response_class(json.dumps(response), mimetype='application/json')

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
    response = [
      {
        "progress": "parts picked out",
        "completion": 10
      },
      {
        "progress": "parts unboxed",
        "completion": 12
      },
      {
        "progress": "parts looked at",
        "completion": 15
      },
      {
        "progress": "parts assembled",
        "completion": 20
      },
      {
        "progress": "coffee break",
        "completion": 22
      },
      {
        "progress": "cables plugged in",
        "completion": 25
      },
      {
        "progress": "smoke break",
        "completion": 30
      },
      {
        "progress": "packaging computer",
        "completion": 35
      },
      {
        "progress": "ready for delivery",
        "completion": 99
      },
    ]
    return app.response_class(json.dumps(response), mimetype='application/json')

@app.route('/correlator', methods=['GET', 'POST', 'PUT'])
def base():
    
    headers = dict(request.headers)
    body = dict(request.get_json())

    with open('log.txt', 'a') as logfile:
        timestamp = datetime.now()
        logfile.write(f"COMING IN HOT | {timestamp.strftime('%d/%m/%Y %H:%M:%S')} | HEADERS {headers} | BODY | {body}\n")
    logfile.close()

    headerContentId = ""
    headerContentId = headers.get('Content-Id')

    if headerContentId == "UsbC4Eva":
        cpu = body.get('cpu')
        cpuCooler = body.get('cpu cooler')
        ram = body.get('memory')
        gpu = body.get('gpu')
        instantiateProcess(cpu=cpu, cpuCooler=cpuCooler, ram=ram, gpu=gpu)

    return app.response_class("kid named finger")

def instantiateProcess(cpu, cpuCooler, ram, gpu):
    url = "https://cpee.org/flow/start/xml/"
    headers = {'Content-Type': 'multipart/form-data;boundary=----'}
    start = '------' + "\r\n" + 'Content-Disposition: form-data; name="behavior"' + "\r\n\r\n" + 'fork_running' + "\r\n" + '------' + "\r\n" + 'Content-Disposition: form-data; name="xml"' + "\r\n" + 'Content-Type: text/xml' + "\r\n\r\n"
    end =  "\r\n" + '------' + "\r\n"
    xmlBody = f"""
    <testset xmlns="http://cpee.org/ns/properties/2.0">
  <executionhandler>ruby</executionhandler>
  <dataelements/>
  <endpoints>
    <teil1>http://131.130.122.25:9302/inventory/cpus/{cpu}</teil1>
    <timeout>http://gruppe.wst.univie.ac.at/~mangler/services/timeout.php</timeout>
    <teil2>http://131.130.122.25:9302/inventory/cpucoolers/{cpuCooler}</teil2>
    <teil3>http://131.130.122.25:9302/inventory/ram/{ram}</teil3>
    <teil4>http://131.130.122.25:9302/inventory/gpus/{gpu}</teil4>
    <progress>http://131.130.122.25:9302/inventory/status</progress>
    <correlation>http://131.130.122.25:9302/correlator</correlation>
    <produzieren>http://cpee.org:9350</produzieren>
  </endpoints>
  <attributes>
    <info>IOP Production - a11946646</info>
    <modeltype>CPEE</modeltype>
    <theme>preset</theme>
  </attributes>
  <description>
    <description xmlns="http://cpee.org/ns/description/1.0">
      <manipulate id="man">
        data.pid = Digest::MD5.hexdigest(Kernel::rand().to_s)
      </manipulate>
      <parallel wait="-1" cancel="last">
        <parallel_branch pass="" local="">
          <call id="a11" endpoint="teil1">
            <parameters>
              <label>amount part1</label>
              <method>:get</method>
              <arguments/>
              <_context_data_analysis>
                <probes/>
                <ips/>
              </_context_data_analysis>
              <report>
                <url/>
              </report>
            </parameters>
            <code>
              <prepare/>
              <finalize output="result">data.teil1 = result["amount"] - 1</finalize>
              <update output="result"/>
              <rescue output="result"/>
            </code>
            <annotations>
              <_timing>
                <_timing_weight/>
                <_timing_avg/>
                <explanations/>
              </_timing>
              <_notes>
                <_notes_general/>
              </_notes>
            </annotations>
            <input/>
            <output/>
            <implementation>
              <description/>
            </implementation>
            <code>
              <description/>
            </code>
          </call>
          <call id="a21" endpoint="teil1">
            <parameters>
              <label>set amount part1</label>
              <method>:put</method>
              <arguments>
                <amount>!data.teil1</amount>
              </arguments>
              <_context_data_analysis>
                <probes/>
                <ips/>
              </_context_data_analysis>
              <report>
                <url/>
              </report>
            </parameters>
            <code>
              <prepare/>
              <finalize output="result"/>
              <update output="result"/>
              <rescue output="result"/>
            </code>
            <annotations>
              <_timing>
                <_timing_weight/>
                <_timing_avg/>
                <explanations/>
              </_timing>
              <_notes>
                <_notes_general/>
              </_notes>
            </annotations>
            <input/>
            <output/>
            <implementation>
              <description/>
            </implementation>
            <code>
              <description/>
            </code>
          </call>
        </parallel_branch>
        <parallel_branch pass="" local="">
          <call id="a12" endpoint="teil2">
            <parameters>
              <label>amount part2</label>
              <method>:get</method>
              <arguments/>
              <_context_data_analysis>
                <probes/>
                <ips/>
              </_context_data_analysis>
              <report>
                <url/>
              </report>
            </parameters>
            <code>
              <prepare/>
              <finalize output="result">data.teil2 = result["amount"] - 1</finalize>
              <update output="result"/>
              <rescue output="result"/>
            </code>
            <annotations>
              <_timing>
                <_timing_weight/>
                <_timing_avg/>
                <explanations/>
              </_timing>
              <_notes>
                <_notes_general/>
              </_notes>
            </annotations>
            <input/>
            <output/>
            <implementation>
              <description/>
            </implementation>
            <code>
              <description/>
            </code>
          </call>
          <call id="a22" endpoint="teil2">
            <parameters>
              <label>set amount part2</label>
              <method>:put</method>
              <arguments>
                <amount>!data.teil2</amount>
              </arguments>
              <_context_data_analysis>
                <probes/>
                <ips/>
              </_context_data_analysis>
              <report>
                <url/>
              </report>
            </parameters>
            <code>
              <prepare/>
              <finalize output="result"/>
              <update output="result"/>
              <rescue output="result"/>
            </code>
            <annotations>
              <_timing>
                <_timing_weight/>
                <_timing_avg/>
                <explanations/>
              </_timing>
              <_notes>
                <_notes_general/>
              </_notes>
            </annotations>
            <input/>
            <output/>
            <implementation>
              <description/>
            </implementation>
            <code>
              <description/>
            </code>
          </call>
        </parallel_branch>
        <parallel_branch pass="" local="">
          <call id="a13" endpoint="teil3">
            <parameters>
              <label>amount part3</label>
              <method>:get</method>
              <arguments/>
              <_context_data_analysis>
                <probes/>
                <ips/>
              </_context_data_analysis>
              <report>
                <url/>
              </report>
            </parameters>
            <code>
              <prepare/>
              <finalize output="result">data.teil3 = result["amount"] - 1</finalize>
              <update output="result"/>
              <rescue output="result"/>
            </code>
            <annotations>
              <_timing>
                <_timing_weight/>
                <_timing_avg/>
                <explanations/>
              </_timing>
              <_notes>
                <_notes_general/>
              </_notes>
            </annotations>
            <input/>
            <output/>
            <implementation>
              <description/>
            </implementation>
            <code>
              <description/>
            </code>
          </call>
          <call id="a23" endpoint="teil3">
            <parameters>
              <label>set amount part3</label>
              <method>:put</method>
              <arguments>
                <amount>!data.teil3</amount>
              </arguments>
              <_context_data_analysis>
                <probes/>
                <ips/>
              </_context_data_analysis>
              <report>
                <url/>
              </report>
            </parameters>
            <code>
              <prepare/>
              <finalize output="result"/>
              <update output="result"/>
              <rescue output="result"/>
            </code>
            <annotations>
              <_timing>
                <_timing_weight/>
                <_timing_avg/>
                <explanations/>
              </_timing>
              <_notes>
                <_notes_general/>
              </_notes>
            </annotations>
            <input/>
            <output/>
            <implementation>
              <description/>
            </implementation>
            <code>
              <description/>
            </code>
          </call>
        </parallel_branch>
        <parallel_branch pass="" local="">
          <call id="a14" endpoint="teil4">
            <parameters>
              <label>amount part4</label>
              <method>:get</method>
              <arguments/>
              <_context_data_analysis>
                <probes/>
                <ips/>
              </_context_data_analysis>
              <report>
                <url/>
              </report>
            </parameters>
            <code>
              <prepare/>
              <finalize output="result">data.teil4 = result["amount"] - 1</finalize>
              <update output="result"/>
              <rescue output="result"/>
            </code>
            <annotations>
              <_timing>
                <_timing_weight/>
                <_timing_avg/>
                <explanations/>
              </_timing>
              <_notes>
                <_notes_general/>
              </_notes>
            </annotations>
            <input/>
            <output/>
            <implementation>
              <description/>
            </implementation>
            <code>
              <description/>
            </code>
          </call>
          <call id="a24" endpoint="teil4">
            <parameters>
              <label>set amount part4</label>
              <method>:put</method>
              <arguments>
                <amount>!data.teil4 </amount>
              </arguments>
              <_context_data_analysis>
                <probes/>
                <ips/>
              </_context_data_analysis>
              <report>
                <url/>
              </report>
            </parameters>
            <code>
              <prepare/>
              <finalize output="result"/>
              <update output="result"/>
              <rescue output="result"/>
            </code>
            <annotations>
              <_timing>
                <_timing_weight/>
                <_timing_avg/>
                <explanations/>
              </_timing>
              <_notes>
                <_notes_general/>
              </_notes>
            </annotations>
            <input/>
            <output/>
            <implementation>
              <description/>
            </implementation>
            <code>
              <description/>
            </code>
          </call>
        </parallel_branch>
      </parallel>
      <call id="a3" endpoint="produzieren">
        <parameters>
          <label>produce part</label>
          <method>:post</method>
          <arguments>
            <delegate>!endpoints.progress</delegate>
            <async>!endpoints.correlation</async>
            <pid>!data.pid</pid>
          </arguments>
          <_context_data_analysis>
            <probes/>
            <ips/>
          </_context_data_analysis>
          <report>
            <url/>
          </report>
        </parameters>
        <code>
          <prepare/>
          <finalize output="result"/>
          <update output="result"/>
          <rescue output="result"/>
        </code>
        <annotations>
          <_timing>
            <_timing_weight/>
            <_timing_avg/>
            <explanations/>
          </_timing>
          <_notes>
            <_notes_general/>
          </_notes>
        </annotations>
        <input/>
        <output/>
        <implementation>
          <description/>
        </implementation>
        <code>
          <description/>
        </code>
      </call>
      <loop mode="pre_test" condition="data.progress != 'FINITO'">
        <call id="a4" endpoint="correlation">
          <parameters>
            <label>wait for progress</label>
            <method>:post</method>
            <arguments>
              <pid>!data.pid</pid>
            </arguments>
            <_context_data_analysis>
              <probes/>
              <ips/>
            </_context_data_analysis>
            <report>
              <url/>
            </report>
          </parameters>
          <code>
            <prepare/>
            <finalize output="result">p result;data.progress = result["progress"]</finalize>
            <update output="result"/>
            <rescue output="result"/>
          </code>
          <annotations>
            <_timing>
              <_timing_weight/>
              <_timing_avg/>
              <explanations/>
            </_timing>
            <_notes>
              <_notes_general/>
            </_notes>
          </annotations>
          <input/>
          <output/>
          <implementation>
            <description/>
          </implementation>
          <code>
            <description/>
          </code>
        </call>
      </loop>
    </description>
  </description>
  <transformation>
    <description type="copy"/>
    <dataelements type="none"/>
    <endpoints type="none"/>
    </transformation>
    </testset>
    """

    body = start + xmlBody + end

    response = requests.post(url, data=body, headers=headers)

    with open('log.txt', 'a') as logfile:
        timestamp = datetime.now()
        logfile.write(f"INSTANTIATED CPEE | {timestamp.strftime('%d/%m/%Y %H:%M:%S')} | HEADERS {response.headers} | BODY | {response.json()}\n")
    logfile.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9302)