from flask import Flask, render_template, request, redirect, url_for
import os
import openai

#set up Open AI key as local environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

#Asks Open AI to classify the given tweet and give it a sentiment rating, then return that rating
#Uses tweet text from index.html as the prompt, then asks OpenAI to give it a sentiment rating
def tweetClassify(tweet):
	response = openai.Completion.create(
	model="text-davinci-003",
	prompt="Classify the sentiment in this tweet:\n\n" + tweet + "\n\nTweet sentiment rating:",
	temperature=0,
	max_tokens=60,
	top_p=1.0,
	frequency_penalty=0.0,
	presence_penalty=0.0
	)
        
	return response["choices"][0]["text"]


app = Flask(__name__)

#Helper function that runs the OpenAI function. The url returns the OpenAI response, which is used
#to append to the HTML list using JQuery
@app.route("/classifytweet/<tweet>", methods=['GET', 'POST'])
def classify_tweet(tweet):
	return tweetClassify(tweet)

#Main route, opens the index.html frontend for the program
@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template('index.html')