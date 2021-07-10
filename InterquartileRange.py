import pandas as pd
import seaborn as sns
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("savings_data.csv")
df.quantile([.1,.25,.5,.75],axis =0)
sns.boxplot(data = df,x=df["quant_saved"])
all_savings = new_df["quant_saved"].tolist()

print(f"Mean of the savings - {statistics.mean(all_savings)}")
print(f"Median of the savings - {statistics.median(all_savings)}")
print(f"Standard deviation in the savings - {statistics.stdev(all_savings)}")

sampling_mean_list = []
for i in range(1000):
 temp_list = []
 for j in range (100):
     temp_list.append(random.choice(all_savings))
     sampling_mean_list.append(statistics.mean(temp_list))

     mean_sampling = statistics.mean(sampling_mean_list)

     fig = ff.create_displot([sampling_mean_list],["Savings (Sampling)"], show_hist = False)
     fig.add_trace(go.Scatter(x = [mean_sampling,mean_sampling], y = [0, 0.1], mode = "lines", name = "MEAN"))
     fig.show()

     print(f"Standard deviation of the sampling data - {statistics.stdev(sampling_mean_list)}")
     print(f"Mean of the Population - {statistics.mean(all_savings)}")
     print(f"Mean of the Sampling Distribution - {mean_sampling}")

     temp_df = new_df[new_df.age!= 0]

     age = temp_df["age"].tolist()
     savings = temp_df["quant_saved"].tolist()

     correlation = np.corrcoef(age,savings)
     print(f"Correlation between the age of the person and their savings is - {correlation[0,1]}")

     z_score = (sampling_mean_list - mean_sampling)/statistics.stdev
     print (f"Z score is - {z_score}")
