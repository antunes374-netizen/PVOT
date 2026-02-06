from datetime import date
from sqlalchemy.orm import Session

from .db import Base, engine, SessionLocal
from .models import (
    CategoriaDiaria,
    DiariaValor,
    Militar,
    PostoGraduacao,
    Pvot,
    Secao,
    StatusPVOT,
    TipoUG,
    Trecho,
    TipoVisita,
    Uga,
    Visita,
)


def seed_ugas(db: Session):
    ugas_data = [
        {"sigla": "Cmdo 7ª RM", "nome_completo": "Comando da 7ª Região Militar", "codigo_uasg": "160200", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PLENA},
        {"sigla": "Esc R Op C Pipa 7ª RM", "nome_completo": "Escritório Regional de Operação Carro-Pipa 7ª RM", "codigo_uasg": "160201", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.ORCAMENTARIA, "opera_carro_pipa": True},
        {"sigla": "Ba Adm Curado", "nome_completo": "Base Administrativa do Curado", "codigo_uasg": "160202", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PLENA},
        {"sigla": "7º D Sup", "nome_completo": "7º Depósito de Suprimento", "codigo_uasg": "160203", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PLENA, "possui_paiol": True},
        {"sigla": "14º B Log", "nome_completo": "14º Batalhão Logístico", "codigo_uasg": "160204", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PLENA},
        {"sigla": "CRO/7", "nome_completo": "Centro de Reabilitação e Odontologia /7", "codigo_uasg": "160205", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PLENA},
        {"sigla": "Pq R Mnt/7", "nome_completo": "Parque Regional de Manutenção/7", "codigo_uasg": "160206", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PLENA},
        {"sigla": "CMR", "nome_completo": "Colégio Militar do Recife", "codigo_uasg": "160207", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PLENA},
        {"sigla": "5º CTA", "nome_completo": "5º Centro de Telemática de Área", "codigo_uasg": "160208", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PATRIMONIAL},
        {"sigla": "4º B Com", "nome_completo": "4º Batalhão de Comunicações", "codigo_uasg": "160209", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PATRIMONIAL},
        {"sigla": "HMAR", "nome_completo": "Hospital Militar de Área do Recife", "codigo_uasg": "160210", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PLENA, "sensivel": True},
        {"sigla": "4º BPE", "nome_completo": "4º Batalhão de Polícia do Exército", "codigo_uasg": "160211", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PATRIMONIAL},
        {"sigla": "10ª Bda Inf Mtz", "nome_completo": "10ª Brigada de Infantaria Motorizada", "codigo_uasg": "160212", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PATRIMONIAL},
        {"sigla": "7ª Cia Com", "nome_completo": "7ª Companhia de Comunicações", "codigo_uasg": "160213", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PATRIMONIAL},
        {"sigla": "7º GAC", "nome_completo": "7º Grupo de Artilharia de Campanha", "codigo_uasg": "160214", "cidade": "Olinda", "estado": "PE", "tipo_ug": TipoUG.PATRIMONIAL},
        {"sigla": "CMNE", "nome_completo": "Comando Militar do Nordeste", "codigo_uasg": "160215", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PLENA},
        {"sigla": "CPOR/R", "nome_completo": "Centro de Preparação de Oficiais da Reserva/Recife", "codigo_uasg": "160216", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PLENA},
        {"sigla": "3º CGEO", "nome_completo": "3º Centro de Geoinformação", "codigo_uasg": "160217", "cidade": "Olinda", "estado": "PE", "tipo_ug": TipoUG.PLENA},
        {"sigla": "14º BIMtz", "nome_completo": "14º Batalhão de Infantaria Motorizado", "codigo_uasg": "160218", "cidade": "Jaboatão dos Guararapes", "estado": "PE", "tipo_ug": TipoUG.PATRIMONIAL},
        {"sigla": "10º Esqd C Mec", "nome_completo": "10º Esquadrão de Cavalaria Mecanizado", "codigo_uasg": "160219", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PATRIMONIAL},
        {"sigla": "71º BIMtz", "nome_completo": "71º Batalhão de Infantaria Motorizado", "codigo_uasg": "160220", "cidade": "Garanhuns", "estado": "PE", "tipo_ug": TipoUG.PLENA},
        {"sigla": "10ª Cia E Cmb", "nome_completo": "10ª Companhia de Engenharia de Combate", "codigo_uasg": "160221", "cidade": "São Bento do Una", "estado": "PE", "tipo_ug": TipoUG.PLENA},
        {"sigla": "72º BI Caat", "nome_completo": "72º Batalhão de Infantaria de Caatinga", "codigo_uasg": "160222", "cidade": "Petrolina", "estado": "PE", "tipo_ug": TipoUG.PLENA},
        {"sigla": "Esc Av OP Pipa 7ª RM", "nome_completo": "Escritório Avançado Operação Carro-Pipa 7ª RM", "codigo_uasg": "160223", "cidade": "Petrolina", "estado": "PE", "tipo_ug": TipoUG.PLENA, "opera_carro_pipa": True},
        {"sigla": "7º CGCFEx", "nome_completo": "7º Centro de Gestão, Contabilidade e Finanças do Exército", "codigo_uasg": "160224", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PLENA},
        {"sigla": "Outras UG PE", "nome_completo": "Unidades Gestoras Diversas - PE", "codigo_uasg": "160225", "cidade": "Recife", "estado": "PE", "tipo_ug": TipoUG.PLENA},
        {"sigla": "H Gu JP", "nome_completo": "Hospital de Guarnição de João Pessoa", "codigo_uasg": "160226", "cidade": "João Pessoa", "estado": "PB", "tipo_ug": TipoUG.PLENA},
        {"sigla": "Ba Adm JP", "nome_completo": "Base Administrativa de João Pessoa", "codigo_uasg": "160227", "cidade": "João Pessoa", "estado": "PB", "tipo_ug": TipoUG.PLENA},
        {"sigla": "15º BIMtz", "nome_completo": "15º Batalhão de Infantaria Motorizado", "codigo_uasg": "160228", "cidade": "João Pessoa", "estado": "PB", "tipo_ug": TipoUG.PATRIMONIAL},
        {"sigla": "31º BI Mtz", "nome_completo": "31º Batalhão de Infantaria Motorizado", "codigo_uasg": "160229", "cidade": "Campina Grande", "estado": "PB", "tipo_ug": TipoUG.PLENA},
        {"sigla": "1º Gpt E", "nome_completo": "1º Grupamento de Engenharia", "codigo_uasg": "160230", "cidade": "João Pessoa", "estado": "PB", "tipo_ug": TipoUG.PLENA},
        {"sigla": "Esc R Op C Pipa 1º Gpt E", "nome_completo": "Escritório Regional Operação Carro-Pipa 1º Gpt E", "codigo_uasg": "160231", "cidade": "João Pessoa", "estado": "PB", "tipo_ug": TipoUG.ORCAMENTARIA, "opera_carro_pipa": True},
        {"sigla": "16º RCMec", "nome_completo": "16º Regimento de Cavalaria Mecanizado", "codigo_uasg": "160232", "cidade": "Bayeux", "estado": "PB", "tipo_ug": TipoUG.PATRIMONIAL},
        {"sigla": "Outras UG PB", "nome_completo": "Unidades Gestoras Diversas - PB", "codigo_uasg": "160233", "cidade": "João Pessoa", "estado": "PB", "tipo_ug": TipoUG.PLENA},
        {"sigla": "59º BI Mtz", "nome_completo": "59º Batalhão de Infantaria Motorizado", "codigo_uasg": "160234", "cidade": "Maceió", "estado": "AL", "tipo_ug": TipoUG.PLENA},
        {"sigla": "Outras UG AL", "nome_completo": "Unidades Gestoras Diversas - AL", "codigo_uasg": "160235", "cidade": "Maceió", "estado": "AL", "tipo_ug": TipoUG.PLENA},
    ]

    for uga in ugas_data:
        exists = db.query(Uga).filter_by(sigla=uga["sigla"]).first()
        if not exists:
            db.add(Uga(**uga))


