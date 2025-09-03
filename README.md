# tweetcli
Para poder mandar tweets desde la terminal y ya no tener que perder el tiempo y seguir programando que felicidad porque no se me ocurrió antes te puede evitar horas de distracción.

**TweetCLI** es una aplicación de consola en Python 3 que te permite enviar tweets desde tu terminal de forma interactiva. Escribe un tweet, presiona Enter, y publícalo en tu cuenta de Twitter/X. Ideal para hackers, desarrolladores y entusiastas de la automatización que quieren interactuar con la API de Twitter/X desde la línea de comandos. 🚀

## ✨ Características

- **Interfaz interactiva**: Escribe tweets y envíalos con Enter.
- **Soporte para emojis**: Publica tweets con emojis como 😎 o 🐍.
- **Autenticación segura**: Usa OAuth 1.0a con Consumer Key, Consumer Secret, Access Token y Access Token Secret.
- **Retraso de 8 segundos**: Evita superar los límites de la API (~50 tweets/día en el nivel gratuito).
- **Carga de credenciales**: Soporta archivo `.env` para evitar ingresar credenciales manualmente.
- **Simple y ligero**: Perfecto para entornos de hacking o scripts rápidos.

## 🛠️ Requisitos

- **Python 3.7+**
- **Tweepy**: `pip3 install tweepy`
- **Opcional**: `python-dotenv` para cargar credenciales desde un archivo `.env` (`pip3 install python-dotenv`)
- Credenciales de la API de Twitter/X:
  - Consumer Key (API Key)
  - Consumer Secret (API Key Secret)
  - Access Token
  - Access Token Secret
