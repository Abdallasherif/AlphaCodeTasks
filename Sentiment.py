import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud

# ----------------------------
# Load your dataset
# ----------------------------
df = pd.read_csv('Books.csv')  

# ----------------------------
# Create dummy reviews if none exist
# ----------------------------
if 'Review' not in df.columns:
    sample_reviews = [
        "Loved this book!",
        "It was okay, nothing special.",
        "Horrible. Waste of time.",
        "A masterpiece!",
        "Not good, not bad. Just average."
    ]
    df['Review'] = sample_reviews * (len(df) // len(sample_reviews))

# ----------------------------
# Sentiment Analysis using TextBlob
# ----------------------------
df['Polarity'] = df['Review'].apply(lambda x: TextBlob(x).sentiment.polarity)

def get_sentiment(polarity):
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment'] = df['Polarity'].apply(get_sentiment)

# ----------------------------
# Visualization: Sentiment Distribution
# ----------------------------
plt.figure(figsize=(6, 4))
sns.countplot(x='Sentiment', data=df, palette='coolwarm')
plt.title('Sentiment Analysis of Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.grid(True)
plt.tight_layout()
plt.show()

# ----------------------------
# Word Cloud of All Reviews
# ----------------------------
all_text = ' '.join(df['Review'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of All Reviews')
plt.tight_layout()
plt.show()

# ----------------------------
# Export Sentiment Results
# ----------------------------
df[['Review', 'Polarity', 'Sentiment']].to_csv('Sentiment_Results.csv', index=False)
print("Sentiment analysis complete. Results saved to 'Sentiment_Results.csv'.")
