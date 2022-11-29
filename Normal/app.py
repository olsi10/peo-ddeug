import sqlite3

# 전역 변수 선언
db, cur = None, None  # 연결자, 커서를 저장하는 변수 초기화

# 테이블 삭제


def saveType(addTitle, addSec, addMsec, addtype):
    db = sqlite3.connect("./alarmDB")  # db, sqlite 연결
    cur = db.cursor()                   # db 명령어 연결

    # db.execute("DROP TABLE studentTable")
    # 테이블 있는지 확인
    cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE name = 'alarmTable'")
    tableCheck = cur.fetchone()
    if tableCheck[0] == 0:
        # 테이블 추가
        cur.execute(
            "CREATE TABLE alarmTable (title char(15), sec char(15), mSec char(15), type char(15))")

    cur.execute("INSERT INTO alarmTable (title, sec, mSec, type) VALUES(?, ?, ?, ?)", [
                addTitle, addSec, addMsec, addtype])

    db.commit()
    db.close()


def getType():
    db = sqlite3.connect("./alarmDB")  # db, sqlite 연결
    cur = db.cursor()                   # db 명령어 연결

    # 데이터 조회
    cur.execute("SELECT * FROM alarmTable")
    row = cur.fetchone()
    title = row[0]

    db.close()

    return title
