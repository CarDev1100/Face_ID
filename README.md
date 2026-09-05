# Face ID
Face ID is facial recognition software I developed that takes two folders known faces and unknown faces and it takes the unknown faces and it trys to see if its a known person if it is it says hi to them else it says unknown face

## Setup
To set this up you need to install face_recognition which is a python library with a pre trained model to compare faces. In order to install you will need to be on a older python version I installed it on 3.11 but anything 4.0 and under should work. While installing if you get a error saying it failed to build try these commands
```
pip install dlib-bin
```
```
pip install numpy Pillow Click face_recognition_models
```
```
pip install face_recognition --no-deps
```
After you install face_recognition you need to install pathlib you can do this with pip
```
pip install pathlib
```
Now that all the dependencies are installed you will need to make the paths to the directorie faces match the ones on your computer. Once this is complete you should be able to try this out yourself!

### Other versions
If you want something more advanced or flashy you can change branches which I should have other versions of this. I am planning to make one that has a like webcam that labels who people are live on the webcam when there in frame, and then another that says hi to anyone who shows up in front of the web cam
