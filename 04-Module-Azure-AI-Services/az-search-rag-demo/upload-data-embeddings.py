from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI
import os
import json
from dotenv import load_dotenv

# Load env variables
load_dotenv()

endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
key = os.getenv("AZURE_SEARCH_KEY")

search_client = SearchClient(endpoint, "rag-demo-index", AzureKeyCredential(key))

openai_client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-01"
)

## verify env variables
# print("ENDPOINT:", os.getenv("AZURE_OPENAI_ENDPOINT"))
# print("DEPLOYMENT:", os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"))

# Load data
with open("data.json") as f:
    docs = json.load(f)

def get_embedding(text):
    response = openai_client.embeddings.create(
        model=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
        input=text
    )
    return response.data[0].embedding

# Add embeddings
for doc in docs:
    doc["contentVector"] = get_embedding(doc["content"])

# Upload
result = search_client.upload_documents(docs)

for r in result:
    print(r.succeeded, r.key, r.error_message)

print("Documents uploaded!")