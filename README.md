# Crypto Monitor Dashboard 🚀

![Estado del proyecto](https://img.shields.io/badge/Estado-Desarrollo%20Inicial-yelloworange)
![Versión](https://img.shields.io/badge/Versión-0.1.0-blue)
![Licencia](https://img.shields.io/badge/Licencia-AGPL--3.0-green)

## 📌 Descripción

**Crypto Monitor** es un sistema avanzado de seguimiento de criptomonedas que actualmente se encuentra en **desarrollo cerrado**. El proyecto será open source bajo licencia AGPL-3.0 una vez alcanzada una versión estable inicial.

Características principales:
- Web scraping de múltiples fuentes de noticias
- Análisis de sentimiento del mercado con IA
- Generación de informes automáticos
- Sistema de newsletters programables

> 🔒 **Política de acceso**: Durante esta fase inicial, el repositorio permanecerá privado hasta alcanzar la versión 1.0.0 estable. No se aceptarán contribuciones externas hasta entonces.

## 🛠️ Estructura del Proyecto

El proyecto está dividido en:

1. **Core**: Modelos principales y configuración base
2. **Scraper**: Sistema de extracción de datos
3. **Dashboard**: Interfaz visual con gráficos
4. **Newsletter**: Sistema de envío de reportes

## 🛠️ Estructura Técnica
```
crypto-monitor/
├── backend/ # Configuración Django principal
├── core/ # Modelos de datos y lógica central
├── dashboard/ # Interfaz visual y gráficos
├── newsletter/ # Sistema de envío de reportes
├── scraper/ # Módulo de extracción de datos
├── static/ # Assets estáticos (CSS/JS)
├── templates/ # Plantillas base
├── .gitignore # Archivos excluidos
└── README.md # Este archivo
```

## ⚙️ Configuración Inicial

1. Clonar repositorio:
```bash
git clone [url-del-repositorio]
cd crypto-monitor
```
2. Configuación de entorno virtual:
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```
3. Ejecutar migraciones y crear superusuario:
```
python manage.py migrate
python manage.py createsuperuser
```
4. Ejecutar servidor:
```
python manage.py runserver
```

## 🚀 Próximas Funcionalidades
- Integración con APIs de criptomonedas
- Análisis de sentimiento avanzado
- Dashboard interactivo
- Sistema de alertas

## 🤝 Contribución
Actualmente no se aceptan contribuciones externas mientras el proyecto está en fase inicial.

## 📜 Licencia (Futura)
El proyecto se liberará bajo GNU Affero General Public License v3.0 (AGPL-3.0), que garantiza:
- Libertad para usar, estudiar y modificar el software
- Requisito de compartir mejoras bajo la misma licencia
- Protección contra el "SaaS loophole" (uso en servicios web)
```
Copyright (C) 2025 Raúl Fernández Tirado

Este programa es software libre: puedes redistribuirlo y/o modificarlo
bajo los términos de la GNU Affero General Public License publicada por
la Free Software Foundation, ya sea la versión 3 de la Licencia, o
(a tu elección) cualquier versión posterior.
```

## 🚀 Roadmap
### Versión 0.x (Desarrollo Cerrado)
- Implementación core del scraping
- Análisis básico de sentimiento
- Dashboard mínimo viable
### Versión 1.0 (Primera Release Pública)
- Documentación completa
- Sistema de configuración modular
- Pruebas unitarias cubriendo >80% del código