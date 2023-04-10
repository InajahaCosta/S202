import random
import threading
import time
from pymongo import MongoClient

# Abrindo uma conexao com o Sever do MongoDB
client = MongoClient('mongodb://localhost:27017/')
# Indicando qual schema quero acessar
db = client['bancoiot']
# Indicando qual collection deste schema quero acessar
sensores = db.sensores


def sensor(name, tempoExecucao, sensores):
    while True:
        temperatura = random.uniform(30, 40)
        print(f"{name}: {temperatura:.2f}°C")
        document = {
            "nomeSensor": name,
            "valorSensor": temperatura,
            "unidadeMedida": "C°",
            "sensorAlarmado": False
        }

        sensores.replace_one({"nomeSensor": name}, document, upsert=True)
        print(F" {name} Sensor adicionado!")

        # Sensor alarmed:
        if temperatura > 38:
            print(f"Atenção! Temperatura muito alta! Verificar {name}!")
            sensores.update_one({"nomeSensor": name}, {"$set": {"sensorAlarmado": True}})
            print(F" {name} Sensor atualizado!")
            break
        else:
            time.sleep(tempoExecucao)

# Criação das Thread
thread1 = threading.Thread(target=sensor, args=("Sensor1", 10, sensores))
thread2 = threading.Thread(target=sensor, args=("Sensor2", 20, sensores))
thread3 = threading.Thread(target=sensor, args=("Sensor3", 30, sensores))

# Iniciando as Threads:
thread1.start()
thread2.start()
thread3.start()

