from __future__ import annotations

import cv2
import mediapipe as mp
import numpy as np

_HANDS = mp.solutions.hands
INDEX_FINGER_TIP = _HANDS.HandLandmark.INDEX_FINGER_TIP


def create_detector(max_num_hands: int = 1, min_detection_confidence: float = 0.7):
    """Build a MediaPipe Hands detector configured for live video."""
    return _HANDS.Hands(
        static_image_mode=False,
        max_num_hands=max_num_hands,
        min_detection_confidence=min_detection_confidence,
    )


def find_fingertip(detector, frame: np.ndarray) -> tuple[int, int] | None:
    """Return the index-fingertip's (x, y) pixel position, or None if no hand is found."""
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = detector.process(rgb)
    if not results.multi_hand_landmarks:
        return None

    landmark = results.multi_hand_landmarks[0].landmark[INDEX_FINGER_TIP]
    height, width = frame.shape[:2]
    return (int(landmark.x * width), int(landmark.y * height))
