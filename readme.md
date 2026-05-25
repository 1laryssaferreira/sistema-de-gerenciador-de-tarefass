# Sistema Web de Gerenciamento de Tarefas

## Sobre o Projeto

Projeto desenvolvido para a disciplina de Engenharia de Software.

O sistema permite o gerenciamento de tarefas utilizando metodologias ágeis e organização por prioridades.

---

## Funcionalidades

- Cadastro de tarefas
- Listagem de tarefas
- Exclusão de tarefas
- Atualização de status
- Priorização de tarefas

---

## Tecnologias Utilizadas

- Python
- Flask
- Pytest
- GitHub Actions

---

## Metodologia Ágil

Foi utilizada a metodologia Kanban para organização das atividades.

O quadro foi dividido em:

- To Do
- In Progress
- Done

---

## Mudança de Escopo

Inicialmente o sistema possuía apenas cadastro simples de tarefas.

Durante o desenvolvimento foi adicionada a funcionalidade de prioridade das tarefas para melhorar a organização do fluxo de trabalho.

---

## Como Executar

### Instalar dependências

pip install -r requirements.txt

### Executar o sistema

python src/app.py

---

## Estrutura do Projeto

task-manager/
│
├── src/
├── tests/
├── docs/
├── .github/
├── README.md
├── requirements.txt
└── .gitignore

---

## Testes Automatizados

Os testes automatizados foram implementados utilizando Pytest.

A integração contínua foi configurada utilizando GitHub Actions.