from __future__ import annotations

from collections import deque

import cv2
import numpy as np

TRAIL_COLOR = (0, 0, 225)


class Trail:
    """Fixed-length buffer of fingertip points, drawn as a tapering line trail.

    A `None` entry marks a gap (e.g. the hand wasn't detected in that frame)
    and breaks the line so the trail doesn't jump across it.
    """

    def __init__(self, max_length: int = 64):
        self._points = deque(maxlen=max_length)

    @property
    def points(self) -> list:
        return list(self._points)

    def add(self, point: tuple[int, int] | None) -> None:
        self._points.appendleft(point)

    def draw(self, frame: np.ndarray) -> None:
        points = self.points
        for i in range(1, len(points)):
            if points[i - 1] is None or points[i] is None:
                continue
            thickness = int(np.sqrt(len(points) / float(i + 1)) * 2.5)
            cv2.line(frame, points[i - 1], points[i], TRAIL_COLOR, thickness)
