from calendar import c
from cgi import test
import mimetypes
from time import time
import requests
from flask import Flask, request, Response

from datetime import datetime
import random
import json

app = Flask(__name__)


@app.route('/inventory')
def getInventory():
    inventory = json.load(open('inventory.json'))
    return app.response_class(json.dumps(inventory), mimetype='application/json')


@app.route('/inventory/<component>')
def getInventoryCPUs(component):
    inventory = json.load(open('inventory.json'))
    partslist = inventory[component]
    return app.response_class(json.dumps(partslist), mimetype='application/json')


@app.route('/inventory/<component>/<componentName>', methods=['GET', 'PUT'])
def getInventoryPartCPUCoolers(component, componentName):
    with open('inventory.json', 'r+') as data:
        inventory = json.load(data)
        if request.method == 'PUT':
            newAmount = request.form.get('amount')  # is immutableMultiDict
            inventory[component][componentName] = int(newAmount)
            data.seek(0)
            json.dump(inventory, data, indent=4)
            data.truncate()
            with open('log.txt', 'a') as logfile:
                timestamp = datetime.now()
                logfile.write(
                    f"INVENTORY UPDATE | {request.method} | COMPONENT {component}/{componentName} | NEW AMOUNT {newAmount} | {timestamp.strftime('%d/%m/%Y %H:%M:%S')} |\n")
            logfile.close()
            return Response(status=200)
        partslist = inventory[component]
        countPart = partslist.get(componentName, -1)
        response = {
            "amount": countPart
        }

    data.close()
    return app.response_class(json.dumps(response), mimetype='application/json')


@app.route('/inventory/createOrder')
def createOrder():
    with open('inventory.json') as file:
        inventory = json.load(file)
        cpus = inventory['cpus']
        cpuCoolers = inventory['cpu_coolers']
        gpus = inventory['gpus']
        ram = inventory['ram']
        response = {
            "cpu": random.choice(list(cpus.keys())),
            "cpu_cooler": random.choice(list(cpuCoolers.keys())),
            "ram": random.choice(list(ram.keys())),
            "gpu": random.choice(list(gpus.keys()))
        }
        file.close()
    return app.response_class(json.dumps(response), mimetype='application/json')


@app.route('/progress')
def getProgressSteps():
    with open('progress.json', 'r') as data:
        json_ = json.load(data)
    data.close()
    return app.response_class(json.dumps(json_), mimetype='application/json')


@app.route('/progress/<step>')
def getProgressStep(step):
    with open('progress.json', 'r') as data:
        json_ = json.load(data)
        progress = json_[int(step)]
    data.close()
    return app.response_class(json.dumps(progress), mimetype='application/json')

@app.route('/correlator', methods=['GET', 'POST'])
def newCorrelator():
  headers = dict(request.headers)
  if headers.get('Content-Id') == 'UsbC4Eva':
    body = dict(request.get_json())
    instantiateProcess(requestMethod=request.method, requestHeaders=headers,requestBody=body)
  elif headers.get('Content-Id') == 'producing':
    body = dict(request.get_json())
    updateInstanceStore(body)
  else:
    #check if instance finished i guess
    pid = request.form.get("pid")
    with open('instancestore.json', 'r+') as file:
      instancestore = json.load(file)
      processFinished = False
      try:
        for entry in instancestore[pid]:
          if entry['progress'] == 'FINITO':
            processFinished = True
            break
      except:
        # Dangerous, needs proper error handling if pid not in store
        processFinished = False
    file.close()
    if processFinished:
      responseBody = {
        "progress": "FINITO"
      }
      return app.response_class(json.dumps(responseBody), mimetype="application/json")
    else:
      responseBody = {
        "progress": "INTERMEDIATE"
      }
      return app.response_class(json.dumps(responseBody), mimetype="application/json")
  return app.response_class("kid named finger")

def updateInstanceStore(requestBody):
  pid = requestBody.get('pid')
  completion = requestBody.get('completion')
  progress = requestBody.get('progress')
  with open('instancestore.json', 'r+') as file:
    timestamp = datetime.now()
    instanceStore = json.load(file)
    if not pid in instanceStore:
      instanceStore[pid] = [{
          "progress": progress,
          "completion": completion,
          "timestamp": timestamp.strftime('%d/%m/%Y %H:%M:%S')
        }]
    else:
      instanceStore[pid].append({
        "progress": progress,
        "completion": completion,
        "timestamp": timestamp.strftime('%d/%m/%Y %H:%M:%S')
      })
    file.seek(0)
    json.dump(instanceStore, file, indent=4)
  file.close()
  with open('log.txt', 'a') as logfile:
    timestamp = datetime.now()
    logfile.write(f"UPDATING INSTANCESTORE | {pid} | {progress} | {completion} | {timestamp.strftime('%d/%m/%Y %H:%M:%S')}\n")
  logfile.close()

def instantiateProcess(requestMethod, requestHeaders, requestBody):
  cpu = requestBody.get('cpu')
  cpuCooler = requestBody.get('cpu_cooler')
  ram = requestBody.get('ram')
  gpu = requestBody.get('gpu')
  with open('log.txt', 'a') as logfile:
      timestamp = datetime.now()
      logfile.write(
          f"CREATE | {requestMethod} | HEADERS {requestHeaders} | BODY | {requestBody} | {timestamp.strftime('%d/%m/%Y %H:%M:%S')}\n")
  logfile.close()

  url = "https://cpee.org/flow/start/xml/"
  headers = {'Content-Type': 'multipart/form-data;boundary=----'}
  start = '------' + "\r\n" + 'Content-Disposition: form-data; name="behavior"' + "\r\n\r\n" + 'fork_running' + "\r\n" + \
        '------' + "\r\n" + 'Content-Disposition: form-data; name="xml"' + \
            "\r\n" + 'Content-Type: text/xml' + "\r\n\r\n"
  end = "\r\n" + '------' + "\r\n"
  xmlBody = f"""
    <testset xmlns="http://cpee.org/ns/properties/2.0">
  <executionhandler>ruby</executionhandler>
  <dataelements/>
  <endpoints>
    <teil1>http://131.130.122.25:9302/inventory/cpus/{cpu}</teil1>
    <timeout>http://gruppe.wst.univie.ac.at/~mangler/services/timeout.php</timeout>
    <teil2>http://131.130.122.25:9302/inventory/cpu_coolers/{cpuCooler}</teil2>
    <teil3>http://131.130.122.25:9302/inventory/ram/{ram}</teil3>
    <teil4>http://131.130.122.25:9302/inventory/gpus/{gpu}</teil4>
    <progress>http://131.130.122.25:9302/progress</progress>
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
