import streamlit as st
from utils import process_tweet, lookup
import json



def naive_bayes_predict(tweet, logprior, loglikelihood):
    
    # process the tweet to get a list of words
    word_l = process_tweet(tweet)

    # initialize probability to zero
    p = 0

    # add the logprior
    p += logprior

    for word in word_l:

        # check if the word exists in the loglikelihood dictionary
        if word in loglikelihood:
            # add the log likelihood of that word to the probability
            p += loglikelihood[word]

    return p


with open("loglikelihood.json", "r") as outfile: 
    loglikelihood = json.load(outfile)


#start the user interface
st.write("This is just a small text classification app. Type in your text below and don't forget to press the enter button before clicking/pressing the 'classify' button")
st.write("Don't fret if the prediction is not correct or if it is not what you expected, the model is not perfect.")

st.write("There is no provision for neutral text, yet...")
my_text = st.text_input("Enter the text you want to classify", "Change this...", max_chars=100, key='to_classify')

logprior = 0.0

if st.button('Classify', key='classify_button'):
    if naive_bayes_predict(my_text, logprior, loglikelihood) > 0:
        # the predicted class is 1
        st.write('Your input text is positive')
    else:
        # otherwise the predicted class is 0
        st.write('Your input text is negative')