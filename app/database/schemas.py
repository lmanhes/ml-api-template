from pydantic import BaseModel


###############  Input schemas  ###############

class MLInput(BaseModel):
    feat_1: float
    feat_2: float
    feat_3: float
    name: str

    class Config:
        orm_mode = True