import random
print('\033[33m'+"★★★★★★★★★★"+'\033[0m')
print("暗記アプリ2")
print('\033[33m'+"★★★★★★★★★★"+'\033[0m')
name=input('あなたの名前を入力してください')
score=0
seikai_count=0
matigai_count=0
print(score,"点")

mondai1_list  = ["「き」の連体形を選びなさい", "「ぬ」の接続を選びなさい","命令形「せよ」の基本形を選びなさい","「ず」の連体形を選びなさい","「ず」の意味を選びなさい","下一段活用である語を選びなさい","「けり」の意味を選びなさい"]
sentaku1_list = ["1:す","2:け","3:し","4:く"]
sentaku2_list = ["1:連用形","2:連体形","3:未然形","4:終止形"]
sentaku3_list = ["1:○（ない）","2:し","3:する","4:す"]
sentaku4_list = ["1:ね","2:ざれ","3:ざる","4:む"]
sentaku5_list = ["1:完了","2:断定","3:打消","4:推量"]
sentaku6_list = ["1:隠れる","2:蹴る","3:得る","4:耐える"]
sentaku7_list = ["1:断定","2:完了","3:過去","4:使役"]
kotae_list    = ['\033[32m'+"正解！"+'\033[0m', '\033[31m'+"不正解、、"+'\033[0m']

#mondai1_sentaku = random.sample(mondai1_list,3)
#print(mondai1_sentaku)
for i in range(5): 
    print (i+1,'問')
    question = random.choice(mondai1_list)
    if question == mondai1_list[0]:
        print(mondai1_list[0])
        print(sentaku1_list)
        q0 = int(input("1 or 2 or 3 or 4 で回答してください！"))
        if q0 == 3:
            print(kotae_list[0])
            print(sentaku1_list[2])
            score+=1
            seikai_count+=1
        else:
            print(kotae_list[1])
            matigai_count+=1
    elif question == mondai1_list[1]:
        print(mondai1_list[1])
        print(sentaku2_list)
        q0 = int(input("1 or 2 or 3 or 4 で回答してください！"))
        if q0 == 1:
            print(kotae_list[0])
            print(sentaku2_list[0])
            score+=1
            seikai_count+=1
        else:
            print(kotae_list[1])
            matigai_count+=1
    elif question == mondai1_list[2]:
        print(mondai1_list[2])
        print(sentaku3_list)
        q0 = int(input("1 or 2 or 3 or 4 で回答してください！"))
        if q0 == 4:
            print(kotae_list[0])
            print(sentaku3_list[3])
            score+=1
            seikai_count+=1
        else:
            print(kotae_list[1])
            matigai_count+=1
    elif question == mondai1_list[3]:
        print(mondai1_list[3])
        print(sentaku4_list)
        q0 = int(input("1 or 2 or 3 or 4 で回答してください！"))
        if q0 == 3:
            print(kotae_list[0])
            print(sentaku4_list[2])
            score+=1
            seikai_count+=1
        else:
            print(kotae_list[1])
            matigai_count+=1
    elif question == mondai1_list[4]:
        print(mondai1_list[4])
        print(sentaku5_list)
        q0 = int(input("1 or 2 or 3 or 4 で回答してください！"))
        if q0 == 3:
            print(kotae_list[0])
            print(sentaku5_list[2])
            score+=1
            seikai_count+=1
        else:
            print(kotae_list[1])
            matigai_count+=1
    elif question == mondai1_list[5]:
        print(mondai1_list[5])
        print(sentaku6_list)
        q0 = int(input("1 or 2 or 3 or 4 で回答してください！"))
        if q0 == 2:
            print(kotae_list[0])
            print(sentaku6_list[1])
            score+=1
            seikai_count+=1
        else:
            print(kotae_list[1])
            matigai_count+=1
    elif question == mondai1_list[6]:
        print(mondai1_list[6])
        print(sentaku7_list)
        q0 = int(input("1 or 2 or 3 or 4 で回答してください！"))
        if q0 == 3:
            print(kotae_list[0])
            print(sentaku7_list[2])
            score+=1
            seikai_count+=1
        else:
            print(kotae_list[1])
            matigai_count+=1
print ('\033[36m'+'〈あなたの得点〉'+'\033[0m')
print (name)
print (score,"点")
print ('\033[32m'+"正解"+'\033[0m'"した問題は",seikai_count,"問")
print ('\033[31m'+"間違え"+'\033[0m'"た問題は",matigai_count,"問")