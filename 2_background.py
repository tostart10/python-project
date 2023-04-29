import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기     ()안에 파일의 경로를 써준다  경로의 백슬러쉬를 두번씩 써주거나 그냥슬러쉬로 바꿔준다
background = pygame.image.load("C:/Users/Nadocoding/Desktop/PythonWorkspace/pygame_basic/background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    #screen.fill((0, 0, 255)) ->배경을 이미지로 안하고 색을 체우는 방법임 R, G, B 로 빨강,초록,파랑을 나타내는데 지금은 파랑의 최대값을 적은상태임
    screen.blit(background, (0, 0)) # 배경 그리기  (x좌표(오른쪽으로감), y좌표(아래쪽으로감)) =>게임이미지를 배경이미지로 하는 방법

    pygame.display.update() # 게임화면을 다시 그리기!
#pygame에서는 매번 매 프레임마다 화면을 계속그려줘야하기 때문에 update를 함으로써 while부분을 계속돌며 계속 화면을 그려주는것
    
# pygame 종료
pygame.quit()