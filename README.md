# Fast demo on how to setup Autogen

### Install Anaconda

```bash
brew install --cask anaconda     
```
### Initialize Conda commands

 ```bash
conda create -n ag python=3.11
# im using zsh in this case
conda init zsh 
conda activate ag
# install autogen with pip - You might need evalated rights with sudo
pip install autogen
 ```

## Setup Azure OpenAI API Keys
```bash
export AZURE_OPENAI_API_KEY=your_azure_api_key_here
```

### Install the Autogen Studio 2.0

```bash
pip install autogenstudio
# Launch AutoGenStuio
autogenstudio ui --port 8081
```

Open your preferred web browser.
Navigate to http://localhost:8081/. This is the URL where AutoGen Studio is running.
Once you access this URL, you will enter the AutoGen Studio user interface.

Auutogen should start writing to console a la: 
```bash
INFO:     Started server process [2987]
INFO:     Waiting for application startup.
***** App started *****
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8081 (Press CTRL+C to quit)
INFO:     10.240.2.23:0 - "GET / HTTP/1.1" 200 OK
INFO:     10.240.2.23:0 - "GET /framework-3b041e76ed3d1ab0eeef.js HTTP/1.1" 200 OK
INFO:     10.240.2.23:0 - "GET /webpack-runtime-003e5a4dae73ca3d30f6.js HTTP/1.1" 304 Not Modified
INFO:     10.240.2.23:0 - "GET /app-3ed6e3171738688d710e.js HTTP/1.1" 200 OK
INFO:     10.240.2.23:0 - "GET /images/svgs/welcome.svg HTTP/1.1" 200 OK
INFO:     10.240.2.23:0 - "GET /page-data/index/page-data.json HTTP/1.1" 304 Not Modified
INFO:     10.240.2.23:0 - "GET /favicon-32x32.png?v=46131b614287332146ea078703a67d38 HTTP/1.1" 304 Not Modified
INFO:     10.240.2.23:0 - "GET /page-data/app-data.json HTTP/1.1" 304 Not Modified
INFO:     10.240.2.23:0 - "GET /318ce576f236b79fd96f75904c13f6e55c3eee57-8947c1bbfe0e74e2ecd5.js HTTP/1.1" 200 OK
INFO:     10.240.2.23:0 - "GET /6c05b3ab656a8bfc225a64b3d73a36a92f83c05e-42226684478f854c0fb4.js HTTP/1.1" 304 Not Modified
INFO:     10.240.2.23:0 - "GET /component---src-pages-index-tsx-fffd2b9446035e300706.js HTTP/1.1" 304 Not Modified
INFO:     10.240.2.23:0 - "GET /api/version HTTP/1.1" 200 OK
INFO:     10.240.2.23:0 - "GET /api/sessions?user_id=guestuser@gmail.com HTTP/1.1" 200 OK
INFO:     10.240.2.23:0 - "GET /api/sessions?user_id=guestuser@gmail.com HTTP/1.1" 200 OK
INFO:     10.240.2.23:0 - "GET /page-data/build/page-data.json HTTP/1.1" 304 Not Modified
INFO:     10.240.2.23:0 - "GET /page-data/gallery/page-data.json HTTP/1.1" 304 Not Modified
INFO:     10.240.2.23:0 - "GET /page-data/gallery/page-data.json HTTP/1.1" 304 Not Modified
INFO:     10.240.2.23:0 - "GET /page-data/build/page-data.json HTTP/1.1" 304 Not Modified
INFO:     10.240.2.23:0 - "GET /component---src-pages-gallery-index-tsx-c3fc2757a2d5430da4ce.js HTTP/1.1" 304 Not Modified
INFO:     10.240.2.23:0 - "GET /component---src-pages-build-tsx-2e117a4aac3139c72928.js HTTP/1.1" 304 Not Modified
```

Remember to setup you URL so it looks like: 

```bash
https://{resource}.openai.azure.com/openai/deployments/{deployment}/chat/completions?api-version=2024-02-01
```


## Seting up models in Autogen:

Give your model a name.
Get your Azure OpenAI key![Screenshot 2024-05-08 at 09 42 43](https://github.com/gkaleta/autogen-demo/assets/22896482/30c3495d-81bb-4ce8-935a-003fa8ba7dab)

When using Azure OpenAI you need to fill all boxes out:
Give it a name. 
API Key - get the key from the Azure portal or Azure OpenAI portal. 
API Type should have: Azure. 
Base url should look like the one mentioned above - remember to update the API version which can be found in Azure Docs for OpenAI.
Api version should be in the format of: 2024-02-01. Description can be what ever you want it to be. 



