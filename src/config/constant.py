from pydantic import BaseModel


class Constant(BaseModel):
    APP_NAME: str = "NeuroAR"


constant = Constant()
