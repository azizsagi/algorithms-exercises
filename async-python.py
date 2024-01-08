import time
import asyncio

async def take_cinema_ticket():
    print("Start take_cinema_ticket()")
    await asyncio.sleep(3)
    print("End take_cinema_ticket()")
    return "Ticket is ready please collect"

async def post_picture_on_instagram():
    print("Start post_picture_on_instagram()")
    await asyncio.sleep(2)
    print("End post_picture_on_instagram")
    return "Picture has been posted on instagram"

async def main():
    start_time = time.time()
    
    batch = asyncio.gather(take_cinema_ticket(), post_picture_on_instagram())
    ticket, picture = await batch

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(ticket)
    print(picture)
    print("Elapsed time is ")
    print(elapsed_time)

# Drive main function
asyncio.run(main())