from unittest import result
import plotly.figure_factory as ff
import pandas as pd
import statistics

df = pd.read_csv("StudentsPerformance.csv")
mathscore = df["math score"].tolist()


math_score_mean = statistics.mean(mathscore)
math_score_median = statistics.median(mathscore)
math_score_mode = statistics.mode(mathscore)

print(f"mean, median, mode are {math_score_mean}, {math_score_median} and {math_score_mode} respectively")

mathscore_stdev = statistics.stdev(mathscore)

zone1_s,zone1_e = math_score_mean-mathscore_stdev,math_score_mean+mathscore_stdev
zone2_s,zone2_e = math_score_mean-2*mathscore_stdev,math_score_mean+2*mathscore_stdev
zone3_s,zone3_e = math_score_mean-3*mathscore_stdev,math_score_mean+3*mathscore_stdev
n = len(mathscore)

zone1 = [result for result in mathscore if result > zone1_s and result < zone1_e]
zone2 = [result for result in mathscore if result > zone2_s and result < zone2_e]
zone3 = [result for result in mathscore if result > zone3_s and result < zone3_e]

print("{}% of data lies within one standard deviation".format(len(zone1)/n*100))
print("{}% of data lies within two standard deviation".format(len(zone2)/n*100))
print("{}% of data lies within three standard deviation".format(len(zone3)/n*100))