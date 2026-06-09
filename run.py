import cv2

from hand_tracking.detector import create_detector, find_fingertip
from hand_tracking.trail import Trail

QUIT_KEY = 32  # space bar


def main() -> None:
    capture = cv2.VideoCapture(0)
    detector = create_detector()
    trail = Trail()

    try:
        while True:
            read_ok, frame = capture.read()
            if not read_ok:
                break

            fingertip = find_fingertip(detector, frame)
            trail.add(fingertip)
            trail.draw(frame)

            if fingertip is not None:
                cv2.circle(frame, fingertip, 6, (0, 255, 255), -1)

            cv2.imshow("Air Canvas", frame)
            if cv2.waitKey(30) & 0xFF == QUIT_KEY:
                break
    finally:
        capture.release()
        detector.close()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
