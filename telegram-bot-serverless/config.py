import boto3

ssm_client = boto3.client("ssm")
response = ssm_client.get_parameter(Name="telegramToken", WithDecryption=True)
TELEGRAM_TOKEN = response["Parameter"]["Value"]

response = ssm_client.get_parameter(Name="omdbApiKey", WithDecryption=True)
OMDB_API_KEY = response["Parameter"]["Value"]
OMDB_URL = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&"
