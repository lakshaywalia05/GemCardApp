import os
import urllib.request

# This script downloads the internet files so your app works offline
assets_dir = os.path.join(os.getcwd(), "assets")

urls = {
    "tailwindcss.js": "https://cdn.tailwindcss.com",
    "cropper.min.css": "https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.5.13/cropper.min.css",
    "cropper.min.js": "https://cdnjs.cloudflare.com/ajax/libs/cropperjs/1.5.13/cropper.min.js",
    "qrious.min.js": "https://cdnjs.cloudflare.com/ajax/libs/qrious/4.0.2/qrious.min.js",
    "fontawesome.css": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
}

print("Downloading offline files...")
for name, url in urls.items():
    print(f"Downloading {name}...")
    try:
        urllib.request.urlretrieve(url, os.path.join(assets_dir, name))
    except Exception as e:
        print(f"Failed to download {name}: {e}")

print("Done! You can now run the main app.")