import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler = AsyncIOScheduler()

# scheduler.add_job(mail, "interval", minutes=1)

async def start_scheduler():
    scheduler.start()

    print("📅 Планировщик запущен\n")

if __name__ == "__main__":
    asyncio.run(start_scheduler())