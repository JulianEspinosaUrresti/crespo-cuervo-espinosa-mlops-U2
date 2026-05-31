\# Diagrama General del Pipeline de MLOps



```text

&#x20;                   ┌─────────────────────┐

&#x20;                   │  Fuentes de Datos   │

&#x20;                   │                     │

&#x20;                   │ • Historias clínicas│

&#x20;                   │ • Laboratorios      │

&#x20;                   │ • Registros médicos │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │ Ingesta de Datos    │

&#x20;                   │ PostgreSQL          │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │ Validación Datos    │

&#x20;                   │ Great Expectations  │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │ Feature Engineering │

&#x20;                   │ Pandas / Sklearn    │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │ Entrenamiento       │

&#x20;                   │ RF / XGBoost        │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │ Evaluación          │

&#x20;                   │ Accuracy/F1/Recall  │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │ MLflow Registry     │

&#x20;                   │ Versionamiento      │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │ GitHub Actions      │

&#x20;                   │ CI/CD               │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │ Docker + FastAPI    │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │ Kubernetes          │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │ Médico / Usuario    │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │ Monitoreo           │

&#x20;                   │ Prometheus/Grafana  │

&#x20;                   └──────────┬──────────┘

&#x20;                              │

&#x20;                              ▼

&#x20;                   ┌─────────────────────┐

&#x20;                   │ Reentrenamiento     │

&#x20;                   └─────────────────────┘

```



\## Flujo General



1\. Los datos clínicos son capturados desde diferentes fuentes.

2\. Se almacenan en PostgreSQL.

3\. Se validan mediante Great Expectations.

4\. Se transforman mediante procesos de Feature Engineering.

5\. Se entrena el modelo.

6\. Se evalúan métricas de desempeño.

7\. El modelo se registra en MLflow.

8\. GitHub Actions automatiza CI/CD.

9\. Docker y FastAPI permiten el despliegue.

10\. Kubernetes administra la ejecución.

11\. Prometheus y Grafana monitorean el comportamiento.

12\. Ante degradación del desempeño se activa un nuevo ciclo de entrenamiento.

