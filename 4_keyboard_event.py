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
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)

# 이동할 좌표  /좌표를 바꿔주기위해서 새로운 변수생성
to_x = 0
to_y = 0

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인  /키보드의 키가 눌렸을 때 작동하는 구문/어떤키가 눌렸는지에 따라 작동하게 조건을 만들어준 구문
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= 5 # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += 5
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= 5
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += 5

                
#/사용자가 키보드에서 손을 땟을때 작동하는 구문/ 눌렸던키가 떨어졌을때 해당하는 키에대한 조건을 구현하는 구문
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤     
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0   #x축은 좌우로 움직
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0   #y축은 위아래

    character_x_pos += to_x   #위의 for문과 같은 위치에서 시작(들여쓰기 위치 잘봐!)
    character_y_pos += to_y 
    #키에서 손을 때면 to_y, to_x 가 모두 0으로 되도록 해줬기때문에(바로위에if문에서) 캐릭터의 포지션에 0을 더하는 거기때문에 위치에 변함이 없도록하는 구문이다
    #이 구문으로 캐릭터의 위치를 정해준거임
    
    # 가로 경계값 처리      /캐릭이 화면밖으로 나가지 않게하기(x축-좌우)
    if character_x_pos < 0:  #0보다 작다는거는 캐릭터가 화면 맨 왼쪽밖으로 나가버렸다는 뜻
        character_x_pos = 0  #0으로 만들어줘서 화면밖으로 캐릭이 나가지 않게 해줌
    elif character_x_pos > screen_width - character_width: 
        character_x_pos = screen_width - character_width  #캐릭이 화면 오른쪽 밖으로 나가지 않게해줌
'''컴퓨터는 시작점을 기준으로 오른쪽 아래로 이미지를 그려내기 때문에 화면 끝지점에서 캐릭터 x 크기만큼 빼준 지점을 시작점으로
해줘야 화면 밖으로 나가지않고 오른쪽 끝에 위치한걸로 할 수 있음'''
        
        
    # 세로 경계값 처리     /캐릭이 화면밖으로 나가지 않게하기(y축-위아래)
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()
