import asyncio
import time



async def get_movie_tickets():
    await asyncio.sleep(5)
    print("got the movie tickets")

async def like_ig():
    await asyncio.sleep(2)
    print("liked the instagram post")

async def main():
    start = time.time()
    task1 = asyncio.create_task(get_movie_tickets())
    task2 = asyncio.create_task(like_ig())
    await task1
    await task2
    print(f"total time taken for executing tasks --> {time.time() - start}")


asyncio.run(main())