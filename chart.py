import matplotlib.pyplot as mpl
import pandas as pd

# read data
file_path = r'C:\Users\Graham\Documents\Python Scripts\Self-projects\Big projects\data.csv'
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