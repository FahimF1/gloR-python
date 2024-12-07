import pandas as pd
from gloR.calculate import calculate_attractiveness

def test_calculate_attractiveness():
    data = pd.DataFrame({
        'Region': ['Austin', 'Denver'],
        'Cost_of_Living': [0.5, 0.6],
        'Visa_Ease': [0.8, 0.7]
    })
    weights = {'Cost_of_Living': 0.6, 'Visa_Ease': 0.4}
    result = calculate_attractiveness(data, weights)
    assert result.iloc[0]['Region'] == 'Denver'  # Expected Denver, not Austin

