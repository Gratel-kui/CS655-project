import replicate
from clip_api import ClipApi


API_TOKEN = "4de28bff579af30f33ff52a1bc2c2135b2d94a8d"
client = replicate.Client(api_token=API_TOKEN)


def imageToText(path):
    image_paths = ["./images/Kodak/kodim01.png"]

    clip = ClipApi(client=client)
    captions = clip.get_caption_list(image_paths)

    print(captions)
    return captions[0]


if __name__ == '__main__':
    imageToText()