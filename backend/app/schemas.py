from datetime import date
from typing import List, Optional
from pydantic import BaseModel

from .models import (
    CategoriaDiaria,
    EstadoBrasileiro,
    FuncaoNaVisita,
    PostoGraduacao,
    Secao,
    StatusPVOT,
    StatusVisita,
    TipoUG,
    TipoVisita,
)


class UgaBase(BaseModel):
    sigla: str
    nome_completo: str
    codigo_uasg: str
    cidade: str
    estado: EstadoBrasileiro
    endereco: Optional[str] = None
    tipo_ug: TipoUG
    ug_vinculadora_id: Optional[int] = None
    telefone_ritex: Optional[str] = None
    email_institucional: Optional[str] = None
    comandante_atual: Optional[str] = None
    possui_paiol: bool = False
    opera_carro_pipa: bool = False
    sensivel: bool = False
    ultima_vot_data: Optional[date] = None
    ultima_vot_principais_achados: Optional[str] = None


class UgaRead(UgaBase):
    id: int

    class Config:
        from_attributes = True


class MilitarBase(BaseModel):
    nome_guerra: str
    nome_completo: str
    posto_graduacao: PostoGraduacao
    categoria_diaria: CategoriaDiaria
    secao: Secao
    funcao: Optional[str] = None
    especialidades: List[str]
    ativo: bool = True


class MilitarRead(MilitarBase):
    id: int

    class Config:
        from_attributes = True


class TrechoRead(BaseModel):
    id: int
    descricao: str
    qtd_diarias: float
    transporte: str
    passagem: bool

    class Config:
        from_attributes = True


class DiariaValorRead(BaseModel):
    id: int
    categoria: CategoriaDiaria
    capital: float
    interior: float

    class Config:
        from_attributes = True


class PvotRead(BaseModel):
    id: int
    ano: int
    data_aprovacao: Optional[date]
    enviado_apg_sef: bool
    data_envio_apg_sef: Optional[date]
    observacoes: Optional[str]
    status: StatusPVOT

    class Config:
        from_attributes = True


class VisitaRead(BaseModel):
    id: int
    pvot_id: int
    uga_id: int
    data_inicio: date
    data_fim: date
    duracao_dias: int
    tipo_visita: TipoVisita
    status: StatusVisita
    trecho_id: Optional[int]
    requer_pernoite: bool
    requer_passagem_aerea: bool
    observacao_visita: Optional[str]

    class Config:
        from_attributes = True


class EquipeVisitaRead(BaseModel):
    id: int
    visita_id: int
    militar_id: int
    funcao_na_visita: FuncaoNaVisita
    areas_atuacao: List[str]

    class Config:
        from_attributes = True


class VisitaDashboard(BaseModel):
    id: int
    uga_id: int
    uga_sigla: str
    data_inicio: date
    duracao_dias: int
    status: StatusVisita


class DashboardResumo(BaseModel):
    visitas_planejadas: int
    visitas_concluidas: int
    proximas_visitas: List[VisitaDashboard]
    alertas: List[str]
    distribuicao_estado: dict
    distribuicao_mensal: dict
