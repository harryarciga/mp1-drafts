from dataclasses import dataclass

@dataclass
class Moves:
    LEFTWARD: str = 'l'
    RIGHTWARD: str = 'r'
    FORWARD: str = 'f' 
    BACKWARD: str = 'b' 

class Board:
	WALL: str = '🧱'
	GRASS: str = '🟩' 
	PAN: str = '🍳'
	EGG: str = '🥚'
	EMPTYNEST: str = '🪹'
	FULLNEST: str = '🪺'
