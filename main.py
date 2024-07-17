import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
#from llama_index.core import
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("How long my presentation of a project needs to be ?")
print(response)