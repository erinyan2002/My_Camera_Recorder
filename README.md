# 🎥 Camera Video Recorder using OpenCV

## 📌 프로젝트 소개
이 프로젝트는 **OpenCV를 이용한 간단한 비디오 녹화 프로그램**입니다.  
사용자는 웹캠을 통해 영상을 녹화할 수 있으며, **흑백 필터**와 **밝기 조절 기능**을 적용할 수 있습니다.  
또한, **녹화 상태를 시각적으로 표시하는 기능**이 포함되어 있어 쉽게 사용할 수 있습니다.

## 🛠 주요 기능
✅ **비디오 녹화 기능** (스페이스바로 시작/중지)  
✅ **필터 기능** (기본, 흑백, 밝기 조정)  
✅ **녹화 중 빨간 원 표시** (녹화 중인지 확인 가능)  
✅ **AVI 형식으로 저장 (`output.avi`)**  
✅ **웹캠 해상도 및 FPS 설정 가능**  

## 🎮 사용 방법
1️⃣ **프로그램 실행**  
```bash
python video_recorder.py
기본 설정
설정 항목	값
📹 비디오 소스	기본 웹캠 (video_source = 0)
💾 출력 파일	output.avi
🖼 프레임 크기	640x480
🎞 FPS	20.0
🎥 코덱	XVID (.avi 형식)
🎨 필터 모드
모드 번호	설명
0 (기본)	원본 화면 그대로 출력
1 (흑백)	흑백 필터 적용
2 (밝기)	밝기 증가 (contrast=1.2, brightness=30)
📷 실행 화면 예시
기본 모드	흑백 모드	밝기 조정 모드
🛠 필요한 라이브러리
이 프로젝트를 실행하려면 Python과 OpenCV 라이브러리가 필요합니다.
아래 명령어를 입력하여 OpenCV를 설치하세요:

bash
Copy
Edit
pip install opencv-python
🏗 코드 설명
프로그램의 주요 기능은 OpenCV의 cv2.VideoCapture 와 cv2.VideoWriter 를 이용하여 구현됩니다.
다음은 주요 코드 흐름입니다:

1️⃣ 웹캠 연결 및 설정

python
Copy
Edit
cap = cv2.VideoCapture(0)  # 웹캠 연결
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 해상도 설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 20)
2️⃣ 비디오 저장을 위한 설정

python
Copy
Edit
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # 파일 저장 설정
3️⃣ 녹화 및 필터 적용

python
Copy
Edit
if filter_mode == 1:
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 흑백 필터
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)  # 다시 BGR 변환 (출력 및 저장)
elif filter_mode == 2:
    frame = cv2.convertScaleAbs(frame, alpha=1.2, beta=30)  # 밝기 증가
4️⃣ 사용자 입력 처리

python
Copy
Edit
key = cv2.waitKey(1) & 0xFF
if key == 27:  # ESC 키 -> 종료
    break
elif key == 32:  # 스페이스바 -> 녹화 시작/중지
    recording = not recording
elif key == ord('f'):  # F 키 -> 필터 변경
    filter_mode = (filter_mode + 1) % 3
🏁 프로젝트 마무리
이 프로젝트는 OpenCV를 활용한 간단한 비디오 녹화 및 필터 적용 예제입니다.
필요에 따라 기능을 추가하거나 GUI를 적용하여 개선할 수도 있습니다.
즐겁게 활용하세요! 🚀
