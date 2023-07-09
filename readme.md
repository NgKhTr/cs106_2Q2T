# CoLight

- Tham khảo và sửa đổi từ: `https://github.com/wingsweihua/colight.git`
  - author: Wei, Hua and Xu, Nan and Zhang, Huichu and Zheng, Guanjie and Zang, Xinshi and Chen, Chacha and Zhang, Weinan and Zhu, Yamin and Xu, Kai and Li, Zhenhui
  - title: CoLight: Learning Network-level Cooperation for Traffic Signal Control
  - booktitle: Proceedings of the 28th ACM International Conference on Information and Knowledge Management
  - series: CIKM '19
  - year: 2019
  - location: Beijing, China

## Sử dụng

Yêu cầu cài đặt docker để chạy code

1. Pull docker image cung cấp các thư viện để chạy code: `docker pull ngkhtrf/cs106`

2. Pull code Colight từ git: `git clone https://github.com/NgKhTr/cs106_2Q2T.git`

3. Tạo docker container từ docker image vừa được pull về và mount tới thư mục chứa code Colight:
`docker run -it -v /path/to/your/workspace/colight/:/colight/ --shm-size=8gb --name ngkhtrf/cs106:latest /bin/bash`
(Lưu ý: ký hiệu phân cách trong path là `/`)

5. Terminal đã được được liên kết với terminal của docker container, di chuyển vào thư mục colight: `cd colight`

6. Chạy thử nghiệm với Colight model, có thể thiết lập các đối số để chọn map, round train, ...: `python -O runexp.py`

7. Chạy thử nghiệm với Baseline model, có thể thiết lập các đối số để chọn map, baseline model, ...: `python -O run_baseline.py`

Chạy giả lập

1. Pull code CityFlow từ git: `git clone https://github.com/cityflow-project/CityFlow.git`

2. Mở file: `Cityflow/frontend/index.html`

3. Chọn `roadnetLogFile.json` và `replayLogFile.txt` trong thư mục thuộc thư mục có tên được thiết lập bằng tham số `--memo` khi chạy, trong thư mục `records`

4. Bấm start để xem giả lập
