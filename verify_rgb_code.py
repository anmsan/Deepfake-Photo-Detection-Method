import cv2

def verify_rgb_code(image_path, expected_rgb_code):
    # Load the image
    image = cv2.imread(image_path)
    
    binary_code = ''
    
    rows, cols, _ = image.shape
    for row in range(rows):
        for col in range(cols):
            pixel = image[row, col]
            for channel in range(3):  # For R, G, B channels
                binary_code += str(pixel[channel] & 1)
    
    # Convert binary code back to RGB
    extracted_rgb_code = (
        int(binary_code[:8], 2),
        int(binary_code[8:16], 2),
        int(binary_code[16:24], 2)
    )
    
    return extracted_rgb_code == expected_rgb_code

# Example usage
image_path = r'images/embedded_image.png'
expected_rgb_code = (123, 45, 67)

if verify_rgb_code(image_path, expected_rgb_code):
    print("The RGB code matches!")
else:
    print("The RGB code does not match.")
 
