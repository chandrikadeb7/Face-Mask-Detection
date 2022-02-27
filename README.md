<h1 align="center">Face Mask Detection</h1>

<div align= "center"><img src="https://github.com/Vrushti24/Face-Mask-Detection/blob/logo/Logo/facemaskdetection.ai%20%40%2051.06%25%20(CMYK_GPU%20Preview)%20%2018-02-2021%2018_33_18%20(2).png" width="200" height="200"/>
  <h4>Face Mask Detection System built with OpenCV, Keras/TensorFlow using Deep Learning and Computer Vision concepts in order to detect face masks in static images as well as in real-time video streams.</h4>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/chandrikadeb7/Face-Mask-Detection/issues)
[![Forks](https://img.shields.io/github/forks/chandrikadeb7/Face-Mask-Detection.svg?logo=github)](https://github.com/chandrikadeb7/Face-Mask-Detection/network/members)
[![Stargazers](https://img.shields.io/github/stars/chandrikadeb7/Face-Mask-Detection.svg?logo=github)](https://github.com/chandrikadeb7/Face-Mask-Detection/stargazers)
[![Issues](https://img.shields.io/github/issues/chandrikadeb7/Face-Mask-Detection.svg?logo=github)](https://github.com/chandrikadeb7/Face-Mask-Detection/issues)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555)](https://www.linkedin.com/in/chandrika-deb/)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Live Demo](https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/Readme_images/Demo.gif)

## :point_down: Support me here!
<a href="https://www.buymeacoffee.com/chandrikadeb7" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## :innocent: Motivation
Amid the ongoing COVID-19 pandemic, there are no efficient face mask detection applications which are now in high demand for transportation means, densely populated areas, residential districts, large-scale manufacturers and other enterprises to ensure safety. The absence of large datasets of __‘with_mask’__ images has made this task cumbersome and challenging. 

## PPT and Project Report sharing costs ₹1000 ($15)
If interested, contact me at chandrikadeb7@gmail.com

# 🌟 [Purchase at a Discounted Rate](https://gum.co/GetFaceMask)
 
## :hourglass: Project Demo
:movie_camera: [YouTube Demo Link](https://youtu.be/wYwW7gAYyxw)

:computer: [Dev Link](https://dev.to/chandrikadeb7/face-mask-detection-my-major-project-3fj3)

[![Already deployed version](https://raw.githubusercontent.com/vasantvohra/TrashNet/master/hr.svg)](https://face-mask--detection-app.herokuapp.com/)



<p align="center"><img src="https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/Readme_images/Screen%20Shot%202020-05-14%20at%208.49.06%20PM.png" width="700" height="400"></p>


## :warning: TechStack/framework used

- [OpenCV](https://opencv.org/)
- [Caffe-based face detector](https://caffe.berkeleyvision.org/)
- [Keras](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)
- [MobileNetV2](https://arxiv.org/abs/1801.04381)

## :star: Features
Our face mask detector doesn't use any morphed masked images dataset and the model is accurate. Owing to the use of MobileNetV2 architecture, it is computationally efficient, thus making it easier to deploy the model to embedded systems (Raspberry Pi, Google Coral, etc.).

This system can therefore be used in real-time applications which require face-mask detection for safety purposes due to the outbreak of Covid-19. This project can be integrated with embedded systems for application in airports, railway stations, offices, schools, and public places to ensure that public safety guidelines are followed.

## :file_folder: Dataset
The dataset used can be downloaded here - [Click to Download](https://github.com/chandrikadeb7/Face-Mask-Detection/tree/master/dataset)

This dataset consists of __4095 images__ belonging to two classes:
*	__with_mask: 2165 images__
*	__without_mask: 1930 images__

The images used were real images of faces wearing masks. The images were collected from the following sources:

* __Bing Search API__ ([See Python script](https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/search.py))
* __Kaggle datasets__ 
* __RMFD dataset__ ([See here](https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset))

## :key: Prerequisites

All the dependencies and required libraries are included in the file <code>requirements.txt</code> [See here](https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/requirements.txt)

## 🚀&nbsp; Installation
1. Clone the repo
```
$ git clone https://github.com/chandrikadeb7/Face-Mask-Detection.git
```

2. Change your directory to the cloned repo 
```
$ cd Face-Mask-Detection
```

3. Create a Python virtual environment named 'test' and activate it
```
$ virtualenv test
```
```
$ source test/bin/activate
```

4. Now, run the following command in your Terminal/Command Prompt to install the libraries required
```
$ pip3 install -r requirements.txt
```

## :bulb: Working

1. Open terminal. Go into the cloned project directory and type the following command:
```
$ python3 train_mask_detector.py --dataset dataset
```

2. To detect face masks in an image type the following command: 
```
$ python3 detect_mask_image.py --image images/pic1.jpeg
```

3. To detect face masks in real-time video streams type the following command:
```
$ python3 detect_mask_video.py 
```
## :key: Results

#### Our model gave 98% accuracy for Face Mask Detection after training via <code>tensorflow-gpu==2.5.0</code>

<a href="https://colab.research.google.com/drive/1AZ0W2QAHnM3rcj0qbTmc7c3fAMPCowQ1?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
####          
![](https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/Readme_images/Screenshot%202020-06-01%20at%209.48.27%20PM.png)

#### We got the following accuracy/loss training curve plot
![](https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/plot.png)

## Streamlit app

Face Mask Detector webapp using Tensorflow & Streamlit

command
```
$ streamlit run app.py 
```
## Images

<p align="center">
  <img src="Readme_images/1.PNG">
</p>
<p align="center">Upload Images</p>

<p align="center">
  <img src="Readme_images/2.PNG">
</p>
<p align="center">Results</p>

## :clap: And it's done!
Feel free to mail me for any doubts/query 
:email: chandrikadeb7@gmail.com

---

## Internet of Things Device Setup

### Expected Hardware
* [Raspberry Pi 4 4GB with a case](https://www.canakit.com/raspberry-pi-4-4gb.html)
* [5MP OV5647 PiCamera from Arducam](https://www.arducam.com/docs/cameras-for-raspberry-pi/native-raspberry-pi-cameras/5mp-ov5647-cameras/)

### Getting Started
* Setup the Raspberry Pi case and Operating System by following the Getting Started section on page 3 at `documentation/CanaKit-Raspberry-Pi-Quick-Start-Guide-4.0.pdf` or https://www.canakit.com/Media/CanaKit-Raspberry-Pi-Quick-Start-Guide-4.0.pdf
  * With NOOBS, use the recommended operating system
* Setup the PiCamera
  * Assemble the PiCamera case from Arducam using `documentation/Arducam-Case-Setup.pdf` or https://www.arducam.com/docs/cameras-for-raspberry-pi/native-raspberry-pi-cameras/5mp-ov5647-cameras/
  * [Attach your PiCamera module to the Raspberry Pi and enable the camera](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2)

### Raspberry Pi App Installation & Execution

> Run these commands after cloning the project

| Commands                                                                                                                     | Time to completion |
|------------------------------------------------------------------------------------------------------------------------------|--------------------|
| sudo apt install -y libatlas-base-dev liblapacke-dev gfortran                                                                | 1min               |
| sudo apt install -y libhdf5-dev libhdf5-103                                                                                  | 1min               |
| pip3 install -r requirements.txt                                                                                             | 1-3 mins           |
| wget "https://raw.githubusercontent.com/PINTO0309/Tensorflow-bin/master/tensorflow-2.4.0-cp37-none-linux_armv7l_download.sh" | less than 10 secs  |
| ./tensorflow-2.4.0-cp37-none-linux_armv7l_download.sh                                                                        | less than 10 secs  |
| pip3 install tensorflow-2.4.0-cp37-none-linux_armv7l.whl                                                                     | 1-3 mins           |

---

## :trophy: Awards
Awarded Runners Up position in [Amdocs Innovation India ICE Project Fair]( https://www.amdocs.com/)

![](Readme_images/nn.jpeg)

## :raising_hand: Cited by:

1. https://osf.io/preprints/3gph4/
2. https://link.springer.com/chapter/10.1007/978-981-33-4673-4_49
3. https://ieeexplore.ieee.org/abstract/document/9312083/
4. https://link.springer.com/chapter/10.1007/978-981-33-4673-4_48
5. https://www.researchgate.net/profile/Akhyar_Ahmed/publication/344173985_Face_Mask_Detector/links/5f58c00ea6fdcc9879d8e6f7/Face-Mask-Detector.pdf

## 👏 Appreciation

### Selected in [Devscript Winter Of Code](https://devscript.tech/woc/)
<img src="Readme_images/Devscript.jpeg" height=300 width=300>

### Selected in [Script Winter Of Code](https://swoc.tech/project.html)
<img src="Readme_images/winter.jpeg" height=300 width=300>

### Seleted in [Student Code-in](https://scodein.tech/)
<img src="Readme_images/sci.jpeg" height=300 width=300>

## :+1: Credits
* [https://www.pyimagesearch.com/](https://www.pyimagesearch.com/)
* [https://www.tensorflow.org/tutorials/images/transfer_learning](https://www.tensorflow.org/tutorials/images/transfer_learning)

## :handshake: Contribution

#### Please read the Contribution Guidelines [here](https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/CONTRIBUTING.md)
Feel free to **file a new issue** with a respective title and description on the the [Face-Mask-Detection](https://github.com/chandrikadeb7/Face-Mask-Detection/issues) repository. If you already found a solution to your problem, **I would love to review your pull request**! 

## :handshake: Our Contributors

<a href="https://github.com/chandrikadeb7/Face-Mask-Detection/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=chandrikadeb7/Face-Mask-Detection" />
</a>


## :eyes: Code of Conduct

You can find our Code of Conduct [here](/CODE_OF_CONDUCT.md).

## :heart: Owner
Made with :heart:&nbsp;  by [Chandrika Deb](https://github.com/chandrikadeb7)

## :eyes: License
MIT © [Chandrika Deb](https://github.com/chandrikadeb7/Face-Mask-Detection/blob/master/LICENSE)

