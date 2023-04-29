import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/Nadocoding/Desktop/PythonWorkspace/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/Nadocoding/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴 rect는 사각형을 의미
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기  캐릭터의 1위치에있는값
#x축을 기준으로 왼/오른쪽 움직임 (가로)  y축 기준으로 위/아래 움직임 (세로)
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)  화면크기의 절반이면 정가운데에 위치해있다는 소리임
#x축은 왼쪽에서 오른쪽으로 그려지는 것, 화면의 총 가로 길이를 절반으로 한 위치를 기준으로 시작해서 오른쪽으로 그려지므로 오른쪽으로 치우치게 된다
#정확히 가운데에 캐릭을 위치시키려면 총화면 길이의 절반길이에 캐릭터 절반의길이를 뻬준위치를 시작점으로 잡아야함

character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
#총 화면길이(y축= 위에서 아래로 그려짐)에서 캐릭터크기만큼 뺀곳의 위치에서 부터 시작해서 그려지는 원리이므로 빼준위치로 설정해줘야한다

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()