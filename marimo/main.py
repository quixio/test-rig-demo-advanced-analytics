import marimo

__generated_with = "0.16.2"
app = marimo.App(width="wide")


@app.cell
def _():
    import math
    import requests
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from collections import defaultdict
    import seaborn as sns
    sns.set()
    return defaultdict, math, mo, np, pd, plt, requests


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
    mo.md(r"""# Query experiment data""")
    return


@app.cell
def _(mo):
    q = mo.query_params()

    campaign_id = q.get("campaign_id", 'AERO_SHOW_DEMO')
    environment_id = q.get("environment_id", 'ENV_01')
    test_id = q.get("test_id", 'javi-23-09-t001')
    return campaign_id, environment_id, test_id


@app.cell
def _(requests):
    url = "https://backend-api-quixers-quixtestmanager-new.az-france-0.app.quix.io/api/v1/tests"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer sdk-2be80acf56ea48b8bd4dadf2e6a34c1b"
    }
    response = requests.get(url, headers=headers)

    # Check response
    if response.status_code == 200:
        data = response.json()   # Parse JSON
    else:
        print(f"Error {response.status_code}: {response.text}")
    return (data,)


@app.cell
def _(data, defaultdict):
    def nested_dict():
        return defaultdict(nested_dict)

    def build_hierarchy(data_list):
        hierarchy = defaultdict(lambda: defaultdict(dict))
    
        for item in data_list:
            env = item["environment_id"]
            campaign = item["campaign_id"]
            test = item["test_id"]
        
            # Store the whole test dict (you can customize if you only want part of it)
            hierarchy[campaign][env][test] = None
    
        return hierarchy

    dict_tags = build_hierarchy(data)
    return (dict_tags,)


@app.function
def standard_value(previously_selected, options):
    if previously_selected in options:
        standard_value = previously_selected
    else:
        standard_value = options[0]
    return standard_value


@app.cell
def _(campaign_id, dict_tags, mo):
    campaign_selector = mo.ui.dropdown(
        options=list(dict_tags.keys()),
        value = standard_value(campaign_id, list(dict_tags.keys())),
        label="Campaign",
    )

    campaign_selector
    return (campaign_selector,)


@app.cell
def _(campaign_selector, dict_tags, environment_id, mo):
    environment_selector = mo.ui.dropdown(
        options=list(dict_tags[campaign_selector.value].keys()),
        value=standard_value(environment_id, list(dict_tags[campaign_selector.value].keys())),
        label="Environment",
    )
    environment_selector
    return (environment_selector,)


@app.cell
def _(campaign_selector, dict_tags, environment_selector, mo, test_id):
    test_selector = mo.ui.dropdown(
        options=list(dict_tags[campaign_selector.value][environment_selector.value].keys()),
        value=standard_value(test_id, list(dict_tags[campaign_selector.value][environment_selector.value].keys())),
        label="Test",
    )
    test_selector
    return (test_selector,)


@app.cell
def _(QuixLakeClient):
    MYTOKEN = "sdk-95f80fd699934f759b2f12f3c06f34d9"

    client = QuixLakeClient(
        base_url = "https://quixlake-quixers-testrigdemodatawarehouse-prod.az-france-0.app.quix.io/", 
        token = MYTOKEN)
    return (client,)


@app.cell
def _(campaign_selector, environment_selector, mo, test_selector):
    sql_query = f"""
    SELECT *
    FROM config-enriched-data
    WHERE campaign_id = '{campaign_selector.value}' AND environment_id = '{environment_selector.value}' AND test_id = '{test_selector.value}'
    """

    mo.md(f"```sql\n{sql_query}\n```")
    return (sql_query,)


@app.cell
def _(client, sql_query):
    # Query the client
    df_i = client.query(sql_query)
    return (df_i,)


@app.cell
def _(mo):
    mo.md(r"""# Data analysis""")
    return


@app.cell
def _(df_i):
    df_i
    return


@app.cell
def _(mo):
    mo.md(r"""### Basic visualisation of raw data""")
    return