def seed_trechos_diarias(db: Session):
    trechos = [
        {"descricao": "Recife-PE/João Pessoa-PB/Recife-PE", "qtd_diarias": 4.5, "transporte": "Van", "passagem": False},
        {"descricao": "Recife-PE/Petrolina-PE/Recife-PE", "qtd_diarias": 4.5, "transporte": "Aéreo", "passagem": True},
        {"descricao": "Recife-PE/Garanhuns-São Bento Una/Recife-PE", "qtd_diarias": 4.5, "transporte": "Van", "passagem": False},
        {"descricao": "Recife-PE/Maceió-AL/Recife-PE", "qtd_diarias": 3.5, "transporte": "Van", "passagem": False},
        {"descricao": "Recife-PE/Campina Grande-PB/Recife-PE", "qtd_diarias": 3.5, "transporte": "Van", "passagem": False},
    ]
    for trecho in trechos:
        exists = db.query(Trecho).filter_by(descricao=trecho["descricao"]).first()
        if not exists:
            db.add(Trecho(**trecho))

    diarias = [
        {"categoria": CategoriaDiaria.OF_SUP, "capital": 450.0, "interior": 395.0},
        {"categoria": CategoriaDiaria.OF_INT_SUB, "capital": 380.0, "interior": 335.0},
        {"categoria": CategoriaDiaria.CB_SD, "capital": 315.0, "interior": 280.0},
    ]
    for diaria in diarias:
        exists = db.query(DiariaValor).filter_by(categoria=diaria["categoria"]).first()
        if not exists:
            db.add(DiariaValor(**diaria))


