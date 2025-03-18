# 🎥 Camera Video Recorder using OpenCV

## 📌 프로젝트 소개
이 프로젝트는 **OpenCV를 이용한 간단한 비디오 녹화 프로그램**입니다.  
사용자는 웹캠을 통해 영상을 녹화할 수 있으며, **흑백 필터**와 **밝기 조절 기능**을 적용할 수 있습니다.  
또한, **녹화 상태를 시각적으로 표시하는 기능**이 포함되어 있어 쉽게 사용할 수 있습니다.


![Camera_Recorder](https://github.com/user-attachments/assets/4a2c90d3-3e94-4d08-acfb-c38fa3b08ab5)

![output](https://github.com/user-attachments/assets/ccfdca9d-6a72-4eab-9732-bb60d7d84e73)


## 🛠 주요 기능
✅ **비디오 녹화 기능** (스페이스바로 시작/중지)  
✅ **필터 기능** (기본, 흑백, 밝기 조정)  
✅ **녹화 중 빨간 원 표시** (녹화 중인지 확인 가능)  
✅ **AVI 형식으로 저장 (`output.avi`)**  
✅ **웹캠 해상도 및 FPS 설정 가능**  

# 🎥 Video Recorder using OpenCV

## 📌 프로젝트 소개
이 프로젝트는 **OpenCV를 이용한 간단한 비디오 녹화 프로그램**입니다.  
웹캠을 통해 영상을 녹화할 수 있으며, 다양한 **필터 적용 기능**을 제공합니다.  
녹화 상태를 시각적으로 표시하여 사용자가 쉽게 확인할 수 있습니다.

## 🛠 기본 설정
| 설정 항목   | 값                        |
|------------|--------------------------|
| 📹 **비디오 소스** | 기본 웹캠 (`video_source = 0`) |
| 💾 **출력 파일**   | `output.avi` |
| 🖼 **프레임 크기** | `640x480` |
| 🎞 **FPS**        | `20.0` |
| 🎥 **코덱**       | `XVID (.avi 형식)` |

## 🎨 필터 모드
| 모드 번호 | 설명 |
|-----------|----------------------|
| 0 (기본)  | 원본 화면 그대로 출력 |
| 1 (흑백)  | 흑백 필터 적용 |
| 2 (밝기)  | 밝기 증가 (contrast=1.2, brightness=30) |

## 📷 실행 화면 예시
| 기본 모드 | 흑백 모드 | 밝기 조정 모드 |
|-----------|----------|--------------|
| ![기본 모드](basic.jpg) | ![흑백 모드](gray.jpg) | ![밝기 증가](bright.jpg) |

## 🛠 필요한 라이브러리
이 프로젝트를 실행하려면 **Python과 OpenCV 라이브러리**가 필요합니다.  
아래 명령어를 입력하여 OpenCV를 설치하세요:

```bash
pip install opencv-python

## OpenCV Video Recorder

## 📌 프로젝트 소개
이 프로젝트는 **OpenCV를 이용한 간단한 비디오 녹화 프로그램**입니다.  
웹캠을 사용하여 비디오를 녹화하고, 다양한 **필터를 적용**할 수 있습니다.

## 🏗 코드 설명
이 프로젝트는 **OpenCV의 `cv2.VideoCapture` 와 `cv2.VideoWriter`** 를 이용하여 구현되었습니다.  
다음은 주요 코드 흐름입니다:

### 1️⃣ 웹캠 연결 및 설정
```python
cap = cv2.VideoCapture(0)  # 웹캠 연결
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 해상도 설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 20)

