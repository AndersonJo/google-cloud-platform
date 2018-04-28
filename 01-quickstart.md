[TOC]

# Cloud SDK

##  Install SDK

설치방식에는 2가지가 있습니다.
Interactive Installer는 사람이 쓰기 편하고, versioned SDK 를 다운로드 받아서 하는 경우는 특정 버젼을 받거나, automation으로 처리할때 사용합니다. 

1. [Interactive Installer](https://cloud.google.com/sdk/downloads#interactive)
2. [Download versioned SDK](https://cloud.google.com/sdk/downloads#versioned)

Interactive Installer를 사용해서 설치하는 방법은 다음과 같이 한다.

```
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
```
> Datalab GPU 활용시 다음의 regions으로 설정해줘야 합니다.  (현재 Beta버젼이라서 supported regions이 적음. `gcloud init` 할때 설정 하면 됩니다)
>
> - us-east1
> - us-central1
> - asia-east1
> - europe-west1 

# 주요 명령어 

## Authentication

#### 계정 리스트 보기

```bash
gcloud auth list
```

####  설정 파일의 속성 보기


```bash
$ gcloud config list
[core]
account = anderson@exem.ai
disable_usage_reporting = True

Your active configuration is: [default]
```

####  설정 파일 정보 그리고 SDK 설정 정보 확인

```bash
gcloud info
```

## Projects

#### 프로젝트 리스트 출력

```bash
gcloud projects list
```

####  프로젝트 생성

새로운 프로젝트를 만들려면 다음의 명령어 실행.
Project ID는 6자리 이상이며, 다른 사람이 만든 프로젝트 이름과 겹치면 안된다.

```bash 
gcloud projects create [project-id]
```

####  프로젝트 변경

```bash
gcloud config set project [project-id]
```

변경되었는지는 `gcloud info` 또는 `gcloud config list` 로 확인이 가능하다. 

