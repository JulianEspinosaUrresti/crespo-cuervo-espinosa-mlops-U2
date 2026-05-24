from flask import Flask, request, jsonify
from modelo import evaluar_paciente

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = None

    if request.method == "POST":
        temperatura = float(request.form["temperatura"])
        frecuencia_cardiaca = float(request.form["frecuencia_cardiaca"])
        oxigeno = float(request.form["oxigeno"])

        resultado = evaluar_paciente(
            temperatura,
            frecuencia_cardiaca,
            oxigeno
        )

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Evaluación Médica</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                margin: 0;
                padding: 0;
            }}

            .container {{
                width: 420px;
                margin: 80px auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            }}

            h1 {{
                text-align: center;
                color: #1f4e79;
            }}

            label {{
                font-weight: bold;
                display: block;
                margin-top: 15px;
            }}

            input {{
                width: 100%;
                padding: 10px;
                margin-top: 5px;
                border: 1px solid #ccc;
                border-radius: 6px;
            }}

            button {{
                width: 100%;
                margin-top: 25px;
                padding: 12px;
                background-color: #1f77d0;
                color: white;
                border: none;
                border-radius: 6px;
                font-size: 16px;
                cursor: pointer;
            }}

            button:hover {{
                background-color: #155a9c;
            }}

            .resultado {{
                margin-top: 25px;
                padding: 15px;
                text-align: center;
                font-size: 18px;
                font-weight: bold;
                border-radius: 8px;
                background-color: #e8f4ff;
                color: #1f4e79;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Evaluación Médica</h1>

            <form method="POST">
                <label>Temperatura corporal</label>
                <input type="number" step="0.1" name="temperatura" required>

                <label>Frecuencia cardíaca</label>
                <input type="number" step="1" name="frecuencia_cardiaca" required>

                <label>Nivel de oxígeno</label>
                <input type="number" step="1" name="oxigeno" required>

                <button type="submit">Evaluar paciente</button>
            </form>

            {f'<div class="resultado">Resultado: {resultado}</div>' if resultado else ''}
        </div>
    </body>
    </html>
    """


@app.route("/evaluar", methods=["POST"])
def evaluar():
    data = request.get_json()

    temperatura = data.get("temperatura")
    frecuencia_cardiaca = data.get("frecuencia_cardiaca")
    oxigeno = data.get("oxigeno")

    if temperatura is None or frecuencia_cardiaca is None or oxigeno is None:
        return jsonify({
            "error": "Debe enviar temperatura, frecuencia_cardiaca y oxigeno"
        }), 400

    resultado = evaluar_paciente(
        temperatura,
        frecuencia_cardiaca,
        oxigeno
    )

    return jsonify({
        "resultado": resultado
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)