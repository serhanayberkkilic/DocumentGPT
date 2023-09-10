from app.utils.textExtraction.azureCognitiveServices.main import client
from io import BytesIO


class textExtraction ():

    def __init__(self):
        pass

    def Text(self,file) -> list:
        response = client.read_in_stream(BytesIO(file), raw=True)
        operation_location = response.headers["Operation-Location"]
        operation_id = operation_location.split("/")[-1]
        while True:
            result = client.get_read_result(operation_id)
            if result.status.lower () not in ['notstarted', 'running']:
                break
        
        text_info_total=[]

        for readResult in result.analyze_result.read_results:
            for line in readResult.lines:
                text_info_total.append([line.text])

        return text_info_total

