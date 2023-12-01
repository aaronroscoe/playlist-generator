import pandas as pd

# Define the funtion search_song_list, opens the playlist spreadsheet and searches based on 2 inputs
def search_song_list(decade, genre):
    df = pd.read_csv('playlistsongs.csv', sep=',')

    # Filter rows based on user inputs for decade and genre
    filtered_df = df[(df['decade'] == decade) & (df['genre'] == genre)]

    # Choose at random 8 rows from the filtered DataFrame
    selected_rows = filtered_df.sample(8)['artist and title']

    return selected_rows.to_list()

# Define the funtion search_song_colour, opens the playlist spreadsheet and searches based on colour input
def search_song_colour(colour):
    df = pd.read_csv('playlistsongs.csv', sep=',')
    # Filter rows based on user inputs for colour
    filtered_df = df[(df['colour'] == colour)]
    # Choose 1 row at random from the filtered DataFrame
    selected_rows = filtered_df.sample(1)['artist and title']
    return selected_rows.to_list()

# Define the funtion search_song_weather, opens the playlist spreadsheet and searches based on weather input
def search_song_weather(weather):
    df = pd.read_csv('playlistsongs.csv', sep=',')
    # Filter rows based on user inputs for weather
    filtered_df = df[(df['weather'] == weather)]
    # Choose 1 row at random from the filtered DataFrame
    selected_rows = filtered_df.sample(1)['artist and title']
    return selected_rows.to_list()

# Inputs from user for playlist selection
print("Welcome to the random playlist generator. \nAnswer these questions, and I will build a playlist for you!")

user_input_name = str(input("What is your name: "))
user_input_decade = int(input("\nWhat is your favourite decade? \n1960/1970/1980/1990/2000: "))
user_input_genre = str(input("\nWhich genre is your preferred choice? \nPop/Dance/RnB/Rock/Relaxing: ")).lower()
user_input_colour = str(input("\nWhat is your favourite colour: \nRed/Green/Yellow/Blue/Purple/Black: ")).lower()
user_input_weather = str(input("\nWhat is your favourite weather? \nSun/Rain/Wind/Storm: ")).lower()

result_one = search_song_list(user_input_decade, user_input_genre)
result_colour = search_song_colour(user_input_colour)
result_weather = search_song_weather(user_input_weather)

print(f"Thanks {user_input_name.title()}... here's some songs I suggest:")
print(f"1. {result_one[0]}")
print(f"2. {result_one[1]}")
print(f"3. {result_one[2]}")
print(f"4. {result_one[3]}")
print(f"5. {result_one[4]}")
print(f"6. {result_one[5]}")
print(f"7. {result_one[6]}")
print(f"8. {result_one[7]}")
print(f"9. {result_colour[0].title()}")
print(f"10. {result_weather[0].title()}")
