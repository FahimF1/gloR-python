import matplotlib.pyplot as plt

def visualize_scores(data):
    """
    Visualizes Attractiveness Scores for regions.

    Parameters:
    - data (pd.DataFrame): Regions with scores.
    """
    plt.bar(data['Region'], data['Attractiveness_Score'], color='skyblue')
    plt.title("Attractiveness Scores by Region")
    plt.xlabel("Region")
    plt.ylabel("Attractiveness Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
