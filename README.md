# 2D Finite Difference For Object Edge Detection


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

## Usage
The predictObjectEdge takes 2 arguments, first one is Image Object which can be created by using PIL.Image and the second one is boundary. Experiment with the boundary value to get the best result. From my experience it's about 5-25.

```python
from image_detection import predictObjectEdge
from PIL import Image

if __name__ == '__main__':
    # load image
    img = Image.open('sample_sunflower.jpg')
    img_result = combineImage(img,predictObjectEdge(img, 15))
    img_result.save('./result/result_sunflower' + '.jpg')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
