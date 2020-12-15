from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import pandas as pd

# Get 2019-2020 advanced season statistics for all players
filename = "data/player_advanced_stats_2020.csv"
client.players_advanced_season_totals(season_end_year=2020,
    output_type=OutputType.CSV, output_file_path="data/player_advanced_stats_2020.csv")
client.players_season_totals(season_end_year=2020,
    output_type=OutputType.CSV, output_file_path="data/player_stats_2020.csv")

with open('data/player_advanced_stats_2020.csv') as advanced:
    with open('data/player_stats_2020.csv') as regular:
        newdata = open('data/player_combined_data_2020.csv', 'w+')
        i = 0
        reglines = regular.readlines()
        for line in advanced.readlines():
                newdata.write(line.replace('\n','') + reglines[i])
                i += 1