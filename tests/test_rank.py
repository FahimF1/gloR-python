import pandas as pd
from gloR.calculate import calculate_attractiveness

def test_rank_regions():
    data = pd.DataFrame({
        'Region': ['Austin', 'Denver'],
        'Attractiveness_Score': [0.62, 0.64]
    })
    result = rank_regions(data, top_n=1)
    assert result.iloc[0]['Region'] == 'Denver'
