import os
import time
import argparse
import requests

URL_SCORES_NOW = "https://api-web.nhle.com/v1/score/now"

COLOR_RESET = '\033[0m'
COLOR_WINNER = '\033[92m'
COLOR_LOSER = '\033[31m'
COLOR_FINAL_SCORE = '\033[32m'
COLOR_ERROR = '\033[91m'

def get_scores():
    try:
        response = requests.get(URL_SCORES_NOW, timeout=20)
        response.raise_for_status() # if response not 200
        scores = response.json()

        if "games" not in scores:
            print(f"{COLOR_ERROR}Error: Unexpected data format.{COLOR_RESET}")
            return {}
        return scores

    except requests.exceptions.RequestException as long_error:
        short_error = str(long_error).split(':')[-1].strip()
        print(f"{COLOR_ERROR}Network error: {short_error}{COLOR_RESET}")
        return {}

def show_scores(scores):
    if len(scores) == 0: return

    print(f"\nNHL Live Scores ({scores.get("currentDate")})\n")
    print(f"{'Away  ':>18}{'Score':6} {'Home':<16} {'Time':<5} {'Period':<8} {'State'}")
    print("-"*62)

    for game in scores["games"]:
        game_state = game.get("gameState", "Unknown")
        away_team = game.get("awayTeam", {}).get("name", {}).get("default", "Unknown")
        home_team = game.get("homeTeam", {}).get("name", {}).get("default", "Unknown")
        away_score = safe_int(game.get("awayTeam", {}).get("score", "0"))
        home_score = safe_int(game.get("homeTeam", {}).get("score", "0"))
        game_clock = game.get("clock", {}).get("timeRemaining", "00:00")
        game_period_number = game.get("periodDescriptor", {}).get("number", "0")
        game_period_type = game.get("periodDescriptor", {}).get("periodType", "N/A")

        away_color = COLOR_RESET
        home_color = COLOR_RESET
        state_color = COLOR_RESET
        if game_state == 'FINAL' or game_state == 'OFF':
            state_color = COLOR_FINAL_SCORE
            if away_score > home_score:
                away_color = COLOR_WINNER
                home_color = COLOR_LOSER
            if home_score > away_score:
                home_color = COLOR_WINNER
                away_color = COLOR_LOSER

        print(f"{away_color}{away_team+' ':>17}{COLOR_RESET} {away_score:<1} - {home_score:<2} {home_color}"
              f"{home_team:<16}{COLOR_RESET} {game_clock} ({game_period_number}) {game_period_type:<3} {state_color} {game_state}{COLOR_RESET}")
    return

def safe_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return int(0)

def main():
    parser = argparse.ArgumentParser(description="Simple NHL live scores")
    parser.add_argument("--update_interval", type=int, metavar="update_interval", default=30,
                        help="Update interval (seconds) for fetching live NHL scores. Default 30s.")
    args = parser.parse_args()
    update_interval = max(args.update_interval, 1) # At least 1 second between updates

    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            show_scores(get_scores())
            time.sleep(update_interval)
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == '__main__':
    main()