\# Supuestos y Decisiones de Diseño



\## Introducción



La propuesta de reestructuración MLOps se construye sobre un conjunto de supuestos relacionados con la disponibilidad de datos, la infraestructura tecnológica y los usuarios finales del sistema. Asimismo, se documentan las principales decisiones tecnológicas adoptadas para garantizar trazabilidad, escalabilidad, reproducibilidad y mantenimiento continuo de los modelos de Machine Learning.



\# Supuestos del Problema



\## Disponibilidad de Datos



Se asume que existen registros clínicos históricos suficientes para entrenar modelos destinados a la predicción de enfermedades comunes.



Para el caso de enfermedades huérfanas, se asume que la cantidad de registros disponibles es significativamente menor, por lo que podrían requerirse técnicas especializadas como Transfer Learning o Few-Shot Learning.



\## Calidad de los Datos



Se asume que la información clínica puede presentar problemas de calidad típicos en sistemas de información hospitalarios, tales como:



\- Valores faltantes.

\- Registros duplicados.

\- Errores de digitación.

\- Valores fuera de rango.

\- Inconsistencias entre fuentes de información.



Por esta razón se incorpora una etapa formal de validación y control de calidad de datos dentro del pipeline.



\## Infraestructura



Se asume que la solución podrá ejecutarse en diferentes entornos tecnológicos:



\- Equipos locales utilizados por personal médico.

\- Servidores institucionales.

\- Infraestructura cloud.



La arquitectura propuesta busca mantener independencia del entorno de ejecución mediante el uso de contenedores.



\## Usuarios Finales



Se asume que los principales usuarios de la solución serán:



\- Médicos.

\- Personal clínico.

\- Investigadores.

\- Instituciones prestadoras de servicios de salud.



Estos usuarios requerirán resultados rápidos, confiables y fácilmente interpretables.



\# Decisiones Tecnológicas



\## PostgreSQL



\### Decisión



Utilizar PostgreSQL como sistema gestor de bases de datos.



\### Justificación



PostgreSQL es una plataforma robusta, ampliamente utilizada en entornos empresariales y adecuada para almacenar grandes volúmenes de información clínica estructurada.



\## Great Expectations



\### Decisión



Incorporar Great Expectations como herramienta de validación de datos.



\### Justificación



Permite automatizar controles de calidad, generar evidencia de validación y detectar inconsistencias antes del entrenamiento de los modelos.



\## Pandas y Scikit-Learn



\### Decisión



Utilizar Pandas y Scikit-Learn para el procesamiento y modelado de datos.



\### Justificación



Son herramientas estándar dentro del ecosistema de Machine Learning y cuentan con amplia adopción en entornos académicos e industriales.



\## MLflow



\### Decisión



Implementar MLflow para la gestión del ciclo de vida de los modelos.



\### Justificación



Permite:



\- Registrar experimentos.

\- Comparar ejecuciones.

\- Versionar modelos.

\- Mantener trazabilidad de resultados.



\## GitHub Actions



\### Decisión



Automatizar procesos mediante GitHub Actions.



\### Justificación



Facilita la implementación de prácticas de Integración Continua (CI) y Despliegue Continuo (CD), reduciendo errores manuales y mejorando la calidad del software.



\## Docker



\### Decisión



Utilizar Docker para la contenerización de la solución.



\### Justificación



Garantiza portabilidad, reproducibilidad y consistencia entre ambientes de desarrollo, pruebas y producción.



\## Kubernetes



\### Decisión



Utilizar Kubernetes para la orquestación de contenedores.



\### Justificación



Permite administrar despliegues escalables, tolerantes a fallos y preparados para crecimiento futuro.



\## FastAPI



\### Decisión



Utilizar FastAPI como framework para exponer servicios REST.



\### Justificación



Ofrece alto desempeño, facilidad de integración y documentación automática de APIs.



\## Prometheus y Grafana



\### Decisión



Incorporar herramientas de monitoreo operacional.



\### Justificación



Permiten supervisar:



\- Disponibilidad del servicio.

\- Consumo de recursos.

\- Latencia.

\- Comportamiento del modelo en producción.



\# Beneficios Esperados



La adopción de esta arquitectura MLOps permitirá:



\- Mayor trazabilidad de los modelos.

\- Reproducibilidad de experimentos.

\- Reducción de errores manuales.

\- Automatización del ciclo de vida de Machine Learning.

\- Escalabilidad de la solución.

\- Mejor gobierno y control de versiones.

\- Monitoreo continuo de los modelos desplegados.



\# Conclusión



Las decisiones tecnológicas adoptadas buscan transformar la solución inicial basada en Flask y Docker en una arquitectura MLOps completa, capaz de gestionar de manera eficiente el ciclo de vida de modelos de Machine Learning para la predicción de enfermedades comunes y huérfanas.

