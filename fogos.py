from time import sleep

import emoji

print("="*14,"\033[037mDesafio 44, Version 1.0\033[0;0m - \033[37mPYTHON\033[0;0m","="*14)
print("="*20,"\033[31mContagem de FOGOS!!!\033[0;0m","="*20,"\nAperte ENTER para iniciar a \033[32mCONTAGEM...\033[0;0m")
ok = input("")
print("VAI COMEÇAR EM....")
for c in range (10,-1,-1):
    sleep(1)
    print("\033[32m{}\033[0;0m".format(c))
print("="*6,"\033[32mAEOOOOOOOOOOOOOOO FOOOOGOOOSSS POHHAAAAAA, MORRAM CACHORROS\033[0;0m","="*6)#DESCULPA
print(emoji.emojize("""
\033[034m
\033[31mA\033[34m
⊂_ヽ\033[31mM\033[34m
　 ＼＼ \033[31mO\033[34m＿
　　 ＼(　•_•) \033[31mF\033[34m
　　　 <　⌒ヽ \033[31mO\033[34m
　　　/ 　 へ＼ \033[31mG\033[34m
　　 /　　/　＼＼ \033[31mO\033[34m
　　 ﾚ　ノ　　 ヽ_つ \033[31mS\033[34m
　　/　/ \033[31mD\033[34m
　 /　/| \033[31mE\033[34m
　(　(ヽ 
　|　|、＼ \033[32mARTIFÍCIOS\033[34m  :fireworks: :fireworks: :fireworks: :fireworks: :fireworks: 
　| 丿 ＼ ⌒)   :clap::clap: :fire::fire:
　| |　　) /
`ノ )　 Lﾉ
(_／/
\033[0;0m
""",use_aliases=True))
print("\033[37mFim...")