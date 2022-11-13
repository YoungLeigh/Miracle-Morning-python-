import time
import os.path
import tkinter
import Motivation_Message
import pygame
from datetime import datetime
from tkinter import *
from tkinter import messagebox

#
today_date = datetime.today().strftime("%Y/%m/%d") ## YYYY/mm/dd 형태의 날짜 출력
# currentTime = time.localtime(time.time())
#
# print(f"안녕하세요 000님! 모닝 루틴 프로그램 '미라클 모닝'을 실행시켜주셔서 감사합니다😄"
#       f" \n현재 시각은 {currentTime.tm_year}년 {currentTime.tm_mon}월 {currentTime.tm_mday}일 {currentTime.tm_hour}시 {currentTime.tm_min}분 입니다. ")
#

#시작 화면
root = Tk()
root.title("Miracle Morning")
root.geometry("850x500") #창 화면크기
root.resizable(False, False) #창 화면 조정 금지


mainTitle = Label(root) #메인 타이틀
mainTitle.config(text="Miracle Morning", background="white", foreground="black")
mainTitle.config(font=("Times", 50))
mainTitle.place(x=190, y=30)

subTitle = Label(root) #부제목
subTitle.config(text="당신의 아침을 책임져줄 모닝루틴 프로그램", background="white", foreground="black")
subTitle.config(font=("함초롬바탕", 15))
subTitle.place(x=240, y=120)

userNameInput, birthYearInput = StringVar(), StringVar() #사용자 입력값을 저장하기 위한 변수, 변수명.get()으로 사용 가능하다.

#이름 라벨
userNameLab = Label(root)
userNameLab.config(text="이름:", font=("함초롬바탕", 15), background='white', foreground="black")
userNameLab.place(x=285, y=250)

#이름 입력창
userNameEnt = Entry(root, textvariable=userNameInput)
userNameEnt.insert(0, "홍길동") #디폴트 값
userNameEnt.config(font=("함초롬바탕", 15), background='white', foreground="black")
def clear(event):#좌클릭을 했을때 입력창에 있는 내용 모두를 삭제시키는 함수
    if userNameEnt.get() == "홍길동":  # 초기값만 지울 수 있도록 한다
        userNameEnt.delete(0, len(userNameEnt.get()))
userNameEnt.bind("<Button-1>", clear) #클릭했을때 clear함수 실행
userNameEnt.place(x=335, y=250)


#생년월일 라벨
birthYear = Label(root)
birthYear.config(text="생년월일(8자리):", font=("함초롬바탕", 15), background='white', foreground="black")
birthYear.place(x=185, y=300)

#생년월일 입력창
birthYearEnt = Entry(root, textvariable=birthYearInput)
birthYearEnt.insert(0, "00000000") #디폴트 값
birthYearEnt.config(font=("함초롬바탕", 15), background='white', foreground="black")

def clear(event):#좌클릭을 했을때 입력창에 있는 내용 모두를 삭제시키는 함수
    if birthYearEnt.get() == "00000000":  # 초기값만 지울 수 있도록 한다
        birthYearEnt.delete(0, len(birthYearEnt.get()))
birthYearEnt.bind("<Button-1>", clear) #클릭했을때 clear함수 실행
birthYearEnt.place(x=335, y=303)

defaultRoutines = ["물 한잔 마시기 = 01:00", "창문 열어서 환기하기 = 01:00", "스트레칭 해주기 = 01:30", "이불개기 = 02:00"]

routineStr = "" #루틴 한 줄로 표현
routineList = [] #루틴 리스트
timeList = [] #목표시간 리스트

