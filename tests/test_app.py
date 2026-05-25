from src.models import Task

def test_criacao_tarefa():
    tarefa = Task(
        "Estudar Flask",
        "Aprender rotas",
        "Alta"
    )

    assert tarefa.titulo == "Estudar Flask"

def test_concluir_tarefa():
    tarefa = Task(
        "Projeto",
        "Finalizar projeto",
        "Média"
    )

    tarefa.concluir()

    assert tarefa.status == "Concluída"