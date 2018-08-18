
import numpy as np

def simulate_single_battle(n_attackers=3, n_defenders=2, modifiers={'attack1':0, 'attack2':0, 'defense1':0, 'defense2':0}):
    """
    Return the result of a single simulated battle in Risk Legacy. 

    Args:
        n_attackers (int): The number of attacking troops (determines number of dice rolled).
        n_defenders (int): The number of defending troops (determines number of dice rolled).
        modifiers (dict of str: int): The modifiers to be applied to each die roll. Attack1 refers to the highest 
                                      die roll of the attacker while Attack2 is the second-highest. The same ordering 
                                      applies to the Defense1 and Defense2 keys in the modifier dict. 

    Returns:
        (int, int): A tuple containing the number of attacking troops remaining and defending troops remaining.
    """
    attackers_killed = 0
    defenders_killed = 0
    
    attack_roll  = np.random.randint(1, 7, size=min(n_attackers, 3))
    defense_roll = np.random.randint(1, 7, size=min(n_defenders, 2))

    # Sorting rolls allows us to easily find highest and second-highest rolls.
    attack_roll.sort()
    defense_roll.sort()
    
    # Need to apply modifiers to die rolls while keeping the max roll value at 6.
    modified_attack_roll1  = np.minimum((attack_roll[-1] + modifiers['attack1']), 6)
    modified_defense_roll1 = np.minimum((defense_roll[-1] + modifiers['defense1']), 6)
    
    # Compare the highest roll of the attacker and defender. Defender wins ties.
    if modified_attack_roll1 > modified_defense_roll1:
        defenders_killed += 1
    else:
        attackers_killed += 1
        
    # Compare 2nd highest die rolls if both attacker and defender used more than one die.
    if n_attackers > 1 and n_defenders > 1:
        # Only need to modify second highest rolls if we have at least 2 attacking and defending units.
        modified_attack_roll2 = np.minimum((attack_roll[-2] + modifiers['attack2']), 6)
        modified_defense_roll2 = np.minimum((defense_roll[-2] + modifiers['defense2']), 6)
        
        if modified_attack_roll2 > modified_defense_roll2:
            defenders_killed += 1
        else:
            attackers_killed += 1
        
    n_attackers_remaining = n_attackers - attackers_killed
    n_defenders_remaining = n_defenders - defenders_killed
        
    return n_attackers_remaining, n_defenders_remaining

def simulate_n_battles(n_attackers, n_defenders, modifiers={'attack1':0, 'attack2':0, 'defense1':0, 'defense2':0}, n_sims=10**4):
    """
    Simulate a battle until either all attackers or defenders have been killed.  Repeat this process n_simulations number of times.

    Args:
        n_attackers (int): The number of attacking troops at the beginning of the battle.
        n_defenders (int): The number of defending troops at the beginning of the battle.
        modifiers (dict of str: int): The modifiers to be applied to each die roll. Attack1 refers to the highest 
                                      die roll of the attacker while Attack2 is the second-highest. The same ordering 
                                      applies to the Defense1 and Defense2 keys in the modifier dict. 

    Returns:
        dict(str, int): A tuple containing the number of victories for the attacker and defender for n_sims number of simulations.
    """
    wins = {'attacker':0, 'defender':0}
    
    for _ in range(n_sims):
        n_attack = n_attackers
        n_defend = n_defenders
        
        while n_attack > 0 and n_defend > 0:
            n_attack, n_defend = simulate_single_battle(n_attack, n_defend, modifiers)

        if n_attack > 0:
            wins['attacker'] += 1
        else:
            wins['defender'] += 1
    
    return wins