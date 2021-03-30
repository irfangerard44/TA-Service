import pickle
import pandas as pd
from sklearn import model_selection
import json
from flask import Flask, request,jsonify
from flask_cors import CORS, cross_origin
import sys
import re
import cleansingContent
import getDB
import parserGraph


filename = "C:\\Users\\eBdesk\\Documents\\Untitled Folder\\10k-with out stemming II\\10kdata-cluster-10.sav"
loaded_model = pickle.load(open(filename, 'rb'))
filename_stemming = "C:\\Users\\eBdesk\\Documents\\Untitled Folder\\10k-with stemming\\10kdata-cluster-10.sav"
loaded_model_stemming = pickle.load(open(filename_stemming, 'rb'))
app = Flask(__name__) 
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app)

@app.route('/newsClustering', methods=['GET'])
@cross_origin()
def clustering():
    stemming = request.args.get('stemming', default=None)
    data = getDB.getDataBase(request.args.get("size"),request.args.get("start"),request.args.get("end")).getData()
    dataCleansing = cleansingContent.cleasing(Data=data, token=stemming).cleansingData()
    res2 = None
    if stemming is None:
        res2 = loaded_model.fit_predict(dataCleansing)
        data['cluster'] = res2
        MessageModel = {
            'status':200,
            'message':'success',
            'data': parserGraph.parserDftoGraph(data).parse()
        }
    elif stemming == "true":
        res2 = loaded_model_stemming.fit_predict(dataCleansing)    
        data['cluster'] = res2
        MessageModel = {
            'status':200,
            'message':'success',
            'data': parserGraph.parserDftoGraph(data).parse()
        }
    else:
        MessageModel = {
            'status':500,
            'message':'failed',
            'data': None
        }
    return jsonify(MessageModel)

if __name__ == '__main__':
    app.run(host=sys.argv[1], port=sys.argv[2],threaded=True, debug=True)