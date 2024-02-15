from tkinter import *
from PIL import Image, ImageTk
import requests
import statsapi
from io import BytesIO

# ---------------------------- CONSTANTS ------------------------------- #
# BASE_URL = "https://statsapi.mlb.com/api/"
WHITE = "#ffffff"
BLACK = "#000000"
FONT_LARGE = ("Arial", 24)
FONT_SMALL = ("Arial", 12)

# ------------ Player ID's ------------ #
x_id = 542897
acuna_id = 660670
player_id = x_id

# Headshot --- change id for other players
headshot_url = f"https://img.mlbstatic.com/mlb-photos/image/upload/w_248,q_100/v1/people/{player_id}/headshot/83/current"
response = requests.get(headshot_url)

stats = statsapi.player_stat_data(personId=player_id, group='hitting', type="career")
player_name = stats["first_name"] + " " + stats["last_name"]
# ---------------------------- FUNCTIONS ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(f"{player_name}'s Baseball Card")
window.config(padx=20, pady=20, background=WHITE)

# Create a Canvas widget
if response.status_code == 200:
    image_data = response.content

    # Convert image data to PhotoImage
    image = Image.open(BytesIO(image_data))
    photo = ImageTk.PhotoImage(image)
    canvas = Canvas(window, width=photo.width(), height=photo.height(), bg=WHITE, highlightthickness=0)

    # Display the image on the Canvas
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.grid(column=0, row=0)

# ---------------------------- BIO Labels ---------------------------- #
player_name = stats["first_name"] + " " + stats["last_name"]
player_name_lb = Label(text=player_name, bg=WHITE, fg=BLACK)
player_name_lb.grid(column=1, row=0, columnspan=3)

position = stats["position"]
position_lb = Label(text=position, bg=WHITE, fg=BLACK)
position_lb.grid(column=4, row=0)

bat_side = stats["bat_side"]
bat_side_lb = Label(text=bat_side, bg=WHITE, fg=BLACK)
bat_side_lb.grid(column=5, row=0)

pitch_hand = stats["pitch_hand"]
pitch_hand_lb = Label(text=pitch_hand, bg=WHITE, fg=BLACK)
pitch_hand_lb.grid(column=6, row=0)

mlb_debut = stats["mlb_debut"]
mlb_debut_lb = Label(text=mlb_debut, bg=WHITE, fg=BLACK)
mlb_debut_lb.grid(column=7, row=0, columnspan=3)

# ---------------------------- Career Labels ---------------------------- #
career_lb = Label(text="Career", bg=WHITE, fg=BLACK)
career_lb.grid(column=0, row=2)

games = stats["stats"][0]["stats"]["gamesPlayed"]
games_lb = Label(text="G", bg=WHITE, fg=BLACK)
games_lb.grid(column=1, row=1)
games_stats_lb = Label(text=f"{games}", bg=WHITE, fg=BLACK)
games_stats_lb.grid(column=1, row=2)

pa = stats["stats"][0]["stats"]["plateAppearances"]
pa_lb = Label(text="PA", bg=WHITE, fg=BLACK)
pa_lb.grid(column=2, row=1)
pa_stat_lb = Label(text=f"{pa}", bg=WHITE, fg=BLACK)
pa_stat_lb.grid(column=2, row=2)

at_bats = stats["stats"][0]["stats"]["atBats"]
at_bats_lb = Label(text="AB", bg=WHITE, fg=BLACK)
at_bats_lb.grid(column=3, row=1)
at_bats_stat_lb = Label(text=f"{at_bats}", bg=WHITE, fg=BLACK)
at_bats_stat_lb.grid(column=3, row=2)

runs = stats["stats"][0]["stats"]["runs"]
runs_lb = Label(text="R", bg=WHITE, fg=BLACK)
runs_lb.grid(column=4, row=1)
runs_stat_lb = Label(text=f"{runs}", bg=WHITE, fg=BLACK)
runs_stat_lb.grid(column=4, row=2)

hits = stats["stats"][0]["stats"]["hits"]
hits_lb = Label(text="H", bg=WHITE, fg=BLACK)
hits_lb.grid(column=5, row=1)
hits_stat_lb = Label(text=f"{hits}", bg=WHITE, fg=BLACK)
hits_stat_lb.grid(column=5, row=2)

