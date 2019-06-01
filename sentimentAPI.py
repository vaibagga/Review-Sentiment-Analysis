from textblob import TextBlob
def sentiment(sentence):
  opinion = TextBlob(sentence)
  return opinion.sentiment.polarity

sentiment("Good course, but needs to be more detailed")
