import socket
import sys
from datetime import datetime

# 1. Definir el objetivo (servidor público legal para pruebas)
objetivo = "scanme.nmap.org"

try:
    # Traducir el nombre de la web a una dirección IP
    ip_objetivo = socket.gethostbyname(objetivo)
except socket.gaierror:
    print("\n No se pudo resolver el nombre del host.")
    sys.exit()

# 2. Imprimir el diseño en la pantalla
print("-" * 50)
print(f"Escaneando el objetivo: {ip_objetivo}")
print(f"Escaneo iniciado a las: {str(datetime.now())}")
print("-" * 50)

# 3. Lista de puertos comunes a escanear
puertos = [21, 22, 23, 25, 53, 80, 110, 443, 3306]

print("Escaneando puertos abiertos...")

try:
    for puerto in puertos:
        # Crear un socket (conector de red)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Tiempo de espera de 1 segundo por puerto
        s.settimeout(1.0)
        
        # Intentar conectar al puerto
        resultado = s.connect_ex((ip_objetivo, puerto))
        
        if resultado == 0:
            print(f"[+] Puerto {puerto}: ABIERTO")
        
        # Cerrar el conector
        s.close()

except KeyboardInterrupt:
    print("\n\nSaliendo del programa...")
    sys.exit()
except socket.error:
    print("\nNo se pudo conectar al servidor.")
    sys.exit()

print("\nEscaneo finalizado con éxito.")