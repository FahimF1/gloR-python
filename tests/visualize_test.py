def test_visualize_scores():
    data = pd.DataFrame({
        'Region': ['Austin', 'Denver'],
        'Attractiveness_Score': [0.62, 0.64]
    })
    visualize_scores(data)  # Ensure this runs without throwing exceptions
