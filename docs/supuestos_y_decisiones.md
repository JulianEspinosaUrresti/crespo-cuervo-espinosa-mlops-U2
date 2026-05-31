\# Supuestos y Decisiones de Diseño



\## Supuestos del Problema



\### Disponibilidad de datos



Se asume que existen registros clínicos históricos suficientes para entrenar modelos destinados a enfermedades comunes.



Para enfermedades huérfanas se asume que la cantidad de registros disponibles es significativamente menor.



\### Calidad de los datos



Se asume que los datos clínicos pueden contener:



\- Valores faltantes.

\- Registros duplicados.

\- Valores fuera de rango.

\- Errores de digitación.



Por esta razón se incorpora una etapa formal de validación de datos.



\### Infraestructura



Se asume que la solución podrá ejecutarse tanto:



\- Localmente en el computador del médico.

\- En servidores institucionales.

\- En infraestructura cloud.



\### Usuarios finales



Se asume que los usuarios principales serán:



\- Médicos.

\- Personal clínico.

\- Investigadores.



\---



\# Decisiones Tecnológicas



\## PostgreSQL



Seleccionado por ser una base de datos relacional ampliamente utilizada y adecuada para almacenar información clínica estructurada.



\## Great Expectations



Seleccionado para automatizar la validación de calidad de datos antes del entrenamiento.



\## Pandas y Scikit-Learn



Seleccionados por ser herramientas estándar para procesamiento y modelado de datos.



\## MLflow



Seleccionado para:



\- Versionar modelos.

\- Registrar experimentos.

\- Comparar ejecuciones.

\- Mantener trazabilidad.



\## GitHub Actions



Seleccionado para automatizar pruebas y despliegues.



\## Docker



Seleccionado para garantizar portabilidad y reproducibilidad.



\## Kubernetes



Seleccionado para administrar despliegues escalables.



\## FastAPI



Seleccionado por su alto desempeño y facilidad para exponer servicios REST.



\## Prometheus y Grafana



Seleccionados para monitoreo operacional y detección de degradación del modelo.



\---



\# Beneficios Esperados



\- Mayor trazabilidad.

\- Mayor reproducibilidad.

\- Reducción de errores manuales.

\- Automatización del ciclo de vida del modelo.

\- Escalabilidad futura.

\- Gobierno y control de versiones.

