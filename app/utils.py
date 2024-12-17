from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def prepare_texts(df):
    """
    Prepare text data for embedding

    :return: List of processed text snippets
    """
    texts = []

    # Example of extracting non-copyrighted information
    for _, row in df.iterrows():
        # Create descriptive text about the song
        text = f"Song {row.get('Song Name', 'Unknown')} from the album {row.get('Album', 'Unknown')} " \
               f"has lyrics {row.get('Lyrics', 'Unknown')} "
        texts.append(text)

    return texts

def create_vectorstore(texts, embeddings):
    """
    Create a vector store from the prepared texts

    :return: Chroma vector store
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    splits = text_splitter.split_documents(
        [Document(page_content=text) for text in texts]
    )

    return Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
    )
