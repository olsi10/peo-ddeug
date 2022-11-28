import pygame
import random
import imp
from tkinter import *


pygame.init()


def openNewWindow():

    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel()

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="This is a new window").pack()


# 화면 크기 설정
screen_width = 480
screen_height = 640
pygame.display.set_mode((screen_width, screen_height))

screen = pygame.display.set_mode(
    (screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Run Froggy!! comming Poop!!")

# fps
clock = pygame.time.Clock()

# 1. 사용자 초기화 (배경, 캐릭터, 좌표, 속도, 폰트)

background = pygame.image.load("WakeUpGame/img/background1.png")

# 스프라이트 불러오기 (캐릭터)
character = pygame.image.load("/peo-ddeug/WakeUpGame/img/sprite1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 15

# 똥 만들기
ddong = pygame.image.load("/peo-ddeug/WakeUpGame/img/enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0, screen_width - ddong_width)
ddong_y_pos = 0
ddong_speed = 23

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 15

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()  # 시작 tick 을 받아옴

# 음악
sound = pygame.mixer.Sound("/peo-ddeug/WakeUpGame/mp3/BGM.mp3")


# 이벤트 루프
running = True
while running:
    sound.play()  # 음악 재생
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ddong_y_pos += ddong_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    # 충돌 체크
    if character_rect.colliderect(ddong_rect):  # 에너미랑 충돌했는가?
        print("꽝!!!!!!꽝!!!!!!꽝!!!!!!꽝!!!!!!꽝!!!!!!\n꽝!!!!!!꽝!!!!!!꽝!!!!!!꽝!!!!!!꽝!!!!!!")
        running = False

    # 화면에 그리기
    screen.blit(background, (0, 0))  # 좌표, 맨 왼쪽 위 / 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))  # 적 캐릭터 그리기

    screen.blit(background, (0, 0))  # 좌표, 맨 왼쪽 위 / 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))  # 적 캐릭터 그리기

    # 타이머 넣기
    # 경과 시간
    elapes_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간을(ms) 1000으로 나누어서 초(s) 단위

    timer = game_font.render(
        str(int(total_time - elapes_time)), True, (255, 0, 0))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))

    # 만약 시간 0 이하면 게임 종료
    if total_time - elapes_time <= 0:
        print("Time Out!!!")
        running = False

    pygame.display.update()  # while을 돌면서 게임화면을 계속 다시 그리기

# 잠시 대기
pygame.time.delay(5000)  # 2초 정도 대기 (ms)
# pygame 종료5
pygame.quit()

# Finish
# 똥 피하기 게임은 저의 위시리스트 1위였는데 완성했습니다!!
