from PIL import Image, ImageEnhance, UnidentifiedImageError
def deepfry(input: str, output: str, sharpness: int = 10000000, saturation: int = 5):
  """
  **Deepfrys an image.** \n
  Params: \n
  str `input`: Location of image to be deepfried. \n
  str `output`: Location of image to be saved to. \n
  **optional** int `sharpness`: Sharpness of image. Turn up if you want your image more deepfried. \n
  **optional** int `saturation`: Sharpness of image. Turn up if you want your image more deepfried. \n
  Returns `Pillow image file (PIL.Image.Image)`.

  """
  try:
    img = Image.open(input)
  except FileNotFoundError:
    raise Exception("Image not found.")
  except UnidentifiedImageError:
    raise Exception("File is not an image.")
  img2 = ImageEnhance.Sharpness(img).enhance(sharpness)
  img3 = ImageEnhance.Color(img2).enhance(saturation)
  img3.save(output)
  return img3

