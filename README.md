# NexusDocs: Agente de IA Corporativo

NexusDocs es un agente de Inteligencia Artificial diseñado para centralizar y responder preguntas sobre documentación interna de la empresa, facilitando el acceso a políticas de RH, procedimientos operativos y normativas. Este proyecto fue desarrollado como parte del desafío Alura Agentes.

## 🚀 Arquitectura del Proyecto

NexusDocs implementa un sistema **RAG (Retrieval-Augmented Generation)** robusto y modular. A continuación, se detalla el flujo de trabajo de la arquitectura:

1. **Ingesta:** Carga automática de documentos desde la carpeta `/docs` utilizando `DirectoryLoader`.
2. **Procesamiento:** Segmentación de textos con `RecursiveCharacterTextSplitter` y vectorización mediante `HuggingFaceEmbeddings` (`all-MiniLM-L6-v2`).
3. **Almacenamiento:** Base de datos vectorial persistente con `ChromaDB`.
4. **Orquestación:** Cadena moderna (`create_retrieval_chain`) conectada a la API de **Groq** (usando el modelo `llama-3.3-70b-versatile`).
5. **Interfaz:** Aplicación web interactiva desarrollada con `Streamlit`.

## 🛠 Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Framework IA:** LangChain (v0.3+)
- **LLM:** Groq (Llama 3.3)
- **Embeddings:** Sentence-Transformers (HuggingFace)
- **Vector Store:** ChromaDB
- **Interfaz:** Streamlit
- **Infraestructura:** Oracle Cloud Infrastructure (OCI) / Streamlit Cloud

## 📋 Requisitos para Ejecución

1. Clona este repositorio.
2. Crea un entorno virtual e instala las dependencias: `pip install -r requirements.txt`.
3. Crea un archivo .env en la raíz siguiendo el modelo .env.example y añade tu `GROQ_API_KEY` y `GROQ_MODEL_NAME`.
4. Ejecuta la aplicación: `streamlit run src/app.py`.

## ☁️ Opciones de Despliegue

1. Despliegue OCI
   El agente debe desplegarse en Oracle Cloud Infrastructure (OCI).
   Se recomienda el uso de una instancia de cómputo (VM) configurada con Docker o un entorno Python persistente.
   [text](https://www.aluracursos.com/formacion-oracle-cloud-infraestructure)

2. Despliegue Rápido (Streamlit Cloud)
   Para una puesta en marcha ágil o pruebas rápidas:

   Sube tu código a un repositorio público de GitHub.

   Accede a share.streamlit.io.

   Haz clic en "New app", selecciona tu repositorio y el archivo app.py.

   En "Advanced settings", añade tus variables de entorno (GROQ_API_KEY y GROQ_MODEL_NAME).

   Haz clic en "Deploy".

💡 Cómo usar NexusDocs
NexusDocs es una solución RAG modular y abierta. Solo clona el repo, configura tu archivo .env con tus credenciales de Groq y añade tus documentos (PDF, Markdown, etc.) en la carpeta /docs para comenzar.

[INSERTA AQUÍ TU IMAGEN O VIDEO DEL AGENTE EN EJECUCIÓN]

Desafío Alura Agentes - MVP Corporativo

## ☁️ Despliegue en la Nube

El agente está desplegado y operativo en la infraestructura cloud.
[Aquí puedes insertar la imagen o video del agente ejecutándose, como solicita el desafío]

---

_Desafío Alura Agentes - MVP Corporativo_