def login():#실행 시,생년월일 값이 8자리인지 확인 후, 이름 일치 팝업을 출력한다. 사용자가 확인을 누르면 인터페이스를 초기화하는 버튼
    global userName, routineStr, routineList, timeList
    if len(birthYearEnt.get()) == 8:
        nameCheck = messagebox.askyesno(title='이름 확인', message=f"이름: {userNameEnt.get()}\n맞습니까?")
        if nameCheck:
            userName = userNameEnt.get() #이름값 저장
            path = f'{userNameEnt.get()}.txt'  # 해당 폴더 내에 유저 입력값으로 된 텍스트 파일 경로 생성(존재하지 않아도 경로는 생성가능. 존재유무 확인용)
            if not os.path.isfile(path):  # 파일 존재 유무 확인
                userFile = open(f"{userNameEnt.get()}.txt", "w", encoding="utf-8")  # 파일 존재하지 않으면 생성
                for routine in defaultRoutines: #새로운 파일 생성 후 디폴트 루틴 리스트 추가
                    userFile.write(f"{routine}\n")
                userFile.close()
            else:
                pass  # 파일이 존재하면 아무것도 하지 않음.(이건 그냥 표시용)
            f = open(f"{userName}.txt", mode='r', encoding='utf-8')
            lines = f.readlines()
            n=0
            for line in lines: #텍스트 파일 내용을 변수에 담기
                line = line.strip()
                userRoutine, userTime = line.split('=')
                routineList.append(userRoutine)
                timeList.append(userTime)
                n+=1
                if n == len(lines): #마지막 루틴에는 화살표를 넣지 않음
                    routineStr = routineStr + userRoutine
                    break
                routineStr = routineStr + userRoutine + " → "
            f.close()
            menuPage_recall()
    else:
        messagebox.showerror("Error", "8자리 생년월일을 입력해주십시오.")

#시작 버튼
loginBtn =Button(root)
loginBtn.config(text="시작", command=login, font=("함초롬바탕", 15), background='white')
loginBtn.place(x=415, y=350)

#############################메뉴 화면 전환############################
#TODO 사용가능한 전역변수: userNameInput.get(), birthYearInput.get()

def reset():#창 초기화 함수,pack과 place로 추가된 GUI 항목을 모두 삭제한다.
    my_list = root.pack_slaves() + root.place_slaves()
    for i in my_list:
        i.destroy()

def eng_dic():#오늘의 영단어를 보여주는 함수
    from PyDictionary import PyDictionary
    import random
    global word
    words = ['abort', 'absurd', 'accord', 'accumulate', 'bankrupt', 'blast', 'breed', 'brew', 'caption', 'cater',
             'cathedral', 'chamber', 'chronic', 'commence', 'deficiency', 'deficit', 'degradedelegate', 'deliberate',
             'explicit', 'extract', 'extraordinary', 'facilitate', 'faculty', 'fatal', 'federal', 'fertile', 'guardian',
             'gulf', 'habitat', 'halt', 'haunt', 'headquarters', 'intervene', 'intrigue', 'judicial', 'keen', 'knot',
             'lease', 'legislate', 'sweep', 'swell', 'swift', 'tease', 'telegraph', 'temporary', 'tempt', 'tenant',
             'yield']
    word = random.choice(words)
    dict = PyDictionary()
    meaning = dict.meaning("%s" % word)
    try:
        return ("명사: " + meaning["Noun"][0], "\n동사: " + meaning["Verb"][0]), word
    except:
        try:
            return ("명사: " + meaning["Noun"][0]), word
        except:
            return ("동사: " + meaning["Verb"][0]), word




total_elasped_time = 0
total_goal_time = 0

