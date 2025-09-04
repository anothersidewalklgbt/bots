import discord
import asyncio

# Lista con los tokens de tus 6 cuentas
TOKENS = [
    "MTMzMDEyMDUwNDU1MTUzODc5MA.GEq9Xd.OY6gZ46lUWrnOP9vrJBJpD0FcaEYoPEu-iv-0k",
    "MTExNTY3ODc0NDY5OTQ4NjI2OQ.GQB6F-.ebCsRAp4hfPp4TXTj35Xy136imPLei8gJGi8A8",
    "MTQxMDY1NDIxNjYzMjAxMjk2Mw.GSYw67.NQmmldSAvxapZzN24uuF8jfaEISveO6F3kJapo",
    "MTM5ODgwODI4NzE2NzY0Nzg0Nw.GeR0ly.q_WlWm2b8Q0GAEK9a6VNX1ML5RxI8mYObKEHNk",
    "MTQxMDcxOTkxMjk4NDQ0NTA1OQ.GmUBV3.ZhR9jlfruj3z17R5WHXHGXM5s9z8Usnh0KJfHs",
    "MTQxMDY0ODgzOTA5Mzg4MzAyNQ.Gu32YB.bkXMltShjDYq9eBR3hieWyn4jnbEnAPUJF-uOg"
]

CHANNEL_ID = 1403068635869741147  # ID del canal

# Intervalos
INTERVALO_WORK = 10 * 60 + 15       # 10 minutos + 15 segundos
INTERVALO_DEP = 2 * 60 * 60         # 2 horas
INTERVALO_SLUT = 3 * 60 * 60 + 30   # 3 horas + 30 segundos
INTERVALO_CHAT = 7 * 60 * 60        # 7 horas

# Guion de conversación entre 6 cuentas
GUIÓN = [
    (0, "¿Cómo están todos?"),
    (1, "Todo bien, gracias 🙌"),
    (2, "Yo cansado, pero normal 😴"),
    (3, "Aquí comiendo algo 😋"),
    (4, "¿Qué están haciendo ustedes?"),
    (5, "Solo pasando el rato 😎")
]

async def run_bot(token, index):
    client = discord.Client(self_bot=True)

    @client.event
    async def on_ready():
        print(f"{client.user} conectado")
        canal = client.get_channel(CHANNEL_ID)

        async def ciclo_work():
            while True:
                await canal.send(",with all")
                print(f"{client.user} envió ,work")
                await asyncio.sleep(INTERVALO_WORK)

        async def ciclo_dep():
            while True:
                await canal.send(",give DMR all")
                print(f"{client.user} envió ,dep all")
                await asyncio.sleep(INTERVALO_DEP)

        async def ciclo_slut():
            while True:
                await canal.send("B")
                print(f"{client.user} envió ,slut")
                await asyncio.sleep(INTERVALO_SLUT)

        async def ciclo_chat():
            while True:
                for turno, mensaje in GUIÓN:
                    if turno == index:  # este bot habla cuando es su turno
                        await canal.send(mensaje)
                        print(f"{client.user} dijo: {mensaje}")
                    await asyncio.sleep(5)  # 5 segundos entre mensajes
                await asyncio.sleep(INTERVALO_CHAT)

        # Lanzamos todas las tareas en paralelo
        asyncio.create_task(ciclo_work())
        asyncio.create_task(ciclo_dep())
        asyncio.create_task(ciclo_slut())
        asyncio.create_task(ciclo_chat())

    await client.start(token)

async def main():
    await asyncio.gather(*(run_bot(token, i) for i, token in enumerate(TOKENS)))

asyncio.run(main())

