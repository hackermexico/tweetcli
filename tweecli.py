import tweepy
import time

def post_tweet(client, text):
    try:
        client.create_tweet(text=text)
        print(f"✅ Tweet publicado: {text}")
    except tweepy.TweepyException as e:
        print(f"❌ Error al publicar el tweet: {e}")

def main():
    # Solicitar credenciales
    print("🔐 Ingresa tu Consumer Key (API Key):")
    consumer_key = input().strip()
    print("🔐 Ingresa tu Consumer Secret (API Key Secret):")
    consumer_secret = input().strip()
    print("🔐 Ingresa tu Access Token:")
    access_token = input().strip()
    print("🔐 Ingresa tu Access Token Secret:")
    access_token_secret = input().strip()
    
    # Validar que todas las credenciales estén presentes
    if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
        print("❌ Error: Todas las credenciales son requeridas.")
        return
    
    # Crear cliente de Tweepy con OAuth 1.0a
    try:
        client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token=access_token,
            access_token_secret=access_token_secret
        )
    except Exception as e:
        print(f"❌ Error al autenticar: {e}")
        return
    
    print("\n🎉 Terminal interactiva para tweets. Escribe tu tweet y presiona Enter.")
    print("Para salir, usa Ctrl+C.")
    
    while True:
        try:
            print("\n📝 Ingresa el texto del tweet (máx 280 caracteres):")
            tweet_text = input().strip()
            
            if len(tweet_text) > 280:
                print("❌ Error: El tweet excede los 280 caracteres.")
                continue
            if len(tweet_text) == 0:
                print("❌ Error: El tweet no puede estar vacío.")
                continue
            
            # Publicar el tweet
            post_tweet(client, tweet_text)
            
            # Esperar 8 segundos
            print("⏳ Espera 8 segundos antes del próximo tweet...")
            time.sleep(8)
        
        except KeyboardInterrupt:
            print("\n👋 Saliendo de la terminal interactiva.")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            continue

if __name__ == "__main__":
    main()
