import asyncio, requests
from asgiref.sync import sync_to_async


async def create_background_task(function, on_success, func_args={}, db_logger=None,
                                  thread_sensitive=False, is_async=False):
    



    async_function = function
    print("+++++++++++++++++++++", not is_async)
    if not is_async:
        
        async_function = sync_to_async(function, thread_sensitive=thread_sensitive)


    loop = asyncio.get_event_loop()
    async_task = loop.create_task(async_function(**func_args))

    async_task.add_done_callback(on_success)


