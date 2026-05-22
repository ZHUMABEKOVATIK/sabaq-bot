from aiogram.types import BotCommand

def my_commands() -> list[BotCommand]:
    com = [
        BotCommand(command="/start", description="Start bot"),
        BotCommand(command="/game", description="Start game"),
        BotCommand(command="/contact", description="Set my contact"),
        BotCommand(command="/removekb", description="Remove reply keyboard"),
        BotCommand(command="/keyboard", description="Get Keyboard"),
        BotCommand(command="/help", description="Help"),
    ]
    return com