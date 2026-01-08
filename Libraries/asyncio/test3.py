import requests
import time
import asyncio

start  = time.time()
for i in range(1,31):
    url = f"https://pokeapi.co/api/v2/pokemon/{str(i)}"
    result = requests.get(url)
    pokemon = result.json()
    print(pokemon['forms'][0]['name'])
print(f"total time for execution of the code is --> {time.time() - start}")


