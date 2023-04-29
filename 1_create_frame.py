import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 이벤트 루프  파이썬에서는 이벤트루프가 항상실행되고 있어야 창이 꺼지지 않는다 (마우스,키보드의 동작 등 )
running = True # 게임이 진행중인가? 를 확인하는 것  runnig이 True면 게임이 계속 돌고 있다는 의미임
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?  pygame을 쓰기위해서는 무조건 적어야하는 부분임. 동작을 감지하면 그에 맞는 실행을 이 안에서 구현함
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가? 많은이벤트 중에 창을끄는 맨오른쪽 상단의 x 버튼을 눌렀을때 실행됨
            running = False # 게임이 진행중이 아님

# pygame 종료
pygame.quit()