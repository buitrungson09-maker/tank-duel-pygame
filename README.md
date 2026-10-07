# Tank Duel 2D

Game xe tăng đối kháng 2D viết bằng **Python + Pygame**.

## Phiên bản hiện tại

Bản đầu tiên hỗ trợ 2 người chơi trên cùng một máy:

- Player 1: W A S D để di chuyển, Space để bắn.
- Player 2: phím mũi tên để di chuyển, Enter để bắn.
- Mỗi xe có 100 HP.
- Mỗi viên đạn gây 20 sát thương.
- Xe hết HP sẽ thua trận.

## Cấu trúc

```text
tank-duel-pygame/
├── main.py
├── settings.py
├── tank.py
├── bullet.py
├── requirements.txt
└── README.md
```

## Cài đặt

Yêu cầu Python 3.

```bash
pip install -r requirements.txt
```

## Chạy game

```bash
python main.py
```

## Kế hoạch phát triển

- Menu chính
- Chế độ luyện tập đấu với bot
- Bot Dễ / Vừa / Khó / Địa ngục
- Đấu thường 2 người
- Đấu xếp hạng
- Hệ thống điểm và rank
- Bản đồ và vật cản
- Vật phẩm hồi máu, tăng sát thương
- Lưu bảng xếp hạng

Dự án được tổ chức thành nhiều file để thuận tiện học Python và phát triển từng chức năng.
