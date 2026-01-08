import asyncio

async def fetch_data(param):
    print(f"doing something for input: {param}")
    await asyncio.sleep(param)
    print(f"complete the task for input: {param}")
    return f"result of {param}"

async def main():
    task1 = fetch_data(2)
    task2 = fetch_data(4)
    result1 = await task1
    print(f"Task 1 completed")
    result2 = await task2
    print(f"task 2 is completed")
    return [result1, result2]

result = asyncio.run(main())
print(result)


# Even though we have used asyncio syntax to manage the code to do the task in concurrent, this code still works in a synchronous manner.