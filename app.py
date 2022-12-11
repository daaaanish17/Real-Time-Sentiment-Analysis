import streamlit as st
import analyzer

st.title('Sentiment Analysis')

temp = """
<div style="color:black; background-color:orange; padding: 10px; text-align:center ">
<h2 style="color:black">Real Time Sentiment Analysis</h2>
</div>

"""
st.markdown(temp, unsafe_allow_html=True)

text=st.text_input("", "", placeholder="Enter Text...")

if st.button('Predict'):
    
    result = analyzer.semantic_analyzer(text)
    if result == "positive":
        st.success(result)
    if result == "negative":
        st.warning(result)
    if result == "neutral":
        st.info(result)            
    st.balloons()    

