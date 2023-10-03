import tkinter
import tkinter.messagebox
import random

fnt1=("Times New Roman",24)

bg_width = 800 #キャンバスの横幅を定義している変数。
bg_height = 450 #キャンパスの縦幅を定義している変数。
p_size = 100 #プレイヤーのサイズを定義している変数。
px = bg_width /2 #プレイヤーの初期x座標を定義している変数。
py = bg_height - 100      #プレイヤーの初期y座標を定義している変数。
key="" #キーボードやマウスから入力された結果を記録する変数。
koff=False #キーボードが押されているのか話されているのか記録する変数。
direction = 0#プレイヤーの向いている向きを記録する変数。
timer = 600 #ゲームのプレイ時間を定義する変数。
score = 0 #ゲームのスコアを定義する変数。
ITEM_MAX = 5 #りんごの最大個数を定義する変数。
mx=[0]*ITEM_MAX #りんごのx座標管理
my=[0]*ITEM_MAX #りんごのy座標管理



def main():
    global key,koff,timer
    canvas.delete("SCREEN")#背景、女性、りんご、文字情報を（更新するために）削除
    canvas.create_image(bg_width/2 , bg_height/2 , image = img_bg , tag="SCREEN")
    
    timer -= 1
    move_player()
    move_item()
    canvas.create_text(bg_width/2,30,text="SCORE:"+str(score),fill="white", font=fnt1, tag="SCREEN")#スコア表示
    
    if koff==True:
        key=""
        koff=False
    
    if timer== 0:#30秒後にゲーム終了→ウィンドウを閉じる。
        tkinter.messagebox.showinfo("end","終了！")
        root.destroy()
    root.after(50,main)#50msec後にmain()を実行

def key_down(event):
    global key
    key=event.keysym
    koff=False

def key_up(event):
    global key , koff
    key = event.keysym
    koff=True

def move_player():
    global px, direction 
    if key=="Left" and px>p_size/2:
        px=px-25
        direction=0
    if key=="Right" and px<bg_width-p_size/2:
        px=px+25
        direction=1
    canvas.create_image(px,py,image=img_player[direction],tag="SCREEN")#位置と向きに応じて女性を描画

def hit_check(x1,y1,x2,y2):#衝突チェック
    if((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)<25*25):
        return True
    return False

def move_item():
    global timer,score
    for i in range(ITEM_MAX):#りんごの位置を一つずつ更新
        my[i] = my[i]+6+i/5#6ピクセルとランダム誤差（i/5）のスピードで落下
        if my[i]>bg_height-p_size/2:#りんごが下まで落ちたら新しく爆弾作成
            mx[i]=random.randint(0,bg_width)#りんごの初期x座標位置計算
            my[i]=random.randint(-bg_height,0)#りんごの初期y座標位置計算
        if hit_check(px,py,mx[i],my[i])==True:#りんごと衝突したらゲームオーバ
            score += 1
        canvas.create_image(mx[i],my[i],image=img_apple,tag="SCREEN")

root = tkinter.Tk()
root.title("はじめまして")
root.resizable(False,False)

canvas = tkinter.Canvas(root, width = bg_width , height = bg_height , bg ="black" )
canvas.pack()

img_player = [
    tkinter.PhotoImage(file="pic/shopping_cart_woman_left.png") ,
    tkinter.PhotoImage(file="pic/shopping_cart_woman_right.png")
]
img_bg = tkinter.PhotoImage(file= "pic/bg_natural_mori.png")
img_apple = tkinter.PhotoImage(file= "pic/fruit_ringo.png")

root.bind("<KeyPress>",key_down)
root.bind("<KeyRelease>",key_up)

main()

root.mainloop()
