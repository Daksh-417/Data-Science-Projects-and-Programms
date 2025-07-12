import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("USvideos.csv")

# Drop missing or invalid rows
df = df.dropna(subset=['views', 'likes', 'dislikes', 'comment_count'])

# Convert columns to integers
df['views'] = df['views'].astype(int)
df['likes'] = df['likes'].astype(int)
df['dislikes'] = df['dislikes'].astype(int)
df['comment_count'] = df['comment_count'].astype(int)

# Create a 2x2 grid of plots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# 📊 Plot 1: Views Distribution
axs[0, 0].hist(df['views'], bins=50, color='skyblue', edgecolor='black')
axs[0, 0].set_title("Distribution of Views")
axs[0, 0].set_xlabel("Views")
axs[0, 0].set_ylabel("Frequency")

# 📊 Plot 2: Likes vs Dislikes Scatter
axs[0, 1].scatter(df['likes'], df['dislikes'], alpha=0.4, color='mediumpurple', edgecolors='k', linewidths=0.2)
axs[0, 1].set_title("Likes vs Dislikes")
axs[0, 1].set_xlabel("Likes")
axs[0, 1].set_ylabel("Dislikes")
axs[0, 1].set_xscale('log')
axs[0, 1].set_yscale('log')

# 📊 Plot 3: Views vs Comments Scatter
axs[1, 0].scatter(df['views'], df['comment_count'], alpha=0.4, color='darkgreen', edgecolors='k', linewidths=0.2)
axs[1, 0].set_title("Views vs Comments")
axs[1, 0].set_xlabel("Views")
axs[1, 0].set_ylabel("Comments")
axs[1, 0].set_xscale('log')
axs[1, 0].set_yscale('log')

# 📊 Plot 4: Likes Distribution
axs[1, 1].hist(df['likes'], bins=50, color='orange', edgecolor='black')
axs[1, 1].set_title("Distribution of Likes")
axs[1, 1].set_xlabel("Likes")
axs[1, 1].set_ylabel("Frequency")

plt.tight_layout()
plt.show()