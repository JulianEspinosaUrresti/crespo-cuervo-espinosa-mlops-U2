from modelo import evaluar_paciente


def test_no_enfermo():
    resultado = evaluar_paciente(36, 80, 97)
    assert resultado == "NO ENFERMO"


def test_enfermedad_terminal():
    resultado = evaluar_paciente(39, 130, 80)
    assert resultado == "ENFERMEDAD TERMINAL"