import cv2
import sys
import os
import numpy as np

BLUR_LOW = 20
BLUR_MED = 50
BLUR_HIGH = 100

IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.tif', '.webp'}

def adjust_gamma(image, gamma=1.0):
	# from: https://www.pyimagesearch.com/2015/10/05/opencv-gamma-correction/
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	return cv2.LUT(image, table)

def blur_image(image_filename, output_filename, blur_level=BLUR_MED):
    img = cv2.imread(image_filename)
    if img is None:
        print(f"Warning: Could not read {image_filename}, skipping.")
        return False

    blur = cv2.GaussianBlur(img, (blur_level + 1, 0), sigmaX=blur_level, sigmaY=blur_level)
    blur = cv2.GaussianBlur(blur, (0, blur_level + 1), sigmaX=blur_level, sigmaY=blur_level)
    blur = adjust_gamma(blur, 1.5)

    cv2.imwrite(output_filename, blur)
    return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 blur.py <image_file> <output_file>")
        print("       python3 blur.py <directory>")
        exit(1)

    path = sys.argv[1]

    if os.path.isdir(path):
        output_dir = os.path.join(path, "blurred")
        os.makedirs(output_dir, exist_ok=True)

        count = 0
        for filename in sorted(os.listdir(path)):
            ext = os.path.splitext(filename)[1].lower()
            if ext in IMAGE_EXTENSIONS:
                input_path = os.path.join(path, filename)
                output_path = os.path.join(output_dir, filename)
                if blur_image(input_path, output_path):
                    print(f"Blurred: {filename}")
                    count += 1

        print(f"Done. {count} image(s) saved to {output_dir}")
    else:
        if len(sys.argv) != 3:
            print("Usage: python3 blur.py <image_file> <output_file>")
            exit(1)

        image_filename = sys.argv[1]
        output_filename = sys.argv[2]
        blur_image(image_filename, output_filename)