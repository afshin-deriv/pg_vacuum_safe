import requests


def check_datadog_metrics(config):
    headers = {
        'Content-Type': 'application/json',
        'DD-API-KEY': config['api_key'],
        'DD-APPLICATION-KEY': config['app_key']
    }
    metrics = config['metrics']
    for metric, query in metrics.items():
        response = requests.get(
            f'https://api.datadoghq.com/api/v1/query?query={query}&from=now-5m&to=now', headers=headers)
        data = response.json()
        # Process data and check thresholds
        # Example: if data exceeds threshold, raise error
        # ...

# More functions to fetch and process Datadog metrics
