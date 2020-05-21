[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/chandrikadeb7/Face-Mask-Detection/issues)
[![Forks](https://img.shields.io/github/forks/chandrikadeb7/Face-Mask-Detection.svg?logo=github)](https://github.com/chandrikadeb7/Face-Mask-Detection/network/members)
[![Stargazers](https://img.shields.io/github/stars/chandrikadeb7/Face-Mask-Detection.svg?logo=github)](https://github.com/chandrikadeb7/Face-Mask-Detection/stargazers)
[![Issues](https://img.shields.io/github/issues/chandrikadeb7/Face-Mask-Detection.svg?logo=github)](https://github.com/chandrikadeb7/Face-Mask-Detection/issues)
[![MIT License](https://img.shields.io/github/license/chandrikadeb7/Face-Mask-Detection.svg?style=flat-square)](https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/LICENSE)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555)](https://www.linkedin.com/in/chandrika-deb/)

## Face Mask Detection
Face Mask Detection system built with __OpenCV__, __Keras/TensorFlow__ using __Deep Learning__ and __Computer Vision__ concepts in order to detect face masks in static images as well as in real-time video streams.


## Motivation
In the present scenario due to Covid-19, there is no efficient face mask detection applications which are now in high demand for transportation means, densely populated areas, residential districts, large-scale manufacturers and other enterprises to ensure safety. Also, the absence of large datasets of __‘with_mask’__ images has made this task more cumbersome and challenging. 

 
## Project Demo
Project Demo Link: [https://www.youtube.com/watch?v=AAkNyZlUae0](https://www.youtube.com/watch?v=AAkNyZlUae0)

#### Dev Link
[https://dev.to/chandrikadeb7/face-mask-detection-my-major-project-3fj3](https://dev.to/chandrikadeb7/face-mask-detection-my-major-project-3fj3)


![](https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/Readme_images/Screen%20Shot%202020-05-14%20at%208.49.06%20PM.png)



## Tech/framework used

<b>Built with</b>
- [OpenCV](https://opencv.org/)
- [Caffe-based face detector](https://caffe.berkeleyvision.org/)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [MobileNetV2](https://arxiv.org/abs/1801.04381)

## Features
Our face mask detector didn't uses any morphed masked images dataset. The model is accurate, and since we used the MobileNetV2 architecture, it’s also computationally efficient and thus making it easier to deploy the model to embedded systems (Raspberry Pi, Google Coral, etc.).

This system can therefore be used in real-time applications which require face-mask detection for safety purposes due to the outbreak of Covid-19. This project can be integrated with embedded systems for application in airports, railway stations, offices, schools, and public places to ensure that public safety guidelines are followed.


## Prerequisites
* Python 3.0 or later
* cv2 = 4.2.0
* tensorflow = 1.14.0 or later
* keras = 2.3.1
* imutils = 0.5.3
* sklearn = 0.22.1
* numpy = 1.18.2
* matplotlib = 3.1.3
* tensorflow-gpu = 2.0 or later (optional)

## Installation
1. Clone the repo
```
git clone https://github.com/chandrikadeb7/Face-Mask-Detection.git
```

2. Open terminal. Go into the cloned repo folder and type the following command:
```
$ python train_mask_detector.py --dataset dataset
```

3. Now detect the face masks in images or real-time video streams
```
$ python detect_mask_image.py --images <path to image>
```

```
$ python detect_mask_video.py 
```
## Dataset
The dataset used is not public yet. The images used were real images of faces wearing masks. 
__Bing Search API__ and __Kaggle__ was used to collect the dataset


## Contribute
This project is open for further improvement. Feel free to Fork the project and give me credits.


## Credits
* [https://www.pyimagesearch.com/](https://www.pyimagesearch.com/)
* [https://www.tensorflow.org/tutorials/images/transfer_learning](https://www.tensorflow.org/tutorials/images/transfer_learning)


## License

MIT © [Chandrika Deb](https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/LICENSE)
