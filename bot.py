import discord
import asyncio

# Lista con los tokens de tus 5 cuentas
TOKENS = [
    "",
    "",
    "",
    "",
    "",
    ""
]

CHANNEL_ID = 1403068635869741147  # ID del canal donde usarás ,work
INTERVALO = 10 * 60 + 15  # cada 10 minutos + 15 segundos

async def run_bot(token):
    client = discord.Client(self_bot=True)

    @client.event
    async def on_ready():
        print(f"Conectado como {client.user}")
        canal = client.get_channel(CHANNEL_ID)
        while True:
            await canal.send(",give DMR all")  # o cualquier comando que quieras
            print(f"Comando enviado desde {client.user}")
            await asyncio.sleep(INTERVALO)

    await client.start(token)

async def main():
    # Crea una tarea para cada cuenta
    await asyncio.gather(*(run_bot(token) for token in TOKENS))

# Ejecuta todas las cuentas
asyncio.run(main())
