# AGENT.md — FoundLab DEP

## ⚡️ Missão do Agente

Automatizar a geração, expansão e manutenção do backend Python da FoundLab, criando módulos funcionais, endpoints RESTful, lógica de risco e reputação digital.  
O agente é responsável por **preencher lacunas** do repositório, garantir arquitetura escalável e priorizar entregas plugáveis — **sem nunca cair em stub ou código genérico**.

---

## 🎯 Objetivos do Agent

- **Interpretar o README.md, prompts e specs técnicas**
- Criar módulos Python funcionais, não apenas esqueletos
- Implementar lógica de negócio real: score, flags, análise, monitoramento, NFT reputacional
- Garantir modularidade (routers, services, models, utils)
- Gerar exemplos reais de input/output em todos endpoints
- Cobrir mínimo de testes unitários para funções críticas

---

## 🧩 Padrão de Estrutura

```
/main.py
/app
    /routers    # Endpoints REST (score, flags, sigil, sherlock, sentinela)
    /services   # Lógica de negócio de cada módulo (engine, sherlock, sentinela, sigilmesh)
    /models     # Schemas Pydantic (WalletData, Flags, NFT etc)
    /utils      # Funções auxiliares (ex: mocks, helpers)
```

---

## 🚦 Regras de Execução

1. **Nunca entregue apenas stubs.**  
   Todo endpoint deve retornar dados processados (score real, flags computadas, metadata dinâmica).

2. **Documentação integrada.**  
   Inclua docstrings e exemplos de payloads em cada endpoint e função principal.

3. **Payloads reais.**  
   Implemente exemplos que simulem uso real do sistema, não só casos triviais.

4. **Lógica plugável.**  
   Sempre isole lógica de negócio em `/services/`, nunca no endpoint.

5. **Testabilidade.**  
   Adicione `tests/` com pytest, validando o ScoreLab e Engine.

---

## 🔥 Exemplo de Execução

1. Ao receber um prompt com specs, o agente:
    - Lê o que falta no repo.
    - Gera novos arquivos/funções conforme arquitetura padrão.
    - Preenche cada função com lógica de negócio baseada nos exemplos (score, flags, NFT).
    - Adiciona exemplos práticos nas docstrings.
    - Cria ou atualiza testes unitários.
    - Garante que a API sobe com `uvicorn main:app --reload` e retorna JSON conforme a especificação.

2. Caso algo não esteja especificado:
    - Preenche com lógica simulada baseada em melhores práticas de sistemas de reputação, risco e identidade digital.
    - Nunca retorna um stub vazio.  
    - Prefere entregar um módulo executável e auditável.

---

## 🛡️ Padrões de Qualidade

- **Código limpo e modular**
- **Documentação mínima obrigatória**
- **Sem repetições, sem redundância**
- **Respeito às dependências do requirements.txt**
- **Orientação por testes**

---

## 📣 Comportamento Esperado

> "Agente, ao receber novas specs, sua prioridade é transformar requisitos em código funcional imediatamente, priorizando lógica real, outputs de valor e entrega contínua."

---

**Fim do AGENT.md**