@app.cell
def _(np, pd, plt):
    # 1️⃣ Function to create base dataframe
    def create_electrical_df(df, window=3):
        df_e = df[["kafka_timestamp", "timestamp", "ina260__voltage_v", "ina260__current_ma"]].copy()

        # Convert timestamp from ms to seconds
        df_e["timestamp_s"] = (df_e["timestamp"] - df_e["timestamp"][0])/ 1000

        # Convert current to amperes
        df_e["current_a"] = df_e["ina260__current_ma"] / 1000

        return df_e


    # 2️⃣ Function to compute derived metrics (with rolling medians)
    def compute_electrical_metrics(df_e, window=3):
        # Power (W)
        df_e["power_w"] = df_e["ina260__voltage_v"] * df_e["current_a"]

        # Time delta (s)
        df_e["delta_t_s"] = df_e["timestamp_s"].diff().fillna(0)

        # Energy (J), cumulative sum
        df_e["energy_j"] = (df_e["power_w"] * df_e["delta_t_s"]).cumsum()

        # Resistance (Ohm), protect against division by zero
        df_e["resistance_ohm"] = df_e["ina260__voltage_v"] / df_e["current_a"].replace(0, pd.NA)

        # Rolling medians
        for col in ["ina260__voltage_v", "current_a", "power_w", "energy_j", "resistance_ohm"]:
            df_e[f"{col}_rolling"] = df_e[col].rolling(window=window, min_periods=1).median()

        return df_e


    # 3️⃣ Function to plot all metrics
    def plot_electrical_metrics(df_e, figures=False, zoom=False):
        fig = plt.figure(figsize=(15, 12))
        fig.suptitle("Electrical Analysis from INA260 Sensor", fontsize=16)

        # Row 1: Voltage and Current
        ax1 = plt.subplot2grid((3, 2), (0, 0))
        ax2 = plt.subplot2grid((3, 2), (0, 1))

        ax1.plot(df_e["timestamp_s"], df_e["ina260__voltage_v"], color="blue", label="Voltage")
        ax1.plot(df_e["timestamp_s"], df_e["ina260__voltage_v_rolling"], color="blue", alpha=0.5, label="Rolling Median")
        ax1.set_ylabel("Voltage (V)")
        ax1.legend()
        ax1.grid(True)

        ax2.plot(df_e["timestamp_s"], df_e["current_a"], color="orange", label="Current")
        ax2.plot(df_e["timestamp_s"], df_e["current_a_rolling"], color="orange", alpha=0.5, label="Rolling Median")
        ax2.set_ylabel("Current (A)")
        ax2.legend()
        ax2.grid(True)

        # Row 2: Power
        ax3 = plt.subplot2grid((3, 2), (1, 0), colspan=2)
        ax3.plot(df_e["timestamp_s"], df_e["power_w"], color="green", label="Power")
        ax3.plot(df_e["timestamp_s"], df_e["power_w_rolling"], color="green", alpha=0.5, label="Rolling Median")
        ax3.set_ylabel("Power (W)")
        ax3.legend()
        ax3.grid(True)

        # Row 3: Energy and Resistance
        ax4 = plt.subplot2grid((3, 2), (2, 0))
        ax5 = plt.subplot2grid((3, 2), (2, 1))

        ax4.plot(df_e["timestamp_s"], df_e["energy_j"], color="purple", label="Energy")
        ax4.plot(df_e["timestamp_s"], df_e["energy_j_rolling"], color="purple", alpha=0.5, label="Rolling Median")
        ax4.set_ylabel("Energy (J)")
        ax4.legend()
        ax4.grid(True)

        ax5.plot(df_e["timestamp_s"], df_e["resistance_ohm"], color="brown", label="Resistance")
        ax5.plot(df_e["timestamp_s"], df_e["resistance_ohm_rolling"], color="brown", alpha=0.5, label="Rolling Median")
        ax5.set_ylabel("Resistance (Ω)")
        ax5.legend()
        ax5.grid(True)

        # If figures=True, annotate each subplot with median values
        if figures:
            annotations = [
                (ax1, "ina260__voltage_v", "V"),
                (ax2, "current_a", "A"),
                (ax3, "power_w", "W"),
                (ax4, "energy_j", "J"),
                (ax5, "resistance_ohm", "Ω"),
            ]
            for ax, col, unit in annotations:
                if col == "energy_j":
                    _val_j = np.nanmax(df_e[col])
                    text_j = f"{_val_j:.1f} {unit}"
                    ax.text(
                        0.5, 0.55, text_j,
                        transform=ax.transAxes,
                        fontsize=60, color="black",
                        alpha=0.5, ha="center", va="center"
                    )
                    # Convert to Wh (1 Wh = 3600 J)
                    _val_wh = _val_j / 3600
                    text_wh = f"({_val_wh:.2f} Wh)"
                    ax.text(
                        0.5, 0.40, text_wh,
                        transform=ax.transAxes,
                        fontsize=20, color="black",
                        alpha=0.7, ha="center", va="center"
                    )
                else:
                    _val = np.nanmedian(df_e[col])
                    text = f"{_val:.1f} {unit}"
                    ax.text(
                        0.5, 0.5, text,
                        transform=ax.transAxes,
                        fontsize=60, color="black",
                        alpha=0.5, ha="center", va="center"
                    )
                if zoom == False:
                    ax.set_ylim(bottom=0, top=df_e[col].max()*1.1)
                else:
                    if df_e[col].quantile(0.95)*1.2 < df_e[col].max():
                        ax.set_ylim(bottom = df_e[col].quantile(0.05)*0.95, top=df_e[col].quantile(0.95)*1.1)
                    
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        return fig
    return (
        compute_electrical_metrics,
        create_electrical_df,
        plot_electrical_metrics,
    )


