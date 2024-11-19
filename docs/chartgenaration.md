# chart generation
to generate a chart with your needs, clone this repo to your machine: `git clone https://github.com/webbrowser11/chart-gen.git`
# now make a data.csv file
structure it like this (wuthout spaces):
```
topic,num  -  you can have more spaces at the top
word,num  -  mathing the amount of spaces you put at the top
```
# now cutomize the generator
go to chart.py and change it to match your csv data file:
```
import matplotlib.pyplot as mpl
import pandas as pd

# read data
file_path = r'\path\to\script\data.csv'
data = pd.read_csv(file_path)

topic = data['topic'] # made to match the csv file
num = data['num'] # made to match the csv file

data.sort_values(by='num', ascending=False)

# make bar chart
mpl.figure(figsize=(10, 6))
mpl.bar(topic, num, color='skyblue')
mpl.title("chart title", fontsize=16)
mpl.xlabel("label for first bit of chart: topic", fontsize=12)
mpl.ylabel("label for second bit of chart: num", fontsize=12)
mpl.xticks(rotation=45, fontsize=10)
mpl.tight_layout()

open_name = 'chart.png'
mpl.savefig(open_name)
mpl.show()
```
you're all set! now just run chart.py.
