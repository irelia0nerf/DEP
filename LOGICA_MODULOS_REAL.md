# Lógica Realista – Módulos Principais da FoundLab (Python + FastAPI)

## 1. ScoreLab Core – Orquestração da Análise

```python
from fastapi import APIRouter
from models import AnalysisRequest, AnalysisResult
from services import sherlock, kyc, score_engine, mirror, storage

router = APIRouter()

@router.post("/internal/v1/scorelab/analyze", response_model=AnalysisResult)
async def analyze_wallet(request: AnalysisRequest):
    data_sources = {
        "onchain": await sherlock.analyze_wallet(request.wallet_address),
        "kyc": await kyc.get_identity(request.wallet_address)
    }

    flags = aggregate_flags(data_sources)
    score, tier, confidence = score_engine.calculate(flags)

    result = {
        "wallet": request.wallet_address,
        "flags": flags,
        "score": score,
        "tier": tier,
        "confidence": confidence
    }

    await storage.save_analysis(result)
    await mirror.snapshot_event(result)
    return result
```

---

## 2. Dynamic Flag Council (DFC) – Proposição e Aprovação de Flags

```python
@router.post("/v1/dfc/proposals")
async def propose_flag_change(flag_data: dict, user_id: str):
    proposal = await dfc.register_proposal(flag_data, user_id)
    impact = await dfc.simulate_flag_impact(proposal)
    if impact["score_shift"] > 5:
        proposal["status"] = "APPROVED_FOR_STAGING"
    return proposal
```

---

## 3. Sherlock – Análise On-Chain com Bitquery/Alchemy

```python
import httpx

async def analyze_wallet(wallet_address: str):
    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.bitquery.io", json={
            "query": build_graph_query(wallet_address)
        }, headers={"X-API-KEY": "YOUR_API_KEY"})

    data = response.json()
    flags = detect_patterns(data)
    return flags
```

---

## 4. Sentinela – Escuta de Eventos e Reações Automatizadas

```python
import asyncio
from infra.event_bus import listen_events, publish_event

async def monitor_loop():
    async for event in listen_events("wallet.activity"):
        if is_flag_trigger(event):
            await publish_event("score.reanalyze", {
                "wallet_address": event["wallet"],
                "context": event["context"]
            })
```

---

## 5. Score Engine – Cálculo com Algoritmo P(x)/smil

```python
def calculate(flags: list) -> tuple:
    weights = load_weights()
    score = sum(weights.get(flag, 0) for flag in flags)

    if score >= 80:
        tier = "AAA"
    elif score >= 50:
        tier = "BB"
    else:
        tier = "RISK"

    confidence = 0.95  # Simulação estática
    return score, tier, confidence
```

---

## Conexão MongoDB (Storage)

```python
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.foundlab

async def save_analysis(result):
    await db.analysis.insert_one(result)
```

---

## Conclusão

Esta base é plugável com FastAPI, MongoDB e eventos internos, pronta para expansão com módulos como `SigilMesh`, `AI Risk Signals` e `Audit Trail`.