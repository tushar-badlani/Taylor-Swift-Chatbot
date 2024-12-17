import pandas as pd
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from app.utils import prepare_texts, create_vectorstore

# Load the CSV file
df = pd.read_csv("Taylor_Swift_Genius_Data.csv")

# Prepare text for embedding
texts = prepare_texts(df)

load_dotenv()

# Initialize Gemini embedding and language model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    convert_system_message_to_human=True,
)

# Create vector store

vectorstore = create_vectorstore(texts, embeddings)

# Set up memory and retrieval chain




