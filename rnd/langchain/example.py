from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# Load and split documents
loader = TextLoader("sample.txt")  # Load from a text file
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Create embeddings and store in FAISS
embeddings = OpenAIEmbeddings()  # Uses OpenAI for text embeddings
vector_store = FAISS.from_documents(docs, embeddings)

# Create a retriever and a QA chain
retriever = vector_store.as_retriever()
llm = ChatOpenAI(model_name="gpt-4", temperature=0.2)

qa_chain = RetrievalQA(llm=llm, retriever=retriever)

# Ask a question
query = "What does the document say about AI?"
response = qa_chain.run(query)

print("Answer:", response)
