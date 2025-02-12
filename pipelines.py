import logging

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

# Define column names used in the dataset
CAT_COLS = [
    'airline',
    'departure_time',
    'stops',
    'arrival_time',
    'class',
]

CONCAT_COLS = [
    'source_city',
    'destination_city',
]

NUM_COLS = [
    'duration',
    'days_left',
]

def concat_features(X, separator="_"):
    """
    Concatenates multiple string features into one feature for each row.

    Parameters:
    ----------
    X : pandas.DataFrame or numpy.ndarray
        Input data containing features to concatenate. The data should be 2D 
        with string-like columns or elements.

    separator : str, optional, default='_'
        Separator to use between concatenated values.

    Returns:
    -------
    numpy.ndarray
        A 2D numpy array with each row as a single concatenated string 
        feature.

    Example:
    -------
    >>> import pandas as pd
    >>> df = pd.DataFrame({'feature1': ['a'], 'feature2': ['b']})
    >>> concat_features(df)
    array([['a_b']], dtype=object)
    """
    if isinstance(X, pd.DataFrame):
        X_values = X.values
    else:
        X_values = X

    concatenated = [separator.join(map(str, row)) for row in X_values]
    return np.array(concatenated).reshape(-1, 1)

# Pipeline for processing categorical features
cat_pipe = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
    ("onehot", OneHotEncoder(handle_unknown='ignore')),
])

# Pipeline for concatenating and encoding specified features
concat_pipe = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
    ("concatenator", FunctionTransformer(concat_features, validate=False)),
    ("onehot", OneHotEncoder(handle_unknown='ignore')),
])

# Pipeline for processing numerical features
num_pipe = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="mean")),
    ("scaler", StandardScaler()),
])

# Combine all pipelines into a single preprocessor
preprocessor = ColumnTransformer(transformers=[
    ("cat", cat_pipe, CAT_COLS),
    ("concat", concat_pipe, CONCAT_COLS),
    ("num", num_pipe, NUM_COLS),
])

def main():
    """
    Example usage of the preprocessor pipeline.
    Loads sample data, preprocesses it, and fits a simple Linear Regression model.
    """
    # Set up basic configuration for logging
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    logging.info("Starting example...")

    # Load the dataset (replace with your actual data path)
    df = pd.read_csv("./data/Clean_Dataset.csv").sample(100, random_state=42)

    # Separate features and target variable
    X = df.drop("price", axis=1)
    y = df["price"]

    # Fit the preprocessor on the data
    X_preprocessed = preprocessor.fit_transform(X)

    logging.info("Preprocessing completed.")

    # Fit a simple model for demonstration purposes
    model = LinearRegression()
    model.fit(X_preprocessed, y)

    logging.info("Model training completed.")
    logging.info("Example usage finished.")

if __name__ == "__main__":
    main()