import re
import os
import base64

html_files = ["Index.html", "docs/oxohotel-amor-y-amistad.html"]
image_dir = "images"
os.makedirs(image_dir, exist_ok=True)

base_url = "https://raw.githubusercontent.com/acabrales-oxohotel/LP-images/main/images/"

for file_path in html_files:
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex to find base64 images
    pattern = r"data:image/([a-zA-Z0-9]+);base64,([a-zA-Z0-9+/=]+)"
    
    matches = list(re.finditer(pattern, content))
    print(f"Found {len(matches)} images in {file_path}")
    
    offset = 0
    new_content = ""
    last_end = 0
    
    for i, match in enumerate(matches):
        ext = match.group(1)
        if ext == "jpeg":
            ext = "jpg"
        
        img_data = match.group(2)
        img_filename = f"img_{i}.{ext}"
        img_filepath = os.path.join(image_dir, img_filename)
        
        # Save image
        with open(img_filepath, "wb") as img_file:
            img_file.write(base64.b64decode(img_data))
            
        # Replace in HTML
        new_url = base_url + img_filename
        
        new_content += content[last_end:match.start()] + new_url
        last_end = match.end()
        
    new_content += content[last_end:]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Updated {file_path}")
