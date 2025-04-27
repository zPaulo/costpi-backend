from http import HTTPStatus

from ninja import Router

from .schemas import FormIn, StatusSchema, taskOut
from .services import generate_schedule

router = Router(tags=["gantt"])

@router.get(
    'healthcheck',
    response=StatusSchema,
    tags=['gantt'],
    summary='Health Check',
    description='Health Check for Gantt API',
)
def health_check(request):
    return HTTPStatus.OK, {"status": "OK"}

@router.post(
    "/schedule", 
    response=list[taskOut],
    tags=["gantt"],
    summary="Get Gantt Schedule",
    description="Get Gantt Schedule",)
def schedule(request, payload: FormIn):
    """  Gera um cronograma de tarefas baseado no tipo de semente, método de plantio,
    tipo de irrigação e solo, e data de início fornecida.
    """
    return generate_schedule(payload)