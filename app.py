import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


# function to get response from my Llama-2 model
def getLlamaresponse(input_text, no_words, blog_style):
    # calling my Llama-2
    llm = CTransformers(model = 'models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type = 'llama',
                        config = {'max_new_tokens' : 256,
                                  'temperature' :0.01}
    ) 



# Prompt Template 
    template = """
    Write a blog for {blog_style} job profile for a topic {input_text}
    within {no_words} words
    """

    prompt = PromptTemplate(input_variables = ["blog_style", "input_text", 'no_words'],
                        template= template)



# Generate the response from the llama 2 model
    response = llm(prompt.format(blog_style = blog_style, input_text = input_text, no_words = no_words))
    print(response)
    return response



## Set streamlit

st.set_page_config(
    page_title = "Generate Blog",
    page_icon = "A",
    layout = "centered",
    initial_sidebar_state = "collapsed",
)
st.header("Generate the Blogs")

input_text = st.text_input("Enter the Blog Topic") # Creating the input box

# Creating to more columns for additional 2 fields
col1, col2 = st.columns([5,5])

with col1: 
    no_words = st.text_input("No of Words")

with col2:
    blog_style = st.selectbox("Writing the blog for", ('Researchers','DataScientist', 'Common People'), index = 0)

submit = st.button("Generate")


# Final Response
if submit : 
    st.write(getLlamaresponse(input_text, no_words, blog_style))
