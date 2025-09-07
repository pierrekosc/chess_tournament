from typing import List, Set, Tuple
from models.player_model import Player

def _pair_key(p1: Player, p2: Player) -> Tuple[str, str]:
    return tuple(sorted([p1.national_id, p2.national_id]))

def available_pairs(players: List[Player],
                    already_played: Set[Tuple[str, str]]) -> List[Tuple[Player, Player]]:
    pairs: List[Tuple[Player, Player]] = []
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            p1 = players[i]; p2 = players[j]
            if _pair_key(p1, p2) not in already_played:
                pairs.append((p1, p2))
    return pairs