tb = stats["stats"][0]["stats"]["totalBases"]
tb_lb = Label(text="TB", bg=WHITE, fg=BLACK)
tb_lb.grid(column=6, row=1)
tb_stat_lb = Label(text=f"{tb}", bg=WHITE, fg=BLACK)
tb_stat_lb.grid(column=6, row=2)

doubles = stats["stats"][0]["stats"]["doubles"]
doubles_lb = Label(text="2B", bg=WHITE, fg=BLACK)
doubles_lb.grid(column=7, row=1)
doubles_stat_lb = Label(text=f"{doubles}", bg=WHITE, fg=BLACK)
doubles_stat_lb.grid(column=7, row=2)

triples = stats["stats"][0]["stats"]["triples"]
triples_lb = Label(text="3B", bg=WHITE, fg=BLACK)
triples_lb.grid(column=8, row=1)
triples_stat_lb = Label(text=f"{triples}", bg=WHITE, fg=BLACK)
triples_stat_lb.grid(column=8, row=2)

hr = stats["stats"][0]["stats"]["homeRuns"]
hr_lb = Label(text="HR", bg=WHITE, fg=BLACK)
hr_lb.grid(column=9, row=1)
hr_stat_lb = Label(text=f"{hr}", bg=WHITE, fg=BLACK)
hr_stat_lb.grid(column=9, row=2)

rbi = stats["stats"][0]["stats"]["rbi"]
rbi_lb = Label(text="RBI", bg=WHITE, fg=BLACK)
rbi_lb.grid(column=10, row=1)
rbi_stat_lb = Label(text=f"{rbi}", bg=WHITE, fg=BLACK)
rbi_stat_lb.grid(column=10, row=2)

bb = stats["stats"][0]["stats"]["baseOnBalls"]
bb_lb = Label(text="BB", bg=WHITE, fg=BLACK)
bb_lb.grid(column=11, row=1)
bb_stat_lb = Label(text=f"{bb}", bg=WHITE, fg=BLACK)
bb_stat_lb.grid(column=11, row=2)

so = stats["stats"][0]["stats"]["strikeOuts"]
so_lb = Label(text="SO", bg=WHITE, fg=BLACK)
so_lb.grid(column=12, row=1)
so_stat_lb = Label(text=f"{so}", bg=WHITE, fg=BLACK)
so_stat_lb.grid(column=12, row=2)

sb = stats["stats"][0]["stats"]["stolenBases"]
sb_lb = Label(text="SB", bg=WHITE, fg=BLACK)
sb_lb.grid(column=13, row=1)
sb_stat_lb = Label(text=f"{sb}", bg=WHITE, fg=BLACK)
sb_stat_lb.grid(column=13, row=2)

avg = stats["stats"][0]["stats"]["avg"]
avg_lb = Label(text="AVG", bg=WHITE, fg=BLACK)
avg_lb.grid(column=14, row=1)
avg_stat_lb = Label(text=f"{avg}", bg=WHITE, fg=BLACK)
avg_stat_lb.grid(column=14, row=2)

obp = stats["stats"][0]["stats"]["obp"]
obp_lb = Label(text="OBP", bg=WHITE, fg=BLACK)
obp_lb.grid(column=15, row=1)
obp_stat_lb = Label(text=f"{obp}", bg=WHITE, fg=BLACK)
obp_stat_lb.grid(column=15, row=2)

slg = stats["stats"][0]["stats"]["slg"]
slg_lb = Label(text="SLG", bg=WHITE, fg=BLACK)
slg_lb.grid(column=16, row=1)
slg_stat_lb = Label(text=f"{slg}", bg=WHITE, fg=BLACK)
slg_stat_lb.grid(column=16, row=2)

ops = stats["stats"][0]["stats"]["ops"]
ops_lb = Label(text="OPS", bg=WHITE, fg=BLACK)
ops_lb.grid(column=17, row=1)
ops_stat_lb = Label(text=f"{ops}", bg=WHITE, fg=BLACK)
ops_stat_lb.grid(column=17, row=2)


window.mainloop()
