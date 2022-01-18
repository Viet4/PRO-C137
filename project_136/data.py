import pandas as pd

df = pd.read_csv("main.csv")
df = df.to_numpy()

data = []
for star_data in df:
  temp_dict = {
      "name": star_data[0],
      "distance": star_data[1],
      "mass": star_data[2],
      "radius": star_data[3],
      "gravity": star_data[4],
  }
  data.append(temp_dict)

print(data)