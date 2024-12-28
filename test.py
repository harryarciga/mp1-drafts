from mp1 import (
    separate_moves,
    step_shift_eggs_with_rules,
    tilt_grid,
    apply_move
)

def test_separate_moves():
    assert separate_moves('ZZZZZF') == ['f']
    assert separate_moves('') == []
    assert separate_moves('abcdefghijklmnopqrstuvwxyz') == ['b', 'f', 'l', 'r']
    assert separate_moves(1) == []
    assert separate_moves(' ') == []
    assert separate_moves('i am testing my input') == []
    assert separate_moves('i love cs 11 so much') == ['l']
    assert separate_moves('09176151201') == []
    assert separate_moves('us2 ko na magpasko yeah') == []
    assert separate_moves('lLfFrRbB') == ['l', 'l', 'f', 'f', 'r', 'r', 'b', 'b']

def test_step_shift_with_eggs_with_rules():
    assert step_shift_eggs_with_rules('🟩🥚🟩', 0, 'left') == ('🥚🟩🟩', True, 0)
    assert step_shift_eggs_with_rules('🟩🥚🟩', 0, 'right') == ('🟩🟩🥚', True, 0)
    assert step_shift_eggs_with_rules('🍳🥚🟩', 0, 'left') == ('🍳🟩🟩', True, -5)
    assert step_shift_eggs_with_rules('🟩🥚🍳', 0, 'right') == ('🟩🟩🍳', True, -5)
    assert step_shift_eggs_with_rules('🪹🥚🟩', 0, 'left') == ('🪺🟩🟩', True, 10)
    assert step_shift_eggs_with_rules('🟩🥚🪹', 0, 'right') == ('🟩🟩🪺', True, 10)
    assert step_shift_eggs_with_rules('🪺🥚🟩', 0, 'left') == ('🪺🥚🟩', False, 0)
    assert step_shift_eggs_with_rules('🟩🥚🪺', 0, 'right') == ('🟩🥚🪺', False, 0)
    assert step_shift_eggs_with_rules('🥚🥚🟩', 0, 'left') == ('🥚🥚🟩', False, 0)
    assert step_shift_eggs_with_rules('🟩🥚🥚', 0, 'right') == ('🟩🥚🥚', False, 0)
    assert step_shift_eggs_with_rules('🟩🥚🥚🟩', 0, 'left') == ('🥚🥚🟩🟩', True, 0)
    assert step_shift_eggs_with_rules('🟩🥚🥚🟩', 0, 'right') == ('🟩🟩🥚🥚', True, 0)
    assert step_shift_eggs_with_rules('🪹🥚🥚🟩', 0, 'left') == ('🪺🥚🟩🟩', True, 10)
    assert step_shift_eggs_with_rules('🟩🥚🥚🪹', 0, 'right') == ('🟩🟩🥚🪺', True, 10)
    assert step_shift_eggs_with_rules('🪺🥚🥚🟩', 0, 'left') == ('🪺🥚🥚🟩', False, 0)
    assert step_shift_eggs_with_rules('🟩🥚🥚🪺', 0, 'right') == ('🟩🥚🥚🪺', False, 0)
    assert step_shift_eggs_with_rules('🍳🥚🥚🟩', 0, 'left') == ('🍳🥚🟩🟩', True, -5)
    assert step_shift_eggs_with_rules('🟩🥚🥚🍳', 0, 'right') == ('🟩🟩🥚🍳', True, -5)
    assert step_shift_eggs_with_rules('', 0, 'left') == ('', False, 0)
    assert step_shift_eggs_with_rules('', 0, 'right') == ('', False, 0)

