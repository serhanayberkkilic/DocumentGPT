from typing import  List, Union
from pydantic import AnyHttpUrl, EmailStr,validator,BaseModel,Field,constr
from pydantic_settings import BaseSettings

class contact(BaseModel):
    name: str
    url: AnyHttpUrl
    email: EmailStr

class licenseInfo(BaseModel):
    name: str
    url: AnyHttpUrl


class Settings(BaseSettings):
    
    apiStr: str = "/api/v1"
    serverName: str
    serverHost: AnyHttpUrl
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    backendCorsOrigins:List[AnyHttpUrl] = []

    @validator("backendCorsOrigins", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    projectName: str
    projectDescription: str
    projectVersion: float
    termsOfService: str
    contact: contact
    licenseInfo: licenseInfo

class AzureCognitiveServicesSettings(BaseSettings):
    endpoint: str
    key: str

class openaiSettings(BaseSettings):
    key: str


settings = Settings(
    serverName="localhost",
    serverHost="http://localhost:8000",
    backendCorsOrigins=["http://localhost:8000"],
    projectName="Risetechnologies",
    projectDescription="Risetechnologies",
    projectVersion=0.2,
    termsOfService="https://ayberkkilic.com",
    
    contact=contact(
        name="Serhan Ayberk Kilic",
        url ="https://ayberkkilic.com",
        email="serhanayberkkilic@gmail.com"
    ),
    
    licenseInfo=licenseInfo(
        name="Apache 2.0",
        url="https://www.apache.org/licenses/LICENSE-2.0.html"
    )
    
)


azureCognitiveServicesSettings = AzureCognitiveServicesSettings(
    endpoint="https://cognitiveayberk.cognitiveservices.azure.com/",
    key="611f005d036740cc8504679e062dccf0"
)


openaisettings = openaiSettings(
    key="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"
)