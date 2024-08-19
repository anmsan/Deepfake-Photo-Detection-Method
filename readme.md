# Deepfake Photo Detection Method

## Introduction

The **Deepfake Photo Detection Method** project provides a simple yet effective technique to embed and verify hidden RGB codes within images. This method is designed to help detect manipulated content by ensuring that the authenticity of images can be verified in real-time.

## Features

- **Embed RGB Code**: Hide an RGB code within an image’s pixel data, making it imperceptible to the human eye.
- **Verify RGB Code**: Extract and verify the embedded RGB code to confirm the image's authenticity.
- **Non-Invasive**: The method does not alter the visual quality of the image, ensuring that the original content remains unchanged.
- **Lightweight and Efficient**: Simple, fast, and efficient, making it suitable for real-time applications.

## How It Differs from Existing Techniques

This method stands out from existing techniques due to its simplicity, non-invasive nature, and potential for real-time verification. Unlike complex machine learning models that require extensive computational power, this method uses straightforward bitwise operations, making it lightweight and easy to implement.

## Future Implications

Looking ahead, this method could be integrated into digital cameras, smartphones, and social media platforms to ensure that every image is processed with an embedded code, allowing users to verify authenticity instantly. This approach would provide a robust defense against the growing threat of deepfakes.

## Project Structure

- `embed_rgb_code.py`: The script to embed an RGB code into an image.
- `verify_rgb_code.py`: The script to verify the embedded RGB code.
- `images/`: Folder containing example images.

## Usage

### Embedding an RGB Code

```bash
python embed_rgb_code.py
