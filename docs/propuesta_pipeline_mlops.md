\# Propuesta de Pipeline de MLOps



\## 1. Contexto



La solución inicial desarrollada por el equipo consistía en un servicio web implementado en Flask y Docker que simulaba un modelo de predicción médica basado en reglas.



Aunque esta aproximación permitía demostrar el funcionamiento general de un servicio predictivo, no contemplaba los procesos necesarios para administrar el ciclo de vida completo de un modelo de Machine Learning en ambientes productivos.



Por esta razón se propone una arquitectura MLOps que permita gestionar de forma integral los datos, modelos, despliegues y monitoreo.



\---



\# 2. Objetivo



Diseñar un pipeline de MLOps capaz de soportar el ciclo de vida completo de modelos destinados a la predicción de enfermedades comunes y enfermedades huérfanas.



\---



\# 3. Arquitectura General



El pipeline estará compuesto por las siguientes etapas:



1\. Ingesta de datos.

2\. Validación de datos.

3\. Procesamiento y transformación.

4\. Entrenamiento.

5\. Evaluación.

6\. Registro de modelos.

7\. Integración continua.

8\. Despliegue continuo.

9\. Monitoreo.

10\. Reentrenamiento.



\---



\# 4. Ingesta de Datos



Los datos podrán provenir de:



\- Historias clínicas.

\- Laboratorios.

\- Registros hospitalarios.

\- Sistemas externos de salud.



Tecnología propuesta:



\- PostgreSQL.



Justificación:



Permite almacenar información estructurada y facilita la integración con herramientas de Machine Learning.



\---



\# 5. Validación de Datos



Antes del entrenamiento se validarán:



\- Campos vacíos.

\- Valores fuera de rango.

\- Datos duplicados.

\- Inconsistencias clínicas.



Tecnología propuesta:



\- Great Expectations.



Justificación:



Permite automatizar controles de calidad de datos.



\---



\# 6. Procesamiento de Datos



Actividades:



\- Limpieza.

\- Normalización.

\- Codificación de variables.

\- Balanceo de clases.



Tecnologías:



\- Pandas.

\- Scikit-Learn.



\---



\# 7. Entrenamiento



Para enfermedades comunes:



\- Random Forest.

\- XGBoost.



Para enfermedades huérfanas:



\- Transfer Learning.

\- Few-Shot Learning.



Justificación:



Permiten trabajar tanto con grandes cantidades de información como con escenarios donde los datos son escasos.



\---



\# 8. Evaluación



Métricas consideradas:



\- Accuracy.

\- Precision.

\- Recall.

\- F1 Score.

\- ROC AUC.



\---



\# 9. Registro de Modelos



Tecnología:



\- MLflow.



Funcionalidades:



\- Versionamiento.

\- Comparación de experimentos.

\- Registro de métricas.

\- Gestión de artefactos.



\---



\# 10. Integración Continua



Tecnología:



\- GitHub Actions.



Actividades:



\- Validación automática.

\- Pruebas unitarias.

\- Construcción de contenedores.



\---



\# 11. Despliegue Continuo



Tecnologías:



\- Docker.

\- Kubernetes.

\- FastAPI.



El médico podrá acceder al sistema mediante:



\- Ejecución local.

\- Consumo remoto mediante API.



\---



\# 12. Monitoreo



Tecnologías:



\- Prometheus.

\- Grafana.



Variables monitoreadas:



\- Latencia.

\- Errores.

\- Disponibilidad.

\- Drift de datos.



\---



\# 13. Reentrenamiento



Cuando se detecte degradación del modelo:



1\. Recolección de nuevos datos.

2\. Nuevo entrenamiento.

3\. Evaluación.

4\. Registro.

5\. Despliegue.



\---



\# 14. Beneficios



\- Escalabilidad.

\- Reproducibilidad.

\- Trazabilidad.

\- Automatización.

\- Gobierno del modelo.

\- Mantenimiento continuo.

