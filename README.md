# Deploying_imagenet_pretrained_models_as_flask_web_service

### 1. After downloading, you have to open Command prompt/Anaconda prompt/Visual studio terminal to run this project.


### 2. Before running any files, you have to set up  virtual environment in the directory where the project is located and 
install all the dependenices required for this project.


Creating virtual environment enable us to install the dependencies virtually for this project only without affecting the python dependencies on  your computer.


A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them.


For installing virtual environment on command prompt and visual studio terminal:


##### i) First of all you have to install virtual environment tool to create one.


 For installation:
   
   
### On Windows:
   
   
      python -m pip install --user virtualenv
      
##### Recommended
For installing virtual environment on Anaconda Prompt(Windows):


       conda install -c anaconda virtualenv
   
  
     
##### ii) After installing virtual environment, you have to install all the dependencies required to run this project in your virtual environment. For doing so you have to follow the following steps:
  
  
  
        cd /*location to the repository *
  
  
 ##### iii) After changing the working directory to the current repository/project create a virtual environment by using the following commands:
 
 ### On Windows:
     
     python -m venv venv 
     python -m venv deployment
     
    Here venv is the name of the environment you like to choose. imagenet is the name of the virtual environment that i choose to use in     the example
     
 
 #### Recommended
     On Anaconda Prompt (Windows)
     
     conda create -n "your virtual environment name" python=3.6 (The code is tested and implemented in 3.6 so install python 3.6)
     e.g.
     
     conda create -n deployment python=3.6
     
     
     
 ### On Linux or Mac:
     python3 -m venv venv
     
    
     
##### iv) After creating a virtual environment in a working directory, you need to activate the virtual environment:

 ### On Windows:
   
    On Visual Studio Code:
 
       venv\Scripts\activate
       
 
 #### Recommended
   On Anaconda Prompt (Windows):
  
     conda activate "your virtual environment name"
   
   
     conda activate deployment
   

#### v) Now you need to install all the requirements and dependencies for running this project.You can do this by using the command:


            pip install -r requirements.txt
            
            
#### vi) After installing all those dependencies,just run the flask app by using the command:

            python app.py
      vii) to acces the web type on searchbar http://localhost:5000/

#� �M�L�N�N�
�
�
