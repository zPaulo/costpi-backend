from datetime import timedelta

from .schemas import FormIn, taskOut

BASE_CYCLE = {"milho":100, "feijao":80, "mandioca":300,
              "arroz":120, "tomate":110}

MULT = {
    "plantio": {"MANUAL_ENXADA": 1.5, "SEMI_MECANIZADO": 1.2, "MECANIZADO": 1},
    "tratos":  {"GOTEJO": 0.9, "ASPERSAO_MANUAL": 1.4, "CHUVA_NATURAL": 1},
    "solo":    {"PLANTIO_DIRETO": .85, "ORGÂNICO": 1.1, "CONVENCIONAL": 1},
}

def generate_schedule(p:FormIn) -> list[taskOut]:
    """
    Gera um cronograma de tarefas baseado no tipo de semente, método de plantio,
    tipo de irrigação e solo, e data de início fornecida.
    """
    ciclo = BASE_CYCLE[p.seed.lower()]
    plantio = round(1 * MULT["plantio"][p.metodo_plantio])
    tratos = round((ciclo - 30)  * MULT["tratos"][p.irrigacao])
    vegetativo, florescimento, maturacao = tratos // 2, tratos - tratos // 2, 30
    etapas = [
        ("Preparo de solo", 3 * MULT["solo"][p.solo]),
        ("Plantio", plantio),
        ("Crescimento vegetativo", vegetativo),
        ("Florescimento", florescimento),
        ("Maturação", maturacao),
        ("Colheita", 2),
        ("Pós-colheita", 2),
    ]
    cron = []
    cursor = p.data_inicio
    for nome, dias in etapas:
        fim = cursor + timedelta(days=int(dias))
        cron.append(taskOut(task=nome,start=cursor, end=fim))
        cursor = fim
    return cron