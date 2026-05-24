# Pipeline de MLOps para Predicción de Enfermedades Comunes y Huérfanas

## Integrantes

- Julián Espinosa
- David Crespo
- Jhon Jairo Cuervo

## Descripción del Proyecto

Este repositorio contiene la evolución de un servicio médico desarrollado inicialmente con Python, Flask y Docker hacia una propuesta reestructurada de pipeline MLOps.

La solución inicial permite ingresar variables clínicas básicas de un paciente y retornar una clasificación automática del estado del paciente. La propuesta reestructurada amplía esta solución hacia una arquitectura MLOps capaz de gestionar el ciclo de vida completo de modelos de Machine Learning para la predicción de enfermedades comunes y huérfanas.

## Contexto del Problema

En medicina existe una gran cantidad de información clínica disponible para enfermedades comunes. Sin embargo, para enfermedades huérfanas la cantidad de datos es limitada, lo que dificulta la construcción de modelos predictivos confiables.

Por esta razón, se propone un pipeline que permita desarrollar, desplegar, monitorear y mantener modelos de Machine Learning capaces de apoyar la predicción preliminar de enfermedades a partir de síntomas y variables clínicas.

## Objetivo General

Diseñar un pipeline de MLOps end-to-end para soportar el ciclo de vida completo de modelos de Machine Learning orientados a la predicción de enfermedades comunes y huérfanas.

## Objetivos Específicos

- Garantizar la calidad de los datos antes del entrenamiento.
- Implementar mecanismos de versionamiento de datos y modelos.
- Automatizar procesos de entrenamiento, validación y despliegue.
- Monitorear el comportamiento de los modelos en producción.
- Permitir el reentrenamiento cuando se detecte degradación del desempeño.

## Solución Inicial

La primera versión del proyecto implementa un servicio médico simple que simula un modelo de predicción de enfermedades utilizando reglas de negocio.

### Tecnologías de la Solución Inicial

- Python
- Flask
- Docker
- GitHub Actions
- Pytest

### Variables Utilizadas

| Variable | Descripción |
|---|---|
| temperatura | Temperatura corporal del paciente |
| frecuencia_cardiaca | Pulsaciones por minuto |
| oxigeno | Saturación de oxígeno |

### Estados Posibles del Modelo

- NO ENFERMO
- ENFERMEDAD LEVE
- ENFERMEDAD AGUDA
- ENFERMEDAD CRÓNICA
- ENFERMEDAD TERMINAL

## Propuesta MLOps Reestructurada

El pipeline propuesto contempla las siguientes etapas:

1. Ingesta de datos.
2. Validación de datos.
3. Procesamiento y Feature Engineering.
4. Entrenamiento.
5. Evaluación.
6. Registro y versionamiento de modelos.
7. Integración continua.
8. Despliegue continuo.
9. Monitoreo.
10. Reentrenamiento.

## Tecnologías Propuestas

| Componente | Tecnología |
|---|---|
| Control de versiones | Git + GitHub |
| API | FastAPI |
| Contenedores | Docker |
| Orquestación | Kubernetes |
| Tracking de experimentos | MLflow |
| Base de datos | PostgreSQL |
| Validación de datos | Great Expectations |
| Monitoreo | Prometheus |
| Visualización | Grafana |
| Automatización CI/CD | GitHub Actions |
| Procesamiento de datos | Pandas |
| Machine Learning | Scikit-Learn |

## Estructura del Repositorio

```text
crespo-cuervo-espinosa-mlops-U2/
│
├── app.py
├── modelo.py
├── requirements.txt
├── Dockerfile
├── README.md
├── CHANGELOG.md
├── estadisticas.json
│
├── docs/
│   ├── diagrama_pipeline.md
│   ├── propuesta_pipeline_mlops.md
│   └── supuestos_y_decisiones.md
│
├── tests/
│   └── test_modelo.py
│
└── .github/
    └── workflows/
        └── ci.yml
```

## Funcionalidades de la Solución Actual

- Formulario web para ingresar datos del paciente.
- Endpoint API para realizar predicciones.
- Registro de estadísticas por categoría.
- Consulta de últimas predicciones.
- Pruebas unitarias con pytest.
- Construcción de imagen Docker.
- Pipeline CI/CD con GitHub Actions.
- Documentación de propuesta MLOps.

## Ejecución Local sin Docker

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

## Construcción de la Imagen Docker

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

## Uso del Endpoint de Predicción

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

## Endpoint de Estadísticas

Endpoint:

```text
GET /estadisticas
```

Permite consultar:

- Número total de predicciones por categoría.
- Últimas predicciones realizadas.
- Fecha de la última predicción.

Ejemplo:

```text
http://127.0.0.1:5000/estadisticas
```

## Pruebas Unitarias

Ejecutar:

```bash
python -m pytest
```

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

## Documentación Complementaria

- Propuesta detallada: `docs/propuesta_pipeline_mlops.md`
- Supuestos y decisiones: `docs/supuestos_y_decisiones.md`
- Diagrama del pipeline: `docs/diagrama_pipeline.md`
- Registro de cambios: `CHANGELOG.md`

## Ramas Utilizadas

- `main`: rama principal.
- `solucion-inicial`: primera versión funcional del servicio médico.
- `segunda-version`: incorporación de nueva categoría y estadísticas.
- `añadir-github-actions`: configuración del pipeline CI/CD.
- `solucion-reestructurada-mlops`: propuesta de reestructuración MLOps.

## Conclusión

La solución inicial permitió implementar un servicio médico básico con Flask y Docker. La propuesta reestructurada incorpora principios de MLOps para gestionar el ciclo de vida completo de modelos de Machine Learning, incluyendo validación de datos, versionamiento, CI/CD, despliegue, monitoreo y reentrenamiento.