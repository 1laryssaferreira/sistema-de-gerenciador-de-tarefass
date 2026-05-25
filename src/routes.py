from flask import render_template_string, request, redirect
from models import Task

tarefas = []

HTML = """

<!DOCTYPE html>
<html lang="pt-br">

<head>

    <meta charset="UTF-8">

    <title>Kanban Task Manager</title>

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family: 'Segoe UI', sans-serif;
        }

        body{

            min-height:100vh;

            background:
            linear-gradient(
                135deg,
                #14001f,
                #2d1148,
                #4b1f73,
                #6d28d9
            );

            color:white;

            padding:40px;
        }

        h1{

            text-align:center;

            margin-bottom:35px;

            font-size:48px;

            font-weight:700;

            letter-spacing:2px;

            color:#f5e9ff;

            text-shadow:0 0 20px rgba(255,255,255,0.2);
        }

        .container{

            max-width:1500px;

            margin:auto;
        }

        form{

            background:rgba(255,255,255,0.08);

            backdrop-filter: blur(14px);

            border:1px solid rgba(255,255,255,0.12);

            border-radius:28px;

            padding:25px;

            margin-bottom:40px;

            display:flex;

            gap:15px;

            flex-wrap:wrap;

            box-shadow:0 8px 32px rgba(0,0,0,0.25);
        }

        input{

            flex:1;

            min-width:220px;

            padding:16px;

            border:none;

            outline:none;

            border-radius:18px;

            background:rgba(255,255,255,0.12);

            color:white;

            font-size:15px;
        }

        input::placeholder{

            color:#ddd;
        }

        button{

            padding:16px 24px;

            border:none;

            border-radius:18px;

            background:linear-gradient(
                135deg,
                #c084fc,
                #9333ea
            );

            color:white;

            font-weight:bold;

            cursor:pointer;

            transition:0.3s;

            font-size:15px;
        }

        button:hover{

            transform:translateY(-2px);

            box-shadow:0 0 18px rgba(192,132,252,0.6);
        }

        .kanban{

            display:grid;

            grid-template-columns: repeat(3, 1fr);

            gap:25px;
        }

        .column{

            background:rgba(255,255,255,0.08);

            backdrop-filter: blur(14px);

            border-radius:28px;

            padding:22px;

            min-height:600px;

            border:1px solid rgba(255,255,255,0.12);

            box-shadow:0 8px 32px rgba(0,0,0,0.2);
        }

        .column h2{

            text-align:center;

            margin-bottom:25px;

            font-size:28px;

            color:#f3d9ff;
        }

        .task{

            background:rgba(255,255,255,0.10);

            border:1px solid rgba(255,255,255,0.08);

            border-radius:22px;

            padding:20px;

            margin-bottom:20px;

            transition:0.3s;
        }

        .task:hover{

            transform:translateY(-5px);

            box-shadow:0 0 18px rgba(255,255,255,0.08);
        }

        .titulo{

            font-size:22px;

            font-weight:bold;

            margin-bottom:10px;

            color:#ffffff;
        }

        .descricao{

            color:#e9d5ff;

            margin-bottom:14px;

            line-height:1.4;
        }

        .prioridade{

            display:inline-block;

            margin-bottom:16px;

            background:rgba(255,255,255,0.12);

            padding:8px 14px;

            border-radius:14px;

            color:#f5d0fe;

            font-size:14px;
        }

        .buttons{

            display:flex;

            gap:10px;

            flex-wrap:wrap;
        }

        .btn{

            text-decoration:none;

            padding:11px 14px;

            border-radius:14px;

            color:white;

            font-size:14px;

            transition:0.3s;
        }

        .progress{

            background:linear-gradient(
                135deg,
                #7c3aed,
                #9333ea
            );
        }

        .progress:hover{

            box-shadow:0 0 14px rgba(147,51,234,0.7);
        }

        .done{

            background:linear-gradient(
                135deg,
                #22c55e,
                #16a34a
            );
        }

        .done:hover{

            box-shadow:0 0 14px rgba(34,197,94,0.6);
        }

        .delete{

            background:linear-gradient(
                135deg,
                #f43f5e,
                #e11d48
            );
        }

        .delete:hover{

            box-shadow:0 0 14px rgba(244,63,94,0.6);
        }

        @media(max-width:1100px){

            .kanban{

                grid-template-columns:1fr;
            }
        }

    </style>

</head>

<body>

<div class="container">

    <h1>✨ Kanban Task Manager ✨</h1>

    <form method="POST" action="/add">

        <input
            type="text"
            name="titulo"
            placeholder="Título da tarefa"
            required
        >

        <input
            type="text"
            name="descricao"
            placeholder="Descrição"
            required
        >

        <input
            type="text"
            name="prioridade"
            placeholder="Prioridade"
            required
        >

        <button type="submit">
            Adicionar Tarefa
        </button>

    </form>

    <div class="kanban">

        <!-- TO DO -->

        <div class="column">

            <h2>📌 To Do</h2>

            {% for tarefa in tarefas %}

                {% if tarefa.status == "To Do" %}

                    <div class="task">

                        <div class="titulo">
                            {{ tarefa.titulo }}
                        </div>

                        <div class="descricao">
                            {{ tarefa.descricao }}
                        </div>

                        <div class="prioridade">
                            ✨ {{ tarefa.prioridade }}
                        </div>

                        <div class="buttons">

                            <a
                                class="btn progress"
                                href="/iniciar/{{ loop.index0 }}"
                            >
                                Iniciar
                            </a>

                            <a
                                class="btn delete"
                                href="/delete/{{ loop.index0 }}"
                            >
                                Excluir
                            </a>

                        </div>

                    </div>

                {% endif %}

            {% endfor %}

        </div>

        <!-- IN PROGRESS -->

        <div class="column">

            <h2>🚀 In Progress</h2>

            {% for tarefa in tarefas %}

                {% if tarefa.status == "In Progress" %}

                    <div class="task">

                        <div class="titulo">
                            {{ tarefa.titulo }}
                        </div>

                        <div class="descricao">
                            {{ tarefa.descricao }}
                        </div>

                        <div class="prioridade">
                            ✨ {{ tarefa.prioridade }}
                        </div>

                        <div class="buttons">

                            <a
                                class="btn done"
                                href="/concluir/{{ loop.index0 }}"
                            >
                                Concluir
                            </a>

                            <a
                                class="btn delete"
                                href="/delete/{{ loop.index0 }}"
                            >
                                Excluir
                            </a>

                        </div>

                    </div>

                {% endif %}

            {% endfor %}

        </div>

        <!-- DONE -->

        <div class="column">

            <h2>✅ Done</h2>

            {% for tarefa in tarefas %}

                {% if tarefa.status == "Done" %}

                    <div class="task">

                        <div class="titulo">
                            {{ tarefa.titulo }}
                        </div>

                        <div class="descricao">
                            {{ tarefa.descricao }}
                        </div>

                        <div class="prioridade">
                            ✨ {{ tarefa.prioridade }}
                        </div>

                        <div class="buttons">

                            <a
                                class="btn delete"
                                href="/delete/{{ loop.index0 }}"
                            >
                                Excluir
                            </a>

                        </div>

                    </div>

                {% endif %}

            {% endfor %}

        </div>

    </div>

</div>

</body>
</html>

"""

def configure_routes(app):

    @app.route("/")
    def index():

        return render_template_string(
            HTML,
            tarefas=tarefas
        )

    @app.route("/add", methods=["POST"])
    def add():

        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        prioridade = request.form["prioridade"]

        nova_tarefa = Task(
            titulo,
            descricao,
            prioridade
        )

        tarefas.append(nova_tarefa)

        return redirect("/")

    @app.route("/iniciar/<int:id>")
    def iniciar(id):

        tarefas[id].iniciar()

        return redirect("/")

    @app.route("/concluir/<int:id>")
    def concluir(id):

        tarefas[id].concluir()

        return redirect("/")

    @app.route("/delete/<int:id>")
    def delete(id):

        tarefas.pop(id)

        return redirect("/")