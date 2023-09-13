from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from app.core.config import azureCognitiveServicesSettings

credentials = CognitiveServicesCredentials(azureCognitiveServicesSettings.key)
client = ComputerVisionClient(azureCognitiveServicesSettings.endpoint, credentials)
