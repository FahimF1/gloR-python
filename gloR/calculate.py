import pandas as pd

def calculate_attractiveness(data, weights):
    """
    Computes Attractiveness Scores for regions.

    Parameters:
    - data (pd.DataFrame): Regional metrics.
    - weights (dict): Weights for each metric.

    Returns:
    - pd.DataFrame: Regions with their calculated scores.
    """
    scores = data.copy()
    scores['Attractiveness_Score'] = sum(
        scores[metric] * weight for metric, weight in weights.items()
    )
    return scores.sort_values(by='Attractiveness_Score', ascending=False)
