from flask import Flask, render_template,request,url_for,redirect,jsonify
import ssl
from elasticsearch import Elasticsearch, RequestsHttpConnection
from elasticsearch.connection import create_ssl_context
import os
import warnings
app = Flask(__name__)


warnings.filterwarnings("ignore")
app = Flask(__name__)

context = create_ssl_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
es = Elasticsearch(
    ['tux-es1.cci.drexel.edu','tux-es2.cci.drexel.edu','tux-es3.cci.drexel.edu'],
     http_auth=('pk593', 'wah9eReed4ie'),
     scheme="https",
     port=9200,
     ssl_context = context,)
DEBUG = os.environ.get("FLASK_DEBUG") == "1"
app.config.update(DEBUG=DEBUG, JSON_PRETTYPRINT_REGULAR=DEBUG)
@app.route('/')
def main():
    return render_template('search.html')
@app.route('/search', methods=['GET','POST'])
def search():
    keywords = request.form['input']
    query_body = {
        "query": {
            "bool":{
                "must":[{
                     "multi_match": {
                        "query": keywords,
                        "fields": ["question_content","processed_title"]
                         }}],
                "should":{
                    "rank_feature": {
                        "field":"overall_scores",
                        "sigmoid":{"pivot": 10, "exponent": 0.6}
                 }

             }
        }
    }
    }
    res = es.search(index="pk593_info624_201904_finalproject",  body=query_body)
    print(res)
    return render_template("results.html", res = res)

if __name__ == '__main__':
    app.run()
