# Propuesta de Pipeline de MLOps para Predicción de Enfermedades Comunes y Huérfanas

## 1. Introducción

La solución inicial desarrollada por el equipo consistía en una aplicación web construida con Flask y Docker que simulaba la clasificación de pacientes mediante reglas predefinidas.

Aunque esta aproximación permitió demostrar el funcionamiento básico de un servicio predictivo, no contemplaba las actividades necesarias para gestionar el ciclo de vida completo de un modelo de Machine Learning en producción.

Por esta razón se propone una arquitectura MLOps que permita garantizar trazabilidad, reproducibilidad, monitoreo y mantenimiento continuo de los modelos utilizados para la predicción de enfermedades comunes y huérfanas.

---

## 2. Objetivo General

Diseñar un pipeline de MLOps end-to-end que permita administrar todo el ciclo de vida de modelos de Machine Learning utilizados para apoyar el diagnóstico preliminar de enfermedades.

---

## 3. Arquitectura General

El pipeline estará compuesto por las siguientes etapas:

1. Captura e ingesta de datos.
2. Validación y control de calidad.
3. Procesamiento y transformación de datos.
4. Entrenamiento de modelos.
5. Evaluación de desempeño.
6. Registro y versionamiento.
7. Integración continua.
8. Despliegue continuo.
9. Monitoreo.
10. Reentrenamiento.

---

## 4. Ingesta de Datos

Los datos podrán provenir de diferentes fuentes:

- Historias clínicas electrónicas.
- Resultados de laboratorio.
- Registros hospitalarios.
- Sistemas de información en salud.

### Tecnología Propuesta

- PostgreSQL

### Justificación

Permite almacenar grandes volúmenes de información estructurada y facilita la integración con herramientas analíticas y modelos de Machine Learning.

---

## 5. Validación de Datos

Antes de utilizar los datos para entrenamiento se realizarán controles automáticos de calidad.

### Validaciones

- Valores nulos.
- Registros duplicados.
- Campos obligatorios.
- Valores fuera de rango.
- Inconsistencias clínicas.

### Tecnología Propuesta

- Great Expectations

### Justificación

Permite automatizar verificaciones de calidad y generar evidencia de cumplimiento.

---

## 6. Procesamiento y Transformación

Una vez validados los datos se ejecutarán procesos de preparación.

### Actividades

- Limpieza de datos.
- Normalización.
- Codificación de variables categóricas.
- Balanceo de clases.
- Selección de variables.

### Tecnologías

- Pandas
- Scikit-Learn

---

## 7. Entrenamiento de Modelos

El sistema permitirá entrenar diferentes tipos de modelos dependiendo de la disponibilidad de información.

### Enfermedades Comunes

- Random Forest
- XGBoost

### Enfermedades Huérfanas

- Transfer Learning
- Few-Shot Learning

### Justificación

Estas técnicas permiten trabajar tanto con grandes cantidades de datos como con escenarios donde la información disponible es limitada.

---

## 8. Evaluación del Modelo

Los modelos serán evaluados utilizando múltiples métricas.

### Métricas

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

### Objetivo

Garantizar que los modelos cumplan criterios mínimos de desempeño antes de ser desplegados.

---

## 9. Registro y Versionamiento

Todos los experimentos serán almacenados y versionados.

### Tecnología

- MLflow

### Funcionalidades

- Registro de métricas.
- Comparación de experimentos.
- Gestión de artefactos.
- Versionamiento de modelos.

---

## 10. Integración Continua (CI)

Cada cambio realizado en el repositorio activará procesos automáticos.

### Tecnología

- GitHub Actions

### Actividades

- Validación de código.
- Ejecución de pruebas.
- Construcción de imágenes Docker.

---

## 11. Despliegue Continuo (CD)

Los modelos aprobados serán desplegados automáticamente.

### Tecnologías

- Docker
- FastAPI
- Kubernetes

### Modalidades de Uso

- Ejecución local en el computador del médico.
- Consumo remoto mediante API REST.

---

## 12. Monitoreo

Después del despliegue se realizará monitoreo continuo.

### Tecnologías

- Prometheus
- Grafana

### Indicadores

- Latencia.
- Disponibilidad.
- Consumo de recursos.
- Drift de datos.
- Drift de modelos.

---

## 13. Reentrenamiento

Cuando se detecte degradación en el desempeño del modelo se iniciará un nuevo ciclo de entrenamiento.

### Flujo

1. Recolección de nuevos datos.
2. Validación.
3. Entrenamiento.
4. Evaluación.
5. Registro.
6. Despliegue.

---

## 14. Beneficios Esperados

- Reproducibilidad.
- Trazabilidad.
- Escalabilidad.
- Automatización.
- Gobierno de modelos.
- Mantenimiento continuo.
- Mayor confiabilidad operativa.

---

## 15. Conclusión

La propuesta reestructurada incorpora los principios de MLOps para administrar el ciclo de vida completo de modelos de Machine Learning, permitiendo una solución más robusta, escalable y mantenible que la versión inicial basada únicamente en Flask y Docker.