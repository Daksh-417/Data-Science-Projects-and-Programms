import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("USvideos.csv")  # Change file path to your dataset

# # Video labels and values
# top_videos = df.nlargest(10, 'views')
# video_ids = top_videos['title']
# likes = top_videos['likes']
# dislikes = top_videos['dislikes']
# x = np.arange(len(video_ids))
# width = 0.35
# plt.figure(figsize=(12, 6))
# plt.bar(x - width/2, likes, width, label='Likes', color='skyblue')
# plt.bar(x + width/2, dislikes, width, label='Dislikes', color='salmon')
# plt.xlabel('Video ID')
# plt.ylabel('Count')
# plt.title('Likes and Dislikes for Top 10 Videos')
# plt.xticks(x, video_ids, rotation=45)
# plt.legend()
# plt.tight_layout()
# plt.show()

# # Top categories by count
# df['publish_time'] = pd.to_datetime(df['publish_time'])
# top_categories = df['category_id'].value_counts().head(10)
# top_categories.plot(kind='bar', color='skyblue')
# plt.title("Top Categories of Trending Videos")
# plt.xlabel("Category ID")
# plt.ylabel("Number of Videos")
# plt.show()

# # Upload hour analysis
# df['hour'] = df['publish_time'].dt.hour
# df['hour'].value_counts().sort_index().plot(kind='bar', color='orange')
# plt.title("Number of Videos Published by Hour")
# plt.xlabel("Hour of Day")
# plt.ylabel("Number of Videos")
# plt.show()

# # Plotting the pie chart
# review_counts = df['comment_review'].value_counts()
# plt.figure(figsize=(6, 6))
# plt.pie(review_counts, labels=review_counts.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#ff9999','#99ff99'])
# plt.title('Distribution of Comment Reviews')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.tight_layout()
# plt.show()

# # Scatter plot: Likes vs Dislikes with comment size
# plt.figure(figsize=(10, 6))
# scatter = plt.scatter(df['likes'], df['dislikes'], 
#                       s=df['comment_count'] / 10,  # size by comment count (scaled)
#                       alpha=0.5, c='purple', edgecolors='w', linewidth=0.5)
# plt.xlabel('Likes')
# plt.ylabel('Dislikes')
# plt.title('Scatter Plot of Likes vs Dislikes (Size = Comment Count)')
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# Select top 10 videos by views
top_videos = df.nlargest(10, 'views')
video_ids = top_videos['video_id']
likes = top_videos['likes']
dislikes = top_videos['dislikes']

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Line plot for Likes
ax1.plot(video_ids, likes, marker='o', color='green', linestyle='-', linewidth=2)
ax1.set_title('Likes per Video')
ax1.set_ylabel('Likes')
ax1.grid(True)

# Line plot for Dislikes
ax2.plot(video_ids, dislikes, marker='o', color='red', linestyle='-', linewidth=2)
ax2.set_title('Dislikes per Video')
ax2.set_ylabel('Dislikes')
ax2.set_xlabel('Video ID')
ax2.grid(True)

# Rotate x-axis labels
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()