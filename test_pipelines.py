# test_pipelines.py

import pytest
import pandas as pd
import numpy as np
from sklearn.exceptions import NotFittedError
from sklearn.linear_model import LinearRegression

# Import the functions and pipeline creator to be tested
from pipelines import concat_features, get_preprocessor

def test_concat_features_with_dataframe():
    """
    Test the concat_features function with a pandas DataFrame input.
    """
    # Create a sample DataFrame
    df = pd.DataFrame({
        'source_city': ['Delhi', 'Mumbai'],
        'destination_city': ['Kolkata', 'Chennai']
    })
    # Expected output
    expected_output = np.array([['Delhi_Kolkata'], ['Mumbai_Chennai']])
    
    # Call the function
    result = concat_features(df)
    
    # Assert that the result matches the expected output
    assert np.array_equal(result, expected_output), "concat_features did not produce the expected output with DataFrame input."

def test_concat_features_with_numpy_array():
    """
    Test the concat_features function with a numpy array input.
    """
    # Create a sample numpy array
    arr = np.array([
        ['Delhi', 'Kolkata'],
        ['Mumbai', 'Chennai']
    ])
    # Expected output
    expected_output = np.array([['Delhi_Kolkata'], ['Mumbai_Chennai']])
    
    # Call the function
    result = concat_features(arr)
    
    # Assert that the result matches the expected output
    assert np.array_equal(result, expected_output), "concat_features did not produce the expected output with numpy array input."

def test_concat_features_with_custom_separator():
    """
    Test the concat_features function using a custom separator.
    """
    # Create a sample DataFrame
    df = pd.DataFrame({
        'feature1': ['A', 'B'],
        'feature2': ['X', 'Y']
    })
    # Expected output with custom separator '-'
    expected_output = np.array([['A-X'], ['B-Y']])
    
    # Call the function with custom separator
    result = concat_features(df, separator='-')
    
    # Assert that the result matches the expected output
    assert np.array_equal(result, expected_output), "concat_features did not respect the custom separator."

def test_preprocessor_pipeline():
    """
    Test the preprocessor pipeline to ensure it transforms data as expected.
    """
    # Create a sample DataFrame with all required columns
    df = pd.DataFrame({
        'airline': ['Air India', 'IndiGo'],
        'departure_time': ['Early Morning', 'Evening'],
        'stops': ['zero', 'one'],
        'arrival_time': ['Morning', 'Late Night'],
        'class': ['Economy', 'Business'],
        'source_city': ['Delhi', 'Mumbai'],
        'destination_city': ['Kolkata', 'Chennai'],
        'duration': [120, 180],
        'days_left': [20, 10]
    })
    # Fit and transform the data using the preprocessor
    preprocessor = get_preprocessor()
    preprocessor.fit(df)
    transformed_data = preprocessor.transform(df)
    
    # Check that the transformed data has the expected shape
    # Since we are one-hot encoding categorical features, the exact number of columns can vary
    # Here, we check that the transformed data has the correct number of rows
    assert transformed_data.shape[0] == df.shape[0], "Preprocessor did not transform the correct number of samples."

def test_pipeline_integration_with_model():
    """
    Test the integration of the preprocessor pipeline with a simple Linear Regression model.
    """
    # Create a sample DataFrame with all required columns
    df = pd.DataFrame({
        'airline': ['Air India', 'IndiGo', 'SpiceJet'],
        'departure_time': ['Early Morning', 'Evening', 'Night'],
        'stops': ['zero', 'one', 'two_or_more'],
        'arrival_time': ['Morning', 'Late Night', 'Evening'],
        'class': ['Economy', 'Business', 'Economy'],
        'source_city': ['Delhi', 'Mumbai', 'Chennai'],
        'destination_city': ['Kolkata', 'Chennai', 'Delhi'],
        'duration': [120, 180, 240],
        'days_left': [20, 10, 5],
        'price': [5000, 7000, 6500]
    })
    # Separate features and target
    X = df.drop('price', axis=1)
    y = df['price']
    
    # Fit the preprocessor and transform the features
    preprocessor = get_preprocessor()
    X_transformed = preprocessor.fit_transform(X)
    
    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_transformed, y)
    
    # Make predictions
    predictions = model.predict(X_transformed)
    
    # Check that predictions were made
    assert len(predictions) == len(y), "Model did not make predictions for all samples."

def test_concat_features_empty_input():
    """
    Test concat_features with an empty input to ensure it handles it gracefully.
    """
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['feature1', 'feature2'])
    
    # Call the function
    result = concat_features(df)
    
    # Expected output is an empty array with shape (0, 1)
    expected_output = np.empty((0, 1), dtype=object)
    
    # Assert that the result matches the expected output
    assert result.shape == expected_output.shape, "concat_features did not handle empty input as expected."

def test_preprocessor_not_fitted_error():
    """
    Test that the preprocessor raises a NotFittedError when transform is called before fit.
    """
    preprocessor = get_preprocessor()
    df = pd.DataFrame({
        'airline': ['Air India'],
        'departure_time': ['Early Morning'],
        'stops': ['zero'],
        'arrival_time': ['Morning'],
        'class': ['Economy'],
        'source_city': ['Delhi'],
        'destination_city': ['Kolkata'],
        'duration': [120],
        'days_left': [20]
    })

    # Try transforming without fitting
    with pytest.raises(NotFittedError):
        preprocessor.transform(df)