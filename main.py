from osuapi import OsuApi, ReqConnector; import os; from dotenv import load_dotenv

load_dotenv()
apiKey = os.getenv("API_KEY")

# Initialize API
api = OsuApi(apiKey, connector=ReqConnector())

userUsernameInput = input("Enter the user of the stats you want to see: ")
# User to get stats for x
user = api.get_user(username=userUsernameInput)

# Display stats
print(f"User: {user[0].username}")
print(f"Rank: {user[0].pp_rank}")
print(f"Play Count: {user[0].playcount}")
print(f"Accuracy: {user[0].accuracy}")
print(f"PP: {user[0].pp_raw}")

# Fetch user's top plays
top_plays = api.get_user_best(username=userUsernameInput, limit=1)

if top_plays:
    top_play = top_plays[0]
    
    # Fetch beatmap details using beatmap_id
    beatmap = api.get_beatmaps(beatmap_id=top_play.beatmap_id)
    
    if beatmap:
        beatmap = beatmap[0]  # Get the first (and usually only) beatmap
        print(f"\nTop Play:")
        print(f"Score: {top_play.score}")
        print(f"PP: {top_play.pp}")
        print(f"Beatmap: {beatmap.title} ({beatmap.version})")
        print(f"Accuracy: {top_play.accuracy:.2f}%")
        print(f"Date: {top_play.date}")
    else:
        print("Beatmap details not found.")
else:
    print("No top plays found for this user.")