def num1(): #'루틴 실행' 버튼 클릭 시 실행, 대기화면을 출력한다.
    reset()

    def RoutineStart():

        def RoutineRecursion(i):
            global total_elasped_time, total_goal_time, routineList
            reset()

            if i == len(routineList):
                routineResultLab = Label(root, text='모닝루틴 실행 결과', font=("함초롬바탕", 30), background='white', foreground="black")
                routineResultLab.pack(pady=10)

                totalGoalMin, totalGoalSec = divmod(total_goal_time, 60)
                totalGoalTimeLab = Label(root, text = f"총 목표시간 = {totalGoalMin:02d}:{totalGoalSec:02d}")
                totalGoalTimeLab.config(font=("함초롬바탕", 20), background='white', foreground="black")
                totalGoalTimeLab.pack(pady=10)

                totalElaspedMin, totalElaspedSec = divmod(total_elasped_time, 60)
                totalElaspedTimeLab = Label(root, text = f"총 경과시간 =  {totalElaspedMin:02d}:{totalElaspedSec:02d}")
                totalElaspedTimeLab.config(font=("함초롬바탕", 20), background='white', foreground="black")
                totalElaspedTimeLab.pack(pady=10)

                if total_goal_time >= total_elasped_time:
                    goodJobLab = Label(root, text="축하드립니다!\n오늘 하루 어떤 일이든 모두 해낼 수 있을 거예요!")
                    goodJobLab.config(font=("함초롬바탕", 20), background='white', foreground="black")
                    goodJobLab.pack(pady=15)
                else:
                    badJobLab = Label(root, text="시간을 조금 넘겼네요! 그래도 수고 많았습니다!\n남은 하루도 화이팅!")
                    badJobLab.config(font=("함초롬바탕", 20), background='white', foreground="black")
                    badJobLab.pack(pady=15)

                recallBtn = Button(root)
                recallBtn.config(text="확인", command=menuPage_recall, font=("함초롬바탕", 15), background='white', foreground="black")
                recallBtn.pack(pady=20)
                return

            else:
                reset()

                routineLab = Label(root)  # "루틴 실행" 타이틀
                routineLab.config(text=routineList[i], background="white", font=("Times", 50), foreground="black")
                routineLab.pack(side="top", pady=30, fill=BOTH)

                goalTimeLab = Label(root, font=("Helvetica", 30), text=f"목표시간 = {timeList[i]}", foreground="black")
                goalTimeLab.pack()

                elaspedTimeLab = Label(root, font=("Helvetica", 30), text="경과시간 = 00:00", foreground="black")
                elaspedTimeLab.pack()

                nextRoutineBtn = Button(root, text="다음", command=lambda: RoutineRecursion(i + 1), font=("함초롬바탕", 15), background='white', foreground="black")
                nextRoutineBtn.pack(side="top", pady=30)


                string_split = timeList[i].split(":")
                goalMin = int(string_split[0])
                goalSec = int(string_split[1])
                currentGoalTime = (goalMin * 60) + goalSec
                total_goal_time += currentGoalTime

                current_seconds = 0

                while True:
                    current_seconds += 1
                    total_elasped_time += 1
                    minutes, seconds = divmod(current_seconds, 60)
                    elaspedTimeLab.config(text=f"경과시간 =  {minutes:02d}:{seconds:02d}")
                    root.update()
                    time.sleep(1)

        RoutineRecursion(0)


    routinePrintTitle = Label(root)  # "루틴 실행" 타이틀
    routinePrintTitle.config(text="루틴 실행", background="white", foreground="black")
    routinePrintTitle.config(font=("함초롬바탕", 30))
    routinePrintTitle.pack(anchor="n")

    routinePrintSubTitle = Label(root)  # "루틴 실행" 부제목
    routinePrintSubTitle.config(text="시작을 누르면 저장된 루틴이 시작됩니다! 설정된 루틴은 다음과 같습니다.", font=("함초롬바탕", 15))
    routinePrintSubTitle.config(background="white", foreground="black")
    routinePrintSubTitle.pack(side="top", pady=30)

    routineIntroduction = Label(root)  # 루틴명만 모두 출력
    routineIntroduction.config(text=routineStr, font=("함초롬바탕", 15), background="white", foreground="black",wraplength=600)
    routineIntroduction.pack(side="top", pady=30)

    RoutineStartButton = Button(root)
    RoutineStartButton.config(text="시작", command=RoutineStart, font=("함초롬바탕", 15), background='white', foreground="black")
    RoutineStartButton.pack(side="top", pady=30)

def num2(): #'루틴 수정'버튼 클릭 시 실행되는 함수
    global inputText
    reset()
    #'루틴 수정' title
    editTitle = Label(root)
    editTitle.config(text="루틴 수정", background="white", foreground="black")
    editTitle.config(font=("함초롬바탕", 28))
    editTitle.pack(side="top", pady=20)

    inputText = Text(root, width=60, height=20, font=("함초롬바탕", 10), background="white", foreground="black")
    file = open(f"{userName}.txt", mode='r', encoding='utf-8')
    lines = file.readlines()
    for line in lines: #text file내용을 textBox안에 담기
        inputText.insert(tkinter.CURRENT, f"{line}\n")
    inputText.pack(pady=20)
    file.close()
    getTextBtn = Button(root, width="10", height="3", text="저장", command=get_text, background="white", foreground="black" )
    getTextBtn.place(x=400, y=380)

