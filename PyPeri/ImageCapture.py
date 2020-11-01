from cv2 import VideoCapture, imshow, cvtColor, \
    COLOR_BGR2GRAY, waitKey, destroyAllWindows, \
    imwrite

from uuid import uuid4
from os.path import join
from pathlib import Path
Path("./dataset/persons").mkdir(parents=True, exist_ok=True)


class GetImage:

    def __init__(self):
        self.camera = VideoCapture(0)
        self.frame = None
        self.uuid = None

    def get_frame(self):

        # Get frame for video capture
        while True:
            # Capture frame-by-frame
            ret, frame = self.camera.read()

            # Our operations on the frame come here
            gray = cvtColor(frame, COLOR_BGR2GRAY)

            # Display the resulting frame
            imshow('Image Capture (Press C)', gray)
            if waitKey(1) & 0xFF == ord('c'):
                break
        self.camera.release()
        destroyAllWindows()
        self.frame = frame

    def save_image(self):
        # Write frame to file
        self.uuid = f'{str(uuid4())}.jpg'
        path = 'dataset/persons'
        imwrite(join(path, self.uuid), self.frame)

    def capture(self):
        self.get_frame()
        self.save_image()
        return self.uuid


if __name__ == '__main__':
    image = GetImage()
    image.capture()
