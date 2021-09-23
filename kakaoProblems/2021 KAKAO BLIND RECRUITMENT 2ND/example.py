import requests
url = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
x_auth_token = '582a18f8ad60c7700f1142cc40a967cd'
def start(problem):
    uri = url + '/start'
    # Start API 를 통해 발급받은 key, 이후 문제 풀이에 진행되는 모든 API에 이 key를 사용, 선택한 시나리오 번호,
    # 현재 카카오 T 바이크 서비스에서의 시각 (0부터 시작) 반환
    return requests.post(uri, headers={"X-Auth-Token": x_auth_token}, json={"problem": problem}).json()

def get_locations(auth_key):
    uri = url + "/locations"
    # 각 자전거 대여소의 ID, 보유하고 있는 자전거 수에 대한 정보를 담은 배열 반환
    return requests.get(uri, headers={'Authorization': auth_key}).json()

def get_trucks(auth_key):
    uri = url + "/trucks"
    # 각 트럭의 ID, 현재 위치, 싣고 있는 자전거 수에 대한 정보를 담은 배열
    return requests.get(uri, headers={'Authorization': auth_key}).json()


# orders = [{ "truck_id": 0, "command": [2, 5, 4, 1, 6]}, ...] 이 꼴
def simulate(auth_key, orders):
    uri = url + "/simulate"
    # response
    # status	String	현재 카카오 T 서버의 상태
    # time	Integer	현재 시각 (요청 시각에서 1분 경과)
    # failed_requests_count	Integer	실패한 요청 수
    # distance	String	모든 트럭이 현재까지 이동한 거리의 총합(km 단위)
    return requests.put(uri, headers={'Authorization': auth_key}, json={"commands": orders}).json()


def get_score(auth_key):
    uri = url + '/score'
    # 획득한 점수 반환, finished == false이면 무조건 0점 반환
    return requests.get(uri, headers={'Authorization': auth_key}).json()


def make_board(board):
    idx = 0
    for y in range(len(board)):
        for x in range(len(board)-1, -1, -1):
            board[x][y] = idx
            idx += 1

def p1_simulator():
    problem = 1
    n = 5
    default_bicycle = 4
    truck_cnt = 5

    board = [[0]*n for _ in range(n)]
    make_board(board)

    ret = start(problem)
    auth_key = ret['auth_key']
    # test
    locations = get_locations(auth_key)['locations']
    for location in locations:
        print(location)
    # print(get_trucks(auth_key))
    # while True:
    #     res = simulate(auth_key, [])
    #     if res['status'] == 'finished': break
    #     print(res)
    print(get_score(auth_key))
    return
if __name__ == '__main__':
    # problem = 2
    # n = 60
    # default_bicycle = 3
    # truck_cnt = 10

    p1_simulator()