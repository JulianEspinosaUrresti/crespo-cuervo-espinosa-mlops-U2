\# CHANGELOG



\## Comparación entre la Propuesta Inicial y la Propuesta Reestructurada con MLOps



| Componente | Propuesta Inicial | Propuesta Reestructurada |

|------------|-------------------|--------------------------|

| Modelo | Simulación basada en reglas | Modelos de Machine Learning entrenados |

| Framework API | Flask | FastAPI |

| Contenerización | Docker | Docker + Kubernetes |

| Datos | Entrada manual desde formulario | Pipeline de datos estructurado |

| Validación de datos | No implementada | Great Expectations |

| Procesamiento | No definido formalmente | Pandas y Scikit-Learn |

| Entrenamiento | No existe | Pipeline automatizado |

| Evaluación | No existe | Accuracy, Precision, Recall, F1 y ROC-AUC |

| Versionamiento de modelos | No existe | MLflow Model Registry |

| Seguimiento de experimentos | No existe | MLflow Tracking |

| Integración Continua | No existe | GitHub Actions |

| Despliegue Continuo | No existe | GitHub Actions + Docker |

| Monitoreo | No existe | Prometheus y Grafana |

| Reentrenamiento | No existe | Reentrenamiento basado en monitoreo |

| Escalabilidad | Limitada a contenedor local | Escalable mediante Kubernetes |

| Gobierno del modelo | No existe | Versionamiento y trazabilidad completa |



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

