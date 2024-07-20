import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_cohere import CohereEmbeddings
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv
from collections import deque

class DocumentResponder:
    def __init__(self, pdf_path):
        load_dotenv()
        self.pdf_path = pdf_path
        self.cohere_api_key = os.getenv("COHERE_API_KEY")
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.vectorstore = None
        self.chat = None
        self.retrieval_chain = None
        self.prompt_template = None
        self.history = deque(maxlen=5)
        self.initialize()

    def initialize(self):
        loader = PyPDFLoader(self.pdf_path)
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=500
        )
        splits = text_splitter.split_documents(docs)

        embeddings = CohereEmbeddings(
            model="embed-english-light-v3.0", cohere_api_key=self.cohere_api_key
        )
        self.vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

        self.chat = ChatGroq(
            temperature=0.2,
            groq_api_key=self.groq_api_key,
            model_name="llama3-70b-8192",
        )

        template = """
        You have a corpus containing information about a business that sells wines. They have their own website which customers often visit. 

        The chatbot is deployed on the business's website to provide quick and accurate responses based on this corpus. 
        
        It should not use information outside this corpus. If a user's query is not addressed by the information in the corpus, the chatbot should inform them to contact the business directly.

        Use the following pieces of context to answer the question at the end. If the answer is not found in the corpus, respond with 'I am unable to help you, please contact the business directly.' and don't mention about your corpus to the customer. And dogs allowed too.

        Relevant Information:

        {history}

        {context}

        Question: {input}

        Helpful Answer:
        """

        self.prompt_template = PromptTemplate.from_template(template)

        document_chain = create_stuff_documents_chain(self.chat, self.prompt_template)
        retriever = self.vectorstore.as_retriever()
        self.retrieval_chain = create_retrieval_chain(retriever, document_chain)

    def response(self, user_query, history):
        self.prompt = self.prompt_template.format(
            history='\n'.join(f"Q: {q}\nA: {a}" for q, a in self.history), context="context", input=user_query
        )
        res = self.retrieval_chain.invoke({"input": user_query, "history": history})
        self.history.append({"question": user_query, "answer": res['answer']})
        return res["answer"]
