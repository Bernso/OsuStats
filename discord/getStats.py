import os
from dotenv import load_dotenv
import aiohttp
import asyncio

#################### THIS FILE IS FOR THE DISCORD BOT #################################
# You can still use this if you want though

# Load environment variables
load_dotenv()
api_key = os.getenv("API_KEY")

# osu! API base URL
BASE_URL = "https://osu.ppy.sh/api/"

async def get_user(api_key, username):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}get_user?k={api_key}&u={username}") as response:
            if response.status == 200:
                return await response.json()
            else:
                raise Exception(f"Failed to fetch user data: {response.status}")

async def get_user_best(api_key, username, limit=1):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BASE_URL}get_user_best?k={api_key}&u={username}&limit={limit}") as response:
            if response.status == 200:
                return await response.json()
            else:
                raise Exception(f"Failed to fetch user best data: {response.status}")

async def main(username):
    try:
        user = await get_user(api_key, username)

        if user:
            user = user[0]
            statString = (f"User: {user['username']}\n"
                          f"Rank: {user['pp_rank']}\n"
                          f"Play Count: {user['playcount']}\n"
                          f"Accuracy: {user['accuracy']}%\n"
                          f"PP: {user['pp_raw']}")

            top_plays = await get_user_best(api_key, username)
            if top_plays:
                top_play = top_plays[0]
                beatmap_id = top_play['beatmap_id']
                statString += (f"\n\nTop Play:\n"
                               f"    Score: {top_play['score']}\n"
                               f"    PP: {top_play['pp']}\n"
                               f"    Beatmap ID: {beatmap_id}")
            else:
                statString += "\nNo top plays found for this user."

            return statString
        else:
            return "User not found."

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    username = "Bernso"  # Replace with desired username or get input dynamically
    result = asyncio.run(main(username))
    print(result)
