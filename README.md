# Air Canvas — Hand Movement Detection

![Air Canvas banner](assets/banner.png)

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hands-00897B)](https://developers.google.com/mediapipe)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Draw in the air and watch your fingertip leave a glowing trail — tracked live
from your webcam, no special markers or gloves required. Air Canvas uses
Google's MediaPipe Hands to find your index finger in real time and renders
its motion as a fading light trail, turning your hand into a paintbrush.

## How it works

```
webcam frame → MediaPipe Hands (landmark detection) → index fingertip (x, y)
            → trail buffer (last 64 points) → tapering line trail drawn on frame
```

The original 2018 version of this project tracked a colored object via HSV
color thresholding — it needed a brightly colored marker and broke under
different lighting. This rebuild replaces that with MediaPipe Hands: real
hand-landmark detection that works on a bare hand, in varied lighting,
without any marker at all.

## Quickstart

```bash
git clone https://github.com/mauryasameer/hand_movement_detection.git
cd hand_movement_detection
pip install -r requirements.txt
```

**Run it:**

```bash
python run.py
```

A window opens showing your webcam feed. Hold your hand up so MediaPipe can
see it, move your index finger around, and watch the trail follow it. Press
the space bar to quit — the camera is released automatically.

## Project structure

```
hand_tracking/   # detector (MediaPipe Hands wrapper) + trail buffer/renderer
run.py           # local webcam app — wires detector + trail together
tests/           # pytest suite for the trail buffer (pure logic, no camera needed)
legacy/          # the original 2018 HSV-color-tracking script, kept for history
```

## Tech stack

Python · OpenCV · MediaPipe · NumPy · pytest

## License

[MIT](LICENSE)
