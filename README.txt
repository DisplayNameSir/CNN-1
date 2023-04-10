This file will include instructions explaining the steps needed to operate each
program successfully without running into any errors. A video demonstrations will also
be included in this file for users that wish to watch a demonstration of each program
being executed.

Youtube Links
=========================================
CNN - Baseline + Increasing Dropout...:
https://youtu.be/KIfEtm1YMmk

CNN - Challenge test:
https://youtu.be/XnGNs8IsQXs

Game Development - Flight:
https://youtu.be/OfCBoZFie6c

Hello World to OpenAI:
https://youtu.be/nIftmuTB_4E

Hello World to CHATGPT:
https://youtu.be/WltkJXir9gs
=========================================

GITHUB Respository:
+++++++++++++++++++++++++++++++++++++++++
CNN
https://github.com/DisplayNameSir/CNN 
Happy Garden Game
https://github.com/DisplayNameSir/Happy-Garden-Game 
Hello World and Intro to OpenAI
https://github.com/DisplayNameSir/Intro-to-OpenAI

+++++++++++++++++++++++++++++++++++++++++

DISCLAIMER:
Users that wish to run the following programs will need to install libraries that were
previously uploaded to python to give access to devlopers to a wider range of commands and programs.
It is essential to download the following libraries in order to run the program sueccessfully.


How to download libraries:
To install the modules needed for the program or verify that its installed, users will open their anaconda powershell and type the following commands
1. Open Anaconda Powershell Prompt
2. Type "pip install (missing module name)"
3. Allow the powershell to install the module
4. Once its finished repeat the same steps for the other modules
5. Allow that module to finish downloading and the program should be ready to go!
6. If the program runs into any issues try updating spyder or restarting the IDE.

Installed Modules:
-numpy
-scipy
-math
-matplotlib
-pint
-pandas
-pgzrun
-pygame
-pgzero
-sympy
-random
-heartpy
-tensorflow
-keras
-CUDA
-UPDATE NUMPY

==================================================
Description of each program and brief instructions:
==================================================
Part 1: CNN - Baseline + Increasing Drop...
This program gather images off a specific URL and puts the compliation of images to recognization commdands and functions that allows the program to identify the image and be able to identify what the image is and later classify it for a future
program. This concept is known as machine learning which allows programs and AIs to gradually learn. The following program is gathered by MIT and modieifed to fit our program. By running the program with the installed 
modules, students will be able to run the file for the program to run over 210 epochs which are essential trial and error tests that allow the program to learn from the data given. Later that data will be used to verify the the AI
has truly learned how to recofnize and classify images

Part 2: CNN - Challenge Test
The Challenge test is about putting the file that was generated from the previous program to the test. If the previous file generated a high accuracy value, students can expect for the CNN challenge test to perform successfully to be 
able to identify any image into the calssifications identified in the program. Students are able to use image URLs which the program will gatehr the image and then process using the previous data then display the classification of the image.

Part 3: Game Development - Flight
The following program is a video game called Happy Garden that allows users to multitask between keeping the garden crops nice and water as well as dodge dangerous enemies called Fang Flowers. For this program, we gathered the program online which is the base code on GITHUB, 
then we were assigned to add additional difficulties in the game such as fang flowers, wilted flowers, and rain which are mostly all factors that increase the difficult of the game. By running the game into Spyder, the game window will appear where the user will be able to control
the cow character to water crops and dodge fang flowers

Part 4: Hello World to Openai
The following program is a quickstart that introduces users to using OPENAI or ChatGPT or AI technology to forming their own HTML website that allows a name generator. To run the program, students will need to open the Anacona Powershell Prompt and set their directory to the folder that
was set to isntall the program. With the directory set, studetns may run the program by downloading and upating the listed modules then operate the website by typing flask run which flashes the HTML website onto a local host for students to log onto the website made. THen students are able
to type the speicies they wish to generate a funny nickname for

Part 5: Hello World to ChatGPT
With the previous experiment performed, performing this experiment will allow students to identify the purpose of the parameters used to define and customzie the response chatgpt can output. By modifying each of the parameters to different states and values, students will be able to see
the outcome of each parameter. It is recommended that students form two files for the Chatgpt Openloop File in order to recognize the differences as well as ask the same quesiton.

Here are some of the following oberservations I made when performing the experiment
Engine:
The Engine parameter of the program allows the program to utilize different engines that are operated on Chatgpt.
Each of the engines have their own benefit and disadvantages depending on the usage of the AI.
Most of the engine names mentioned below are currently not working but explain the different usages of the engines
such as the "code-davinci-002" allowing better feedback on programs and "text-davinci-003" offering better language tasks
for responses.

Prompt:
The promot parameter of the prgram allows the starting text of the language model to generate the response. In this program
I modified the prompt parameter to generate a different start message to politely ask "what would you like to ask me today?", which
I beleive is a better approach for a chatbot that is built to assist users. The prompt parameter also allows text and font modification when additional parameters
are added to the prompt.

Max_tokens:
Max_tokens specifies the maximum number of tokens that the langauge model can generate in the response of the program. By settinga higher
or lower value to the max_tokens we will be able to see longer or shorter responses being generated by the AI. Typically it is best to have the bot generate as much
tokens as possible, but in scenarios such as small essays would benefit more when using a lower value.

n:
The "n" parameter of the program specifies the number of responses to generate. It also defines how well detailed
the responses will be along with how much time will be taken for  the repsonse. The higher the n value is the more detailed the response
but the longer it will take for the response to generate. For this program we only set it to generate 5 responses which causes a long pause after each question and only
displays the the first response.

stop:
The stop parameter is a string set to ask users additonal questions or allows quick cancellation of the program or regenerate the response. The stop can be used for many functions
and was originally used for nothing but is now being used to recieve feedback from users after the AI answers a question. This allows the AI to learn if they should keep the repsonses for future
similar questions. The stop parameter also sets a stopping point if needed that is taken priority if the max_token value isnt met.

Temperature:
The temperature parameter allows control over the creativity of the responses. By setting the value to a higher or lower value results in a variety of resposnes. Typically being unpredicatble and more creative the more we increase
the temperature value. By setting the value closer to 0 we will notice lower effort repsonses that are short,concise, and straight to the point.


