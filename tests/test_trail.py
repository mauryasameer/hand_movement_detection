import numpy as np

from hand_tracking.trail import Trail


def test_add_respects_max_length():
    trail = Trail(max_length=3)
    trail.add((1, 1))
    trail.add((2, 2))
    trail.add((3, 3))
    trail.add((4, 4))

    assert trail.points == [(4, 4), (3, 3), (2, 2)]


def test_add_preserves_none_gap_markers():
    trail = Trail(max_length=5)
    trail.add((1, 1))
    trail.add(None)
    trail.add((2, 2))

    assert trail.points == [(2, 2), None, (1, 1)]


def test_draw_renders_a_line_between_points():
    trail = Trail()
    trail.add((10, 10))
    trail.add((50, 50))
    frame = np.zeros((100, 100, 3), dtype=np.uint8)

    trail.draw(frame)

    assert frame.any()


def test_draw_does_not_crash_on_empty_or_sparse_trails():
    trail = Trail()
    trail.add((10, 10))
    trail.add(None)
    trail.add((20, 20))
    frame = np.zeros((100, 100, 3), dtype=np.uint8)

    Trail().draw(frame)
    trail.draw(frame)
