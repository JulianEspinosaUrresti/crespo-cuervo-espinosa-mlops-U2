from flask import Flask, request, jsonify, render_template_string
from modelo import evaluar_paciente
from datetime import datetime

app = Flask(__name__)

# Estadísticas globales
estadisticas = {
    "NO ENFERMO": 0,
    "ENFERMEDAD LEVE": 0,
    "ENFERMEDAD AGUDA": 0,
    "ENFERMEDAD CRÓNICA": 0,
    "ENFERMEDAD TERMINAL": 0
}

ultimas_predicciones = []
ultima_fecha = None


@app.route("/")
def inicio():

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Evaluación Médica</title>

        <style>

            body{
                font-family: Arial;
                background-color:#f2f2f2;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
            }

            .contenedor{
                background:white;
                padding:40px;
                border-radius:15px;
                width:400px;
                box-shadow:0px 0px 10px rgba(0,0,0,0.2);
            }

            h1{
                text-align:center;
                color:#1d4f91;
            }

            input{
                width:100%;
                padding:10px;
                margin-top:5px;
                margin-bottom:20px;
                border-radius:5px;
                border:1px solid #ccc;
            }

            button{
                width:100%;
                padding:12px;
                background:#2d7dd2;
                color:white;
                border:none;
                border-radius:5px;
                cursor:pointer;
                font-size:16px;
            }

            .resultado{
                margin-top:25px;
                padding:15px;
                background:#e8f1fb;
                border-radius:8px;
                text-align:center;
                font-size:18px;
                font-weight:bold;
                color:#1d4f91;
            }

            table{
                width:100%;
                margin-top:20px;
                border-collapse:collapse;
            }

            table, th, td{
                border:1px solid #ccc;
            }

            th, td{
                padding:8px;
                text-align:center;
            }

        </style>

    </head>

    <body>

        <div class="contenedor">

            <h1>Evaluación Médica</h1>

            <form method="POST" action="/evaluar">

                <label>Temperatura corporal</label>
                <input type="number" step="0.1" name="temperatura" required>

                <label>Frecuencia cardíaca</label>
                <input type="number" name="frecuencia_cardiaca" required>

                <label>Nivel de oxígeno</label>
                <input type="number" name="oxigeno" required>

                <button type="submit">Evaluar paciente</button>

            </form>

        </div>

    </body>

    </html>
    """

    return render_template_string(html)


@app.route("/evaluar", methods=["POST"])
def evaluar():

    global ultima_fecha

    if request.is_json:

        datos = request.get_json()

        temperatura = float(datos["temperatura"])
        frecuencia_cardiaca = int(datos["frecuencia_cardiaca"])
        oxigeno = int(datos["oxigeno"])

    else:

        temperatura = float(request.form["temperatura"])
        frecuencia_cardiaca = int(request.form["frecuencia_cardiaca"])
        oxigeno = int(request.form["oxigeno"])

    resultado = evaluar_paciente(
        temperatura,
        frecuencia_cardiaca,
        oxigeno
    )

    estadisticas[resultado] += 1

    ultimas_predicciones.append(resultado)

    if len(ultimas_predicciones) > 5:
        ultimas_predicciones.pop(0)

    ultima_fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if request.is_json:

        return jsonify({
            "resultado": resultado
        })

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>

        <title>Resultado</title>

        <style>

            body{{
                font-family:Arial;
                background:#f2f2f2;
                display:flex;
                justify-content:center;
                align-items:center;
                height:100vh;
            }}

            .contenedor{{
                background:white;
                padding:40px;
                border-radius:15px;
                width:500px;
                box-shadow:0px 0px 10px rgba(0,0,0,0.2);
            }}

            h1{{
                text-align:center;
                color:#1d4f91;
            }}

            .resultado{{
                margin-top:20px;
                padding:15px;
                background:#e8f1fb;
                border-radius:8px;
                text-align:center;
                font-size:22px;
                font-weight:bold;
                color:#1d4f91;
            }}

            table{{
                width:100%;
                margin-top:20px;
                border-collapse:collapse;
            }}

            table, th, td{{
                border:1px solid #ccc;
            }}

            th, td{{
                padding:8px;
                text-align:center;
            }}

            .boton{{
                margin-top:20px;
                width:100%;
                padding:12px;
                background:#2d7dd2;
                color:white;
                text-decoration:none;
                border-radius:5px;
                display:block;
                text-align:center;
            }}

        </style>

    </head>

    <body>

        <div class="contenedor">

            <h1>Resultado de la Evaluación</h1>

            <div class="resultado">
                {resultado}
            </div>

            <h3>Estadísticas</h3>

            <table>

                <tr>
                    <th>Categoría</th>
                    <th>Cantidad</th>
                </tr>

                <tr>
                    <td>NO ENFERMO</td>
                    <td>{estadisticas["NO ENFERMO"]}</td>
                </tr>

                <tr>
                    <td>ENFERMEDAD LEVE</td>
                    <td>{estadisticas["ENFERMEDAD LEVE"]}</td>
                </tr>

                <tr>
                    <td>ENFERMEDAD AGUDA</td>
                    <td>{estadisticas["ENFERMEDAD AGUDA"]}</td>
                </tr>

                <tr>
                    <td>ENFERMEDAD CRÓNICA</td>
                    <td>{estadisticas["ENFERMEDAD CRÓNICA"]}</td>
                </tr>

                <tr>
                    <td>ENFERMEDAD TERMINAL</td>
                    <td>{estadisticas["ENFERMEDAD TERMINAL"]}</td>
                </tr>

            </table>

            <h3>Últimas 5 predicciones</h3>

            <ul>
                {"".join([f"<li>{p}</li>" for p in ultimas_predicciones])}
            </ul>

            <p>
                <strong>Última predicción:</strong> {ultima_fecha}
            </p>

            <a class="boton" href="/">
                Nueva evaluación
            </a>

        </div>

    </body>

    </html>
    """

    return html


@app.route("/estadisticas", methods=["GET"])
def obtener_estadisticas():

    return jsonify({
        "estadisticas": estadisticas,
        "ultimas_predicciones": ultimas_predicciones,
        "ultima_fecha": ultima_fecha
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )