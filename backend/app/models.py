from datetime import datetime
from enum import Enum
from sqlalchemy import Boolean, Column, Date, DateTime, Enum as SqlEnum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import relationship

from .db import Base


class TipoUG(str, Enum):
    PLENA = "Plena"
    PATRIMONIAL = "Patrimonial"
    CUSTO = "Custo"
    ORCAMENTARIA = "Orçamentária"


class PostoGraduacao(str, Enum):
    CEL = "Cel"
    TEN_CEL = "Ten Cel"
    MAJ = "Maj"
    CAP = "Cap"
    TEN = "Ten"
    SUB_TEN = "Sub Ten"
    SGT = "Sgt"
    CB = "Cb"
    SD = "Sd"


class CategoriaDiaria(str, Enum):
    OF_SUP = "Of Sup"
    OF_INT_SUB = "Of Int/Sub"
    CB_SD = "Cb/Sd"


class Secao(str, Enum):
    PRIMEIRA = "1ª Seção"
    SEGUNDA = "2ª Seção"
    TERCEIRA = "3ª Seção"
    QUARTA = "4ª Seção"


class StatusPVOT(str, Enum):
    RASCUNHO = "Rascunho"
    EM_APROVACAO = "Em Aprovação"
    APROVADO = "Aprovado"
    EM_EXECUCAO = "Em Execução"
    CONCLUIDO = "Concluído"


class TipoVisita(str, Enum):
    REGULAR = "Regular"
    SEGUNDA_SEMESTRAL = "2ª Visita Semestral"


class StatusVisita(str, Enum):
    PLANEJADA = "Planejada"
    OS_ENVIADA = "OS Enviada"
    EM_PREPARACAO = "Em Preparação"
    EM_EXECUCAO = "Em Execução"
    CONCLUIDA = "Concluída"
    CANCELADA = "Cancelada"


class FuncaoNaVisita(str, Enum):
    CHEFE = "Chefe da Equipe"
    ORIENTADOR = "Orientador"
    APOIO = "Apoio"


class Uga(Base):
    __tablename__ = "ugas"

    id = Column(Integer, primary_key=True, index=True)
    sigla = Column(String, nullable=False)
    nome_completo = Column(String, nullable=False)
    codigo_uasg = Column(String(6), nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String(2), nullable=False)
    endereco = Column(String, nullable=True)
    tipo_ug = Column(SqlEnum(TipoUG), nullable=False)
    ug_vinculadora_id = Column(Integer, ForeignKey("ugas.id"), nullable=True)
    telefone_ritex = Column(String, nullable=True)
    email_institucional = Column(String, nullable=True)
    comandante_atual = Column(String, nullable=True)
    possui_paiol = Column(Boolean, default=False)
    opera_carro_pipa = Column(Boolean, default=False)
    sensivel = Column(Boolean, default=False)
    ultima_vot_data = Column(Date, nullable=True)
    ultima_vot_principais_achados = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    ug_vinculadora = relationship("Uga", remote_side=[id])


class Militar(Base):
    __tablename__ = "militares"

    id = Column(Integer, primary_key=True, index=True)
    nome_guerra = Column(String, nullable=False)
    nome_completo = Column(String, nullable=False)
    posto_graduacao = Column(SqlEnum(PostoGraduacao), nullable=False)
    categoria_diaria = Column(SqlEnum(CategoriaDiaria), nullable=False)
    secao = Column(SqlEnum(Secao), nullable=False)
    funcao = Column(String, nullable=True)
    especialidades = Column(JSON, nullable=False, default=list)
    ativo = Column(Boolean, default=True)


class Trecho(Base):
    __tablename__ = "trechos"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    qtd_diarias = Column(Float, nullable=False)
    transporte = Column(String, nullable=False)
    passagem = Column(Boolean, default=False)


class DiariaValor(Base):
    __tablename__ = "diarias"

    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(SqlEnum(CategoriaDiaria), nullable=False)
    capital = Column(Float, nullable=False)
    interior = Column(Float, nullable=False)


class Pvot(Base):
    __tablename__ = "pvots"

    id = Column(Integer, primary_key=True, index=True)
    ano = Column(Integer, nullable=False)
    data_aprovacao = Column(Date, nullable=True)
    enviado_apg_sef = Column(Boolean, default=False)
    data_envio_apg_sef = Column(Date, nullable=True)
    observacoes = Column(Text, nullable=True)
    status = Column(SqlEnum(StatusPVOT), default=StatusPVOT.RASCUNHO)

    visitas = relationship("Visita", back_populates="pvot")


class Visita(Base):
    __tablename__ = "visitas"

    id = Column(Integer, primary_key=True, index=True)
    pvot_id = Column(Integer, ForeignKey("pvots.id"), nullable=False)
    uga_id = Column(Integer, ForeignKey("ugas.id"), nullable=False)
    data_inicio = Column(Date, nullable=False)
    data_fim = Column(Date, nullable=False)
    duracao_dias = Column(Integer, nullable=False)
    tipo_visita = Column(SqlEnum(TipoVisita), default=TipoVisita.REGULAR)
    status = Column(SqlEnum(StatusVisita), default=StatusVisita.PLANEJADA)
    trecho_id = Column(Integer, ForeignKey("trechos.id"), nullable=True)
    requer_pernoite = Column(Boolean, default=False)
    requer_passagem_aerea = Column(Boolean, default=False)
    observacao_visita = Column(String, nullable=True)

    pvot = relationship("Pvot", back_populates="visitas")
    uga = relationship("Uga")
    trecho = relationship("Trecho")
    equipe = relationship("EquipeVisita", back_populates="visita")


class EquipeVisita(Base):
    __tablename__ = "equipe_visita"

    id = Column(Integer, primary_key=True, index=True)
    visita_id = Column(Integer, ForeignKey("visitas.id"), nullable=False)
    militar_id = Column(Integer, ForeignKey("militares.id"), nullable=False)
    funcao_na_visita = Column(SqlEnum(FuncaoNaVisita), nullable=False)
    areas_atuacao = Column(JSON, nullable=False, default=list)

    visita = relationship("Visita", back_populates="equipe")
    militar = relationship("Militar")