def get_text(): #유저가 수정한 텍스트를 텍스트파일에 다시 저장하는 함수
    textEdit = inputText.get(1.0, END) #입력한 텍스트를 저장
    editedText = textEdit.split("\n")
    editedText = list(filter(None, editedText)) #빈 문자열 제거
    userFile = open(f"{userName}.txt", "w", encoding="utf-8")
    for routine in editedText:
        userFile.write(f"{routine}\n")
    userFile.close()
    menuPage_recall()

    # #'루틴 변경' button
    # loginBtn = Button(root)
    # loginBtn.config(text="루틴 변경", command="edit", font=("함초롬바탕", 15), background='white', foreground="black")
    # loginBtn.pack(side="top", pady=50)
    #
    # #'루틴 추가' button
    # loginBtn1 = Button(root)
    # loginBtn1.config(text="루틴 추가", command="add", font=("함초롬바탕", 15), background='white', foreground="black")
    # loginBtn1.pack(side="top", pady=55)



def Eng_words():#'오늘의 영단어'버튼 클릭 시 실행되는 함수
    reset() #창 초기화
    engWords = eng_dic()
    menu3Title = Label(root,text=f"오늘의 영단어: {word}", font=("Times", 40), background='white', foreground="black")
    menu3Title.pack(side="top", pady=20)
    menu3SubTitle = Label(root,text="영단어는 영어 뜻으로 외웠을 때 더 효과적이라고 합니다. 오늘의 영단어를 외워봅시다.",background='white', foreground="black",font=("함초롬바탕", 15))
    menu3SubTitle.pack(side="top", pady=20)
    menu3Phrase = Label(root,text=engWords, font=("함초롬바탕",20), wraplength=600) #wraplength=int(),숫자만큼 줄이 차면 줄바꿈한다.
    menu3Phrase.pack(side="top", pady=30)
    recallBtn = Button(root)
    recallBtn.config(text="확인", font=("함초롬바탕",15), background='white', foreground="black", command=menuPage_recall)
    recallBtn.pack(side="top", pady=40)


def num4():#'명상의 시간' 버튼 클릭 시 시행되는 함수
    reset()
    pygame.mixer.init()
    r = IntVar()
    Title = Label(root)
    Title.config(text="명상 음악", font=("함초롬바탕", 25), background="white", foreground="black")
    Title.place(x=365, y=1)
    def track1(): #음악 실행 함수
        pygame.mixer.music.load("music/Track1.mp3")
        pygame.mixer.music.play(loops=0)
    def track2():
        pygame.mixer.music.load("music/Track2.mp3")
        pygame.mixer.music.play(loops=0)
    def track3():
        pygame.mixer.music.load("music/Track3.mp3")
        pygame.mixer.music.play(loops=0)
    def track4():
        pygame.mixer.music.load("music/Track4.mp3")
        pygame.mixer.music.play(loops=0)
    def track5():
        pygame.mixer.music.load("music/Track5.mp3")
        pygame.mixer.music.play(loops=0)
    def stop(): #음악 정지 함수
        pygame.mixer.music.stop()
    first = Radiobutton(root, font=("Helvetica", 13), width="10", height="3", text="Track-1", variable=r, value=1, command=track1,  foreground="black")
    second = Radiobutton(root, font=("Helvetica", 13), width="10", height="3",  text="Track-2", variable=r, value=1, command=track2,  foreground="black")
    third = Radiobutton(root, font=("Helvetica", 13), width="10", height="3", text="Track-3", variable=r, value=1, command=track3,  foreground="black")
    fourth = Radiobutton(root, font=("Helvetica", 13), width="10", height="3", text="Track-4", variable=r, value=1, command=track4,  foreground="black")
    fifth = Radiobutton(root, font=("Helvetica", 13), width="10", height="3", text="Track-5", variable=r, value=1, command=track5,  foreground="black")
    first.place(x=380, y=60)
    second.place(x=380, y=100)
    third.place(x=380, y=140)
    fourth.place(x=380, y=180)
    fifth.place(x=380, y=220)
    stopBtn = Button(root, font=("Helvetica", 13), text="Stop", command=stop, background='white', foreground="black")
    stopBtn.place(x=420, y=310)
    recallBtn = Button(root)
    recallBtn.config(text="돌아가기", font=("함초롬바탕", 13), background='white', foreground="black", command=menuPage_recall)
    recallBtn.place(x=405, y=360)
    notice = Label(root)
    notice.config(text="#루틴을 실행하며 음악을 듣고 싶다면 Stop 버튼을 누르지 않고 메인화면으로 돌아가면 됩니다. ", font=("함초롬바탕", 9), background="white", foreground="black")
    notice.place(x=200, y=430)



