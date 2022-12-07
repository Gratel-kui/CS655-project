import replicate


class ClipApi():

    def __init__(self, client=replicate.Client(api_token="4de28bff579af30f33ff52a1bc2c2135b2d94a8d")):
        # client = replicate.Client(api_token=API_TOKEN)
        replicate.Client = self.client = client
        self.model = client.models.get("rmokady/clip_prefix_caption")

    def get_caption(self, image_path):
        output = self.model.predict(image=open(image_path, 'rb'))
        return output

    def get_caption_list(self, image_paths):
        output_list = []
        for image_path in image_paths:
            output_list.append(self.get_caption(image_path))
        return output_list
