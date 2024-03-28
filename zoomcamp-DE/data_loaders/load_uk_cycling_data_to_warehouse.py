import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    urls = [
        'https://cycling.data.tfl.gov.uk/usage-stats/346JourneyDataExtract28Nov2022-04Dec2022.csv',
        'https://cycling.data.tfl.gov.uk/usage-stats/347JourneyDataExtract05Dec2022-11Dec2022.csv',
        'https://cycling.data.tfl.gov.uk/usage-stats/348JourneyDataExtract12Dec2022-18Dec2022.csv',
        'https://cycling.data.tfl.gov.uk/usage-stats/349JourneyDataExtract19Dec2022-25Dec2022.csv',
        'https://cycling.data.tfl.gov.uk/usage-stats/350JourneyDataExtract26Dec2022-01Jan2023.csv'
    ]

    dfs = []

    # Define custom headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',  # Example: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        'Referer': 'https://www.emmanuelokoro.com/'  # Example: 'https://www.example.com/'
    }

    for url in urls:
        try:
            # Send the GET request with custom headers
            response = requests.get(url, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Convert the content into a file-like object
                content = io.BytesIO(response.content)
                # Read the CSV data directly into a pandas DataFrame
                dfs.append(pd.read_csv(content))
                # Process the DataFrame as needed
                print("Data loaded successfully!")
            else:
                print(f"Failed to download data: HTTP status code {response.status_code}")

        except requests.exceptions.RequestException as e:
            print("Error:", e)
    
    return pd.concat(dfs)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
