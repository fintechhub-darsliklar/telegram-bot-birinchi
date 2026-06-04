
import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

# Replace this with your actual bot token
TOKEN = "YOUR_BOT_TOKEN_HERE"

# Create a router for our handlers
router = Router()

# Handle the /start command
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Hello! I am an aiogram bot.")

# Handle any text message (Echo)
@router.message(F.text)
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice message!")

async def main() -> None:
    # Initialize the bot instance
    bot = Bot(token=TOKEN)
    
    # Initialize the dispatcher and include our router
    dp = Dispatcher()
    dp.include_router(router)
    
    # Start polling for updates from Telegram
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())





