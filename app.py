"""
Script principal para ejecutar la aplicación Flask.
"""
import os
from musica_api import create_app
from dotenv import load_dotenv
from flask import request

# TODO: Cargar variables de entorno desde archivo .env si existe
load_dotenv()

# TODO: crear la aplicación
app = create_app()

if __name__ == "__main__":
    
    # TODO: Obtener puerto del ambiente o usar 5000 por defecto
    port = int(os.getenv("PORT", 5000))
    
    # TODO: Determinar si se debe usar modo debug

    
    # TODO: Ejecutar aplicación

