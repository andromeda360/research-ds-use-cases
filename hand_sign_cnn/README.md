# Sign language recognition for deaf and mute
## Problem Statement
> Communication is one of the basic requirements of survival and a great way of expressing oneself. Deaf and mute people find it difficult to communicate with normal people. Communicating with normal people has always been a barrier for them. They find it difficult to express their thoughts or convey a message, especially in public places or business places where they become anxious and nervous. Sign language would bridge this gap, but learning sign language is also a difficult process and it is not taught in schools or colleges. An approach that would make this work easier and time-saving which translates a sign into text would be great for these people.<br />
This project aims to train an AI model which when shown real-time video of a hand sign,shows the output of a particular sign in the form of text.<br />

hand_sign_cnn
images:
collected 1200 images using google teachable machine

```Data-preprocessing.ipynb```<br />
>The purpose here is to segement out the object from background.There are various image segemntation technique,
one which i have used is thresholding technique.<br />

```CNN model.ipynb```<br />
>built cnn model and trained.<br />

How to run:<br />
Run ```opencv_detect.py```<br />

### OUTPUT

![image](screenshot/ss.png)
