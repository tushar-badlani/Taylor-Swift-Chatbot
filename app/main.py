from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from .chat import qa_chain
from .schemas import Query, Response

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#
# models.Base.metadata.create_all(bind=engine)
#

@app.get("/")
async def root():
    return {"message": "welcome to my api!!"}


@app.post("/chat", response_model= Response)
async def chat(query: Query):

    system_prompt = """You are Taylor Swift, speaking directly to a fan about your music, life, and creative journey. 
            Speak in first-person, be personal, detailed, and passionate. Share insights about your music 
            as if you're having an intimate conversation with a close friend."""
    result = qa_chain({
        "question": system_prompt + query.query,
    })

    return {"answer": result['answer']}

@app.post("/find", response_model= Response)
async def find(query: Query):

    system_prompt = """You are a helpful assistant, you will be given a theme and you have to find the most relevant lyrics from the dataset."""
    result = qa_chain({
        "question": system_prompt + query.query,
    })

    return {"answer": result['answer']}