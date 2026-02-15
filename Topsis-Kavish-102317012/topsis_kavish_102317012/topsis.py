import pandas as pd
import numpy as np
import sys
import os


def validate_inputs(df, weights, impacts):
    if df.shape[1] < 3:
        raise ValueError("Input file must contain three or more columns")

    for col in df.columns[1:]:
        if not pd.api.types.is_numeric_dtype(df[col]):
            raise ValueError(f"Column '{col}' contains non-numeric values. From 2nd to last columns must be numeric only.")
    
    num_criteria = len(df.columns) - 1
    if len(weights) != num_criteria:
        raise ValueError(f"Number of weights ({len(weights)}) must be equal to number of criteria ({num_criteria})")
    
    if len(impacts) != num_criteria:
        raise ValueError(f"Number of impacts ({len(impacts)}) must be equal to number of criteria ({num_criteria})")
    
    for impact in impacts:
        if impact not in ['+', '-']:
            raise ValueError(f"Impacts must be either '+' or '-'. Found: '{impact}'")
    
    return True


def normalize_matrix(df):
    normalized = df.copy()
    for col in df.columns[1:]:
        sum_of_squares = np.sqrt((df[col] ** 2).sum())
        normalized[col] = df[col] / sum_of_squares
    
    return normalized


def calculate_weighted_matrix(normalized_df, weights):
    weighted = normalized_df.copy()
    
    for i, col in enumerate(normalized_df.columns[1:]):
        weighted[col] = normalized_df[col] * weights[i]
    
    return weighted


def calculate_ideal_values(weighted_df, impacts):
    ideal_best = []
    ideal_worst = []
    
    for i, col in enumerate(weighted_df.columns[1:]):
        if impacts[i] == '+':
            ideal_best.append(weighted_df[col].max())
            ideal_worst.append(weighted_df[col].min())
        else:
            ideal_best.append(weighted_df[col].min())
            ideal_worst.append(weighted_df[col].max())
    
    return ideal_best, ideal_worst


def calculate_distances(weighted_df, ideal_best, ideal_worst):
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
    
    return distance_best, distance_worst


def calculate_topsis_score(distance_best, distance_worst):
    scores = []
    
    for i in range(len(distance_best)):
        score = distance_worst[i] / (distance_best[i] + distance_worst[i])
        scores.append(score)
    
    return scores


def topsis(input_file, weights_str, impacts_str, output_file):
    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"File '{input_file}' not found")

        df = pd.read_csv(input_file)
        weights = [float(w.strip()) for w in weights_str.split(',')]
        impacts = [i.strip() for i in impacts_str.split(',')]
        validate_inputs(df, weights, impacts)
        model_names = df.iloc[:, 0]
        normalized_df = normalize_matrix(df)
        weighted_df = calculate_weighted_matrix(normalized_df, weights)
        ideal_best, ideal_worst = calculate_ideal_values(weighted_df, impacts)
        distance_best, distance_worst = calculate_distances(weighted_df, ideal_best, ideal_worst)
        topsis_scores = calculate_topsis_score(distance_best, distance_worst)
        result_df = df.copy()
        result_df['Topsis Score'] = topsis_scores
        result_df['Rank'] = result_df['Topsis Score'].rank(ascending=False).astype(int)
        result_df.to_csv(output_file, index=False)
        
        print(f"Topsis calculation completed successfully!")
        print(f"Results saved to '{output_file}'")
        
        return result_df
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 5:
        print("Error: Incorrect number of parameters")
        print("\nUsage:")
        print("  python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
        print("\nExample:")
        print('  python topsis.py data.xlsx "1,1,1,1" "+,+,-,+" output.csv')
        sys.exit(1)
    
    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]
    
    topsis(input_file, weights, impacts, output_file)


if __name__ == "__main__":
    main()
