from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

load_dotenv()
embeddings = OpenAIEmbeddings()

video_url="https://www.youtube.com/watch?v=lG7Uxts9SXs&t=410s"

def create_vector_db_from_youtube_url(video_url: str)-> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)
    
    db = FAISS.from_documents(docs, embeddings)
    print(docs)
    return db
    

def get_response_from_query(db, query, k=4):
    print('query', query)
     
    # text-davinci-003 can handle up to 4097 tokens. Setting the chunksize to 1000 and k to 4 maximizes
    # the number of tokens to analyze.
    
    
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])
    
    
    llm = OpenAI(model ="text-davinci-003")
    
    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
        You are a helpful assistant that can answer questions about youtube videos 
        based on the video's transcript.
        
        Answer the following question: {question}
        By searching the following video transcript: {docs}
        
        Only use the factual information from the transcript to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        
        Your answers should be verbose and detailed.
        """,
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    response = chain.run(question=query, docs=docs_page_content)
    response = response.replace("\n", "")
    return response, docs

# print(create_vector_db_from_youtube_url(video_url))