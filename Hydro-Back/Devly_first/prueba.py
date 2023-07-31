import asyncio
import websockets
import pymongo
import json
import random

clientes = set()

async def send_random_data(websocket):
    try:
        while True:
            # Generar datos aleatorios para el JSON
            json_data = {
                "waterTem": round(random.uniform(0, 100), 2),
                "temperature": round(random.uniform(0, 40), 2),
                "humedity": round(random.uniform(0,40),2),
                "light": round(random.uniform(0, 500), 2),
                "pH": round(random.uniform(5, 6.5), 2),
                "conduct": round(random.uniform(0, 200), 2),
            }

            # Enviar el JSON al cliente conectado
            json_data_str = json.dumps(json_data)
            await websocket.send(json_data_str)

            print("Clientes conectados:")
            for cliente in clientes:
                print(cliente.remote_address)


            # Esperar 1 segundo antes de enviar nuevos datos
            await asyncio.sleep(5)

    except websockets.exceptions.ConnectionClosedOK:
        pass
    except Exception as e:
        print(f"Ocurrió un error: {e}")

async def handle_client(websocket, path):
    # Agregar la conexión del cliente a la lista
    clientes.add(websocket)

    # Ejecutar la tarea de envío de datos al cliente
    await send_random_data(websocket)

    # Al salir de la tarea de envío, eliminar la conexión del cliente de la lista
    clientes.remove(websocket)

async def main():
    # Recibirá de cualquier dirección
    async with websockets.serve(handle_client, "0.0.0.0", 4000):
        print('Se inició el servidor')
        await asyncio.Future()  # run forever


asyncio.run(main())