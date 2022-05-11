import os
import json
from ocr.detect import NutritionDetectionPipeline


if __name__ == '__main__':
    detect_nutrition = NutritionDetectionPipeline()
    # image_url = 'https://res.cloudinary.com/hlvl5cgpe/image/upload/v1652161903/twfonmhsw9rnfhyvdjvf.jpg'
    # result = detect_nutrition.from_url(image_url, debug=True)
    image_path = os.path.join('ocr/data/images', f'label-{5}.jpg')
    result = detect_nutrition.from_path(image_path, debug=True)
    # print(json.dumps(result))
    print(''.join([f'{k:18} {v["value"]:8} {v["unit"]:4}\n' for k, v in result.items()]))
