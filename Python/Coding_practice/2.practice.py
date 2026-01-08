import asyncio

async def fetch_data(id):

    print(f"task started for id:{id}")
    await asyncio.sleep(2)
    print(f"task finished for id:{id}")
    return f"data:{id*2}"

async def main():

    results = await asyncio.gather(fetch_data(1),fetch_data(2))

    return f"results:{results}"

if __name__ == "__main__":
    asyncio.run(main())