def seed_militares(db: Session):
    militares = [
        {
            "nome_guerra": "Maj Almeida",
            "nome_completo": "Marcos Almeida",
            "posto_graduacao": PostoGraduacao.MAJ,
            "categoria_diaria": CategoriaDiaria.OF_INT_SUB,
            "secao": Secao.PRIMEIRA,
            "funcao": "Chefe da 1ª Seção",
            "especialidades": ["Gestão Orçamentária", "Licitações"],
        },
        {
            "nome_guerra": "Cap Souza",
            "nome_completo": "Renata Souza",
            "posto_graduacao": PostoGraduacao.CAP,
            "categoria_diaria": CategoriaDiaria.OF_INT_SUB,
            "secao": Secao.TERCEIRA,
            "funcao": "Orientadora",
            "especialidades": ["Gestão Patrimonial", "Gestão de Custos"],
        },
        {
            "nome_guerra": "Sgt Lima",
            "nome_completo": "Diego Lima",
            "posto_graduacao": PostoGraduacao.SGT,
            "categoria_diaria": CategoriaDiaria.CB_SD,
            "secao": Secao.QUARTA,
            "funcao": "Apoio Logístico",
            "especialidades": ["Pagamento de Pessoal"],
        },
    ]
    for militar in militares:
        exists = db.query(Militar).filter_by(nome_guerra=militar["nome_guerra"]).first()
        if not exists:
            db.add(Militar(**militar))


