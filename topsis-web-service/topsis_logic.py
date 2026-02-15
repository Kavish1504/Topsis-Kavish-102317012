import pandas as pd
import numpy as np


def validate_inputs(df, weights, impacts):
    if df.shape[1] < 3:
        raise ValueError("Input file must contain three or more columns")
    
    for col in df.columns[1:]:
        if not pd.api.types.is_numeric_dtype(df[col]):
            raise ValueError(f"Column '{col}' contains non-numeric values")
    
    num_criteria = len(df.columns) - 1
    if len(weights) != num_criteria:
        raise ValueError(f"Number of weights must equal number of criteria")
    
    if len(impacts) != num_criteria:
        raise ValueError(f"Number of impacts must equal number of criteria")
    
    for impact in impacts:
        if impact not in ['+', '-']:
            raise ValueError(f"Impacts must be either '+' or '-'")
    
    return True


def topsis_calculate(df, weights, impacts):
    validate_inputs(df, weights, impacts)
    
    normalized_df = df.copy()
    for col in df.columns[1:]:
        sum_of_squares = np.sqrt((df[col] ** 2).sum())
        normalized_df[col] = df[col] / sum_of_squares
    
    weighted_df = normalized_df.copy()
    for i, col in enumerate(normalized_df.columns[1:]):
        weighted_df[col] = normalized_df[col] * weights[i]
    
    ideal_best = []
    ideal_worst = []
    for i, col in enumerate(weighted_df.columns[1:]):
        if impacts[i] == '+':
            ideal_best.append(weighted_df[col].max())
            ideal_worst.append(weighted_df[col].min())
        else:
            ideal_best.append(weighted_df[col].min())
            ideal_worst.append(weighted_df[col].max())
    
    distance_best = []
    distance_worst = []
    for idx in range(len(weighted_df)):
        dist_best = 0
        dist_worst = 0
        for i, col in enumerate(weighted_df.columns[1:]):
            dist_best += (weighted_df[col].iloc[idx] - ideal_best[i]) ** 2
            dist_worst += (weighted_df[col].iloc[idx] - ideal_worst[i]) ** 2
        distance_best.append(np.sqrt(dist_best))
        distance_worst.append(np.sqrt(dist_worst))
    
    scores = []
    for i in range(len(distance_best)):
        score = distance_worst[i] / (distance_best[i] + distance_worst[i])
        scores.append(score)
    
    result_df = df.copy()
    result_df['Topsis Score'] = scores
    result_df['Rank'] = result_df['Topsis Score'].rank(ascending=False).astype(int)
    
    return result_df
