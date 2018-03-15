# Architecture 

## What it does 

1. Cloud ML은 TensorFlow application을 **클라우드 환경에서 학습**할 수 있도록 도와 둡니다.
2. 학습이 끝난 모델은 바로 Inference를 하도록 클라우드 환경에 호스트시킵니다. 

## 


# Requirements

## Install Python Libraries

```
pip3 install --upgrade google-api-python-client oauth2client
```

# 주요 명령어

#### 모델 리스트 

```
gcloud ml-engine models list
```



# Tutorial

파이썬안에서 REST API를 사용해서 Cloud ML을 사용시 

```
from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
```