import pandas as pd


def convert_to_long_format(
    df, id_vars=["District Name"], var_name="Year", value_name="Temperature"
):
    """
    Converts the dataframe in wide format into long format
    """
    df_long = df.melt(id_vars=id_vars, var_name=var_name, value_name=value_name)
    return df_long


def temp_avg_per_district(df, data_type: str, no_of_decimal=2):
    """
    Calculate average temperature per district and scenario.
    """
    avg = (
        df[df["DataType"] == data_type]
        .groupby(["District Name", "Scenario"])["Temperature"]
        .mean()
        .round(no_of_decimal)
        .reset_index(name=f"{data_type[0:4]}_Temp")
    )
    return avg


def calculate_delta(historical_avg, projected_avg):
    """
    Merge historical and projected averages and calculate delta.
    """
    diff = pd.merge(historical_avg, projected_avg, on=["District Name", "Scenario"])
    diff["Delta"] = diff["Proj_Temp"] - diff["Hist_Temp"]
    return diff


def avg_delta_per_district(temp_diff):
    """
    Calculate average delta per district across all scenarios.
    """
    avg = temp_diff.groupby("District Name")["Delta"].mean().reset_index()
    return avg
