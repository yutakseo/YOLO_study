import matplotlib
matplotlib.use('TkAgg')  # 백엔드를 TkAgg로 변경

from ultralytics import YOLO

# YOLOv8 모델 로드
model = YOLO("yolov8n.pt")

# 객체 탐지 수행
results = model("test_image.png", show=True)
