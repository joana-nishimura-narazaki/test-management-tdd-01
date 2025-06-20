````markdown
# Test Management & TDD em Python

Este repositório reúne o projeto de gerenciamento de testes e TDD em Python, desenvolvido durante o MBA em Software Engineering na USP/ESALQ sob orientação do Prof. Helder Prado Santos.

---

## 📄 Descrição

Implementei casos de uso e entidades de domínio em Python, cobrindo:

- Criação e busca de usuários (`CreateUser`, `FindUser`)  
- Entidades `User` e `Task` com validações e regras de negócio  
- Repositório em memória para persistência durante testes  

Em paralelo, desenvolvi **nove testes unitários** que garantem:

- Inicialização e validação de atributos em `Task` e `User`  
- Funcionalidade de marcar tarefas como concluídas  
- Coleta e contagem de tarefas pendentes  
- Criação e busca de usuário via casos de uso  
- Integração e E2E com FastAPI (endpoints `/users/`)  

---

## ⚙️ Instalação

```bash
git clone https://github.com/joana-nishimura-narazaki/test-management-tdd-01.git
cd test-management-tdd-01
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
````

---

## 🚀 Como Executar

1. Iniciar a API FastAPI:

   ```bash
   uvicorn infra.api.main:app --reload
   ```
2. Testes unitários e de integração:

   ```bash
   pytest --cov=referencia
   ```


---

## 🔎 Cobertura de Testes

* **Unitários**: entidades (`Task`, `User`), casos de uso
* **Integração**: métodos de domínio e repositório
* **E2E**: endpoints FastAPI de criação/busca de usuários

Relatório completo gerado pelo `coverage.py`.

---

## 📖 Referências

* Prof. Helder Prado Santos – MBA Software Engineering, USP/ESALQ
* FastAPI, pytest, coverage.py
