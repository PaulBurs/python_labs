from PIL import Image
import numpy as np
# считаем картинку в numpy array
for i in range(1, 4):
    with Image.open(f'lunar_images/lunar0{i}_raw.jpg') as img:
        data = np.array(img)
        new_data = ((data - np.min(data)) * (255 / (np.max(data) - np.min(data)))).astype(np.uint8)

        ans = Image.fromarray(new_data)
        ans.save(f'lunar_image_0{i}_update.jpg')
