from osuapi import OsuApi, ReqConnector; import os; from dotenv import load_dotenv

load_dotenv()
apiKey = os.getenv("API_KEY")

# Initialize API
api = OsuApi(apiKey, connector=ReqConnector())

userUsernameInput = input("Enter the user of the stats you want to see:")
# User to get stats for x
user = api.get_user(username=userUsernameInput)

# Display stats
print(f"User: {user[0].username}")
print(f"Rank: {user[0].pp_rank}")
print(f"Play Count: {user[0].playcount}")
print(f"Accuracy: {user[0].accuracy}")