@app.cell
def _(ideal_aerodynamic_power, np, plt, rpm_from_thrust_and_current):
    # 1️⃣ Function to create base dataframe
    def create_mechanical_df(df, window=3):
        df_m = df[["kafka_timestamp", "timestamp", "ina260__voltage_v", "ina260__current_ma", 'load_cell__raw_value']].copy()

        # Convert timestamp from ms to seconds
        df_m["timestamp_s"] = (df_m["timestamp"] - df_m["timestamp"][0])/ 1000

        # Convert current to amperes
        df_m["current_a"] = df_m["ina260__current_ma"] / 1000

        return df_m

    # 2️⃣ Function to compute derived metrics (with rolling medians)
    def compute_mechanical_metrics(df_m, df_e, df_i, window=3):
        # Thrust (N)
        df_m["thrust_n"] = df_m["load_cell__raw_value"].apply(value_to_Newtons)

        # Thrust per Watt (N/W)
        df_m["tpw"] = df_m["thrust_n"] / df_e["power_w"].replace(0, np.nan)

        # P_aero (W)
        df_m["power_aero_w"] = df_m["thrust_n"].apply(ideal_aerodynamic_power)

        # RPMS method 1
        df_m["RPM_m1"] = df_m["thrust_n"].apply(rpm_1)

        # RPMS method 2
        df_m["RPM_m2"] = df_m[["thrust_n"]].join(df_e[["current_a"]]).join(
            df_i[["set_speed"]]).join(df_i[["ina260__voltage_v"]]).apply(
            lambda row: rpm_from_thrust_and_current(
                row["thrust_n"], row["current_a"], row["set_speed"], row["ina260__voltage_v"]), axis=1)

        # Rolling medians
        for col in ["thrust_n", "tpw", "power_aero_w", "RPM_m1", "RPM_m2"]:
            df_m[f"{col}_rolling"] = df_m[col].rolling(window=window, min_periods=1).median()

        return df_m

    # 
    def plot_mechanical_metrics(df_m, figures=False, zoom=False):
        fig = plt.figure(figsize=(15, 12))
        fig.suptitle("Mechanical Analysis", fontsize=16)

        # Row 1: Thrust and TPW
        ax1 = plt.subplot2grid((3, 2), (0, 0))
        ax2 = plt.subplot2grid((3, 2), (0, 1))

        ax1.plot(df_m["timestamp_s"], df_m["thrust_n"], color="blue", label="Thrust (N)")
        if "thrust_n_rolling" in df_m.columns:
            ax1.plot(df_m["timestamp_s"], df_m["thrust_n_rolling"], color="blue", alpha=0.5, label="Rolling Median")
        ax1.set_ylabel("Thrust (N)")
        ax1.legend()
        ax1.grid(True)

        ax2.plot(df_m["timestamp_s"], df_m["tpw"], color="orange", label="TPW (N/W)")
        if "tpw_rolling" in df_m.columns:
            ax2.plot(df_m["timestamp_s"], df_m["tpw_rolling"], color="orange", alpha=0.5, label="Rolling Median")
        ax2.set_ylabel("TPW (N/W)")
        ax2.legend()
        ax2.grid(True)

        # Row 2: Aerodynamic Power
        ax3 = plt.subplot2grid((3, 2), (1, 0), colspan=2)
        ax3.plot(df_m["timestamp_s"], df_m["power_aero_w"], color="green", label="Aerodynamic Power (W)")
        if "power_aero_w_rolling" in df_m.columns:
            ax3.plot(df_m["timestamp_s"], df_m["power_aero_w_rolling"], color="green", alpha=0.5, label="Rolling Median")
        ax3.set_ylabel("Power Aero (W)")
        ax3.legend()
        ax3.grid(True)

        # Row 3: RPMs
        ax4 = plt.subplot2grid((3, 2), (2, 0))
        ax5 = plt.subplot2grid((3, 2), (2, 1))

        ax4.plot(df_m["timestamp_s"], df_m["RPM_m1"], color="purple", label="RPM Method 1")
        if "RPM_m1_rolling" in df_m.columns:
            ax4.plot(df_m["timestamp_s"], df_m["RPM_m1_rolling"], color="purple", alpha=0.5, label="Rolling Median")
        ax4.set_ylabel("RPM")
        ax4.legend()
        ax4.grid(True)

        ax5.plot(df_m["timestamp_s"], df_m["RPM_m2"], color="brown", label="RPM Method 2")
        if "RPM_m2_rolling" in df_m.columns:
            ax5.plot(df_m["timestamp_s"], df_m["RPM_m2_rolling"], color="brown", alpha=0.5, label="Rolling Median")
        ax5.set_ylabel("RPM")
        ax5.legend()
        ax5.grid(True)

        # Annotations if figures=True
        if figures:
            annotations = [
                (ax1, "thrust_n", "N"),
                (ax2, "tpw", "N/W"),
                (ax3, "power_aero_w", "W"),
                (ax4, "RPM_m1", "RPM"),
                (ax5, "RPM_m2", "RPM"),
            ]
            for ax, col, unit in annotations:
                _val = np.nanmedian(df_m[col])
                if col == "tpw":
                    text = f"{_val:.2f} {unit}"
                elif col in ["RPM_m1", "RPM_m2"]:
                    text = f"{int(_val)} {unit}"
                else:
                    text = f"{_val:.1f} {unit}"
                ax.text(
                    0.5, 0.5, text,
                    transform=ax.transAxes,
                    fontsize=40, color="black",
                    alpha=0.5, ha="center", va="center"
                )
                if zoom==False:
                    ax.set_ylim(bottom=0, top=df_m[col].max()*1.1)
                else:
                    if df_m[col].quantile(0.95)*1.1 < df_m[col].max():
                        ax.set_ylim(bottom = df_m[col].quantile(0.05)*0.95, top=df_m[col].quantile(0.95)*1.1)

        plt.tight_layout(rect=[0, 0, 1, 0.96])
        return fig
    return (
        compute_mechanical_metrics,
        create_mechanical_df,
        plot_mechanical_metrics,
    )


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
    df_i[['ina260__voltage_v', 'ina260__current_ma', 'load_cell__raw_value']].describe()
    return


