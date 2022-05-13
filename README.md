# fourthbrain-cohort6-week13: A Sentiment Analyzer API

Well, this here is a repo for our [fourthbrain](https://www.fourthbrain.ai/) MLE Cohort 6 Week 13 Live Assignment (Thu 12 May 2022). In this assigment we're making a Sentiment Analyzer API using [fastapi](https://fastapi.tiangolo.com/) and HuggingFace's [transformers](https://huggingface.co/docs/transformers/index) for the back end. Furthermore, we're also building a [docker](https://docs.docker.com/) image for it, so we can run it without installing anything else. Except for docker, of course :p

Here's how to use it:

## 1. Clone this repo
<details><summary>Show/hide</summary>

```bash
# Go to your special folder
cd /tmp

# Clone this repo
git clone https://github.com/juswaldy/fourthbrain-cohort6-week13.git

# Go into the repo folder
cd fourthbrain-cohort6-week13
```

</details>

## 2. Setup everything
<details><summary>Show/hide</summary>

You can use docker, or create a conda virtual environment, or whatever you want.

### 2.a. With docker (recommended)

1. Install docker https://docs.docker.com/get-docker/
2. Build docker image
```bash
docker build -t fastapi-sentiment .
```

### 2.b. With conda virtual environment

1. Install anaconda https://docs.anaconda.com/anaconda/install/index.html
2. Create a conda virtual environment, activate it, and install the rest of the dependencies
```bash
conda create -n fastapi_env python=3.8 pip
conda activate fastapi_env
pip install fastapi uvicorn transformers torch torchvision torchaudio
```

### 2.c. Whatever you want (not recommended)

ACHTUNG: Zis mait giviu abigg hehdech vershen heil! (not recommended)

```bash
# Not recommended
# pip install fastapi uvicorn transformers torch torchvision torchaudio
```
</details>

## 3. Stand up the API
<details><summary>Show/hide</summary>

### 3.a. With docker

```bash
docker run -p 8000:8000 fastapi-sentiment
```

### 3.b. With conda

```bash
uvicorn --host 0.0.0.0 --port 8000 main:app
```

</details>

## 4. Visit the endpoint
<details><summary>Show/hide</summary>

Point your browser to http://localhost:8000/docs.

![docs](https://raw.githubusercontent.com/juswaldy/fourthbrain-cohort6-week13/main/pics/docs.PNG)

Click the `/sentiment` endpoint.

![sentiment](https://raw.githubusercontent.com/juswaldy/fourthbrain-cohort6-week13/main/pics/score.PNG)

</details>

## 5. Try to fool the model
<details><summary>Show/hide</summary>

Type the last thing you heard someone say to you for the `query_string` parameter.

![sentence](https://raw.githubusercontent.com/juswaldy/fourthbrain-cohort6-week13/main/pics/score.PNG)

Can you beat my score?

![score](https://raw.githubusercontent.com/juswaldy/fourthbrain-cohort6-week13/main/pics/score.PNG)

</details>
