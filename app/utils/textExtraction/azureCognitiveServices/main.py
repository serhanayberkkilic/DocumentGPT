from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials


endpoint = "https://cognitiveayberk.cognitiveservices.azure.com/"
subscription_key = "611f005d036740cc8504679e062dccf0"


credentials = CognitiveServicesCredentials(subscription_key)
client = ComputerVisionClient(endpoint, credentials)
