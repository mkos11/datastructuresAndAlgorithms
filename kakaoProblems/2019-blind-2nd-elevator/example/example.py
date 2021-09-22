import requests


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


def p0_simulator():
    user = 'tester'
    problem = 0
    count = 1

    ret = start(user, problem, count)
    token = ret['token']
    print('Token for %s is %s' % (user, token))

    print(oncalls(token))
    action(token, [{'elevator_id': 0, 'command': 'UP'}])
    action(token, [{'elevator_id': 0, 'command': 'UP'}])
    action(token, [{'elevator_id': 0, 'command': 'UP'}])
    action(token, [{'elevator_id': 0, 'command': 'STOP'}])
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}])
    action(token, [{'elevator_id': 0, 'command': 'ENTER', "call_ids": [0, 1]}])
    action(token, [{'elevator_id': 0, 'command': 'CLOSE'}])
    print(oncalls(token))



if __name__ == '__main__':
    p0_simulator()
