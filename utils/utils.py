def get_input(year, day):
    import requests
    import os
    from dotenv import load_dotenv

    load_dotenv()

    URL = f"https://adventofcode.com/{year}/day/{day}/input"

    res = requests.get(
        URL,
        cookies={'session': os.getenv('SESSION_ID')},
        headers={'User-Agent': 'https://github.com/LeanneStoDomingo/advent-of-code'}
    )

    return res.text
