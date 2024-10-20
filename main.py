import cv2
from pyzbar.pyzbar import decode

# Function to scan barcode from an image or camera
def scan_barcode(image):
    # Decode the barcode in the image
    barcodes = decode(image)
    
    for barcode in barcodes:
        # Extract the barcode data as a string
        barcode_data = barcode.data.decode("utf-8")
        return barcode_data

    return None

# Capture video from the default camera (0)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture image")
        break

    # Scan the barcode from the current frame
    barcode_number = scan_barcode(frame)

    if barcode_number:
        print(f"Barcode detected: {barcode_number}")
        break  # Exit the loop when a barcode is detected

    # Display the frame (optional, you can remove this line if not needed)
    cv2.imshow("Barcode Scanner", frame)

    # Exit if 'q' is pressed (manual exit option)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
