#!/usr/bin/env python3

import cv2
import requests
import numpy as np

def stream_video():
    STREAM_URL = "http://ip_adress:5000/video_feed"

    # Create a window for displaying the video
    cv2.namedWindow("Video Stream", cv2.WINDOW_NORMAL)

    response = requests.get(STREAM_URL, stream=True)
    if response.status_code == 200:
        bytes_buffer = bytes()
        for chunk in response.iter_content(chunk_size=1024):
            bytes_buffer += chunk
            # Check for JPEG start (SOI) and end (EOI) markers
            a = bytes_buffer.find(b'\xff\xd8')
            b = bytes_buffer.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = bytes_buffer[a:b+2]
                bytes_buffer = bytes_buffer[b+2:]
                img = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                cv2.imshow("Video Stream", img)
                if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
                    break
    else:
        print(f"Unable to connect to the video stream. Status code: {response.status_code}")

    cv2.destroyAllWindows()

if __name__ == "__main__":
    stream_video()