# Supuestos y Decisiones de Diseno

## Introduccion

La propuesta de reestructuracion MLOps se construye sobre un conjunto de supuestos relacionados con la disponibilidad de datos, la infraestructura tecnologica y los usuarios finales del sistema. Asimismo, se documentan las principales decisiones tecnologicas adoptadas para garantizar trazabilidad, escalabilidad, reproducibilidad y mantenimiento continuo de los modelos de Machine Learning.

## Supuestos del Problema

### Disponibilidad de Datos

Se asume que existen registros clinicos historicos suficientes para entrenar modelos destinados a la prediccion de enfermedades comunes.

Para el caso de enfermedades huerfanas, se asume que la cantidad de registros disponibles es significativamente menor, por lo que podrian requerirse tecnicas especializadas como Transfer Learning o Few-Shot Learning.

### Calidad de los Datos

Se asume que la informacion clinica puede presentar problemas de calidad tipicos en sistemas de informacion hospitalarios, tales como:

- Valores faltantes.
- Registros duplicados.
- Errores de digitacion.
- Valores fuera de rango.
- Inconsistencias entre fuentes de informacion.

Por esta razon se incorpora una etapa formal de validacion y control de calidad de datos dentro del pipeline.

### Infraestructura

Se asume que la solucion podra ejecutarse en diferentes entornos tecnologicos:

- Equipos locales utilizados por personal medico.
- Servidores institucionales.
- Infraestructura cloud.

La arquitectura propuesta busca mantener independencia del entorno de ejecucion mediante el uso de contenedores.

### Usuarios Finales

Se asume que los principales usuarios de la solucion seran:

- Medicos.
- Personal clinico.
- Investigadores.
- Instituciones prestadoras de servicios de salud.

Estos usuarios requeriran resultados rapidos, confiables y facilmente interpretables.

## Decisiones Tecnologicas

### PostgreSQL

**Decision:** utilizar PostgreSQL como sistema gestor de bases de datos.

**Justificacion:** PostgreSQL es una plataforma robusta, ampliamente utilizada en entornos empresariales y adecuada para almacenar informacion clinica estructurada.

### Great Expectations

**Decision:** incorporar Great Expectations como herramienta de validacion de datos.

**Justificacion:** permite automatizar controles de calidad, generar evidencia de validacion y detectar inconsistencias antes del entrenamiento de los modelos.

### MLflow

**Decision:** implementar MLflow para la gestion del ciclo de vida de los modelos.

**Justificacion:** permite registrar experimentos, comparar ejecuciones, versionar modelos y mantener trazabilidad de resultados.

### Docker

**Decision:** utilizar Docker para la contenerizacion de la solucion.

**Justificacion:** garantiza portabilidad, reproducibilidad y consistencia entre ambientes.

### Kubernetes

**Decision:** utilizar Kubernetes para la orquestacion de contenedores.

**Justificacion:** permite administrar despliegues escalables, tolerantes a fallos y preparados para crecimiento futuro.

### GitHub Actions

**Decision:** automatizar procesos mediante GitHub Actions.

**Justificacion:** facilita la integracion continua y el despliegue continuo.

### FastAPI

**Decision:** utilizar FastAPI como framework para exponer servicios REST.

**Justificacion:** ofrece alto desempeno, facilidad de integracion y documentacion automatica.

### Prometheus y Grafana

**Decision:** incorporar herramientas de monitoreo operacional.

**Justificacion:** permiten supervisar disponibilidad, latencia, consumo de recursos y comportamiento del modelo.

## Beneficios Esperados

- Mayor trazabilidad.
- Reproducibilidad de experimentos.
- Reduccion de errores manuales.
- Automatizacion del ciclo de vida de Machine Learning.
- Escalabilidad de la solucion.
- Mejor gobierno y control de versiones.
- Monitoreo continuo de los modelos desplegados.

## Conclusion

Las decisiones tecnologicas adoptadas buscan transformar la solucion inicial basada en Flask y Docker en una arquitectura MLOps completa, capaz de gestionar de manera eficiente el ciclo de vida de modelos de Machine Learning para la prediccion de enfermedades comunes y huerfanas.
