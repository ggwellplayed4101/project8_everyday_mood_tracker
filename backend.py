from nltk.sentiment.vader import SentimentIntensityAnalyzer
import glob
import os


def read_mood_of(folder_path="diary/*.txt"):

    files = glob.glob(folder_path) 
    dates = [os.path.splitext(os.path.basename(file))[0] for file in files]
    sentiments = []

    for file_path in files:
        with open(file_path, "r") as file:
            text = file.read()
            analyzer = SentimentIntensityAnalyzer()
            sentiment = analyzer.polarity_scores(text)
            sentiments.append(sentiment)

    positivity_indexes = [item["pos"] for item in sentiments]
    negativity_indexes = [item["neg"] for item in sentiments]

    return (positivity_indexes, negativity_indexes, dates)

if __name__=="__main__":
    read_mood_of()