import time
import os.path
import tkinter

import Motivation_Message
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
mainTitle.pack(side="top", pady=30)

subTitle = Label(root) #부제목
subTitle.config(text="당신의 아침을 책임져줄 모닝루틴 프로그램", background="white", foreground="black")
subTitle.config(font=("함초롬바탕", 15))
subTitle.place(x=240, y=120)

userNameInput, birthYearInput = StringVar(), StringVar() #사용자 입력값을 저장하기 위한 변수, 변수명.get()으로 사용 가능하다.

#이름 라벨
userNameLab = Label(root)
userNameLab.config(text="이름:", font=("함초롬바탕", 15), background='white', foreground="black")
userNameLab.place(x=285, y=280)

#이름 입력창
userNameEnt = Entry(root, textvariable=userNameInput)
userNameEnt.insert(0, "홍길동") #디폴트 값
userNameEnt.config(font=("함초롬바탕", 15), background='white', foreground="black")
def clear(event):#좌클릭을 했을때 입력창에 있는 내용 모두를 삭제시키는 함수
    if userNameEnt.get() == "홍길동":  # 초기값만 지울 수 있도록 한다
        userNameEnt.delete(0, len(userNameEnt.get()))
userNameEnt.bind("<Button-1>", clear) #클릭했을때 clear함수 실행
userNameEnt.place(x=335, y=283)


#생년월일 라벨
birthYear = Label(root)
birthYear.config(text="생년월일(8자리):", font=("함초롬바탕", 15), background='white', foreground="black")
birthYear.place(x=185, y=330)

#생년월일 입력창
birthYearEnt = Entry(root, textvariable=birthYearInput)
birthYearEnt.insert(0, "00000000") #디폴트 값
birthYearEnt.config(font=("함초롬바탕", 15), background='white', foreground="black")

def clear(event):#좌클릭을 했을때 입력창에 있는 내용 모두를 삭제시키는 함수
    if birthYearEnt.get() == "00000000":  # 초기값만 지울 수 있도록 한다
        birthYearEnt.delete(0, len(birthYearEnt.get()))
birthYearEnt.bind("<Button-1>", clear) #클릭했을때 clear함수 실행
birthYearEnt.place(x=335, y=333)

defaultRoutines = ["물 한잔 마시기 = 01:00", "창문 열어서 환기하기 = 01:00", "스트레칭 해주기 = 01:30", "이불개기 = 02:00 "]

def login():#실행 시,생년월일 값이 8자리인지 확인 후, 이름 일치 팝업을 출력한다. 사용자가 확인을 누르면 인터페이스를 초기화하는 버튼
    global userName
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
            menuPage_recall()
    else:
        messagebox.showerror("Error", "8자리 생년월일을 입력해주십시오.")

#시작 버튼
loginBtn =Button(root)
loginBtn.config(text="시작", command=login, font=("함초롬바탕", 15), background='white')
loginBtn.place(x=415, y=380)

#############################메뉴 화면 전환############################
#TODO 사용가능한 전역변수: userNameInput.get(), birthYearInput.get()

def reset():#창 초기화 함수,pack과 place로 추가된 GUI 항목을 모두 삭제한다.
    my_list = root.pack_slaves() + root.place_slaves()
    for i in my_list:
        i.destroy()

