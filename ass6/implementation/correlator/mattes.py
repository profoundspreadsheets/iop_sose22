from cgi import test
import requests
from flask import Flask, request, Response

from datetime import datetime
import random
import json

@app.route('/api/v1/correlator', methods=["POST", "GET"])
def correlator():
    process_ = bool(False)
    header = request.headers
    # print("Current header: ", header)

    if header.get('Content-Id') == "UsbC4Eva":
        print("Erfolgreich in CPEE Instance Erstellung reingegangen")
        request_body = request.json
        request_form = request.form
        # print("reqeust_form: ", request_form)
        # print("Header from Donatello/CPEE: ", header)

        first_key = list(request_body.keys())[0]
        second_key = list(request_body.keys())[1]
        third_key = list(request_body.keys())[2]
        fourth_key = list(request_body.keys())[3]

        xmlstr = f'''<testset xmlns="http://cpee.org/ns/properties/2.0">
              <executionhandler>ruby</executionhandler>
              <dataelements/>
              <endpoints>
                <teil1>http://131.130.122.25:9092/api/v1/inventory/cpus/{first_key}</teil1>
                <timeout>http://gruppe.wst.univie.ac.at/~mangler/services/timeout.php</timeout>
                <teil2>http://131.130.122.25:9092/api/v1/inventory/cpu_coolers/{second_key}</teil2>
                <teil3>http://131.130.122.25:9092/api/v1/inventory/mainboards/{third_key}</teil3>
                <teil4>http://131.130.122.25:9092/api/v1/inventory/ram/{fourth_key}</teil4>
                <progress>http://131.130.122.25:9092/api/v1/progress</progress>
                <correlation>http://131.130.122.25:9092/api/v1/correlator</correlation>
                <produzieren>http://cpee.org:9350</produzieren>
              </endpoints>
              <attributes>
                <info>IOP Production - a12024366</info>
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
                '''

        xml_file = open("production.xml", "w")
        xml_file.write(xmlstr)
        xml_file.close()

        header_data = dict(header)
        body_data = dict(request_body)

        body_data.update(header_data)
        # set timestamp
        gmtime_ = time.gmtime()
        timestamp = calendar.timegm(gmtime_)

        with open("logs/log.json", "r+") as file:
            data = json.load(file)
            data[f"{timestamp}"] = body_data
            file.seek(0)
            json.dump(data, file)
            process_ = bool(True)

        if process_:
            url = "https://wwwlab.cs.univie.ac.at/~mattesb98/iop22-6/start_cpee.php"

            # send get request to cpee
            requests.get(url)

        return "Correlator works so far"

    if header.get('Content-Id') is None:
        print("Im inside the one and only endpoint")
        # collect data from cpee request
        callback_id = header["Cpee-Callback-Id"]
        gmtime_ = time.gmtime()
        timestamp = calendar.timegm(gmtime_)
        callback_url = header["Cpee-Callback"]
        cpee_activity = header["Cpee-Activity"]
        cpee_uuid = header["Cpee-Instance-Uuid"]
        cpee_instance = header["Cpee-Instance"]
        pid = request.form.get("pid")

        print(header)

        # write collected cpee data into database
        process_finished = random.randint(0, 1)

        # create insert command to db
        connection = get_db_connection()
        cur = connection.cursor()
        cur.execute(
            "INSERT INTO cpee_requests (Cpee_Callback_id, created, Cpee_Callback_url,Cpee_Activity, Cpee_uuid, Cpee_instance, Process_finished, pid) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
            f"{callback_id}", f"{timestamp}", f"{callback_url}", f"{cpee_activity}", f"{cpee_uuid}", f"{cpee_instance}",
            int(process_finished), f"{pid}")
        )

        connection.commit()
        connection.close()

        # check if the process is finished -> request on production table
        conn = get_db_connection()
        cursor = conn.cursor()
        finito_check = []
        progress_state = cursor.execute(f"SELECT progress_state FROM production_requests WHERE pid='{pid}'").fetchall()
        conn.close()
        print("- Requested progress states: ", progress_state)
        print("- Single progress state: ", progress_state)

        # iterate over list of progress states
        for i in progress_state:
            finito_check.append(json.dumps(i))

        print("CHECK ARRAY 1 and type: ", finito_check, type(finito_check))
        com_string = '["FINITO"]'

        if com_string in finito_check:
            print("Production is finished")
            # callback holen von der aktuellsten und zugehörigen CPEE instance
            # check if the process is finished -> request on production table
            test_arr = []
            conn = get_db_connection()
            cursor = conn.cursor()
            callback = cursor.execute(
                f"SELECT Cpee_Callback_url, created FROM cpee_requests WHERE pid='{pid}' ORDER BY created DESC LIMIT 1").fetchall()
            conn.close()

            for l in callback:
                test_arr.append(json.dumps(l))

            print("test arr: ", test_arr)

            string_without_brackets = re.sub(r"[\[\]]", '', test_arr[0])
            callback_url_request = string_without_brackets.split(",")[0]
            callback_url_request = callback_url_request.replace('"', '')
            print("Callback URL String: ",callback_url_request)
            #callback_url_request = callback_url_request[:-1]
            callback_url_request = str(callback_url_request)
            # define response body
            response_body = {
                "progress" : 'FINITO'
            }

            # define header
            cpee_header = {
                'Content-Type': 'application/json',
                'CPEE-CALLBACK': 'true'
            }

            #requests.put(callback_url_request, data=response_body, headers=cpee_header)
            #time.sleep(1)
            #return app.response_class(status=200)
            return app.response_class(json.dumps(response_body), mimetype="application/json")

        else:
            print("Production not finished")
            response_body = {
                "progress": "INTERMEDIATE"
            }

            cpee_header = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate',
                'Content-type': 'application/json',
            }
            time.sleep(3.3)
            return app.response_class(json.dumps(response_body), mimetype="application/json")

    if header.get('Content-Id') == "producing":

        print("Producing Anfrage ist erfolgreich eingegangen/verarbeitet worden")
        request_body = request.json
        print("- Producing Request Body: ", request_body)
        progress_state = request_body.get("progress")
        completion = request_body.get("completion")
        pid = request_body.get("pid")
        gmtime_ = time.gmtime()
        timestamp = calendar.timegm(gmtime_)

        # Anfrage, ob es zu der gelieferten PID noch keine CAllback URL gibt

        # create insert command to production table
        connection = get_db_connection()
        cur = connection.cursor()
        cur.execute("INSERT INTO production_requests (pid, created, completion,progress_state) VALUES (?, ?, ?, ?)",
                    (f"{pid}", f"{timestamp}", int(completion), f"{progress_state}"))

        connection.commit()
        connection.close()
        # if progress_state == "FINITO":
        #
        #     cpee_header = {
        #         'Accept': '*/*',
        #         'Accept-Encoding': 'gzip, deflate',
        #         'Content-type': 'application/json',
        #     }
        #
        #     callback_url = inform_cpee(pid)
        #     requests.put(callback_url, json={"progress": progress_state}, headers=cpee_header)
        #
        #     # check if the process is finished -> request on production table
        #     conn = get_db_connection()
        #     cursor = conn.cursor()
        #     production_data = cursor.execute(f"SELECT * FROM production_requests WHERE pid='{pid}'").fetchall()
        #     cpee_data = cursor.execute(f"SELECT * FROM cpee_requests WHERE pid='{pid}'").fetchall()
        #     conn.close()
        #
        #     print("- Production Table Data: ", json.dumps(production_data))
        #     print("- Cpee Table Data: ", json.dumps(cpee_data))

        return "works"