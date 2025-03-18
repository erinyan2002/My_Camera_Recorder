import cv2

# 기본 설정
video_source = 0  # 웹캠 사용 (IP 카메라 주소 입력 가능)
output_filename = 'output.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 코덱 설정 (XVID 사용)
fps = 20.0
frame_size = (640, 480)

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(video_source)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_size[0])
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_size[1])
cap.set(cv2.CAP_PROP_FPS, fps)

# 비디오 저장 객체 생성
out = cv2.VideoWriter(output_filename, fourcc, fps, frame_size)

recording = False  # 녹화 상태
filter_mode = 0  # 필터 모드 (0: 기본, 1: 흑백, 2: 밝기 조정)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 필터 적용
    if filter_mode == 1:  # 흑백 모드
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)  # 저장을 위해 다시 BGR 변환
    elif filter_mode == 2:  # 밝기 증가
        frame = cv2.convertScaleAbs(frame, alpha=1.2, beta=30)  # contrast=1.2, brightness=30

    # 녹화 중이면 화면에 빨간 원 표시
    if recording:
        cv2.circle(frame, (50, 50), 10, (0, 0, 255), -1)  # 빨간 원 추가
        out.write(frame)  # 파일 저장

    # 화면 출력
    cv2.imshow('Video Recorder (Space: 녹화, F: 필터 변경, ESC: 종료)', frame)

    # 키 입력 처리
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC 키 (종료)
        break
    elif key == 32:  # 스페이스바 (녹화 시작/중지)
        recording = not recording
    elif key == ord('f'):  # 'F' 키 (필터 변경)
        filter_mode = (filter_mode + 1) % 3  # 0 → 1 → 2 → 0 순환

# 종료 처리
cap.release()
out.release()
cv2.destroyAllWindows()
