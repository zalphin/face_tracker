import cv2
import time
import serial

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def GetSerialCoord(img,x,y,w,h):
	height, width = img.shape[:2]
	midX = x+w / 2
	midY = y+h / 2
	serX = midX / (width / 180)
	serY = midY / (width / 180)
	print('Calculated X: {} and Y: {}'.format(serX, serY))
	return (int(serX), int(serY))

# X and y need to be 0-180
def SendSerialCoord(x,y):
	if x >= 0 and x <= 180 and y >= 0 and y <= 180:
		strX = 'X'+str(x)
		strY = 'Y'+str(y)
		print('sending {}'.format(strX+strY))
		ser.write((strX+strY).encode())
	

# Read the input image
# img = cv2.imread('test.jpg')
cap = cv2.VideoCapture(0)
# Connect to serial port (arduino)
ser = serial.Serial('COM3', 9600)

while cap.isOpened():
	_, img = cap.read()

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)

	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 3)
	
	if len(faces) > 0:
		x,y,w,h = faces[0]
		serX, serY = GetSerialCoord(img,x,y,w,h)
		SendSerialCoord(serX, serY)
		time.sleep(1)
	# Display the output
	cv2.imshow('img', img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
print('reached here')
cap.release()
ser.close()