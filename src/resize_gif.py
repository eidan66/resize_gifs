import os
from PIL import Image, ImageSequence
import requests
from io import BytesIO

def download_gif(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        img = Image.open(BytesIO(response.content))
        return img
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return None
    except Exception as e:
        print(f"Failed to process GIF from {url}: {e}")
        return None

def resize_gif(img, output_path, target_size=(180, 180)):
    try:
        frames = []
        durations = []
        
        # Resize each frame and store the duration
        for frame in ImageSequence.Iterator(img):
            resized_frame = frame.resize(target_size, Image.NEAREST)
            frames.append(resized_frame)
            durations.append(frame.info['duration'])

        # Save all frames to a new GIF
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=0,
            duration=durations,
            disposal=2
        )
        print(f"Resized and saved: {output_path}")
    except Exception as e:
        print(f"Failed to resize and save GIF: {e}")

def process_gifs_from_urls(urls_file, resized_directory="resized_gifs", target_size=(180, 180)):
    if not os.path.exists(resized_directory):
        os.makedirs(resized_directory)

    with open(urls_file, "r") as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        if url:
            file_name = url.split("/")[-1].split("?")[0]
            
            # Download the GIF
            img = download_gif(url)
            
            if img:
                # Resize and save the GIF
                resized_path = os.path.join(resized_directory, file_name)
                resize_gif(img, resized_path, target_size)

if __name__ == "__main__":
    urls_file = os.path.join(os.path.dirname(__file__), "urls.txt")
    process_gifs_from_urls(urls_file)