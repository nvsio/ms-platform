import time
import picamera

with picamera.PiCamera() as camera:
  camera.resolution = (1024,768)
  camera.start_preview()
  time.sleep(20)
  camera.capture('test-capture.jpg')
  camera.close()