from PIL import Image
import random

# Function to encrypt the image
def encrypt_image(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    # Convert the key to a random seed
    random.seed(key)

    # Encrypt the pixels
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Generate random offsets
            r_offset = random.randint(0, 255)
            g_offset = random.randint(0, 255)
            b_offset = random.randint(0, 255)

            # Apply encryption
            pixels[i, j] = ((r + r_offset) % 256, (g + g_offset) % 256, (b + b_offset) % 256)

    # Save the encrypted image
    img.save(output_path)

# Function to decrypt the image
def decrypt_image(encrypted_path, output_path, key):
    # Open the encrypted image
    img = Image.open(encrypted_path)
    pixels = img.load()
    width, height = img.size

    # Convert the key to a random seed
    random.seed(key)

    # Decrypt the pixels
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Generate random offsets
            r_offset = random.randint(0, 255)
            g_offset = random.randint(0, 255)
            b_offset = random.randint(0, 255)

            # Apply decryption
            pixels[i, j] = ((r - r_offset) % 256, (g - g_offset) % 256, (b - b_offset) % 256)

    # Save the decrypted image
    img.save(output_path)

# Paths
input_image = r"C:\Users\rawse\OneDrive\Desktop\pm\pixelManipulation\tk.jpg"  # Input image file
encrypted_image = r"C:\Users\rawse\OneDrive\Desktop\pm\pixelManipulation\encrypted_tk.jpg"  # Output encrypted image
decrypted_image = r"C:\Users\rawse\OneDrive\Desktop\pm\pixelManipulation\decrypted_tk.jpg"  # Output decrypted image

# Encryption key
key = 12345  # You can set any key you prefer

# Encrypt the image
encrypt_image(input_image, encrypted_image, key)
print("Image encrypted successfully!")

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key)
print("Image decrypted successfully!")
