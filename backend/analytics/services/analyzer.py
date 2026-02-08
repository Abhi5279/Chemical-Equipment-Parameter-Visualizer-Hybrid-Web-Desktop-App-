# import pandas as pd


# def analyze_equipment_csv(csv_file):
#     """
#     Reads equipment CSV and returns analytics summary
#     """

#     df = pd.read_csv(csv_file)

#     # Normalize column names (safety)
#     df.columns = [col.strip().lower() for col in df.columns]

#     total_equipment = len(df)

#     avg_flowrate = round(df["flowrate"].mean(), 2)
#     avg_pressure = round(df["pressure"].mean(), 2)
#     avg_temperature = round(df["temperature"].mean(), 2)

#     # Equipment type distribution
#     type_distribution = (
#         df["type"]
#         .value_counts()
#         .to_dict()
#     )

#     # Risk classification (simple but powerful)
#     high_pressure_threshold = df["pressure"].quantile(0.75)
#     high_temp_threshold = df["temperature"].quantile(0.75)

#     high_risk_count = len(
#         df[
#             (df["pressure"] > high_pressure_threshold) |
#             (df["temperature"] > high_temp_threshold)
#         ]
#     )

#     normal_count = total_equipment - high_risk_count

#     # Health score (rule-based)
#     health_score = int(
#         max(
#             0,
#             100 - (high_risk_count / total_equipment) * 100
#         )
#     )

#     summary = {
#         "total_equipment": total_equipment,
#         "averages": {
#             "flowrate": avg_flowrate,
#             "pressure": avg_pressure,
#             "temperature": avg_temperature,
#         },
#         "equipment_type_distribution": type_distribution,
#         "risk_analysis": {
#             "high_risk": high_risk_count,
#             "normal": normal_count,
#         },
#         "health_score": health_score,
#     }

#     return summary

import pandas as pd
import json


def analyze_equipment_csv(csv_file):
    """
    Reads equipment CSV and returns analytics summary as JSON-compatible dict
    """

    df = pd.read_csv(csv_file)

    # Normalize column names
    df.columns = [col.strip().lower() for col in df.columns]

    total_equipment = int(len(df))

    avg_flowrate = round(float(df["flowrate"].mean()), 2)
    avg_pressure = round(float(df["pressure"].mean()), 2)
    avg_temperature = round(float(df["temperature"].mean()), 2)

    # Equipment type distribution
    type_distribution = (
        df["type"]
        .value_counts()
        .astype(int)
        .to_dict()
    )

    # Risk classification
    high_pressure_threshold = float(df["pressure"].quantile(0.75))
    high_temp_threshold = float(df["temperature"].quantile(0.75))

    high_risk_count = int(
        len(
            df[
                (df["pressure"] > high_pressure_threshold) |
                (df["temperature"] > high_temp_threshold)
            ]
        )
    )

    normal_count = int(total_equipment - high_risk_count)

    # Health score
    health_score = int(
        max(
            0,
            100 - (high_risk_count / total_equipment) * 100
        )
    )

    summary = {
        "total_equipment": total_equipment,
        "averages": {
            "flowrate": avg_flowrate,
            "pressure": avg_pressure,
            "temperature": avg_temperature
        },
        "equipment_type_distribution": type_distribution,
        "risk_analysis": {
            "high_risk": high_risk_count,
            "normal": normal_count
        },
        "health_score": health_score
    }

    return summary
