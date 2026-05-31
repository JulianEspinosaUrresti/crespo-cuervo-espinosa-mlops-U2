# Diagrama General del Pipeline de MLOps

```text
┌──────────────────────────┐
│     Fuentes de Datos     │
│                          │
│ • Historias clínicas     │
│ • Laboratorios           │
│ • Registros médicos      │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│     Ingesta de Datos     │
│       PostgreSQL         │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│   Validación de Datos    │
│  Great Expectations      │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│  Feature Engineering     │
│ Pandas / Scikit-Learn    │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│     Entrenamiento        │
│   Random Forest /        │
│       XGBoost            │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│      Evaluación          │
│ Accuracy - Precision     │
│ Recall - F1 - ROC AUC    │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│     MLflow Registry      │
│   Versionamiento de      │
│        Modelos           │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│     GitHub Actions       │
│          CI/CD           │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│    Docker + FastAPI      │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│       Kubernetes         │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│     Médico / Usuario     │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│       Monitoreo          │
│ Prometheus + Grafana     │
└─────────────┬────────────┘
              │
              ▼
┌──────────────────────────┐
│    Reentrenamiento       │
│      Automático          │
└──────────────────────────┘
```

## Descripción del Flujo

1. Los datos clínicos son capturados desde diferentes fuentes médicas.
2. La información se almacena en PostgreSQL.
3. Great Expectations valida la calidad de los datos.
4. Se ejecutan procesos de transformación y selección de variables.
5. Los modelos son entrenados y evaluados.
6. Los modelos aprobados se registran en MLflow.
7. GitHub Actions automatiza los procesos de CI/CD.
8. Docker y FastAPI permiten el despliegue de la solución.
9. Kubernetes administra la ejecución en producción.
10. Prometheus y Grafana monitorean el desempeño.
11. Cuando se detecta degradación se inicia un nuevo ciclo de entrenamiento.