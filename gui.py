from osuapi import OsuApi, ReqConnector; import os; from dotenv import load_dotenv; import customtkinter as ctk

load_dotenv()

apiKey = os.getenv('API_KEY')
if apiKey is None:
    print("No API_KEY found in environment variables.")
    exit(1)


app = ctk.CTk()
app.title("Osu!")
app.geometry("400x320")
app.resizable(False, False)

usernameCheckBoxVar = ctk.BooleanVar(value=False)
rankCheckBoxVar = ctk.BooleanVar(value=False)
playsCheckBoxVar = ctk.BooleanVar(value=False)
accuracyCheckBoxVar = ctk.BooleanVar(value=False)
ppCheckBoxVar = ctk.BooleanVar(value=False)

def open_stat_window(text):
    stat_window = ctk.CTkToplevel()
    stat_window.title("Stats")
    stat_window.geometry("300x200")

    label = ctk.CTkLabel(stat_window, text=text)
    label.pack(pady=20)

    close_button = ctk.CTkButton(stat_window, text="Close", command=stat_window.destroy)
    close_button.pack(pady=10)


def getStats():
    userName = usernameEntry.get()
    if userName:
        print("User Name Found")
        try:
            api = OsuApi(apiKey, connector=ReqConnector())
            user = api.get_user(username=userName)
            if user:
                statString = f"Stats:\n"
                if usernameCheckBoxVar.get():
                    username = user[0].username
                    statString += f"Username: {username}\n"
                
                if rankCheckBoxVar.get():
                    rank = user[0].pp_rank
                    statString += f"Rank: {rank}\n"
                
                if playsCheckBoxVar.get():
                    plays = user[0].playcount
                    statString += f"Play Count: {plays}\n"

                if accuracyCheckBoxVar.get():    
                    accuracy = user[0].accuracy
                    statString += f"Accuracy: {accuracy}\n"

                if ppCheckBoxVar.get():
                    performancePoints = user[0].pp_raw
                    statString += f"Performance Points: {performancePoints}\n"

                
                open_stat_window(statString)
            else:
                print(f"{userName} Not Found.")
        except Exception as e:
            print(f"Failed to get stats for {userName}.\nError: {e}")
    else:
        print("Please enter a username.")


titleLabel = ctk.CTkLabel(app, text="Select the stats you want to see:")
titleLabel.grid(column=0, row=0, padx=10, pady=10)

usernameEntry = ctk.CTkEntry(app)
usernameEntry.grid(column=0, row=1, padx=10, pady=10)

startStatFind = ctk.CTkButton(app, text='Find Stats', command=getStats)
startStatFind.grid(column=0, row=2,padx=10, pady=10)

usernameCheckBox = ctk.CTkCheckBox(app, text='Username', variable=usernameCheckBoxVar)
usernameCheckBox.grid(column=1, row=1, padx=10, pady=10)

rankCheckBox = ctk.CTkCheckBox(app, text='Rank', variable=rankCheckBoxVar)
rankCheckBox.grid(column=1, row=2, padx=10, pady=10)

playsCheckBox = ctk.CTkCheckBox(app, text='Play Count', variable=playsCheckBoxVar)
playsCheckBox.grid(column=1, row=3, padx=10, pady=10)

accuracyCheckBox = ctk.CTkCheckBox(app, text='Accuracy', variable=accuracyCheckBoxVar)
accuracyCheckBox.grid(column=1, row=4, padx=10, pady=10)

ppCheckBox = ctk.CTkCheckBox(app, text='pp', variable=ppCheckBoxVar)
ppCheckBox.grid(column=1, row=5, padx=10, pady=10)

if __name__ == '__main__':
    app.mainloop()