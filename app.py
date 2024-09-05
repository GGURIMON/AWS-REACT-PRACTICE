from flask import Flask, jsonify, request

# 1. 지금은 POST, PUT, DELETE 등을 POSTMAN에서 테스트 -> 실제로 프론트엔드에서 요청을 보냄
# 2. 실제 일기 X -> 일기 메모리 저장
# 3. DB 연동

app = Flask(__name__)
diaries = []
id_counter = 1

# CRUD
# Create, Read, Update, Delete
# GET -> Read
# POST -> Create
# PUT -> Update
# DELETE -> Delete

# GET, POST
@app.route("/diary", methods = ['GET', 'POST'])
def handle_diaries():
    global id_counter
    if request.method == 'GET':
        # return jsonify(diaries), 200
        return jsonify({'message': '일기 조회', 'diary': diaries}), 200
    elif request.method == 'POST':
        body = request.json
        diary = {
            'id': id_counter,
            'title': body['title'],
            'content': body['content']
        }
        id_counter += 1
        diaries.append(diary)
        return jsonify({'message': '일기가 추가되었습니다.', 'diary': diary}), 201
    return jsonify({'message' : 'Hellaaaoo!'})


# PUT, DELETE
@app.route('/diary/<int:diary_id>', methods = ['PUT', 'DELETE'])
def handle_diary(diary_id):
    if request.method == 'PUT':
        return jsonify({'message': '일기가 수정되었습니다.', 'diary': f"{diary_id}"}), 200
    elif request.method == 'DELETE':
        return jsonify({'message': '일기가 삭제되었습니다.', 'diary': f"{diary_id}"}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

