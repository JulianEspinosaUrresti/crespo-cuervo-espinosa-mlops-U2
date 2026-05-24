# Servicio Médico con Docker

---

# Descripción del proyecto

Este proyecto implementa un servicio médico simple que permite simular un modelo de predicción de enfermedades utilizando Python, Flask y Docker.

La aplicación recibe información clínica básica de un paciente y retorna una clasificación automática del estado del paciente.

El sistema puede retornar uno de los siguientes estados:

- NO ENFERMO
- ENFERMEDAD LEVE
- ENFERMEDAD AGUDA
- ENFERMEDAD CRÓNICA

La solución fue desarrollada como parte de un ejercicio académico orientado a MLOps y contenerización con Docker.

---

# Tecnologías utilizadas

- Python 3.11
- Flask
- Docker

---

# Estructura del proyecto

```text
mlops_docker_medico_grupo2/
│
├── app.py
├── modelo.py
├── requirements.txt
├── Dockerfile
├── README.md
└── propuesta_tecnica.md
```

---

# Explicación de archivos

| Archivo | Función |
|---|---|
| app.py | Aplicación principal y servicio web |
| modelo.py | Simulación del modelo de predicción |
| requirements.txt | Dependencias necesarias |
| Dockerfile | Construcción de la imagen Docker |
| README.md | Documentación del proyecto |
| propuesta_tecnica.md | Explicación del pipeline MLOps |

---

# Variables utilizadas

El sistema utiliza las siguientes variables clínicas:

| Variable | Descripción |
|---|---|
| temperatura | Temperatura corporal |
| frecuencia_cardiaca | Pulsaciones por minuto |
| oxigeno | Saturación de oxígeno |

---

# Estados posibles

El sistema puede retornar:

- NO ENFERMO
- ENFERMEDAD LEVE
- ENFERMEDAD AGUDA
- ENFERMEDAD CRÓNICA

---

# Requisitos previos

Antes de ejecutar el proyecto es necesario tener instalado:

- Docker Desktop
- WSL2 habilitado en Windows

---

# Construcción de la imagen Docker

Ubicarse en la carpeta del proyecto y ejecutar:

```bash
docker build -t modelo-medico .
```

---

# Ejecución del contenedor

Ejecutar:

```bash
docker run -p 5000:5000 modelo-medico
```

---

# Acceso al servicio web

Abrir el navegador y acceder a:

```text
http://localhost:5000
```

La aplicación mostrará un formulario donde el médico podrá ingresar:

- Temperatura corporal
- Frecuencia cardíaca
- Nivel de oxígeno

Luego el sistema mostrará automáticamente el resultado de la evaluación.

---

# Uso del endpoint API

También es posible consumir el servicio mediante API REST.

Endpoint:

```text
POST /evaluar
```

Ejemplo usando PowerShell:

```powershell
Invoke-RestMethod `
-Uri "http://localhost:5000/evaluar" `
-Method POST `
-ContentType "application/json" `
-Body '{"temperatura":39,"frecuencia_cardiaca":120,"oxigeno":90}'
```

---

# Respuesta esperada

```json
{
    "resultado": "ENFERMEDAD AGUDA"
}
```

---

# Ejemplo de funcionamiento

| Temperatura | Frecuencia cardíaca | Oxígeno | Resultado |
|---|---|---|---|
| 36 | 80 | 97 | NO ENFERMO |
| 37.5 | 90 | 95 | ENFERMEDAD LEVE |
| 39 | 120 | 90 | ENFERMEDAD AGUDA |

---

# Posibles mejoras futuras

La solución puede evolucionar hacia:

- Integración con modelos reales de Machine Learning.
- Conexión con bases de datos médicas.
- Historial clínico.
- Despliegue en nube.
- Monitoreo de modelos.
- Reentrenamiento automático.

## Consideración sobre enfermedades huérfanas

La solución desarrollada para esta actividad utiliza una simulación basada en reglas y no un modelo real entrenado con datos clínicos.

Sin embargo, la arquitectura propuesta queda preparada para futuras integraciones con modelos de Machine Learning especializados en escenarios con:

- Grandes volúmenes de datos (enfermedades comunes).
- Pocos datos disponibles (enfermedades huérfanas).

En un escenario real, podrían utilizarse técnicas como:

- Transfer Learning.
- Few-Shot Learning.
- Data Augmentation.
- Modelos preentrenados.
- Aprendizaje semi-supervisado.

Estas técnicas permiten construir modelos capaces de trabajar incluso cuando la cantidad de información disponible es reducida.

---

# Conclusión

La solución desarrollada permite implementar un servicio médico portable utilizando Docker, Flask y Python.

El sistema cumple con los requisitos de contenerización, exposición del servicio y simulación de un modelo predictivo definidos en la actividad académica.