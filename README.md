# Servicio Médico con Docker y GitHub Actions

## Descripción del proyecto

Este proyecto implementa un servicio médico simple que simula un modelo de predicción de enfermedades utilizando Python, Flask, Docker y GitHub Actions.

La aplicación permite ingresar variables clínicas básicas de un paciente y retorna una clasificación del estado del paciente.

## Estados posibles del modelo

El sistema puede retornar una de las siguientes categorías:

- NO ENFERMO
- ENFERMEDAD LEVE
- ENFERMEDAD AGUDA
- ENFERMEDAD CRÓNICA
- ENFERMEDAD TERMINAL

## Variables utilizadas

| Variable | Descripción |
|---|---|
| temperatura | Temperatura corporal del paciente |
| frecuencia_cardiaca | Pulsaciones por minuto |
| oxigeno | Saturación de oxígeno |

## Funcionalidades

- Formulario web para ingresar datos del paciente.
- Endpoint API para realizar predicciones.
- Registro de estadísticas por categoría.
- Consulta de últimas 5 predicciones.
- Registro de fecha de última predicción.
- Pruebas unitarias con pytest.
- Construcción de imagen Docker.
- Pipeline CI/CD con GitHub Actions.

## Estructura del repositorio

```text
crespo-cuervo-espinosa-mlops-U2/
│
├── app.py
├── modelo.py
├── requirements.txt
├── Dockerfile
├── README.md
├── estadisticas.json
├── tests/
│   └── test_modelo.py
└── .github/
    └── workflows/
        └── ci.yml
```

## Ejecución local sin Docker

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
python app.py
```

Abrir en el navegador:

```text
http://127.0.0.1:5000
```

## Construcción de la imagen Docker

```bash
docker build -t modelo-medico .
```

## Ejecución con Docker

```bash
docker run -p 5000:5000 modelo-medico
```

Abrir en el navegador:

```text
http://127.0.0.1:5000
```

## Uso del endpoint de predicción

Endpoint:

```text
POST /evaluar
```

Ejemplo en PowerShell:

```powershell
Invoke-RestMethod `
-Uri "http://127.0.0.1:5000/evaluar" `
-Method POST `
-ContentType "application/json" `
-Body '{"temperatura":39,"frecuencia_cardiaca":130,"oxigeno":80}'
```

Respuesta esperada:

```json
{
  "resultado": "ENFERMEDAD TERMINAL"
}
```

## Endpoint de estadísticas

Endpoint:

```text
GET /estadisticas
```

Permite consultar:

- Número total de predicciones por categoría.
- Últimas 5 predicciones realizadas.
- Fecha de la última predicción.

Ejemplo:

```text
http://127.0.0.1:5000/estadisticas
```

## Pruebas unitarias

Ejecutar:

```bash
python -m pytest
```

El proyecto incluye pruebas para validar que el modelo retorne categorías esperadas.

## CI/CD con GitHub Actions

El repositorio incluye un workflow de GitHub Actions ubicado en:

```text
.github/workflows/ci.yml
```

El pipeline se ejecuta automáticamente en:

- Pull Requests hacia `main`.
- Pushes hacia `main`.

El pipeline realiza:

1. Clonación del repositorio.
2. Configuración de Python.
3. Instalación de dependencias.
4. Ejecución de pruebas unitarias.
5. Construcción de la imagen Docker.

## Ramas utilizadas

- `main`: rama principal.
- `solucion-inicial`: primera versión funcional del servicio.
- `segunda-version`: incorporación de nueva categoría y estadísticas.
- `añadir-github-actions`: configuración del pipeline CI/CD.

## Conclusión

La solución cumple con los requerimientos de la Entrega 2, al incluir control de versiones en GitHub, evolución del modelo, estadísticas de predicción, pruebas unitarias y automatización mediante GitHub Actions.