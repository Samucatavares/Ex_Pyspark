from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os
from fastapi.templating import Jinja2Templates
from connection import get_db_connection, close_db_connection, close_cursor,fetch_data
import lib

app = FastAPI()
app.mount("/static", StaticFiles(directory=os.path.join(os.getcwd(), "static")), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index():
    return RedirectResponse(url="/static/index.html")

@app.get("/cadastrar_cliente")
async def cadastrar_cliente():
    with open("static/cadastrar_cliente.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/contrato")
async def contrato():
    with open("static/contrato.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/transacao")
async def transacao():
    with open("static/transacao.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/salvar_cliente")
async def salvar_cliente(request: Request):
    form_data = await request.form()
    nome = form_data["nome"]

    connection = get_db_connection()
    cursor = connection.cursor()

    insert_query = "INSERT INTO clientes (nome) VALUES (%s)"
    cursor.execute(insert_query, (nome,))

    connection.commit()

    cursor.close()
    connection.close()

    return {"nome": nome}

@app.post("/salvar_contrato")
async def salvar_contrato(request: Request):
    form_data = await request.form()
    ativo = form_data["ativo"]
    percentual = form_data["percentual"]
    cliente_id = form_data["cliente_id"]

    connection = get_db_connection()
    cursor = connection.cursor()

    insert_query = "INSERT INTO contratos (ativo, percentual, cliente_id) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (ativo, percentual, cliente_id))

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "ativo": ativo,
        "percentual": percentual,
        "cliente_id": cliente_id
    }

@app.post("/salvar_transacao")
async def salvar_transacao(request: Request):
    form_data = await request.form()
    contrato_id = form_data["contrato_id"]
    valor_total = form_data["valor_total"]
    percentual_desconto = form_data["percentual_desconto"]

    connection = get_db_connection()
    cursor = connection.cursor()

    insert_query = "INSERT INTO transacoes (contrato_id, valor_total, percentual_desconto) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (contrato_id, valor_total, percentual_desconto))

    connection.commit()

    cursor.close()
    connection.close()

    return {
        "contrato_id": contrato_id,
        "valor_total": valor_total,
        "percentual_desconto": percentual_desconto
    }

@app.get("/lucro_por_cliente")
async def listar_transacoes(request: Request):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """select
                    t1.nome, 
                    format(sum(((t3.valor_total - (t3.valor_total * coalesce((percentual_desconto/100),0)))/100)* t2.percentual),2) as total_lucro
                from cliente t1
                join contrato t2 on t1.cliente_id=t2.cliente_id
                join transacao t3 on t2.contrato_id=t3.contrato_id
                where t2.ativo=1
                group by nome"""
    cursor.execute(query)
    result = cursor.fetchall()

    transacoes = []
    for row in result:
        transacao = {
            "nome": row[0],
            "total_lucro": row[1]
        }
        transacoes.append(transacao)
    print(transacoes)
    close_cursor(cursor)
    close_db_connection(connection)

    return templates.TemplateResponse("lucro_por_cliente.html", {"request": request, "transacoes": transacoes})

@app.get("/ex_4")
async def ex_4():
    with open("static/ex_4.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)
