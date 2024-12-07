def rank_regions(data, top_n=None):
    """
    Ranks regions based on Attractiveness Scores.

    Parameters:
    - data (pd.DataFrame): Regions with scores.
    - top_n (int): Number of top regions to display.

    Returns:
    - pd.DataFrame: Ranked regions.
    """
    ranked = data.sort_values(by='Attractiveness_Score', ascending=False)
    if top_n:
        return ranked.head(top_n)
    return ranked
