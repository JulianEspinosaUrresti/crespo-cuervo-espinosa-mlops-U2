# CHANGELOG

## Comparación entre la Propuesta Inicial y la Propuesta Reestructurada con MLOps

### Modelo

**Propuesta Inicial**

- Simulación basada en reglas.

**Propuesta Reestructurada**

- Modelos de Machine Learning entrenados.

### Framework API

**Propuesta Inicial**

- Flask.

**Propuesta Reestructurada**

- FastAPI.

### Contenerización

**Propuesta Inicial**

- Docker.

**Propuesta Reestructurada**

- Docker + Kubernetes.

### Datos

**Propuesta Inicial**

- Entrada manual desde formulario.

**Propuesta Reestructurada**

- Pipeline de datos estructurado.

### Validación de Datos

**Propuesta Inicial**

- No implementada.

**Propuesta Reestructurada**

- Great Expectations.

### Procesamiento

**Propuesta Inicial**

- No definido formalmente.

**Propuesta Reestructurada**

- Pandas y Scikit-Learn.

### Entrenamiento

**Propuesta Inicial**

- No existe.

**Propuesta Reestructurada**

- Pipeline automatizado de entrenamiento.

### Evaluación

**Propuesta Inicial**

- No existe.

**Propuesta Reestructurada**

- Accuracy, Precision, Recall, F1-Score y ROC-AUC.

### Versionamiento de Modelos

**Propuesta Inicial**

- No existe.

**Propuesta Reestructurada**

- MLflow.

### Monitoreo

**Propuesta Inicial**

- No existe.

**Propuesta Reestructurada**

- Prometheus y Grafana.

### Automatización

**Propuesta Inicial**

- Procesos manuales.

**Propuesta Reestructurada**

- GitHub Actions para CI/CD.

### Escalabilidad

**Propuesta Inicial**

- Limitada a una única instancia.

**Propuesta Reestructurada**

- Arquitectura escalable basada en Kubernetes.

### Beneficios Obtenidos

- Mayor trazabilidad de experimentos y modelos.
- Automatización del ciclo de vida de Machine Learning.
- Mejor calidad y validación de datos.
- Escalabilidad para ambientes productivos.
- Despliegues reproducibles y consistentes.
- Monitoreo continuo de infraestructura y modelos.
- Gobierno y control de versiones de artefactos de Machine Learning.

## Resumen Ejecutivo

La propuesta inicial cumplía el objetivo de demostrar un servicio básico para clasificación de pacientes mediante reglas de negocio. Sin embargo, carecía de capacidades para gestionar el ciclo de vida completo de un modelo de Machine Learning.

La propuesta reestructurada incorpora principios MLOps mediante automatización, validación de datos, versionamiento de modelos, monitoreo y despliegue escalable, permitiendo una solución preparada para entornos empresariales y productivos.