def seed_pvot_visitas(db: Session):
    pvot = db.query(Pvot).filter_by(ano=2026).first()
    if not pvot:
        pvot = Pvot(ano=2026, status=StatusPVOT.APROVADO, observacoes="PVOT 2026 pré-carregado")
        db.add(pvot)
        db.flush()

    uga_by_sigla = {uga.sigla: uga for uga in db.query(Uga).all()}

    visitas_data = [
        ("Cmdo 7ª RM", date(2026, 3, 12), date(2026, 3, 12), 1, "Regular", None),
        ("Esc R Op C Pipa 7ª RM", date(2026, 3, 12), date(2026, 3, 12), 1, "Regular", None),
        ("Ba Adm Curado", date(2026, 3, 17), date(2026, 3, 17), 1, "Regular", "1ª de 2"),
        ("7º D Sup", date(2026, 3, 19), date(2026, 3, 19), 1, "Regular", None),
        ("14º B Log", date(2026, 4, 1), date(2026, 4, 1), 1, "Regular", None),
        ("CRO/7", date(2026, 4, 9), date(2026, 4, 9), 1, "Regular", None),
        ("H Gu JP", date(2026, 4, 13), date(2026, 4, 13), 1, "Regular", "1ª de 2"),
        ("Ba Adm JP", date(2026, 4, 14), date(2026, 4, 14), 1, "Regular", "1ª de 2"),
        ("15º BIMtz", date(2026, 4, 15), date(2026, 4, 15), 1, "Regular", None),
        ("72º BI Caat", date(2026, 5, 4), date(2026, 5, 7), 3, "Regular", None),
        ("Esc Av OP Pipa 7ª RM", date(2026, 5, 4), date(2026, 5, 7), 3, "Regular", None),
        ("Pq R Mnt/7", date(2026, 5, 13), date(2026, 5, 13), 1, "Regular", None),
        ("CMR", date(2026, 5, 14), date(2026, 5, 14), 1, "Regular", None),
        ("5º CTA", date(2026, 5, 19), date(2026, 5, 19), 1, "Regular", None),
        ("4º B Com", date(2026, 5, 20), date(2026, 5, 20), 1, "Regular", None),
        ("HMAR", date(2026, 5, 21), date(2026, 5, 21), 1, "Regular", "1ª de 2"),
        ("4º BPE", date(2026, 6, 2), date(2026, 6, 2), 1, "Regular", None),
        ("10ª Bda Inf Mtz", date(2026, 6, 3), date(2026, 6, 3), 1, "Regular", None),
        ("31º BI Mtz", date(2026, 6, 16), date(2026, 6, 18), 3, "Regular", None),
        ("7ª Cia Com", date(2026, 6, 23), date(2026, 6, 23), 1, "Regular", None),
        ("7º GAC", date(2026, 6, 30), date(2026, 6, 30), 1, "Regular", None),
        ("CMNE", date(2026, 8, 18), date(2026, 8, 18), 1, "Regular", None),
        ("CPOR/R", date(2026, 8, 20), date(2026, 8, 20), 1, "Regular", None),
        ("3º CGEO", date(2026, 9, 3), date(2026, 9, 3), 1, "Regular", None),
        ("1º Gpt E", date(2026, 9, 15), date(2026, 9, 15), 1, "Regular", None),
        ("Esc R Op C Pipa 1º Gpt E", date(2026, 9, 16), date(2026, 9, 16), 1, "Regular", None),
        ("16º RCMec", date(2026, 9, 17), date(2026, 9, 17), 1, "Regular", None),
        ("Ba Adm Curado", date(2026, 9, 22), date(2026, 9, 22), 1, "Regular", "2ª de 2"),
        ("14º BIMtz", date(2026, 9, 24), date(2026, 9, 24), 1, "Regular", None),
        ("71º BIMtz", date(2026, 10, 5), date(2026, 10, 6), 2, "Regular", None),
        ("10ª Cia E Cmb", date(2026, 10, 7), date(2026, 10, 8), 2, "Regular", None),
        ("10º Esqd C Mec", date(2026, 10, 14), date(2026, 10, 14), 1, "Regular", None),
        ("Ba Adm JP", date(2026, 10, 19), date(2026, 10, 20), 2, "Regular", "2ª de 2"),
        ("H Gu JP", date(2026, 10, 20), date(2026, 10, 21), 2, "Regular", "2ª de 2"),
        ("59º BI Mtz", date(2026, 10, 26), date(2026, 10, 30), 3, "Regular", None),
        ("HMAR", date(2026, 11, 4), date(2026, 11, 4), 1, "Regular", "2ª de 2"),
    ]

    for sigla, data_inicio, data_fim, duracao, tipo, observacao in visitas_data:
        uga = uga_by_sigla.get(sigla)
        if not uga:
            continue
        exists = (
            db.query(Visita)
            .filter_by(pvot_id=pvot.id, uga_id=uga.id, data_inicio=data_inicio)
            .first()
        )
        if not exists:
            db.add(
                Visita(
                    pvot_id=pvot.id,
                    uga_id=uga.id,
                    data_inicio=data_inicio,
                    data_fim=data_fim,
                    duracao_dias=duracao,
                    tipo_visita=TipoVisita.REGULAR,
                    observacao_visita=observacao,
                )
            )


def run_seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_ugas(db)
        seed_trechos_diarias(db)
        seed_militares(db)
        seed_pvot_visitas(db)
        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    run_seed()
