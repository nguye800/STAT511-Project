import matplotlib.pyplot as plt
import stemgraphic
import pandas as pd


df_data = pd.read_excel("data.xlsx")
df_wine = pd.read_excel("WineConsumption.xlsx")

# part 1
# sample_columns = ["Sample1", "Sample2", "Sample3"]
# fig, axes = plt.subplots(len(sample_columns), 1, figsize=(6, 12))

# for axis, col in zip(axes, sample_columns):
#     stemgraphic.stem_graphic(
#         df_data[col].dropna(),
#         scale=1,
#         title=f"{col} stem-and-leaf (scale=1)",
#         ax=axis,
#     )

# plt.tight_layout()
# plt.show()

# wine_columns = ["Wine", "Death rate"]
# fig, axes = plt.subplots(len(wine_columns), 1, figsize=(6, 12))
# count = 0
# for axis, col in zip(axes, wine_columns):
#     if count == 0:
#         stemgraphic.stem_graphic(
#             df_wine[col].dropna(),
#             scale=1,
#             title=f"{col} stem-and-leaf (scale=1)",
#             ax=axis,
#         )
#     else:
#         stemgraphic.stem_graphic(
#             df_wine[col].dropna(),
#             scale=100,
#             title=f"{col} stem-and-leaf (scale=100)",
#             ax=axis,
#         )
#     count += 1

# plt.tight_layout()
# plt.show()

# part 2
# columns = ["Sample1", "Sample2", "Sample3"]
# fig, axes = plt.subplots(len(columns), 1, figsize=(6, 9), sharex=True)

# for ax, col in zip(axes, columns):
#     ax.hist(df_data[col].dropna(), bins=15, edgecolor="black")
#     ax.set_title(f"{col} histogram")
#     ax.set_ylabel("Frequency")

# axes[-1].set_xlabel("Value")
# plt.tight_layout()
# plt.show()

# wine_columns = ["Wine", "Death rate"]
# fig, axes = plt.subplots(len(wine_columns), 1, figsize=(6, 12))
# for ax, col in zip(axes, wine_columns):
#     ax.hist(df_wine[col].dropna(), bins=15, edgecolor="black")
#     ax.set_title(f"{col} histogram")
#     ax.set_ylabel("Frequency")

# plt.tight_layout()
# plt.show()
   
# part 3
# summary statistics table

# part 3
# summary statistics table
# summary_series = {
#     "Wine": df_wine["Wine"],
#     "Death rate": df_wine["Death rate"],
# }

# summary_rows = []
# for name, series in summary_series.items():
#     clean = series.dropna()
#     summary_rows.append(
#         {
#             "Variable": name,
#             "Min": clean.min(),
#             "Q1": clean.quantile(0.25),
#             "Median": clean.quantile(0.5),
#             "Q3": clean.quantile(0.75),
#             "Max": clean.max(),
#             "Mean": clean.mean(),
#             "Std Dev": clean.std(ddof=1),
#         }
#     )

# summary_table = pd.DataFrame(summary_rows).set_index("Variable")
# print(summary_table.to_string(float_format=lambda x: f"{x:.3f}"))

# Question 4
# box-and-whisker plot for wine and death rate
fig, ax = plt.subplots(figsize=(6, 6))
box_values = [df_wine["Wine"].dropna()]
labels = ["Wine"]
flier_props = dict(marker="o", markersize=5, markerfacecolor="black", linestyle="none")
ax.boxplot(box_values, labels=labels, whis=1.5, flierprops=flier_props)
ax.set_title("Wine - Boxplot (1.5 IQR whiskers)")
ax.set_ylabel("Value")
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(6, 6))
box_values = [df_wine["Death rate"].dropna()]
labels = ["Death rate"]
flier_props = dict(marker="o", markersize=5, markerfacecolor="black", linestyle="none")
ax.boxplot(box_values, labels=labels, whis=1.5, flierprops=flier_props)
ax.set_title("Death rate - Boxplot (1.5 IQR whiskers)")
ax.set_ylabel("Value")
plt.tight_layout()
plt.show()

# scatter plot showing correlation between wine consumption and death rate
r_value = df_wine["Wine"].corr(df_wine["Death rate"])
fig, ax = plt.subplots(figsize=(7, 6))
ax.scatter(df_wine["Wine"], df_wine["Death rate"], color="tab:blue", edgecolors="black")
ax.set_xlabel("Wine consumption")
ax.set_ylabel("Death rate")
ax.set_title("Wine vs Death Rate Scatter Plot")
ax.text(
    0.05,
    0.95,
    f"r = {r_value:.3f}",
    transform=ax.transAxes,
    ha="left",
    va="top",
    bbox=dict(facecolor="white", alpha=0.8, edgecolor="black"),
)
plt.tight_layout()
plt.show()


# covariance calculation with numerator and denominator output
# aligned = df_wine[["Wine", "Death rate"]].dropna()
# wine = aligned["Wine"]
# death = aligned["Death rate"]
# x_bar = wine.mean()
# y_bar = death.mean()
# numerator = ((wine - x_bar) * (death - y_bar)).sum()
# N = len(aligned)
# denominator = N - 1
# covariance = numerator / denominator

# print(f"Numerator sum((x_i - x_bar)*(y_i - y_bar)): {numerator:.3f}")
# print(f"Denominator N-1: {denominator}")
# print(f"Sample covariance: {covariance:.3f}")
   
