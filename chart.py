import matplotlib.pyplot as mpl
import pandas as pd
import os

# read data
current_path = os.getcwd()
file_path = os.path.join(current_path, 'data.csv')
data = pd.read_csv(file_path)

topics = data['topic']
votes = data['votes']

data.sort_values(by='votes', ascending=False)

# make bar chart
mpl.figure(figsize=(10, 6))
mpl.bar(topics, votes, color='skyblue')
mpl.title("most voted presidents", fontsize=16)
mpl.xlabel("President", fontsize=12)
mpl.ylabel("Votes", fontsize=12)
mpl.xticks(rotation=45, fontsize=10)
mpl.tight_layout()

open_name = 'chart.png'
mpl.savefig(open_name)
mpl.show()
