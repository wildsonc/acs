from app.lib.genieacs import GenieACS
from app.models import CPE
from ninja import Schema


class RebootSchema(Schema):
    status_code: int
    message: str


def reboot_cpe(cpe: CPE) -> RebootSchema:
    ga = GenieACS()

    res = ga.task_reboot(cpe.pk)

    return RebootSchema(status_code=res.status_code, message=res.text)
