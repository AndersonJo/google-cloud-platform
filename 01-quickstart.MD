# Cloud SDK

##  Install SDK

아래 내용대로 Ubuntu에 필요한 패키지 설치하면 끝

[Quickstart for Debian and Ubuntu](https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu)

## 주요 명령어 

### 초기화 

초기화 명령어를 통해서 Ubuntu 환경에 Google Cloud 계정 설정및 프로젝트를 설정할수 있다.

```
gcloud init
```

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

####  프로젝트 변경

먼저 기존의 있는 프로젝트 확인

```bash
gcloud projects list
```

새로운 프로젝트를 만들려면 다음의 명령어 실행.
Project ID는 6자리 이상이며, 다른 사람이 만든 프로젝트 이름과 겹치면 안된다.

```bash 
gcloud projects create [project-id]
```

프로젝트 변경은.. 

```bash
gcloud config set project [project-id]
```

변경되었는지는 `gcloud info` 또는 `gcloud config list` 로 확인이 가능하다. 

