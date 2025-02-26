from modules.twitch import TwitchBot
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

if not API_TOKEN:
    print("Error: API_TOKEN not found. Please set it in your .env file.")
    exit()

initial_channels = [
    "IvanGO", "senyawei", "glebauster",
    "kartav__", "vudek_", "rainbowtaves", "ksuenoot", "danon_osu",
    "wavewyyy", "steisha_owo", "dahujka_owo", "kuukan_osu", "silversnakeuwu",
    "kkanoyaa", "lofkes_", "kury76", "quizzzzz_", "matrix_632",
    "pokemonyaaa", "j1mbeaam", "f0rz__", "mitor0_", "25mosey",
    "desuqe_", "godroponika", "honashhk", "skyfai_", "razorchik__",
]

twitch = TwitchBot(API_TOKEN, initial_channels)
twitch.run()
