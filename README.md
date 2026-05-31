# Pipeline de MLOps para Predicción de Enfermedades Comunes y Huérfanas

## Integrantes

- Julián Espinosa
- David Crespo
- Jhon Jairo Cuervo

## Descripción del problema

En el campo de la medicina existe una gran cantidad de información clínica disponible para enfermedades comunes. Sin embargo, para enfermedades huérfanas la cantidad de datos es limitada, lo que dificulta la construcción de modelos predictivos confiables.

El objetivo de esta propuesta es diseñar un pipeline de MLOps que permita desarrollar, desplegar, monitorear y mantener modelos de Machine Learning capaces de predecir la posible presencia de enfermedades a partir de los síntomas reportados por un paciente.

La solución debe permitir su ejecución tanto en entornos locales como en entornos remotos mediante servicios en la nube.

---

# Objetivos

## Objetivo General

Diseñar un pipeline de MLOps end-to-end para soportar el ciclo de vida completo de modelos de Machine Learning orientados a la predicción de enfermedades comunes y huérfanas.

## Objetivos Específicos

- Garantizar la calidad de los datos antes del entrenamiento.
- Implementar mecanismos de versionamiento de datos y modelos.
- Automatizar el proceso de entrenamiento y despliegue.
- Monitorear el comportamiento de los modelos en producción.
- Permitir el reentrenamiento continuo cuando se detecte degradación.

---

# Arquitectura General

El pipeline propuesto contempla las siguientes etapas:

1. Ingesta de datos.
2. Validación de datos.
3. Procesamiento y Feature Engineering.
4. Entrenamiento.
5. Evaluación.
6. Registro de modelos.
7. Integración continua (CI).
8. Despliegue continuo (CD).
9. Monitoreo.
10. Reentrenamiento.

---

# Tecnologías Propuestas

| Componente | Tecnología |
|------------|------------|
| Control de versiones | Git + GitHub |
| API | FastAPI |
| Contenedores | Docker |
| Orquestación | Kubernetes |
| Tracking de experimentos | MLflow |
| Base de datos | PostgreSQL |
| Monitoreo | Prometheus |
| Visualización | Grafana |
| Automatización CI/CD | GitHub Actions |
| Procesamiento de datos | Pandas |
| Machine Learning | Scikit-Learn |

---

# Estructura del Repositorio

```text
docs/
├── diagrama_pipeline.md
├── propuesta_pipeline_mlops.md
└── supuestos_y_decisiones.md

CHANGELOG.md
README.md
```

---

# Documentación Complementaria

- Propuesta detallada: docs/propuesta_pipeline_mlops.md
- Supuestos y decisiones: docs/supuestos_y_decisiones.md
- Diagrama del pipeline: docs/diagrama_pipeline.md
- Registro de cambios: CHANGELOG.md