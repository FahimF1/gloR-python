def test_tune_weights():
    weights = {'Cost_of_Living': 0.5, 'Visa_Ease': 0.5}
    adjustment = {'Cost_of_Living': 0.1, 'Visa_Ease': -0.2}
    updated_weights = tune_weights(weights, adjustment)
    assert updated_weights['Cost_of_Living'] == 0.6
    assert updated_weights['Visa_Ease'] == 0.3
