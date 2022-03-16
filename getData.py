import json
import connectionToDB
from flask import jsonify

def getWardData(ward):
    try:
        release = []
        consumption = []
        connections = []
        demand = []
        savings = []
        legend_1 = []
        legend_2 = []
        ind_consumption = []
        map = []
        connection = connectionToDB.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM aqua_analytica_general where ward=\"" + ward + "\"")
        value = cursor.fetchone()
        res = dict(zip(cursor.column_names,value))
        for element in json.loads(res["relconconn"]):
            legend_1.append(element)
            release.append(json.loads(res["relconconn"])[element]["release"])
            consumption.append(json.loads(res["relconconn"])[element]["consumption"])
            connections.append(json.loads(res["relconconn"])[element]["connections"])
        for element in json.loads(res["future_demand"]):
            legend_2.append(element)
            demand.append(json.loads(res["future_demand"])[element]["demand"])
            savings.append(json.loads(res["future_demand"])[element]["savings"])
        for element in json.loads(res["ind_consumption"]):
            ind_consumption.append(json.loads(res["ind_consumption"])[element])
        for element in json.loads(res["map"]):
            map.append(json.loads(res["map"])[element])
        keys = ["ward","water_consumption","water_release","area","population","nrw","save","map","demand","savings","release","consumption","connections","ind_consumption","legend_1","legend_2"]
        values = [ward,res["water_consumption"],res["water_release"],res["area"],res["population"],res["nrw"],res["savings"],map,demand,savings,release,consumption,connections,ind_consumption,legend_1,legend_2]
        return dict(zip(keys,values))
    except Exception as e:
        print("Exception")
    finally:
        cursor.close()
        connection.close()