@app.cell
def _(mo):
    mo.md(r"""## Electrical calculations""")
    return


@app.cell
def _(compute_electrical_metrics, create_electrical_df, df_i):
    df_e = create_electrical_df(df_i, window=3)
    df_e = compute_electrical_metrics(df_e, window=3)
    df_e
    return (df_e,)


@app.cell
def _(df_e, plot_electrical_metrics):
    fig1 = plot_electrical_metrics(df_e, figures=True, zoom=True)
    fig1
    return


@app.cell
def _(mo):
    mo.md(r"""## Mechanical calculations""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### RPM calculation
    #### Method 1: Quick RPM estimates
    Using motor Kv, where Kv is in rpm/V (in the engine spec: 4300 rpm/V) and voltage.

    $\text{RPM} \approx K_V \times V_{\text{applied}}$
    """
    )
    return


@app.function
def rpm_1(v, Kv = 4300):
    RPM = int(Kv * v)
    return RPM


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Method 2: Indirect RPM estimate from thrust & electrical data
    Combine simple momentum (actuator-disk) theory for a ducted fan with the motor torque constant Kt (derived from KV) to estimate RPM without measuring voltage/back-EMF directly.
    """
    )
    return


@app.cell
def _(math):
    def ideal_aerodynamic_power(T_newton, D_m=0.064, rho=1.225):
        """Return ideal aerodynamic power (W) from thrust (N) for a disk of diameter D_m."""
        if T_newton <= 0:
            return 0.0
        A = math.pi * (D_m**2) / 4.0
        vi = math.sqrt(T_newton / (2.0 * rho * A))
        return T_newton * vi


    def rpm_from_thrust_and_current(T_newton, I_bat, duty_cycle=1.0, V_bat=None,
                                    kv=4300.0, D_m=0.064):
        """
        Estimate RPM from thrust (N) and battery current (A).
        duty_cycle: ESC PWM duty (0..1). If unknown, leave =1 (assumes full throttle).
        V_bat: optional, battery voltage (V) to sanity-check aerodynamic vs electrical power.
        """
        # basic input checks
        if I_bat <= 0 or T_newton <= 0:
            return float('nan')
        # estimate phase current (approx)
        if duty_cycle <= 0:
            duty_cycle = 1.0
        I_phase = I_bat / duty_cycle

        # aerodynamic power
        P_aero = ideal_aerodynamic_power(T_newton, D_m=D_m)
        # motor torque constant
        Kt = 60.0 / (2.0 * math.pi * kv)   # [N·m / A]
        torque = Kt * I_phase
        if torque <= 0:
            return float('nan')

        # rotational speed from mechanical power = torque * omega
        omega = P_aero / torque           # rad/s
        rpm = omega * 60.0 / (2.0 * math.pi)

        # optional sanity check: aerodynamic power should be <= available electrical power
        if V_bat is not None:
            P_elec = V_bat * I_bat
            if P_aero > P_elec * 1.1:    # allow small margin
                # flag: results probably inconsistent (units or inputs)
                # you can choose to return NaN or the rpm but warn the user
                # I'll return rpm but also raise a warning via numpy.nan for visibility
                # (replace with logging or print in your environment)
                print(f"WARNING: P_aero ({P_aero:.0f} W) > P_elec ({P_elec:.0f} W). Check units/inputs.")

        return int(rpm)
    return ideal_aerodynamic_power, rpm_from_thrust_and_current


@app.cell
def _(compute_mechanical_metrics, create_mechanical_df, df_e, df_i):
    df_m = create_mechanical_df(df_i, window=3)
    df_m = compute_mechanical_metrics(df_m, df_e, df_i)
    df_m
    return (df_m,)


@app.cell
def _(df_m, plot_mechanical_metrics):
    fig2 = plot_mechanical_metrics(df_m, figures=True, zoom=True)
    fig2
    return


@app.cell
def _(mo):
    mo.md(r"""## Comparison""")
    return


