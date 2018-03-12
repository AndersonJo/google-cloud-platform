# Cloud SDK

##  Install SDK

아래 내용대로 Ubuntu에 필요한 패키지 설치하면 끝

[Quickstart for Debian and Ubuntu](https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu)

```bash
# Create an environment variable for the correct distribution
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"

# Add the Cloud SDK distribution URI as a package source
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# Import the Google Cloud Platform public key
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

# Update the package list and install the Cloud SDK
sudo apt-get update && sudo apt-get install google-cloud-sdk
```

초기화 명령어를 통해서 Ubuntu 환경에 Google Cloud 계정 설정및 프로젝트를 설정할수 있다.

```
gcloud init
```


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

