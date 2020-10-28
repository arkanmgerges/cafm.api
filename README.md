### CAFM - API

This is a microservice that provide the clients access to the system api.

### Local Development  
##### Requirements:  
**1 - All infra service are up and running**  
If you don't have them already running then you can do it by following this [link](https://github.com/DigitalMOB2/cafm.infra)  
**2 - Install Pipenv**  
You can run `pip install pipenv` in order to install Pipenv

##### Running API 
**1 - Set up the env vars**  
Make a copy of .env.docker-compose and rename it to .env, then set up the ports for the following
based on the ports of the infrastructure services that you got from [CAFM.Infra Repo](https://github.com/DigitalMOB2/cafm.infra):  
`MESSAGE_BROKER_SERVERS - For kafka`  
`MESSAGE_SCHEMA_REGISTRY_URL - As stated for schema registry url`  
`CAFM_API_REDIS_PORT - As stated for redis`

**2 - Install the dependencies**  
`Pipenv install`   

**3 - Install hupper for watching and restarting the processes (Optional)**  
`pip install hupper`

**4 - Init kafka topics and schemas**  
Open the terminal go the root of this repo, then issue the following commands:  
`pipenv shell`  
`cd src/resource/script`  
**You need python 3 and higher to run the script**
`python admin_script.py`  This will print the help, now issue the command  
`python admin_script.py init-kafka-topics-and-schemas`

And you should get:  
```sh
Topic cafm.api.cmd created
Topic cafm.api.rsp created
```
Now if you visit the link http://localhost:8080/ (check the port from the [CAFM.Infra Repo](https://github.com/DigitalMOB2/cafm.infra)), 
then goto to menu '*topics*', then you will see the topics cafm.api.cmd and cafm.api.rsp (as they set in the .env file). Also
if you visit the menu '*Schema Registry*', then you will see 2 schemas created cafm.api.Command and
cafm.api.Response (as they are set in the .env file)

**4 - Run the API**
You need to open 2 terminals windows:
* One for kafka consumer to consume the responses for the api **Start at the root of this repository**
```sh
pipenv shell
hupper python -m src.port_adapter.messaging.listener.ApiResponseListener
```
* One for running the api  
```sh
pipenv shell
uvicorn src.port_adapter.api.rest.main:app --port 8000 --reload
```
Now you can visit http://localhost:8000/docs  
![api_ui](https://github.com/DigitalMOB2/cafm.api/raw/master/src/resource/img/api_ui.png)   
Also you can change the port above to be any port that you want to use.  
Also the api will service requests on http://localhost:8000/v1 if you want to use 
other clients like [Postman](https://www.postman.com/) and [Insomnia](https://insomnia.rest/)