@app.cell
def _(campaign_selector, environment_selector, mo, test_selector):
    mo.md(f"""
    - **Campaign ID:** {campaign_selector.value}  
    - **Environment ID:** {environment_selector.value}  
    - **Test ID:** {test_selector.value}  
        """)
    return


@app.cell
def _(mo):
    mo.md(f"""VS:""")
    return


@app.cell
def _(campaign_id, dict_tags, mo):
    campaign_selector_2 = mo.ui.dropdown(
        options=list(dict_tags.keys()),
        value = standard_value(campaign_id, list(dict_tags.keys())),
        label="Campaign",
    )
    campaign_selector_2
    return (campaign_selector_2,)


@app.cell
def _(campaign_selector_2, dict_tags, environment_id, mo):
    environment_selector_2 = mo.ui.dropdown(
        options=list(dict_tags[campaign_selector_2.value].keys()),
        value=standard_value(environment_id, list(dict_tags[campaign_selector_2.value].keys())),
        label="Environment",
    )
    environment_selector_2
    return (environment_selector_2,)


@app.cell
def _(campaign_selector_2, dict_tags, environment_selector_2, mo, test_id):
    test_selector_2 = mo.ui.dropdown(
        options=list(dict_tags[campaign_selector_2.value][environment_selector_2.value].keys()),
        value=standard_value(test_id, list(dict_tags[campaign_selector_2.value][environment_selector_2.value].keys())),
        label="Test",
    )
    test_selector_2
    return (test_selector_2,)


