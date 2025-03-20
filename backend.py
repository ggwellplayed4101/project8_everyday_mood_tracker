from nltk.sentiment.vader import SentimentIntensityAnalyzer
import glob
import os

files = glob.glob("diary/*.txt") 
dates = [os.path.splitext(os.path.basename(file))[0] for file in files]
scores = []

print(dates)

for file in files:
    print(file)
    with open(file, "r"):
        analyzer = SentimentIntensityAnalyzer()


