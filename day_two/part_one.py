def check_games(in_games):
    criteria = {
        "red": 12,
        "blue": 14,
        "green": 13
    }

    for game in in_games:
        samples = game.split(",")
        for sample in samples:
            sample = sample.split()
            if int(sample[0]) > criteria[sample[1]]:
                return False
    return True


def task_one(path):
    f = open(path, "r")
    total = 0
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        game_id, games = line.split(":")
        game_id = game_id.split(' ')[1]

        games = games.split(";")
        if check_games(games):
            total += int(game_id)
    return total


print(task_one("input"))