def zodiac():#사용자의 생년월일 값을 바탕으로,'오늘의 운세'와 '띠' 2개의 값을 반환하는 함수이다.
    global birthYearInput
    import requests
    from bs4 import BeautifulSoup
    # <p class="text _cs_fortune_text">
    zodiacSiteList = ["https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%9B%90%EC%88%AD%EC%9D%B4%EB%9D%A0%20%EC%9A%B4%EC%84%B8",
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%8B%AD%EB%9D%A0%20%EC%9A%B4%EC%84%B8",
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EA%B0%9C%EB%9D%A0%20%EC%9A%B4%EC%84%B8",
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%8F%BC%EC%A7%80%EB%9D%A0%20%EC%9A%B4%EC%84%B8",
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%A5%90%EB%9D%A0%20%EC%9A%B4%EC%84%B8",
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%86%8C%EB%9D%A0%20%EC%9A%B4%EC%84%B8",
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%ED%98%B8%EB%9E%91%EC%9D%B4%EB%9D%A0%20%EC%9A%B4%EC%84%B8",
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%ED%86%A0%EB%81%BC%EB%9D%A0%20%EC%9A%B4%EC%84%B8",
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%9A%A9%EB%9D%A0%20%EC%9A%B4%EC%84%B8",
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%B1%80%EB%9D%A0%20%EC%9A%B4%EC%84%B8",
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%A7%90%EB%9D%A0%20%EC%9A%B4%EC%84%B8",
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%96%91%EB%9D%A0%20%EC%9A%B4%EC%84%B8"]
    zodiacBirth = int(birthYearInput.get()[:4]) % 12
    url = zodiacSiteList[zodiacBirth]
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")  # beautifulsoup은 정리하는 도구, req.text는 재료, html.parser는 정리 방식
    txt = soup.find("p", attrs={"class", "text _cs_fortune_text"}).get_text()  # p 태그이면서 특정 속성, 속성값을 가진 p를 찾는다. get_text는 글자들만 뽑아준다

    zodiacList = ['원숭이', '닭', '개', '돼지', '쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양']
    userZodiac = zodiacList[zodiacBirth]
    return txt, userZodiac

routineStr = "" #루틴 한 줄로 표현
routineList = [] #루틴 리스트
timeList = [] #목표시간 리스트
f = open("강민수.txt", mode='r', encoding='utf-8')
lines = f.readlines()
for line in lines:
    line = line.strip()
    userRoutine, userTime = line.split('=')
    routineList.append(userRoutine)
    timeList.append(userTime)
    if line == lines[-1]:
        routineStr = routineStr + userRoutine
        break
    routineStr = routineStr + userRoutine + " → "
f.close()

def num1(): #'루틴 실행' 버튼 클릭 시 실행, 대기화면을 출력한다.
    reset()

    def RoutineStart():  # 루틴 실행 화면을 출력한다.
        reset()

        def RoutineRecursion(i):
            # def RoutineResult():
            #     reset()
            #     recallBtn = Button(root)
            #     recallBtn.config(text="확인", command=menuPage_recall, font=("함초롬바탕", 15), background='white')
            #     recallBtn.place(x=415, y=380)

            if i > len(routineList):
                RoutineResult()
            else:
                reset()
                routionLab = Label(root)  # "루틴 실행" 타이틀
                routionLab.config(text=routineList[i], background="white")
                routionLab.config(font=("Times", 50))
                routionLab.pack(anchor="w",pady=30)

                nextRoutineButton = Button(root)
                nextRoutineButton.config(text="다음", command=lambda:RoutineRecursion(i+1), font=("함초롬바탕", 15),
                                         background='white')
                nextRoutineButton.pack(side="top", pady=30)

        RoutineRecursion(0)


    routinePrintTitle = Label(root)  # "루틴 실행" 타이틀
    routinePrintTitle.config(text="루틴 실행", background="white")
    routinePrintTitle.config(font=("Times", 30))
    routinePrintTitle.pack(anchor="n")

    routinePrintSubTitle = Label(root)  # "루틴 실행" 부제목
    routinePrintSubTitle.config(text="시작을 누르면 루틴이 시작됩니다! 설정된 루틴은 다음과 같습니다.", background="white")
    routinePrintSubTitle.config(font=("함초롬바탕", 15))
    routinePrintSubTitle.pack(side="top", pady=30)

    routineIntroduction = Label(root)  # 루틴명만 모두 출력
    routineIntroduction.config(text=routineStr, background="white", font=("함초롬바탕", 15))
    routineIntroduction.pack(side="top", pady=30)

    RoutineStartButton = Button(root)
    RoutineStartButton.config(text="시작", command=RoutineStart, font=("함초롬바탕", 15), background='white')
    RoutineStartButton.pack(side="top", pady=30)


def num2(): #'루틴 수정'버튼 클릭 시 실행되는 함수
    global inputText
    reset()
    #'루틴 수정' title
    editTitle = Label(root)
    editTitle.config(text="루틴 수정", background="white", foreground="black")
    editTitle.config(font=("함초롱바탕", 28))
    editTitle.pack(side="top", pady=20)

    inputText = Text(root, width=60, height=20, font=("함초롱바탕", 10), background="white", foreground="black")
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



def Zodiac_Sign():#'오늘의 운세'버튼 클릭 시 실행되는 함수
    reset() #창 초기화
    userZodiacPhrase, userZodiac = zodiac()
    menu3Title = Label(root,text="오늘의 운세", font=("Times", 40))
    menu3Title.pack(side="top", pady=20)
    menu3SubTitle = Label(root,text=f"{today_date}, {userZodiac}띠의 운세는", font=("Times", 15))
    menu3SubTitle.pack(side="top", pady=20)
    menu3Phrase = Label(root,text=userZodiacPhrase, font=("함초롱바탕",20), wraplength=600) #wraplength=int(),숫자만큼 줄이 차면 줄바꿈한다.
    menu3Phrase.pack(side="top", pady=30)
    recallBtn = Button(root)
    recallBtn.config(text="확인", font=("함초롬바탕",15), background='white', foreground="black", command=menuPage_recall)
    recallBtn.place(x=415, y=380)

#TODO 디자인요소(폰트,글자크기,글자(배경)색 등등) 업그레이드.

def num4():#'명상의 시간' 버튼 클릭 시 시행되는 함수
    pass

def num5():#'일정 점검' 버튼 클릭 시 시행되는 함수
    pass

def num6():#종료
    pass


def menuPage_recall():#창 초기화 후, 메뉴 페이지를 호출한다.
    reset()
    menuTitle = Label(root)  # 메뉴 타이틀
    menuTitle.config(text="메인 메뉴", background="white", foreground="black")
    menuTitle.config(font=("함초롱 바탕", 25))
    menuTitle.place(x=325, y=20)

    # greetings = Label(root)
    # greetings.config(text="%s" %Motivation_Message.motivationMessage, font=("함초롱바탕, 10"), background="white", foreground="black")
    # greetings.place(x=250, y=50)
    messagebox.showinfo("아침 인사", "%s" %Motivation_Message.motivationMessage)
    # frameBox = Frame(root, relief='solid', bd=1, width=300, height=350) #단순 프레임(도형)이다.
    # frameBox.place(x=282, y=100)

    menu1 = Button(root, text="루틴 실행", background="grey", font=("함초롱바탕,15"), width=25, height=1,command=num1)
    menu2 = Button(root, text="루틴 수정", background="grey", font=("함초롱바탕,15"), width=25, height=1,command=num2)
    menu3 = Button(root, text="오늘의 운세", background="grey", font=("함초롱바탕,15"), width=25, height=1,command=Zodiac_Sign)
    menu4 = Button(root, text="명상의 시간", background="grey", font=("함초롱바탕,15"), width=25, height=1,command=num4)
    menu5 = Button(root, text="일정 점검", background="grey", font=("함초롱바탕,15"), width=25, height=1,command=num5)
    menu6 = Button(root, text="종료", background="grey", font=("함초롱바탕,15"), width=25, height=1,command=num6)

    menu1.place(x=282, y=100)
    menu2.place(x=282, y=150)
    menu3.place(x=282, y=200)
    menu4.place(x=282, y=250)
    menu5.place(x=282, y=300)
    menu6.place(x=282, y=350)


root.configure(background='white') #배경 색깔
root.mainloop() #Tkinter 실행