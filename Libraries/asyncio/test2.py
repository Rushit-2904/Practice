import asyncio
import time

async def fetch_file():
    print("starting to fetch the file")
    await asyncio.sleep(1)
    print("downloaded the file")

async def main():
    start = time.time()
    print("strated the main function")
    await asyncio.gather(
        fetch_file(),
        fetch_file(),
        fetch_file()
    )
    print(f"total time:{time.time() - start}")

asyncio.run(main())

