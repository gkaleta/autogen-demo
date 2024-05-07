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
# install autogen with pip
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
