# cmp272-HRMService

# Postman Collection:
- Workspace :https://www.postman.com/red-water-456173/workspace/cmp-272-hrm/collection/2280968-afae399d-c356-4bb4-a6a1-dc40430eb7d3?ctx=documentation
- Collection is [here](PostmanCollections/cmpe272-HRM.postman_collection.json)
- Environment is [here](PostmanCollections/cmpe-272.postman_environment.json)

# Steps to run locally:
- Create python virtual enviornment (Refernce :https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv)
    ```
        virtualenv venv        
    ```
    Linux/ Mac :
    ```
        source venv/bin/activate
    ```
    Windows
    ```
        .\venv\Scripts\activate.ps1        
    ```
- Edit [config.py](config.py)
- Run following commands
    ```
      pip install -r requirements.txt
      python .\app.py   
     ```


# Deployment Configuration:
- Details are [here](https://docs.google.com/document/d/1rudOWRCKl515L047nCUdlOZ_eukf_gM3JPL9ATwCunI/edit)

# Refernces:

- https://flask-cors.readthedocs.io/en/latest/
- https://pyjwt.readthedocs.io/en/stable/
- https://www.service-architecture.com/articles/web-services/representational-state-transfer-rest.html
- https://www.restapitutorial.com/lessons/httpmethods.html
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- https://www.youtube.com/watch?v=I-faYvoYi-c
- https://www.youtube.com/watch?v=LFkGtg-ZTko
