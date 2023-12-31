# 課題内容
### ①pythonを用いて、さまざまな日付のフォーマットをyyyy-mm-ddの日付型に変換するするスクリプトを作成してください.

<dl>
  <dt>①_a. 日付のフォーマットの種類を網羅</dt>
        <dd>①_a.1 1995.2.4</dd>
        <dd>①_a.2 2008/12/23</dd>
        <dd>①_a.3 平成5年2月6日</dd>
        <dd>①_a.4 R3/08/30</dd>
        <dd>①_a.5 20180506</dd>
</dl>

### ②上記のテストコードをpytestを用いて作成してください。
### ③作成したスクリプトを実行するための環境をDockerで作成してください

# 課題ファイル構成
```
report
 ├- readMe.md
 ├- Dockerfile
 ├- docker-compose.yml
 └─ src
     ├- report1.py
     └─ test_report2.py
 ```

# 使い方

```bash
git clone https://github.com/romero999/report.git
cd report
docker pull python:3.7
docker compose up -d --build
docker compose exec python3 bash
cd src
pytest
exit
docker stop report-python3
```
