import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from wordcloud import WordCloud
pio.templates.default = "plotly_white"
import seaborn as sns
import matplotlib.pyplot as plt

#__1
df = pd.read_csv("/content/Instagram data.csv", encoding="latin-1")
df.head(5)

df.columns

df.info()

#___2
df.describe()

#___3
df.isnull().sum()

#___4

impr = df["Impressions"]
mean = impr.mean()
median = impr.median()
std = impr.std()
min_val = impr.min()
max_val = impr.max()

print("Descriptive Statistics:")
print("Mean: ", mean)
print("Median: ", median)
print("Standard Deviation: ", std)
print("Minimum: ", min_val)
print("Maximum", max_val)

plt.hist(impr, bins=35)
plt.xlabel("Impressions")
plt.ylabel("Frequency")
plt.title("Distribution of Analysis")
plt.show()

#___5
df["Time"] = range(len[df])

plt.figure(figsize=(10, 5))
plt.plot(df["Time"], df["Impressions"])
plt.xlabel("Time")
plt.ylabel("Impressions")
plt.title("Impression/Time")
plt.show()

#___6
df["Time"] = range(len[df])

plt.figure(figsize=(10, 5))
plt.plot(df["Time"], df["Likes"], label="Likes")
plt.plot(df["Time"], df["Saves"], label="Saves")
plt.plot(df["Time"], df["Follows"], label="Follows")
plt.xlabel("Data Point Index")
plt.ylabel("Count")
plt.title("Matrics over Data Points")
plt.legend()
plt.show()

#__7
rf_home = df["From Home"].sum()
rf_hashtag = df["From Hashtags"].sum()
rf_explore = df["From Explore"].sum()
rf_other = df["From other"].sum()

print("Reah from Home: ", rf_home)
print("Reah from Hashtags: ", rf_hashtag)
print("Reah from Explore: ", rf_explore)
print("Reah from Other: ", rf_other)

reach = [294619, 224614, 128294, 20360]
labels = ["Home", "Hashtags", "Explore", "Other"]

plt.pie(reach, labels= labels, autopot= "%1.1f%%")
plt.title("Distribution of Reach")
plt.axis("equal")
plt.show()

#___8
rf_likes = df["Likes"].sum()
rf_saves = df["Saves"].sum()
rf_shares = df["Shares"].sum()
rf_comments = df["Comments"].sum()

print("Reah from Likes: ", rf_likes)
print("Reah from Saves: ", rf_saves)
print("Reah from Shares: ", rf_shares)
print("Reah from Comments: ", rf_comments)

reach = [20680, 18244, 1114, 793]
labels = ["Likes", "Saves", "Shares", "Comments"]

plt.pie(reach, labels= labels, autopot= "%1.1f%%")
plt.title("Distribution of Reach")
plt.axis("equal")
plt.show()

#___9

p_visits = df["Profile Visits"]
follows = df["Follows"]

plt.scatter(p_visits, follows, color="blue")
plt.xlabel("Profile Visits")
plt.ylabel("Follows")
plt.title("Releationship B/W Profile visits & Follows")
plt.show()

#___10
hashtags = df["Hashtag"].str.cat(sep=" ")
wordcloud = WordCloud(width=800, height=400, background_color="black").generate(hashtags)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

#___11
numeric_columns = df.select_dtypes(include=[float, int])
correlation_matrix = numeric_columns.corr()
plt.figure(figure=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.show()

#___12
hashtags = df["Hashtags"].str.split()
all_hashtags = [tag for sublist in hashtags for tag in sublist]
hashtag_counts = pd.Series(all_hashtags).value_counts()
plt.figure(figsize=(20, 10))
hashtag_counts.plot(kind="bar")
plt.xlabel("Count")
plt.ylabel("Hashtag")
plt.title("Distribution of Hashtags")
plt.show()

#___13
hashtags_grouped = df.groupby("Hashtags").agg({"Likes": "sum", "Impressions": "sum"})
hashtags_grouped = hashtags_grouped.sort_values("Likes", ascending=False)
plt.figure(figsize=(10, 6))
hashtags_grouped["Likes"].plot(kind="bar")
plt.xlabel("Hashtags")
plt.ylabel("Likes")
plt.title("Distriution of Likes by Hashtag")
plt.show()

plt.figure(figsize=(10, 6))
hashtags_grouped["Impressions"].plt(kind="bar")
plt.xlabel("Hashtags")
plt.ylabel("Impressions")
plt.title("Distribution of Impressions by Hashtag")
plt.show()