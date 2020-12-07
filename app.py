import streamlit as st
import os
from utils import process_tweet, lookup, naive_bayes_predict

os.environ['PORT'] = 8501


#start the user interface
st.write("This is just a small text classification app. Type in your text below and don't forget to press the enter button before clicking/pressing the 'classify' button")
st.write("Don't fret if the prediction is not correct or if it is not what you expected, the model is not perfect.")

st.write("There is no provision for neutral text, yet...")
my_text = st.text_input("Enter the text you want to classify", "Change this...", max_chars=100, key='to_classify')

if st.button('Classify', key='classify_button'):
    p = naive_bayes_predict(my_text)
    if p > 0:
        # the predicted class is 1
        st.write(f"Your input text is positive and the score is {p}")
    else:
        # otherwise the predicted class is 0
        st.write(f"Your input text is negative and the score is {p}")
