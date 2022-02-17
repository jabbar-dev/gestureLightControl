Gesture Control Home Automation System
Project Details



Introduction:
A lot of home automation systems are currently running in the market, App based and Voice based are the best examples of them, but we are coming up with a system that has the distinct characteristics than rest. A system where you can just use your gesture to control appliances of your home. By the use of AI, ML and Image Processing with Arduino we can perform the mentioned work.


Methodology: 
1. Setting up environment for AI and ML Processing
2. Implementing methods for hand detection
3. Normalization/Validation of Data
4. Sending data to Arduino’s end
5. Getting Hardware Ready


Setting up environment:
Get Ready Python IDE (Pycharm is recommended) for running the code of AI. Installed the required libraries:
1. OpenCV
2. MediaPipe
3. Arduino’s supporting library
4. Maths
5. Numpy


Implementing methods for hand detection:
Now we can use Media Pipe library to code the required methods for hand detection. So we will implement the hand detection, movement, and coordinate methods so that we can use them for detecting our gesture.

Normalization/Validation of Data:
We will use the methods and count the distance between the required parameters, after that its time to normalize the data into a specific range, so that we can throw it to the hardware.

Sending data to arduino:
Its time to program arduino to accept the data from Serial input and Pythons code to Send data respectively so that we can manage the power at defined pins.

Getting Hardware Ready:
Now we can wire the hardware and see the desired output vividly!

