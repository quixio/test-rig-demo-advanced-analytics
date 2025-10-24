import marimo

__generated_with = "0.16.2"
app = marimo.App(width="wide")


@app.cell
def _():
    import math
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set()
    return mo, pd, plt


@app.cell
def _():
    from quixlake import QuixLakeClient
    return (QuixLakeClient,)


@app.cell
def _():
    # Calibration Factor and zero
    CF = 39498.19765159356
    zero = -678
    # see calibration.py for details
    return


@app.function
def value_to_Newtons(value, abs_value=True, CF=39498.19765159356, zero=-678):
    "Converts load cell gauge value to the horizontal Foce value in Newtons"
    Force_Newtons = (value-zero) / CF 
    if abs_value:
        Force_Newtons = abs(Force_Newtons)
    return Force_Newtons


@app.cell
def _(mo):
    mo.md(r"""## Experiment data""")
    return


@app.cell
def _(mo):
    q = mo.query_params()

    campaign_id = q.get("campaign_id", 'AERO_SHOW_DEMO')
    environment_id = q.get("environment_id", 'ENV_01')
    test_id = q.get("test_id", 'javi-23-09-t001')
    return campaign_id, environment_id, test_id


@app.cell
def _(QuixLakeClient):
    MYTOKEN = "sdk-95f80fd699934f759b2f12f3c06f34d9"

    client = QuixLakeClient(
        base_url = "https://quixlake-quixers-testrigdemodatawarehouse-prod.az-france-0.app.quix.io/", 
        token = MYTOKEN)
    return (client,)


@app.cell
def _(campaign_id, environment_id, mo, test_id):
    sql_query = f"""
    SELECT *
    FROM config-enriched-data
    WHERE campaign_id = '{campaign_id}' AND environment_id = '{environment_id}' AND test_id = '{test_id}'
    """

    mo.md(f"```sql\n{sql_query}\n```")
    return (sql_query,)


@app.cell
def _(client, sql_query):
    # Query the client
    df_i = client.query(sql_query)
    return (df_i,)


@app.cell
def _(pd, plt):
    def basic_plot(df_i):
        fig, axes = plt.subplots(3, 1, figsize=(15, 12), sharex=True)

        # Ensure time axis is datetime
        if not pd.api.types.is_datetime64_any_dtype(df_i["kafka_timestamp"]):
            df_i["kafka_timestamp"] = pd.to_datetime(df_i["kafka_timestamp"])

        def set_ylim_quantiles(ax, series):
            """Set y-limits based on 5th and 95th quantiles with scaling."""
            q_low = series.quantile(0.05) * 0.95
            q_high = series.quantile(0.95) * 1.05
            ax.set_ylim(q_low, q_high)

        # --- Plot 1: Voltage ---
        ax = axes[0]
        s = df_i["ina260__voltage_v"]
        ax.plot(df_i["kafka_timestamp"], s, label="Voltage (V)", color="tab:blue")
        ax.plot(
            df_i["kafka_timestamp"],
            s.rolling(3).median(),
            linestyle="--", alpha=0.5, color="tab:blue", label="Rolling Median (3)"
        )
        ax.set_title("INA260 Voltage")
        ax.set_ylabel("Voltage [V]")
        set_ylim_quantiles(ax, s)
        ax.legend()

        # --- Plot 2: Current ---
        ax = axes[1]
        s = df_i["ina260__current_ma"]
        ax.plot(df_i["kafka_timestamp"], s, label="Current (mA)", color="tab:green")
        ax.plot(
            df_i["kafka_timestamp"],
            s.rolling(3).median(),
            linestyle="--", alpha=0.5, color="tab:green", label="Rolling Median (3)"
        )
        ax.set_title("INA260 Current")
        ax.set_ylabel("Current [mA]")
        set_ylim_quantiles(ax, s)
        ax.legend()

        # --- Plot 3: Load Cell Raw Value ---
        ax = axes[2]
        s = df_i["load_cell__raw_value"]
        ax.plot(df_i["kafka_timestamp"], s, label="Load Cell Raw", color="tab:red")
        ax.plot(
            df_i["kafka_timestamp"],
            s.rolling(3).median(),
            linestyle="--", alpha=0.5, color="tab:red", label="Rolling Median (3)"
        )
        ax.set_title("Load Cell Raw Value")
        ax.set_ylabel("Raw Value [a.u.]")
        ax.set_xlabel("Time")
        set_ylim_quantiles(ax, s)
        ax.legend()

        fig.tight_layout()
        return fig
    return (basic_plot,)


@app.cell
def _(basic_plot, df_i):
    basic_plot(df_i)
    return


@app.cell
def _(df_i):
    df_i
    return


@app.cell
def _(df_i):
    df_i[['ina260__voltage_v', 'ina260__current_ma', 'load_cell__raw_value']].describe()
    return


if __name__ == "__main__":
    app.run()
