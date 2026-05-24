def evaluar_paciente(temperatura, frecuencia_cardiaca, oxigeno):
    if temperatura < 37 and frecuencia_cardiaca < 100 and oxigeno >= 95:
        return "NO ENFERMO"

    elif 37 <= temperatura < 38 and oxigeno >= 94:
        return "ENFERMEDAD LEVE"

    elif temperatura >= 38 and frecuencia_cardiaca >= 100 and oxigeno < 94:
        return "ENFERMEDAD AGUDA"

    else:
        return "ENFERMEDAD CRÓNICA"