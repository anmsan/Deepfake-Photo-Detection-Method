import cv2
import numpy as np

def embed_rgb_code(image_path, rgb_code, output_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the RGB code to binary format
    binary_code = ''.join(format(c, '08b') for c in rgb_code)
    
    # Get image dimensions
    rows, cols, _ = image.shape
    
    # Embed the binary code into the image
    code_index = 0
    for row in range(rows):
        for col in range(cols):
            pixel = image[row, col]
            for channel in range(3):  # For R, G, B channels
                if code_index < len(binary_code):
                    # Modify the LSB of the pixel without overflow
                    pixel[channel] = (pixel[channel] & 254) | int(binary_code[code_index])
                    code_index += 1
                else:
                    break
            image[row, col] = pixel
            if code_index >= len(binary_code):
                break
        if code_index >= len(binary_code):
            break
    
    # Save the modified image
    cv2.imwrite(output_path, image)
    print(f"RGB code embedded and saved to {output_path}")

# Example usage
image_path = r'images/original_image.png'  # Path to the input image
output_path = r'images/embedded_image.png'  # Path to save the output image
rgb_code = (123, 45, 67)  # Your unique RGB code

embed_rgb_code(image_path, rgb_code, output_path)
 
