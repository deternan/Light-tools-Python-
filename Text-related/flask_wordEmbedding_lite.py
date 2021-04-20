# -*- coding: utf-8 -*-
'''
Flask RESTful API: /wordVector /wordSimilarity /similarWords
'''
import os
import sys
import json
import gensim
from flask import Flask, g, request, jsonify
from flask_cors import CORS, cross_origin

# If directly execute flask.py ,it will use this url
host = "10.120.138.46"
port = "5647"
model_file = "vec/wiki.zh.vec"


app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

model = gensim.models.KeyedVectors.load_word2vec_format(model_file, binary=False)

def result_to_json(in_list):
    in_json = json.loads('{"result": ""}')
    in_json['result'] = in_list
    in_json = json.dumps(in_json, ensure_ascii=False)
    return in_json


@app.route('/wordVector', methods=['GET', 'POST'])
def wv_get_vec():
    if request.method == 'GET':
        word = request.args.get('word', '').lower()
    elif request.method == 'POST':
        word = request.form.get('word', '').lower()

    if not word:
        raise MissingParameter('word')

    #Error handling: word absent from model
    if word not in model.vocab:
        raise OutOfVocabulary(word)

    try:
        wordVectors = model[word].tolist()  # array to list
        result_json = result_to_json(wordVectors)
        return result_json
    except:
        raise InternalError()

@app.route('/similarWords', methods=['GET', 'POST'])
def wv_most_similar():
    if request.method == 'GET':
        word = request.args.get('word', '').lower()
        num = request.args.get('num', 10)
    elif request.method == 'POST':
        word = request.form.get('word', '').lower()
        num = request.form.get('num', 10)

    if not word:
        raise MissingParameter('word')

    try:
        num = int(num)
    except:
        raise InvalidParameterValue('num')

    if num < 1 or num > 100:
        raise InvalidParameterValue('num')

    #Error handling: word absent from model
    if word not in model.vocab:
        raise OutOfVocabulary(word)

    resultList = model.most_similar(positive=[word], topn=num)
    result = []
    for pair in resultList:
        result.append({"word":pair[0], "score":pair[1]})
    result_json = result_to_json(result)
    return result_json


@app.route('/wordSimilarity', methods=['GET', 'POST'])
def wv_similarity():
    if request.method == 'GET':
        word1 = request.args.get('word1', '').lower()
        word2 = request.args.get('word2', '').lower()
    elif request.method == 'POST':
        word1 = request.form.get('word1', '').lower()
        word2 = request.form.get('word2', '').lower()

    if not word1:
        raise MissingParameter('word1')
    if not word2:
        raise MissingParameter('word2')

    #Error handling: word absent from model
    if word1 not in model.vocab:
        raise OutOfVocabulary(word1)
    if word2 not in model.vocab:
        raise OutOfVocabulary(word2)

    try:
        similarity = model.similarity(word1, word2)
        result_json = result_to_json(similarity)
        return result_json
    except:
        raise InternalError()

@app.route('/wordAnalogy', methods=['GET', 'POST'])
def wv_analogy():
    if request.method == 'GET':
        word1 = request.args.get('word1', '').lower()
        word2 = request.args.get('word2', '').lower()
        word3 = request.args.get('word3', '').lower()
        num = request.args.get('num', 10)
    elif request.method == 'POST':
        word1 = request.form.get('word1', '').lower()
        word2 = request.form.get('word2', '').lower()
        word3 = request.form.get('word3', '').lower()
        num = request.form.get('num', 10)

    #Error handling: null word
    if not word1:
        raise MissingParameter('word1')
    if not word2:
        raise MissingParameter('word2')
    if not word3:
        raise MissingParameter('word3')

    #Error handling: word absent from model
    if word1 not in model.vocab:
        raise OutOfVocabulary(word1)
    if word2 not in model.vocab:
        raise OutOfVocabulary(word2)
    if word3 not in model.vocab:
        raise OutOfVocabulary(word3)

    try:
        num = int(num)
    except:
        raise InvalidParameterValue('num')

    if num < 1 or num > 100:
        raise InvalidParameterValue('num')

    try:
        resultList = model.most_similar(positive=[word1, word3], negative=[word2], topn=num)
        result = []
        for pair in resultList:
            result.append({"word": pair[0], "score": pair[1]})
        result_json = result_to_json(result)
        return result_json
    except:
        raise InternalError()

# Handle custom exceptions
@app.errorhandler(Exception)
def CustomErrorHandle(e):
    response = {'error_code': e.error_code, 'error_message': e.error_message}
    return jsonify(response), e.code

@app.errorhandler(500)
def OtherErrorHandle(e):
    response = {'error_code':'InternalError', 'error_message':'Unknown internal error'}
    return jsonify(response), 500

class MissingParameter(Exception):
    def __init__(self, msg):
        self.code = 400
        self.error_code = 'MissingParameter'
        if msg:
            self.error_message = "Parameter '{}' is missing".format(msg)
        else:
            self.error_message = "Parameter is missing"

class InvalidParameterValue(Exception):
    def __init__(self, msg):
        self.code = 400
        self.error_code = 'InvalidParameterValue'
        if msg:
            self.error_message = "Parameter '{}' has invalid value".format(msg)
        else:
            self.error_message = "Invalid parameter value"

class InternalError(Exception):
    def __init__(self):
        self.code = 500
        self.error_code = 'InternalError'
        self.error_message = 'Unknown service error'

class OutOfVocabulary(Exception):
    def __init__(self, msg):
        self.code = 500
        self.error_code = 'OutOfVocabulary'
        if msg:
            self.error_message = "Word '{}' is out of vocabulary".format(msg)
        else:
            self.error_message = "Oout of vocabulary"

if __name__ == '__main__':
    print('Load word vector model...')
    app.run(host=host, port=port, threaded=True, processes=1)

