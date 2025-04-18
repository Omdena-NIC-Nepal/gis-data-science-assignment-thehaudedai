import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_top_warming_districts(data, top_n=10, xlim=None, palette="RdBu"):
    """
    Barplot figure for top N warming districts.
    """
    top_data = data.sort_values("Delta", ascending=False).head(top_n)

    fig, ax = plt.subplots(figsize=(14, 6))
    sns.barplot(
        data=top_data,
        x="Delta",
        y="District Name",
        hue="District Name",
        palette=palette,
        ax=ax,
    )

    if xlim:
        ax.set_xlim(*xlim)

    return fig, ax


def plot_temp_trends(
    df_4_list, df_8_list, labels=("RCP4.5", "RCP8.5"), palette="RdBu", figsize=(14, 6)
):
    """
    Plots average annual temperature trends for two climate scenarios.
    """
    df_4 = pd.concat(df_4_list).groupby("Year")["Temperature"].mean().reset_index()
    df_4["Scenario"] = labels[0]

    df_8 = pd.concat(df_8_list).groupby("Year")["Temperature"].mean().reset_index()
    df_8["Scenario"] = labels[1]

    df_combined = pd.concat([df_4, df_8])

    fig, ax = plt.subplots(figsize=figsize)
    sns.lineplot(
        data=df_combined,
        x="Year",
        y="Temperature",
        hue="Scenario",
        palette=palette,
        ax=ax,
    )

    return fig, ax


def plot_district_temp_trends(
    df, districts: list, palette="RdBu", style="Scenario", figsize=(14, 6)
):
    """
    Plots temperature trends over time for selected districts.
    """
    filtered_df = df[df["District Name"].isin(districts)]

    fig, ax = plt.subplots(figsize=figsize)
    sns.lineplot(
        data=filtered_df,
        x="Year",
        y="Temperature",
        hue="District Name",
        style=style,
        palette=palette,
        ax=ax,
    )
    return fig, ax
