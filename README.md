# AutomaticFaceCamera & PhotoCompositingompositting

### Designed by

21600447 Seungjun, Yu

## Index

[1. Introduction](#introduction)

[2. Language](#language)

[3. Conclusion](#conclusion)

## Introduction

### What does this project do?

This program recognizes the user's face, shoots only the area of the face, and then synthesizes the photos stored in the location of the face in other photos.

1. Recognize the user's face.
2. Save the recognized face as a file of 'face.jpg'.
3. Load 'background.jpg' as a source file on your computer.
4. Recognize a face in the source file and synthesize 'face.jpg' at the recognized location.
5. Show the result to the user and correct the picture according to the user's keyboard input, or close the program (before the program ends, save the result as 'result.jpg').

### Target User
![image](https://user-images.githubusercontent.com/70478109/173190412-62b76e44-a66e-4961-b794-e9bf71138d6f.png)

#### People who want to composite their face or friends face to other person's face.

![image](https://user-images.githubusercontent.com/70478109/173190447-48a01cb9-4429-4b9a-8ace-761eece085f0.png)
#### People who wants to make sure that a particular hairstyle suits their face

### Why this project is useful?

This program allows the user to perform several processes at once to combine photos.


1. Shooting a target with a camera
2. Cut and save the subject's face
3. Composite the cut and saved photos at the location of the face of the original photo to be combined
4. Adjust size and position

This program can save the user's time by performing the above process in just a few seconds.


**In particular, I expect that it will be able to contribute to saving time for students at Handong University or other universities who have a lot of work to do.**

## Language

![image](https://user-images.githubusercontent.com/70478109/173190699-04a90331-f880-4125-8156-e50a617ce07d.png)      ![image](https://user-images.githubusercontent.com/70478109/173190737-c936d0be-843b-4e0c-90a2-b8b80b6dfb6e.png)        ![image](https://user-images.githubusercontent.com/70478109/173190767-b24119c8-9708-4d75-b286-32f999eb9f41.png)

## How to get started?

### Download the Python

```
$ sudo apt-get install python[version]
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python[version] [number]
```


### Download the OpenCV

```
$ sudo apt-get -y update && sudo apt-get -y upgrade
$ pip install opencv-python
or
$ pip install opencv-contrib-python
```

### Download the Haar Cascade

```
$ git clone https://github.com/opencv/opencv/tree/master/data/haarcascades
```

### Donwload the Project Program Code

```
$ git clone https://github.com/tmddls17/OSS_Final_Project_AutomaticFaceCamera_PhotoCompositingompositting
```

## Conclusion

### Demo Video

Follow this link
(https://youtu.be/Af2Vvm3XuTQ)

### Presentation Video

Follow this link
(https://youtu.be/v7YFg4Vhv88)

### Limitation

An attempt was made to create a mask using R-CNN to cut a picture according to the outline of the face, but failed due to insufficient internal memory of the Raspberry Pi.

If the background photo and the face photo to be synthesized have different saturation, it would be better if you could add a function to change it and apply it.

## Where can people get more help, if needed?

### If you have problem with installing python

(https://angelplayer.tistory.com/219)

### If you have problem with installing OpenCV

(https://nan-sso-gong.tistory.com/29)

### Other Problems

#### Please Cantact!
21600447@handong.ac.kr
