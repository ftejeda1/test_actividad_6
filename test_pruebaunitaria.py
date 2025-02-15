import pytest
import re

# Funciones a probar

def is_valid_name(name: str) -> bool:
    """Verifica si el nombre tiene al menos 3 caracteres."""
    return len(name) >= 3

def is_valid_email(email: str) -> bool:
    """Verifica si el correo tiene un formato válido."""
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(regex, email))

def is_valid_password(password: str) -> bool:
    """Verifica si la contraseña tiene al menos 6 caracteres."""
    return len(password) >= 6

# Casos de prueba

def test_valid_name():
    """Prueba la validación del nombre."""
    assert is_valid_name("John") == True
    assert is_valid_name("Jo") == False

def test_valid_email():
    """Prueba la validación del correo electrónico."""
    assert is_valid_email("correo@dominio.com") == True
    assert is_valid_email("correo@dominio") == False
    assert is_valid_email("correo@") == False

def test_valid_password():
    """Prueba la validación de la contraseña."""
    assert is_valid_password("password123") == True
    assert is_valid_password("123") == False

# Ejecutar las pruebas
if __name__ == "__main__":
    pytest.main()