@app.cell
def _(campaign_selector_2, environment_selector_2, mo, test_selector_2):
    sql_query_2 = f"""
    SELECT *
    FROM config-enriched-data
    WHERE campaign_id = '{campaign_selector_2.value}' AND environment_id = '{environment_selector_2.value}' AND test_id = '{test_selector_2.value}'
    """
    mo.md(f"```sql\n{sql_query_2}\n```")
    return (sql_query_2,)


@app.cell
def _(client, sql_query_2):
    df_i2 = client.query(sql_query_2)
    return (df_i2,)


@app.cell
def _(
    compute_electrical_metrics,
    compute_mechanical_metrics,
    create_electrical_df,
    create_mechanical_df,
    df_i2,
):
    df_e2 = create_electrical_df(df_i2, window=3)
    df_e2 = compute_electrical_metrics(df_e2, window=3)
    df_m2 = create_mechanical_df(df_i2, window=3)
    df_m2 = compute_mechanical_metrics(df_m2, df_e2, df_i2)
    return df_e2, df_m2


@app.cell
def _(np, plt):
    def plot_electrical_metrics_multi(list_df_es, list_labels, figures=False, zoom=False):
        # Define a consistent color cycle
        color_cycle = plt.cm.tab10.colors  # 10 distinct colors
        n_datasets = len(list_df_es)
        colors = [color_cycle[i % len(color_cycle)] for i in range(n_datasets)]

        fig = plt.figure(figsize=(15, 12))
        fig.suptitle("Electrical Analysis from INA260 Sensor", fontsize=16)

        # Row 1: Voltage and Current
        ax1 = plt.subplot2grid((3, 2), (0, 0))
        ax2 = plt.subplot2grid((3, 2), (0, 1))

        # Row 2: Power
        ax3 = plt.subplot2grid((3, 2), (1, 0), colspan=2)

        # Row 3: Energy and Resistance
        ax4 = plt.subplot2grid((3, 2), (2, 0))
        ax5 = plt.subplot2grid((3, 2), (2, 1))

        # Mapping of axes and columns
        plots = [
            (ax1, "ina260__voltage_v", "Voltage (V)"),
            (ax2, "current_a", "Current (A)"),
            (ax3, "power_w", "Power (W)"),
            (ax4, "energy_j", "Energy (J)"),
            (ax5, "resistance_ohm", "Resistance (Ω)"),
        ]

        # Plot all datasets on each subplot
        for df_idx, (df_e, label, color) in enumerate(zip(list_df_es, list_labels, colors)):
            for ax, col, ylabel in plots:
                # Original and rolling
                ax.plot(df_e["timestamp_s"], df_e[col], color=color, label=label)
                rolling_col = f"{col}_rolling"
                if rolling_col in df_e.columns:
                    ax.plot(df_e["timestamp_s"], df_e[rolling_col], color=color, alpha=0.5)

        for ax, col, ylabel in plots:
            ax.set_ylabel(ylabel)
            ax.grid(True)
    
            # Legend
            ax.legend()
    
            # Text annotations (only if figures=True)
            if figures:
                for df_e, label, color in zip(list_df_es, list_labels, colors):
                    if col == "energy_j":
                        _val_j = np.nanmax(df_e[col])
                        ax.text(0.5, 0.55, f"{label}: {_val_j:.1f} J",
                                transform=ax.transAxes, fontsize=12, color=color,
                                alpha=0.7, ha="center", va="center")
                        _val_wh = _val_j / 3600
                        ax.text(0.5, 0.40, f"({_val_wh:.2f} Wh)",
                                transform=ax.transAxes, fontsize=10, color=color,
                                alpha=0.7, ha="center", va="center")
                    else:
                        _val = np.nanmedian(df_e[col])
                        ax.text(0.5, 0.5, f"{label}: {_val:.1f}",
                                transform=ax.transAxes, fontsize=12, color=color,
                                alpha=0.7, ha="center", va="center")
    
            # Zoom logic (always runs)
            all_vals = np.concatenate([df[col].dropna().values for df in list_df_es])
            if zoom:
                top = np.nanquantile(all_vals, 0.95) * 1.1
                ax.set_ylim(top=top)
            else:
                ax.set_ylim(bottom=0, top=np.nanmax(all_vals) * 1.2)

        plt.tight_layout(rect=[0, 0, 1, 0.96])
        return fig
    return (plot_electrical_metrics_multi,)


