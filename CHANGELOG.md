\# CHANGELOG



\## Comparación entre la Propuesta Inicial y la Propuesta Reestructurada con MLOps



\### Modelo



\*\*Propuesta Inicial\*\*

\- Simulación basada en reglas.



\*\*Propuesta Reestructurada\*\*

\- Modelos de Machine Learning entrenados.



\---



\### Framework API



\*\*Propuesta Inicial\*\*

\- Flask.



\*\*Propuesta Reestructurada\*\*

\- FastAPI.



\---



\### Contenerización



\*\*Propuesta Inicial\*\*

\- Docker.



\*\*Propuesta Reestructurada\*\*

\- Docker + Kubernetes.



\---



\### Gestión de Datos



\*\*Propuesta Inicial\*\*

\- Entrada manual desde formulario.



\*\*Propuesta Reestructurada\*\*

\- Pipeline de datos estructurado.



\---



\### Validación de Datos



\*\*Propuesta Inicial\*\*

\- No implementada.



\*\*Propuesta Reestructurada\*\*

\- Great Expectations.



\---



\### Procesamiento



\*\*Propuesta Inicial\*\*

\- No definido formalmente.



\*\*Propuesta Reestructurada\*\*

\- Pandas y Scikit-Learn.



\---



\### Entrenamiento



\*\*Propuesta Inicial\*\*

\- No existe.



\*\*Propuesta Reestructurada\*\*

\- Pipeline automatizado.



\---



\### Evaluación



\*\*Propuesta Inicial\*\*

\- No existe.



\*\*Propuesta Reestructurada\*\*

\- Accuracy, Precision, Recall, F1 Score y ROC-AUC.



\---



\### Versionamiento de Modelos



\*\*Propuesta Inicial\*\*

\- No existe.



\*\*Propuesta Reestructurada\*\*

\- MLflow Model Registry.



\---



\### Seguimiento de Experimentos



\*\*Propuesta Inicial\*\*

\- No existe.



\*\*Propuesta Reestructurada\*\*

\- MLflow Tracking.



\---



\### Integración Continua



\*\*Propuesta Inicial\*\*

\- No existe.



\*\*Propuesta Reestructurada\*\*

\- GitHub Actions.



\---



\### Despliegue Continuo



\*\*Propuesta Inicial\*\*

\- No existe.



\*\*Propuesta Reestructurada\*\*

\- GitHub Actions + Docker.



\---



\### Monitoreo



\*\*Propuesta Inicial\*\*

\- No existe.



\*\*Propuesta Reestructurada\*\*

\- Prometheus y Grafana.



\---



\### Reentrenamiento



\*\*Propuesta Inicial\*\*

\- No existe.



\*\*Propuesta Reestructurada\*\*

\- Reentrenamiento basado en monitoreo.



\---



\### Escalabilidad



\*\*Propuesta Inicial\*\*

\- Limitada a contenedor local.



\*\*Propuesta Reestructurada\*\*

\- Escalable mediante Kubernetes.



\---



\### Gobierno del Modelo



\*\*Propuesta Inicial\*\*

\- No existe.



\*\*Propuesta Reestructurada\*\*

\- Versionamiento y trazabilidad completa.



\---



\## Resumen de Mejoras Incorporadas



\### Datos



\- Se incorpora una capa formal de validación.

\- Se definen procesos de transformación y limpieza.



\### Modelos



\- Se reemplaza la simulación por modelos entrenables.

\- Se incorpora versionamiento y trazabilidad.



\### DevOps



\- Se agrega integración continua.

\- Se agrega despliegue continuo.

\- Se incorpora contenerización escalable.



\### Operación



\- Se incorpora monitoreo.

\- Se incorpora detección de degradación.

\- Se incorpora reentrenamiento continuo.



\### MLOps



La nueva propuesta cubre el ciclo de vida completo de un modelo de Machine Learning, desde la captura de datos hasta el monitoreo y mantenimiento en producción.

