from dataclasses import dataclass
from environs import Env


@dataclass
class TBot:
    token: str


@dataclass
class Config:
    bot: TBot


def load_config(path=None):
    env = Env()
    env.read_env(path)
    token = env('BOT_TOKEN')
    bot = TBot(token)
    config = Config(bot)
    return config
