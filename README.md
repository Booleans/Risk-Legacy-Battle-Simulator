#  Battle Simulator for Risk Legacy

### Purpose

This code was written to give myself an advantage when playing against my friends in the board game [Risk Legacy](https://boardgamegeek.com/boardgame/105134/risk-legacy).

Unlike the standard version of the game Risk, battles in Risk Legacy often have modifiers applied to die rolls. A few examples of modifiers include:

* Bunker: Add 1 to the defender's highest die
* Ammo Shortage: Subtract 1 from the defender's highest die
* Die Mechaniker: Add 1 to both dice when defending your HQ as the Die Mechaniker faction

In each game there comes a point where you think "I can win right now if I manage to capture my friend's headquarters". However, it's near-impossible to do the math in your head and make a judgement about how likely you are to succeed and whether you're willing to accept the risk.  

So how do you calculate probability without doing the math? Simulation!

My code allows the simulation of battles along a path given an initial number of starting troops along with the number of defenders and types of modifiers applied to each territory you want to attack.
