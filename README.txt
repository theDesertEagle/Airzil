           _          _ _    _____            _     
     /\   (_)        (_) |  |  __ \          | |    
    /  \   _ _ __ _____| |  | |  | | __ _ ___| |__  
   / /\ \ | | '__|_  / | |  | |  | |/ _` / __| '_ \ 
  / ____ \| | |   / /| | |  | |__| | (_| \__ \ | | |
 /_/    \_\_|_|  /___|_|_|  |_____/ \__,_|___/_| |_|                          

------------------------------------------------------------

The effortless software reproducibility of our data product is critical to facilitate its seamless deployment and use by our clients.  
The Docker repository 'thedeserteagle/airzil' contains the Python 3.7.4 Miniconda environment consisting of the key data science 
libraries pivotal to the development of this project. A couple of commands should invoke the entire application along with its 
data science environment and underlying dependencies.

------------------------------------------------------------

<< SYSTEM REQUIREMENTS >>>
- Docker host that supports creation of Linux Docker containers
- Bash / Powershell / CMD 

------------------------------------------------------------
   
<<< FOR USERS >>>
• Please ensure you have a similar project directory on your PC:
root _________ data ____airbnb ____ listings.csv
	|       |_______proc-backup
	|	|_______states
        |       |_______zillow ____ Zip_Zhvi_2bedroom
	|_____ docker-files _______ Dockerfile
	|
	|_____ docs (optional)
	|
	|_____ eda ______ eda.ipynb
	|
	|_____ img (optional)
	|_____ model ____ knn_imputer
	|_____ util _____ augment_data
	|_____ docker-compose.yml
	|_____ jnb_startup.sh
	|_____ README

The data should be placed in the data folder, since the docker container will attach the volume for the project root folder

• To startup the Python environment, navigate to the project root folder containing 'docker-compose.yml' file and type:
docker-compose run --service-ports airzil 

• To startup the Jupyter notebook that reports our findings, navigate to the project root containing 'jnb_startup.sh' script and type:
./jnb_startup.sh

This should spin up the Airzil Jupyter notebook application 'eda.ipynb' 

------------------------------------------------------------

<<< FOR DEVELOPERS >>>
• If the docker base enviornment (as described in 'Dockerfile' in the docker-files folder) has been updated, rebuild the image as follows:   
docker build . -t thedeserteagle/airzil:latest -t thedeserteagle/airzil:1.0.0
                    {username}  {repo} {newtag}    {username}  {repo} {newtag}

• If any new changes in a Docker container are to be incorporated, stop the container, commit the changes and create a new image as follows:
docker commit CONTAINER_ID thedeserteagle/airzil:1.0.1
NOTE: Please ensure to never commit data or code files to the docker image, as it is only meant to recreate and host the Python environment