@app.cell
def _(np, plt):
    def plot_mechanical_metrics_multi(list_df_ms, list_labels, figures=False, zoom=False):
        # Define a consistent color cycle
        color_cycle = plt.cm.tab10.colors  # 10 distinct colors
        n_datasets = len(list_df_ms)
        colors = [color_cycle[i % len(color_cycle)] for i in range(n_datasets)]

        fig = plt.figure(figsize=(15, 12))
        fig.suptitle("Mechanical Analysis", fontsize=16)

        # Row 1: Thrust and TPW
        ax1 = plt.subplot2grid((3, 2), (0, 0))
        ax2 = plt.subplot2grid((3, 2), (0, 1))

        # Row 2: Aerodynamic Power
        ax3 = plt.subplot2grid((3, 2), (1, 0), colspan=2)

        # Row 3: RPMs
        ax4 = plt.subplot2grid((3, 2), (2, 0))
        ax5 = plt.subplot2grid((3, 2), (2, 1))

        # Mapping of axes and columns
        plots = [
            (ax1, "thrust_n", "Thrust (N)"),
            (ax2, "tpw", "TPW (N/W)"),
            (ax3, "power_aero_w", "Power Aero (W)"),
            (ax4, "RPM_m1", "RPM (Method 1)"),
            (ax5, "RPM_m2", "RPM (Method 2)"),
        ]

        # Plot all datasets on each subplot
        for df_m, label, color in zip(list_df_ms, list_labels, colors):
            for ax, col, ylabel in plots:
                ax.plot(df_m["timestamp_s"], df_m[col], color=color, label=label)
                rolling_col = f"{col}_rolling"
                if rolling_col in df_m.columns:
                    ax.plot(df_m["timestamp_s"], df_m[rolling_col], color=color, alpha=0.5)

        # Configure each subplot
        for ax, col, ylabel in plots:
            ax.set_ylabel(ylabel)
            ax.grid(True)
    
            # Legend
            ax.legend()
    
            # Text annotations (only if figures=True)
            if figures:
                for df_m, label, color in zip(list_df_ms, list_labels, colors):
                    if col == "energy_j":
                        _val_j = np.nanmax(df_m[col])
                        ax.text(0.5, 0.55, f"{label}: {_val_j:.1f} J",
                                transform=ax.transAxes, fontsize=12, color=color,
                                alpha=0.7, ha="center", va="center")
                        _val_wh = _val_j / 3600
                        ax.text(0.5, 0.40, f"({_val_wh:.2f} Wh)",
                                transform=ax.transAxes, fontsize=10, color=color,
                                alpha=0.7, ha="center", va="center")
                    else:
                        _val = np.nanmedian(df_m[col])
                        ax.text(0.5, 0.5, f"{label}: {_val:.1f}",
                                transform=ax.transAxes, fontsize=12, color=color,
                                alpha=0.7, ha="center", va="center")
    
            # Zoom logic (always runs)
            all_vals = np.concatenate([df[col].dropna().values for df in list_df_ms])
            if zoom:
                top = np.nanquantile(all_vals, 0.95) * 1.1
                ax.set_ylim(top=top)
            else:
                ax.set_ylim(bottom=0, top=np.nanmax(all_vals) * 1.2)

        plt.tight_layout(rect=[0, 0, 1, 0.96])
        return fig
    return (plot_mechanical_metrics_multi,)


@app.cell
def _(test_selector, test_selector_2):
    labels_list = [test_selector.value, test_selector_2.value]
    return (labels_list,)


@app.cell
def _(df_e, df_e2, labels_list, plot_electrical_metrics_multi):
    fig3 = plot_electrical_metrics_multi([df_e, df_e2], labels_list, figures=False, zoom=False)
    fig3
    return


@app.cell
def _(df_m, df_m2, labels_list, plot_mechanical_metrics_multi):
    fig4 = plot_mechanical_metrics_multi([df_m, df_m2], labels_list, figures=False, zoom=True)
    fig4
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
