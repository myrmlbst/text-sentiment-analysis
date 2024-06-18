# analyze texts from the web
 
from textblob import TextBlob
from newspaper import Article

# url of web article being used
url = 'https://en.wikipedia.org/wiki/Mathematics'
article = Article(url)

article.download()
article.parse()
article.nlp()

# output a summary of the text
text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity = -1 to 1
print(sentiment)
