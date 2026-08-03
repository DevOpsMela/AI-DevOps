from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchField
from azure.search.documents.indexes.models import (
    SearchIndex, SimpleField, SearchableField, VectorSearch,
    HnswAlgorithmConfiguration, VectorSearchProfile
)
from azure.core.credentials import AzureKeyCredential
import os
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
key = os.getenv("AZURE_SEARCH_KEY")

index_client = SearchIndexClient(endpoint, AzureKeyCredential(key))

index = SearchIndex(
    name="rag-demo-index",
fields=[
    SimpleField(name="id", type="Edm.String", key=True),
    SearchableField(name="content", type="Edm.String"),
    SearchableField(name="category", type="Edm.String"),
    SearchField(   # ✅ FIXED
        name="contentVector",
        type="Collection(Edm.Single)",
        searchable=True,
        vector_search_dimensions=1536,
        vector_search_profile_name="my-vector-profile"
    )
],
    vector_search=VectorSearch(
        profiles=[VectorSearchProfile(
            name="my-vector-profile",
            algorithm_configuration_name="my-algo"
        )],
        algorithms=[HnswAlgorithmConfiguration(name="my-algo")]
    )
)

index_client.create_or_update_index(index)
print("Index created!")