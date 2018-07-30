[TOC]

# Apache Beam Python SDK 설치

일단 가장 중요한 점은 Apache Beam은 Python2.7을 지원하고 있으며, 아직까지는 3.x를 지원하고 있지 않습니다. 
아래의 명령어로 Apache Beam Python SDK를 설치합니다.

```bash
sudo pip install --upgrade pip virtualenv setuptools apache-beam
sudo pip install --upgrade apache-beam
```


Extra requirements도 설치하기 위해서 다음과 같이 합니다.

* apache-beam[gcp] : Google DataFlow, GCS IO, Datastore IO, BigQuery IO 에 필요
* apache-beam[test] : Unittests 에 필요

```
sudo pip install --upgrade apache-beam[gcp] apache-beam[test]
```