def test_tilt_grid():
    assert tilt_grid([['🟩'], ['🟩'], ['🥚'],], 0, -1, 0) == ([['🥚'], ['🟩'], ['🟩']], 0)
    assert tilt_grid([['🪹'], ['🟩'], ['🥚'],], 0, -1, 0) == ([['🪺'], ['🟩'], ['🟩']], 10)
    assert tilt_grid([['🍳'], ['🟩'], ['🥚'],], 0, -1, 0) == ([['🍳'], ['🟩'], ['🟩']], -5)
    assert tilt_grid([['🥚'], ['🟩'], ['🥚'],], 0, -1, 0) == ([['🥚'], ['🥚'], ['🟩']], 0)
    assert tilt_grid([['🪺'], ['🟩'], ['🥚'],], 0, -1, 0) == ([['🪺'], ['🥚'], ['🟩']], 0)
    assert tilt_grid([['🥚'], ['🟩'], ['🟩'],], 0, 1, 0) == ([['🟩'], ['🟩'], ['🥚']], 0)
    assert tilt_grid([['🥚'], ['🟩'], ['🪹'],], 0, 1, 0) == ([['🟩'], ['🟩'], ['🪺']], 10)
    assert tilt_grid([['🥚'], ['🟩'], ['🍳'],], 0, 1, 0) == ([['🟩'], ['🟩'], ['🍳'], ], -5)
    assert tilt_grid([['🥚'], ['🟩'], ['🥚'],], 0, 1, 0) == ([['🟩'], ['🥚'], ['🥚']], 0)
    assert tilt_grid([['🥚'], ['🟩'], ['🪺'],], 0, 1, 0) == ([['🟩'], ['🥚'], ['🪺']], 0)
    assert tilt_grid([['🟩', '🟩', '🥚']], 0, 0, -1) == ([['🥚', '🟩', '🟩']], 0)
    assert tilt_grid([['🪹', '🟩', '🥚']], 0, 0, -1) == ([['🪺', '🟩', '🟩']], 10)
    assert tilt_grid([['🍳', '🟩', '🥚']], 0, 0, -1) == ([['🍳', '🟩', '🟩']], -5)
    assert tilt_grid([['🥚', '🟩', '🥚']], 0, 0, -1) == ([['🥚', '🥚', '🟩']], 0)
    assert tilt_grid([['🪺', '🟩', '🥚']], 0, 0, -1) == ([['🪺', '🥚', '🟩']], 0)
    assert tilt_grid([['🥚', '🟩', '🟩']], 0, 0, 1) == ([['🟩', '🟩', '🥚']], 0)
    assert tilt_grid([['🥚', '🟩', '🪹']], 0, 0, 1) == ([['🟩', '🟩', '🪺']], 10)
    assert tilt_grid([['🥚', '🟩', '🍳']], 0, 0, 1) == ([['🟩', '🟩', '🍳']], -5)
    assert tilt_grid([['🥚', '🟩', '🥚']], 0, 0, 1) == ([['🟩', '🥚', '🥚']], 0)
    assert tilt_grid([['🥚', '🟩', '🪺']], 0, 0, 1) == ([['🟩', '🥚', '🪺']], 0)

def test_apply_move():
    assert apply_move([['🟩', '🟩', '🥚']], 'l', 0) == ([['🥚', '🟩', '🟩']], 0)
    assert apply_move([['🪹', '🟩', '🥚']], 'l', 0) == ([['🪺', '🟩', '🟩']], 10)
    assert apply_move([['🍳', '🟩', '🥚']], 'l', 0) == ([['🍳', '🟩', '🟩']], -5)
    assert apply_move([['🥚', '🟩', '🥚']], 'l', 0) == ([['🥚', '🥚', '🟩']], 0)
    assert apply_move([['🪺', '🟩', '🥚']], 'l', 0) == ([['🪺', '🥚', '🟩']], 0)
    assert apply_move([['🥚', '🟩', '🟩']], 'r', 0) == ([['🟩', '🟩', '🥚']], 0)
    assert apply_move([['🥚', '🟩', '🪹']], 'r', 0) == ([['🟩', '🟩', '🪺']], 10)
    assert apply_move([['🥚', '🟩', '🍳']], 'r', 0) == ([['🟩', '🟩', '🍳']], -5)
    assert apply_move([['🥚', '🟩', '🥚']], 'r', 0) == ([['🟩', '🥚', '🥚']], 0)
    assert apply_move([['🥚', '🟩', '🪺']], 'r', 0) == ([['🟩', '🥚', '🪺']], 0)
