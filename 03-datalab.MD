# Setting up Cloud Datalab

## Before you begin

1. Google Cloud Platform 콘솔에서 프로젝트를 생성 또는 선택
2. 해당 프로젝트의 billing을 설정
3. `Google Compute Engine` 그리고 `Cloud Source Repository` API 를 enable시킨다

## Installation

업데이트후 `datalab`을 설치합니다.

```
gcloud components update
gcloud components install datalab
```

설치후 `gcloud components list` 명령어를 통해 설치 된 components를 확인 할 수 있습니다.

## Creating Datalab Instance

```
datalab create [datalab-instance-name]
```

만약 K80 GPU 를 갖은 Cloud Datalab VM 을 생성하고자 하면 다음과 같이 합니다.

> Multi GPUs 를 사용할때는 `--accelerator-count [number]` flag를 사용

```
datalab beta create-gpu [datalab-instance-name]
```

생성까지 조금 시간이 걸리며, 생성완료된후 `localhost:8081` 같은 주소로 접속이 가능합니다. 

![Datalab1](images/datalab1.png)

현재 GPU Datalab 은 Beta라서 다음의 regions만 가능합니다.
 
* us-east1
* us-central1
* asia-east1
* europe-west1


## Cleaning Up Datalab Instance

생성된 Datalab에 대한 자원을 종료를 해줍니다. (cleaning up을 안 할 경우 비용이 추가적으로 나올 수 있습니다.) Datalab VM instance의 생성부터 종료까지 비용이 발생하게 되며, notebooks이 저장되어 있는 persistent disk에 대해서도 비용이 발생합니다. 

다음의 명령어는 **Datalab Instance** 그리고 **Persistent Disk**  모두 제거합니다. 

> `datalab list` 를 통해서 instances를 확인 가능합니다.

```
datalab delete --delete-disk [instance-name]
```

## Package Installation

#### Pytorch & TorchVision

```
!pip3 install http://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp35-cp35m-linux_x86_64.whl
!pip3 install torchvision
```

설치 확인 코드

```
import torch
from torch.autograd import Variable

a = Variable(torch.cuda.FloatTensor([[1, 2, 3], [0, 1, 1], [1, 0, 3]]))
b = Variable(torch.cuda.FloatTensor([[1, 0, 4], [1, 5, 3], [2, 3, 0]]))
%time a.matmul(b) # a @ b
```