def num5():#'사용시 주의사항' 버튼 클릭 시 시행되는 함수
    reset()
    Title = Label(root)
    Title.config(text="사용시 주의사항", background="white", foreground="black")
    Title.config(font=("함초롬바탕", 28))
    Title.pack(side="top", pady=20)
    text = Label(root)  # 루틴명만 모두 출력
    text.config(text="1. 루틴 실행시 뜨는 에러: 루틴 실행을 마치면 _tkinter.TclError: invalid command name 이라는 에러가 발생합니다. 해당 에러는 재귀함수를 강제 종료하며 발생하는 오류로 프로그램 실행에는 지장이 없으니 무시해도 됩니다."
                     "\n\n2. 루틴 수정 이후 적용이 안될 때: 루틴 수정을 마치면 프로그램을 종료하고 재실행해야 루틴 실행에서 수정한 내용이 적용됩니다."
                     "\n\n3. 루틴 수정 시 규칙: 루틴 수정시 무조건 >>>루틴 내용 = 00(분):00(초)<<<의 구조로 저장하셔야 합니다.", font=("함초롬바탕", 13), background="white", foreground="black",wraplength=600)
    text.pack(side="top", pady=30)
    recallBtn = Button(root)
    recallBtn.config(text="확인", font=("함초롬바탕",15), background='white', foreground="black", command=menuPage_recall)
    recallBtn.place(x=390, y=380)

def menuPage_recall():#창 초기화 후, 메뉴 페이지를 호출한다.
    reset()
    menuTitle = Label(root)  # 메뉴 타이틀
    menuTitle.config(text="메인 메뉴", background="white", foreground="black")
    menuTitle.config(font=("함초롱 바탕", 25))
    menuTitle.place(x=345, y=20)

    greetings = Label(root)
    greetings.config(text="%s" %Motivation_Message.motivationMessage, font=("함초롬바탕, 10"), background="white", foreground="black", wraplength=400)
    greetings.place(x=225, y=75)
    # frameBox = Frame(root, relief='solid', bd=1, width=300, height=350) #단순 프레임(도형)이다.
    # frameBox.place(x=282, y=100)

    menu1 = Button(root, text="루틴 실행", background="grey", font=("함초롬바탕,15"), width=25, height=1,command=num1)
    menu2 = Button(root, text="루틴 수정", background="grey", font=("함초롬바탕,15"), width=25, height=1,command=num2)
    menu3 = Button(root, text="오늘의 영단어", background="grey", font=("함초롬바탕,15"), width=25, height=1, command=Eng_words)
    menu4 = Button(root, text="명상의 시간", background="grey", font=("함초롬바탕,15"), width=25, height=1,command=num4)
    menu5 = Button(root, text="사용시 주의사항", background="grey", font=("함초롬바탕,15"), width=25, height=1,command=num5)
    menu6 = Button(root, text="종료", background="grey", font=("함초롬바탕,15"), width=25, height=1, command=root.destroy)

    menu1.place(x=302, y=130)
    menu2.place(x=302, y=180)
    menu3.place(x=302, y=230)
    menu4.place(x=302, y=280)
    menu5.place(x=302, y=330)
    menu6.place(x=302, y=380)

root.configure(background='white') #배경 색깔
root.mainloop() #Tkinter 실행