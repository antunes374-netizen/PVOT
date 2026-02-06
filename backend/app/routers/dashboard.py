from datetime import date, timedelta
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import SessionLocal
from .. import models, schemas

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def _build_alerts(visitas):
    today = date.today()
    alerts = []
    for visita in visitas:
        if visita.data_inicio < today:
            continue
        delta_days = (visita.data_inicio - today).days
        if delta_days == 30:
            alerts.append(
                f"Iniciar aquisição de passagens para VOT em {visita.uga.sigla} - {visita.data_inicio:%d/%m/%Y}"
            )
        if delta_days == 15:
            alerts.append(
                f"Enviar Ordem de Serviço para {visita.uga.sigla}"
            )
        if delta_days == 8:
            alerts.append(
                f"Aguardando dúvidas da {visita.uga.sigla} por DIEx"
            )
        if delta_days == 7:
            alerts.append(
                f"Finalizar Relatório Diagnóstico para {visita.uga.sigla}"
            )
        if delta_days == -15:
            alerts.append(
                f"Prazo final para Relatório Final da VOT em {visita.uga.sigla}"
            )
    return alerts


@router.get("/resumo", response_model=schemas.DashboardResumo)
def dashboard_resumo(db: Session = Depends(get_db)):
    visitas = db.query(models.Visita).order_by(models.Visita.data_inicio).all()
    visitas_planejadas = len(visitas)
    visitas_concluidas = len([v for v in visitas if v.status == models.StatusVisita.CONCLUIDA])

    today = date.today()
    proximas_visitas = [v for v in visitas if v.data_inicio >= today][:5]

    distribuicao_estado = {}
    distribuicao_mensal = {}
    for visita in visitas:
        distribuicao_estado[visita.uga.estado] = distribuicao_estado.get(visita.uga.estado, 0) + 1
        mes = visita.data_inicio.strftime("%m/%Y")
        distribuicao_mensal[mes] = distribuicao_mensal.get(mes, 0) + 1

    proximas = [
        schemas.VisitaDashboard(
            id=visita.id,
            uga_id=visita.uga_id,
            uga_sigla=visita.uga.sigla,
            data_inicio=visita.data_inicio,
            duracao_dias=visita.duracao_dias,
            status=visita.status,
        )
        for visita in proximas_visitas
    ]

    return schemas.DashboardResumo(
        visitas_planejadas=visitas_planejadas,
        visitas_concluidas=visitas_concluidas,
        proximas_visitas=proximas,
        alertas=_build_alerts(visitas),
        distribuicao_estado=distribuicao_estado,
        distribuicao_mensal=distribuicao_mensal,
    )
