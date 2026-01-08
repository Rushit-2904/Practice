import asyncio

async def sqr(n):
    return n*n

async def main():

    x = await sqr(2)
    print(x)

    y = await sqr(4)
    print(y)

    z = x+y
    print(z)

asyncio.run(main())