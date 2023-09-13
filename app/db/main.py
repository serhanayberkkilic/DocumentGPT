import pinecone


class Database:

    def __init__(self):
        api_key = "5d260f06-d98a-4536-bbdc-f742a62e0103"
        pinecone.init(api_key=api_key,environment='gcp-starter')

    def createIndex(self, name):
        pinecone.create_index(name)
    
    def deleteIndex(self, name):
        pinecone.delete_index(name)
    
    def listIndexes(self):
        return self.pinecone.list_indexes()
    
    def insert(self, indexName, data):
        pinecone.Index(indexName).upsert([data])
    
    def search(self, indexName, vector,top_k=3):
        return pinecone.Index(indexName).query(vector=vector, top_k=top_k,include_metadata=True)

