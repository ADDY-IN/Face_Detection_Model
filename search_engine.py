#Elasticsearch indexing/search logic
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")
try:
    print("Connected:", es.info().get('cluster_name'))
except:
    print("Not connected")
