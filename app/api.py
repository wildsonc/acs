from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ninja import Router

from app import controller

from .models import CPE, Model
from .schemas import CPEOut, ModelOut, RebootSchema
from app import schemas


router = Router()


@router.get("/sync-cpes", tags=["CPE"])
def sync_cpes(request):
    return {"status": "ok"}


@router.get("/models", tags=["Models"], response=list[ModelOut])
def list_models(request):
    return Model.objects.all()


@router.get("/cpes", tags=["CPEs"], response=list[CPEOut])
def list_cpes(request):
    return CPE.objects.all()


@router.get("/cpes/{cpe_id}", tags=["CPEs"], response=CPEOut)
def get_cpe(request, cpe_id: int):
    return CPE.objects.get(id=cpe_id)


@router.post("/cpes/", tags=["CPEs"], response=CPEOut)
def create_cpe(request, payload: schemas.CPEIn):
    print(payload.dict())
    cpe = CPE.objects.create(**payload.dict())
    return cpe


@router.post("/cpes/{sn}/reboot", tags=["CPEs"])
def reboot_cpe(request, sn: str, force_reboot: bool | None = None):
    cpe = get_object_or_404(CPE, sn=sn)
    res = controller.reboot_cpe(cpe)

    return JsonResponse({"message": res.message}, status=res.status_code)
