import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from azure.core.credentials import AzureKeyCredential

load_dotenv()

# Azure AI Search client
search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name="rag-demo-index",
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
)

# Azure OpenAI client
openai_client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-05-01-preview"
)

def get_embedding(text):
    response = openai_client.embeddings.create(
        model=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
        input=text
    )
    return response.data[0].embedding

def search_documents(query):
    embedding = get_embedding(query)

    vector_query = VectorizedQuery(
        vector=embedding,
        k_nearest_neighbors=3,
        fields="contentVector"
    )

    results = search_client.search(
        search_text=None,
        vector_queries=[vector_query]
    )

    return [doc["content"] for doc in results]

def generate_answer(query, context_docs):
    context = "\n".join(context_docs)

    prompt = f"""
    Answer the question using only the context below:

    Context:
    {context}

    Question:
    {query}
    """

    response = openai_client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

# Test OpenAI connection
response = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What is RAG?"}]
)

print(response.choices[0].message.content)

# Main logic - retrieve relevant documents and generate answer
# query = "What is RAG?"

# docs = search_documents(query)
# answer = generate_answer(query, docs)

# print("Answer:\n", answer)