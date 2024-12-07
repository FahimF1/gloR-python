def tune_weights(weights, adjustment):
    """
    Adjusts weights for metrics based on user input.

    Parameters:
    - weights (dict): Current weights for each metric.
    - adjustment (dict): Changes to apply to the weights.

    Returns:
    - dict: Updated weights.
    """
    updated_weights = weights.copy()
    for metric, delta in adjustment.items():
        if metric in updated_weights:
            updated_weights[metric] += delta
            # Ensure weights remain non-negative
            updated_weights[metric] = max(0, updated_weights[metric])
    return updated_weights
