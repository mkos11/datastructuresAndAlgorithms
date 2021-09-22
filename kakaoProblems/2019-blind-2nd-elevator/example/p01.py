import requests

UP, DOWN = 1, -1
url = 'http://localhost:8000'


def start(user, problem, count):
    uri = url + '/start' + '/' + user + '/' + str(problem) + '/' + str(count)
    return requests.post(uri).json()


def oncalls(token):
    uri = url + '/oncalls'
    return requests.get(uri, headers={'X-Auth-Token': token}).json()


def action(token, cmds):
    uri = url + '/action'
    return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': cmds}).json()


def search_same_floor(passengers, calls, floor):
    enter_list, exit_list = [], []
    for passenger in passengers:
        if floor == passenger['end']: exit_list.append(passenger['id'])
    for call in calls:
        if floor == call['start']: enter_list.append(call['id'])
    return enter_list, exit_list

def search_same_dir(passengers, calls, floor, direction):
    start_list, end_list = [], []
    for passenger in passengers:
        if direction == UP:
            if floor < passenger['end']: end_list.append(passenger['id'])
        else:
            if floor > passenger['end']: end_list.append(passenger['id'])
    for call in calls:
        if direction == UP:
            if floor < call['start']: start_list.append(call['id'])
        else:
            if floor > call['start']: start_list.append(call['id'])
    return start_list, end_list

def simulator():
    user = 'tester'
    problem = 1
    count = 2
    max_people = 8
    directions = [UP] * count
    ret = start(user, problem, count)
    token = ret['token']
    print('Token for %s is %s' % (user, token))

    while True:
        info = oncalls(token)
        if info['is_end']: break

        elevators = info['elevators']
        calls = info['calls']

        for i, elevator in enumerate(elevators):
            passengers = elevators[i]['passengers']
            floor = elevator['floor']
            status = elevator['status']
            enter_list, exit_list = search_same_floor(passengers, calls, floor)
            start_list, end_list = search_same_dir(passengers, calls, floor, directions[i])
            if status == 'STOPPED':
                if enter_list and (max_people - len(passengers) > 0): action(token, [{'elevator_id': i, 'command': 'OPEN'}])
                elif exit_list: action(token, [{'elevator_id': i, 'command': 'OPEN'}])
                elif start_list or end_list: action(token, [{'elevator_id': i, 'command': 'UP' if directions[i] == UP else 'DOWN'}])
                else:
                    # 진행 방향에 더이상 없음, 방향 전환
                    directions[i] *= -1
                    action(token, [{'elevator_id': i, 'command': 'UP' if directions[i] == UP else 'DOWN'}])
            elif status == 'OPENED':
                # 먼저 내리는게 매너
                if exit_list: action(token, [{'elevator_id': i, 'command': 'EXIT', "call_ids": exit_list}])
                elif enter_list and (max_people - len(passengers) > 0):
                    print(len(passengers), min(max_people-len(passengers), len(enter_list)))
                    action(token, [{'elevator_id': i, 'command': 'ENTER', "call_ids": enter_list[:min(max_people-len(passengers), len(enter_list))]}])
                else: action(token, [{'elevator_id': i, 'command': 'CLOSE'}])
            elif status in ['UPWARD', 'DOWNWARD']:
                if enter_list or exit_list: action(token, [{'elevator_id': i, 'command': 'STOP'}])
                else:
                    action(token, [{'elevator_id': i, 'command': 'UP' if directions[i] == UP else 'DOWN'}])
        # print(info)

if __name__ == '__main__':
    simulator()
