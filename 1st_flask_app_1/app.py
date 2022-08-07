from flask import Flask, render_template

app = Flask(__name__) # 새로운 플라스크 인스턴스를 초기화한다.
@app.route('/) # 라우트 데코레이터, 특정 URL이 index 함수를 실행하도록 지정
def index():
  return render_template('first_app.html')
if __name__ =='__main__':
  app.run()
