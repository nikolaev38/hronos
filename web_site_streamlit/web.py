import PyPDF2
import streamlit as st
from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from streamlit import file_uploader

callback = CallbackManager([StreamingStdOutCallbackHandler()])
llm = LlamaCpp(
    model_path="gemma-2-9b-it-q4_k_m.gguf",
    temperature=0.4,
    n_gpu_layers=50,
    n_batch=2048,
    n_ctx=2048,
    max_tokens=2048,
    top_p=1,
    callback_manager=callback,
)

template = """
    Carry out the summarization of this part of the scientific article. Describe it in one paragraph, in 1-3 short sentences. Speak clearly on the topic, without unnecessary phrases, without introductory words
    {text}
    
    SUMMARY SCIENTIFIC ARTICLE:
    """

promptT = PromptTemplate(template=template, input_variables=['text'])
chain = promptT | llm | StrOutputParser()

def calculate_cosine_similarity(reference_text, generated_summary):
    vectorizer = CountVectorizer().fit_transform([reference_text, generated_summary])
    vectors = vectorizer.toarray()
    similarity = cosine_similarity(vectors[0].reshape(1, -1), vectors[1].reshape(1, -1))
    similarity_percentage = similarity[0][0] * 100
    return similarity_percentage

def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text

def summarize_input_document(uploaded_file):
    file_text = extract_text_from_pdf(uploaded_file)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=4096, chunk_overlap=50)
    with st.expander("Оригинал"):
        st.markdown(file_text, unsafe_allow_html=True)
    st.write("Краткое содержание:")
    v = text_splitter.split_text(file_text)
    print('dlina', len(v))
    for i, chunk in enumerate(v, start=1):
        print(f'text {i}')
        st.write_stream(chain.stream( {'text': chunk} ))

def main():
    st.title("Суммаризация статей")
    file = file_uploader(label='Загрузите файл', type='pdf')
    if file:
        summarize_input_document(file)

    pass

if __name__ == "__main__":
    main()
