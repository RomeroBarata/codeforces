def compute_run_lengths(players_config: str) -> dict:
    run_lengths = {player_id: [] for player_id in set(players_config)}
    last_player, count = players_config[0], 1
    for player in players_config[1:]:
        if player == last_player:
            count += 1
        else:
            run_lengths[last_player].append(count)
            last_player, count = player, 1
    run_lengths[last_player].append(count)
    return run_lengths


def is_dangerous(players_config: str) -> bool:
    run_lengths = compute_run_lengths(players_config)
    longest_run_of_zeros, longest_run_of_ones = max(run_lengths['0']), max(run_lengths['1'])
    return (longest_run_of_zeros >= 7) or (longest_run_of_ones >= 7)


def main():
    players_config = input()
    if is_dangerous(players_config):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
