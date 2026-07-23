# SGVOT - Sistema de Gestão do Plano de Visitas de Orientação Técnica

Este repositório contém um MVP funcional do SGVOT (PVOT 2026), com backend em FastAPI e um painel web estático para consulta rápida dos indicadores principais.

## Estrutura

- `backend/`: API FastAPI, modelos SQLAlchemy e script de seed.
- `frontend/`: dashboard estático consumindo a API.

## Como executar localmente

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.seed
uvicorn app.main:app --reload
```

Acesse em `http://localhost:8000`.

## Dados iniciais

O script `python -m app.seed` carrega:

- 40 UGAs (incluindo todas as UGAs listadas no PVOT 2026)
- Trechos e valores de diárias (Decreto 10.987/2024)
- PVOT 2026 com 36 visitas pré-cadastradas
- Militares de exemplo para demonstração

## Siglas de estados

O cadastro de UGA aceita as 27 siglas das unidades federativas brasileiras. O
seletor pode ser preenchido pelo endpoint `GET /ugas/estados`.

## Próximos passos

- Implementar autenticação JWT e perfis de usuário
- Adicionar geração de documentos (OS, relatórios) em PDF/DOCX
- Evoluir o frontend para React e dashboards com gráficos
- Criar módulo de execução com workflow de prazos e alertas
