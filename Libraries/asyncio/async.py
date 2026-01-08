import asyncio

async def fetch_data(param):
    print(f"doing something for input: {param}")
    await asyncio.sleep(param)
    print(f"complete the task for input: {param}")
    return f"result of {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    print(f"Task 1 completed")
    result2 = await task2
    print(f"task 2 completed")
    return [result1, result2]

result = asyncio.run(main())
print(result)


# Here there are two things to observe
# 1. We have performed the task in concurent manner and
# 2. We have also seen that task 2 was completed first, so we got output for that first, meaning, which ever task is completed first we get the output for that task