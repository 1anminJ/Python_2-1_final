# 가위비아보 중 하나를 임의로 선택하기 함수
from random import choice

# 가위바위보 게임 판정에 사용할 딕셔너리
madwin = {'가위' : '보',
          '바위' : '가위',
          '보' : '바위'}
game = ['가위 # 바위 # 보 게임', '가위', '바위', '보']
msg = ['비겼습니다.', '축하합니다! 당신이 이겼습니다.']
msg.append('아쉽지만, 컴퓨터가 이겼습니다.')

print((game[0] + '시작 ').center(55, '='))
# 게임 시작
while True:
    try:
        s = ' 0(종료), 1(가위), 2(바위), 3(보[자기]) 중 하나 선택 >> '
        num = int(input(s))
    except:
        num = 1
    if num == 0:
        break
    if not (0 <= num <= 3):  # 범위 값이 아니므로 다시 시작
        print('\t 입력이 잘못됐습니다. 다시 하세요! ')
        continue

    # 컴퓨터에게 하나 선택
    player = game[num]
    com = choice(game[1:])  # 가위바위보는 1부터 시작
    # 게임 판정
    if player == com:
        winner = 0  # 비김
    elif madwin[player] == com:
        winner = 1  # 플레이어 이김
    else:
        winner = 2  # 컴퓨터 이김

    print('당신 : ', player, 'vs', '컴퓨터 : ', com)
    print(msg[winner] + '\n')

# end
print('\n', '종료합니다. '.center(55, '='))