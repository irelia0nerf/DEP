# AGENT.md — FoundLab DEP (Nova Versão)

## 🎯 Missão do Agente

- Automatizar a geração e manutenção do backend Python da FoundLab.
- Priorizar módulos **completos**, **testes consistentes** e **exemplos reais** de uso.
- Manter aderência **estrita à arquitetura padrão** `/app`, `/tests`, sem estruturas paralelas.

## 📌 Objetivos Principais

1. Interpretar `README.md` e arquivos do repositório para expandir as APIs REST existentes.
2. Implementar **lógicas de negócio reais**, como:
   - Score financeiro reativo
   - Flags reputacionais e DFC
   - NFT de reputação (SigilMesh)
3. Garantir que **toda nova função tenha testes unitários correspondentes.**
4. Documentar via **docstrings padrão Python** e **exemplos de payload**.
5. Validar comandos:
   ```bash
   flake8
   pytest
   coverage run -m pytest && coverage report
   ```
   antes de finalizar qualquer entrega.

## 🔧 Regras de Execução

- ❌ Nunca entregar código stub ou funções sem lógica real.
- ✅ Toda integração de serviço deve ser **assíncrona** (`async/await`).
- ✅ Separar rigidamente:
  - `routers/` → endpoints REST
  - `services/` → lógica de negócio
- ✅ Armazenar dados usando **MongoDB >= 4.4** via **Motor (async driver)**.

## 🧱 Estrutura Esperada

```
/main.py
/app/
  routers/     # Endpoints REST
  services/    # Regras de negócio
  models/      # Schemas Pydantic
  utils/       # Funções auxiliares e helpers
/tests/
  test_score.py
  test_flags.py
  test_nft.py
  ...
```

## ✅ Padrões de Qualidade

- Código limpo, modular e documentado.
- Testes unitários e de integração com coverage > 90%.
- Zero dependências não listadas no `requirements.txt`.
- Scripts prontos para `venv`, `run`, `test`, `lint` e `build`.

## 💡 Exemplo Esperado de Payload e Lógica

```json
POST /internal/v1/scorelab/analyze

{
  "wallet": "0xabc123...",
  "history": ["tx1", "tx2", ...],
  "metadata": {
    "kyc_level": 2,
    "known_labels": ["mixer", "binance"],
    "last_activity": "2025-06-01"
  }
}
```

**Output esperado:**

```json
{
  "score": 692,
  "tier": "B",
  "flags": ["mixer_detected", "low_volume"],
  "nft_status": "pending",
  "recommendation": "REVIEW"
}
```
