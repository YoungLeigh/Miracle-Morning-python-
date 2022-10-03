import time
from tkinter import *
#
# currentTime = time.localtime(time.time())
#
# print(f"안녕하세요 000님! 모닝 루틴 프로그램 '미라클 모닝'을 실행시켜주셔서 감사합니다😄"
#       f" \n현재 시각은 {currentTime.tm_year}년 {currentTime.tm_mon}월 {currentTime.tm_mday}일 {currentTime.tm_hour}시 {currentTime.tm_min}분 입니다. ")
#

#시작 화면
root = Tk()
root.title("Miracle Morning")
root.geometry("850x500") #창 화면크기
root.resizable(False, False)


mainTitle = Label(root) #메인 타이틀
mainTitle.config(text="Miracle Morning", background="white")
mainTitle.config(font=("Times", 50))
mainTitle.pack(side="top", pady=30)

subTitle = Label(root) #부제목
subTitle.config(text="당신의 아침을 책임져줄 모닝루틴 프로그램", background="white")
subTitle.config(font=("함초롬바탕", 15))
subTitle.place(x=240, y=120)

#이름 라벨
userNameLab = Label(root)
userNameLab.config(text="이름:", font=("함초롬바탕", 15), background='white')
userNameLab.place(x=285, y=280)
#이름 입력창
userNameEnt = Entry(root)
userNameEnt.insert(0, "홍길동") #디폴트 값
userNameEnt.config(text="이름", font=("함초롬바탕", 15), background='white')
def clear(event):#좌클릭을 했을때 입력창에 있는 내용 모두를 삭제시키는 함수
    if userNameEnt.get() == "홍길동":  # 초기값만 지울 수 있도록 한다
        userNameEnt.delete(0, len(userNameEnt.get()))
userNameEnt.bind("<Button-1>", clear) #클릭했을때 clear함수 실행
userNameEnt.place(x=335, y=283)

#생년월일 라벨
birthYear = Label(root)
birthYear.config(text="생년월일(6자리):", font=("함초롬바탕", 15), background='white')
birthYear.place(x=185, y=330)
#생년월일 입력창
birthYearEnt = Entry(root)
birthYearEnt.insert(0, "000000") #디폴트 값
birthYearEnt.config(text="생년월일", font=("함초롬바탕", 15), background='white')
def clear(event):#좌클릭을 했을때 입력창에 있는 내용 모두를 삭제시키는 함수
    if birthYearEnt.get() == "000000":  # 초기값만 지울 수 있도록 한다
        birthYearEnt.delete(0, len(birthYearEnt.get()))
birthYearEnt.bind("<Button-1>", clear) #클릭했을때 clear함수 실행
birthYearEnt.place(x=335, y=333)

#시작 버튼
loginBtn =Button(root)
loginBtn.config(text="시작", font=("함초롬바탕", 15), background='white')
loginBtn.place(x=415, y=380)
def login():
    userName = userNameEnt.get()
    userBirthYear = birthYearEnt.get()
    print(userName, userBirthYear)
loginBtn.config(command=login)

root.configure(background='white') #배경 색깔
root.mainloop() #Tkinter 실행