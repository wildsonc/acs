from ninja import ModelSchema, Schema

from .models import CPE, Model, Parameter

__all__ = [
    "CPEOut",
    "ModelOut",
    "ParameterOut",
    "RebootSchema",
]


class ParameterOut(ModelSchema):
    is_writable: bool

    class Meta:
        model = Parameter
        fields = ["name", "path"]

    @staticmethod
    def resolve_is_writable(obj: Parameter):
        return "cpu" in obj.name


class ModelOut(ModelSchema):
    parameters: list[ParameterOut]

    class Meta:
        model = Model
        fields = "__all__"


class CPEIn(Schema):
    id: str
    sn: str
    model_id: int


class CPEOut(ModelSchema):
    model: ModelOut

    class Meta:
        model = CPE
        fields = "__all__"


class RebootSchema(Schema):
    success: bool
    message: str
