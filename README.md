# Network Port Scanner in Python 🔒

Este es un script interactivo desarrollado en **Python** diseñado para realizar tareas de reconocimiento y auditoría de ciberseguridad (*footprinting*). El programa toma un nombre de dominio o una dirección IP, resuelve su identidad en la red y escanea de forma automatizada una lista de los puertos más comunes y críticos para detectar cuáles se encuentran expuestos (abiertos).

El proyecto fue diseñado con un enfoque práctico y de rendimiento, ideal para auditorías iniciales de seguridad y como parte de mi portafolio en Ingeniería en Desarrollo de Software.

---

## 🚀 Características Principales

* **Resolución de DNS Automática:** Traduce nombres de dominio (hosts) a direcciones IPv4 en tiempo real usando sockets nativos.
* **Escaneo Eficiente con Timeouts:** Implementa un límite de espera de 1.0 segundo por puerto para optimizar el tiempo de respuesta y evitar bloqueos por puertos filtrados.
* **Manejo de Excepciones Avanzado:**
    * `KeyboardInterrupt`: Permite al usuario abortar el escaneo limpiamente en cualquier momento (`Ctrl + C`).
    * `socket.gaierror`: Detecta fallas de conectividad o errores al resolver el nombre del host.
    * `socket.error`: Captura errores generales de conexión de red.
* **Estructura Limpia:** Código modular, documentado paso a paso y fácil de escalar para auditorías más profundas.

---

## 🛠️ Tecnologías y Librerías Utilizadas

El script utiliza exclusivamente librerías nativas de Python, demostrando el dominio de la biblioteca estándar para redes:

* **`socket`**: Para la gestión de conexiones de red a bajo nivel (TCP/IP).
* **`sys`**: Para el control de salidas limpias del sistema durante excepciones.
* **`datetime`**: Para registrar la estampa de tiempo exacta del inicio de la auditoría.

---

## 📦 Puertos Evaluados

El escáner se enfoca por defecto en auditar los servicios estándar más explotados en la industria:

* **21 (FTP)** - Transferencia de archivos
* **22 (SSH)** - Acceso remoto seguro
* **23 (Telnet)** - Acceso remoto obsoleto/inseguro
* **25 (SMTP)** - Envío de correo electrónico
* **53 (DNS)** - Resolución de nombres de dominio
* **80 (HTTP)** - Tráfico web sin cifrar
* **110 (POP3)** - Recepción de correo electrónico
* **443 (HTTPS)** - Tráfico web seguro/cifrado
* **3306 (MySQL)** - Conexión a bases de datos

---

## 💻 Instrucciones de Uso

### Prerrequisitos
Tener instalado **Python 3.x** en el sistema.

### Ejecución
1. Descarga o clona este repositorio.
2. Abre una terminal de comandos en la ruta del archivo.
3. Ejecuta el siguiente comando:
```bash
python escaner.py
--------------------------------------------------
Escaneando el objetivo: 45.33.32.156
Escaneo iniciado a las: 2026-06-02 22:04:44.409898
--------------------------------------------------
Escaneando puertos abiertos...
[+] Puerto 22: ABIERTO
[+] Puerto 53: ABIERTO
[+] Puerto 80: ABIERTO

Escaneo finalizado con éxito.
```
Descargo de Responsabilidad (Disclaimer)
Este script fue desarrollado estrictamente con fines educativos y de aprendizaje en ciberseguridad defensiva. El objetivo por defecto (scanme.nmap.org) es una infraestructura pública autorizada para pruebas de escaneo legales. El uso de esta herramienta contra objetivos sin autorización previa está bajo la total responsabilidad del usuario
