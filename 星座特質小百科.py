import tkinter as tk

def click1():
    win1=tk.Tk()
    win1.geometry("1100x600")
    win1.title("牡羊座小百科")
    text=tk.Text(win1,font=("jf open 粉圓 1.1",20),padx=5,pady=5)
    text.insert(tk.INSERT,"牡羊座 星座日期 3月21日-4月20日\n")
    text.insert(tk.INSERT,"正面關鍵字： 競爭、領先、單純；負面關鍵字： 魯莽、自私、衝動\n")
    text.insert(tk.INSERT,"牡羊座是基本星座，也是火象星座。基本星座的特質：創造、開始、源頭、純粹；火象星座的特質：勇敢、衝動、直覺、自信\n")
    text.insert(tk.INSERT,"牡羊座勇於開創，常能成為開路先鋒，只是偶爾顯得過度急躁，吃緊弄破碗，或是三分鐘熱度，持久力差。\n")
    text.insert(tk.INSERT,"以上資料來自:https://wonderstarlife.com/constellations-date/\n\n")
    text.insert(tk.INSERT,"相處起來最合諧的星座： 射手座、獅子座；相處起來最有挑戰的星座： 巨蟹座、摩羯座\n")
    text.insert(tk.INSERT,"牡羊座在與人相處方面要記得控制好自己衝動的個性與暴躁的脾氣，有動力是件好事，不過如果因為太過急躁而壞事可就得不償失囉。牡羊在忙於自己事業的同時也不要忘了跟朋友或伴侶分享生活點滴喔！\n")
    text.insert(tk.END,"以上資料來自:https://wonderstarlife.com/constellation-matches/")
    text.pack()
    text.config(state=tk.DISABLED)
def click2():
    win1=tk.Tk()
    win1.geometry("1100x600")
    win1.title("金牛座小百科")
    text=tk.Text(win1,font=("jf open 粉圓 1.1",20),padx=5,pady=5)
    text.insert(tk.INSERT,"金牛座 星座日期 4月21日-5月20日\n")
    text.insert(tk.INSERT,"正面關鍵字： 穩重，踏實，溫和；負面關鍵字： 固執，懶惰，遲鈍\n")
    text.insert(tk.INSERT,"金牛座是固定星座，也是土象星座。固定星座的特質： 專注、頑固、自戀、孤僻；土象星座的特質： 物質、守舊、實際、謹慎\n")
    text.insert(tk.INSERT,"金牛座非常重視物質，他們不一定要用很貴的東西，但一定要很有質感，因為他們的感官比較敏銳，粗製濫造的東西他們可接受不了。\n")
    text.insert(tk.INSERT,"以上資料來自:https://wonderstarlife.com/constellations-date/\n\n")
    text.insert(tk.INSERT,"相處起來最合諧的星座： 摩羯座、處女座；相處起來最有挑戰的星座： 獅子座、水瓶座\n")
    text.insert(tk.INSERT,"金牛座不善於表達自己內心的想法，因此很容易生悶氣或與另一半陷入冷戰，如果沒有人願意主動道歉的話會非常容易影響彼此的感情，這是金牛座最需要注意的地方。\n")
    text.insert(tk.END,"以上資料來自:https://wonderstarlife.com/constellation-matches/")
    text.pack()
    text.config(state=tk.DISABLED)
def click3():
    win1=tk.Tk()
    win1.geometry("1100x600")
    win1.title("雙子座小百科")
    text=tk.Text(win1,font=("jf open 粉圓 1.1",20),padx=5,pady=5)
    text.insert(tk.INSERT,"雙子座 星座日期 5月21日-6月21日\n")
    text.insert(tk.INSERT,"正面關鍵字： 機智、風趣、敏捷；負面關鍵字： 善變、輕浮、膚淺\n")
    text.insert(tk.INSERT,"雙子座是變動星座，也是風象星座。變動星座的特質：機智、焦慮、多元、複雜；風象星座的特質：聰明、理性、冷靜、靈活。雙子座關鍵字就是一個字「易」，可以解讀成變易、容易、交易\n")
    text.insert(tk.INSERT,"雙子座的特點就是喜歡四處打聽消息並傳遞給別人，愛到處跑不喜歡被限制，需要極大的彈性與個人空間，感情上亦是如此。\n")
    text.insert(tk.INSERT,"以上資料來自:https://wonderstarlife.com/constellations-date/\n\n")
    text.insert(tk.INSERT,"相處起來最合諧的星座： 天秤座、水瓶座；相處起來最有挑戰的星座： 處女座、雙魚座\n")
    text.insert(tk.INSERT,"雙子座很常被貼上花心的標籤，其實雙子雖然表面上看起來輕浮，對任何事情都抱著玩玩的心態，其實內心非常脆弱，他們用輕鬆幽默的舉止來掩飾自己的內心。在還沒有認定一段感情之前可能會同時和多個對象曖昧，藉此來測試自己是否真的喜歡對方。\n")
    text.insert(tk.END,"以上資料來自:https://wonderstarlife.com/constellation-matches/")
    text.pack()
    text.config(state=tk.DISABLED)
def click4():
    win1=tk.Tk()
    win1.geometry("1100x600")
    win1.title("巨蟹座小百科")
    text=tk.Text(win1,font=("jf open 粉圓 1.1",20),padx=5,pady=5)
    text.insert(tk.INSERT,"巨蟹座 星座日期 6月22日 - 7月22日\n")
    text.insert(tk.INSERT,"正面關鍵字： 體貼、感性、慈愛、顧家；負面關鍵字： 多慮、敏感、不安、疑心\n")
    text.insert(tk.INSERT,"巨蟹座是基礎星座，也是水象星座。基礎星座的特質：積極、獨立、性急、魯莽；水象星座的特質：浪漫、感性、直覺、內斂\n")
    text.insert(tk.INSERT,"巨蟹喜歡建構一個屬於自己的小天地，並從中尋求呵護與溫暖，或給予別人關懷和依靠。巨蟹有很強的防衛心，所以要進入他們的內心並不容易，也因為如此，任何形式的切割與離別會對巨蟹帶來巨大的傷害，久久不能忘懷。\n")
    text.insert(tk.INSERT,"以上資料來自:https://wonderstarlife.com/constellations-date/\n\n")
    text.insert(tk.INSERT,"相處起來最合諧的星座： 處女座、摩羯座；相處起來最有挑戰的星座： 牡羊座、天秤座\n")
    text.insert(tk.INSERT,"巨蟹座的優點就是細膩而且念舊，喜歡把愛人照顧得無微不至，只是巨蟹的內心比較脆弱，很容易胡思亂想為自己想像各種恐怖的小劇場自己嚇自己。\n")
    text.insert(tk.END,"以上資料來自:https://wonderstarlife.com/constellation-matches/")
    text.pack()
    text.config(state=tk.DISABLED)
def click5():
    win1=tk.Tk()
    win1.geometry("1100x600")
    win1.title("獅子座小百科")
    text=tk.Text(win1,font=("jf open 粉圓 1.1",20),padx=5,pady=5)
    text.insert(tk.INSERT,"獅子座 星座日期 7月23日 - 8月22日\n")
    text.insert(tk.INSERT,"正面關鍵字： 威風、尊貴、開朗、高尚；負面關鍵字： 虛榮、驕傲、奢華、自大\n")
    text.insert(tk.INSERT,"獅子座是固定星座，也是火象星座。固定星座的特質：執著、頑固、專注、穩定；火象星座的特質：勇敢、衝動、直覺、自信\n")
    text.insert(tk.INSERT,"獅子座會用誇張表現來博得眾人眼球，簡單講就是「愛出鋒頭」，受到重視可以讓他們得到快樂，由於想要成為焦點，獅子座對大眾流行特別敏感，很容易就知道大家喜歡甚麼，也很擅長經營自我品牌，販售高級用品\n")
    text.insert(tk.INSERT,"以上資料來自:https://wonderstarlife.com/constellations-date/\n\n")
    text.insert(tk.INSERT,"相處起來最合諧的星座： 牡羊座、射手座；相處起來最有挑戰的星座： 天蠍座、金牛座\n")
    text.insert(tk.INSERT,"高調的獅子就像個明星，他們需要一個欣賞他的對象，獅子會把自己認為最好的給愛人，因此給予讚美或驚喜的回應是相當中意的喔！不過獅子座偶爾會顯得過於目中無人或是以自我為中心，另一半最好是比較會配合且懂得看臉色的對象。\n")
    text.insert(tk.END,"以上資料來自:https://wonderstarlife.com/constellation-matches/")
    text.pack()
    text.config(state=tk.DISABLED)
def click6():
    win1=tk.Tk()
    win1.geometry("1100x600")
    win1.title("處女座小百科")
    text=tk.Text(win1,font=("jf open 粉圓 1.1",20),padx=5,pady=5)
    text.insert(tk.INSERT,"處女座 星座日期 8月23日 - 9月22日\n")
    text.insert(tk.INSERT,"正面關鍵字： 專業、秩序、細緻、完美；負面關鍵字： 瑣碎、挑剔、碎嘴、挑剔\n")
    text.insert(tk.INSERT,"處女座是變動星座，也是土象星座。變動星座的特質：提升、多元、循環、適應；土象星座的特質：實際、保守、踏實、物質\n")
    text.insert(tk.INSERT,"處女座非常要求完美且重視細節，總是希望事情能夠盡善盡美，但是過度挑剔的個性常常讓他們忽略大處，在有時間壓力的狀態下容易焦慮緊張。\n")
    text.insert(tk.INSERT,"以上資料來自:https://wonderstarlife.com/constellations-date/\n\n")
    text.insert(tk.INSERT,"相處起來最合諧的星座： 金牛座、摩羯座；相處起來最有挑戰的星座： 射手座、雙子座\n")
    text.insert(tk.INSERT,"追求完美的處女座對自己和伴侶的要求都很高，最合適的星座就是同為土象星座的摩羯與金牛這兩個 12 星座中少數能耐得住嘮叨的星座，被處女嘮叨其實是好事，這代表他們是關心你是愛你的，如果不關心你根本就懶得理你。\n")
    text.insert(tk.END,"以上資料來自:https://wonderstarlife.com/constellation-matches/")
    text.pack()
    text.config(state=tk.DISABLED)
def click7():
    win1=tk.Tk()
    win1.geometry("1100x600")
    win1.title("天秤座小百科")
    text=tk.Text(win1,font=("jf open 粉圓 1.1",20),padx=5,pady=5)
    text.insert(tk.INSERT,"天秤座 星座日期 9月23日 - 10月23日\n")
    text.insert(tk.INSERT,"正面關鍵字： 合作、協調、優雅、和平；負面關鍵字： 猶豫、虛偽、依賴、油滑\n")
    text.insert(tk.INSERT,"天秤座是基本星座，也是風象星座。基本星座的特質：開創、純粹、原始、單純；風象星座的特質：理性、冷靜、靈活、交際\n")
    text.insert(tk.INSERT,"天秤座具備天生的協調美感，喜歡一切美的事物，舉止優雅深具魅力，擅長社交活動，渴望獲得認同。\n")
    text.insert(tk.INSERT,"以上資料來自:https://wonderstarlife.com/constellations-date/\n\n")
    text.insert(tk.INSERT,"相處起來最合諧的星座： 水瓶座、雙子座；相處起來最有挑戰的星座： 巨蟹座、摩羯座\n")
    text.insert(tk.INSERT,"天秤擁有姣好的外貌與絕佳的社交能力，在愛情上會以一種「試探」的心態去測試自己與對方的愛，因此常會被貼上花心的標籤，天秤在愛情中最需要的就是自由的空間與豐富的知性交流。\n")
    text.insert(tk.END,"以上資料來自:https://wonderstarlife.com/constellation-matches/")
    text.pack()
    text.config(state=tk.DISABLED)
def click8():
    win1=tk.Tk()
    win1.geometry("1100x600")
    win1.title("天蠍座小百科")
    text=tk.Text(win1,font=("jf open 粉圓 1.1",20),padx=5,pady=5)
    text.insert(tk.INSERT,"天蠍座 星座日期 10月24日 - 11月22日\n")
    text.insert(tk.INSERT,"正面關鍵字： 深情、神秘、堅定、謀略；負面關鍵字： 貪婪、忌妒、毒辣、殘忍\n")
    text.insert(tk.INSERT,"天蠍座是固定星座，也是水象星座。固定星座的特質：專注、頑固、執著、穩定；水象星座的特質：敏感、深情、浪漫、細膩\n")
    text.insert(tk.INSERT,"天蠍座具有洞悉人性的能力，很容易看穿別人的想法，也擅長謀略。天蠍座也有很高的靈性潛力，對神祕學問也有濃厚興趣；只是個性極端，喜歡掌控一切事情，有很強的佔有欲，因此也容易因為報復心的驅使，做出毀滅性的行為。\n")
    text.insert(tk.INSERT,"以上資料來自:https://wonderstarlife.com/constellations-date/\n\n")
    text.insert(tk.INSERT,"相處起來最合諧的星座： 巨蟹座、雙魚座；相處起來最有挑戰的星座： 獅子座、水瓶座\n")
    text.insert(tk.INSERT,"在感情方面天蠍只要認定對方就會死心踏地，同時也會希望對方也這樣對他，這容易讓另一半感到壓力（尤其是風象、火象星座）。\n")
    text.insert(tk.END,"以上資料來自:https://wonderstarlife.com/constellation-matches/")
    text.pack()
    text.config(state=tk.DISABLED)
def click9():
    win1=tk.Tk()
    win1.geometry("1100x600")
    win1.title("射手座小百科")
    text=tk.Text(win1,font=("jf open 粉圓 1.1",20),padx=5,pady=5)
    text.insert(tk.INSERT,"射手座 星座日期 11月23日 - 12月21日\n")
    text.insert(tk.INSERT,"正面關鍵字： 樂觀、豪爽、開朗、幸運；負面關鍵字： 誇大、放縱、輕率、浪費\n")
    text.insert(tk.INSERT,"射手座是變動星座，也是火象星座。變動星座的特質：多元、適應、提升、變通；火象星座的特質：勇敢、衝動、直覺、火爆\n")
    text.insert(tk.INSERT,"射手座愛好自由，瀟灑的個性使他們不願受到拘束，有時會藉由遠走他方來逃避事情，給人不負責任的感覺。過度的自信讓射手座時常表現出自大、粗心，這多半也是他們失敗的原因。射手座對應第九宮 － 文化宮，象徵大智慧、旅行、哲學。\n")
    text.insert(tk.INSERT,"以上資料來自:https://wonderstarlife.com/constellations-date/\n\n")
    text.insert(tk.INSERT,"相處起來最合諧的星座： 牡羊座、獅子座；相處起來最有挑戰的星座： 處女座、雙魚座\n")
    text.insert(tk.INSERT,"射手愛玩特質也容易給人輕浮、花心的印象。射手在愛情中追求的是自由與智慧的成長，如果另一半比較保守不願意嘗試新事物會讓射手覺得無趣。\n")
    text.insert(tk.END,"以上資料來自:https://wonderstarlife.com/constellation-matches/")
    text.pack()
    text.config(state=tk.DISABLED)
def click10():
    win1=tk.Tk()
    win1.geometry("1100x600")
    win1.title("摩羯座小百科")
    text=tk.Text(win1,font=("jf open 粉圓 1.1",20),padx=5,pady=5)
    text.insert(tk.INSERT,"摩羯座 星座日期 12月22日 - 1月20日\n")
    text.insert(tk.INSERT,"正面關鍵字： 嚴謹、紀律、節制、堅毅；負面關鍵字： 壓抑、悲觀、死板、老派\n")
    text.insert(tk.INSERT,"摩羯座是基本星座，也是土象星座。基本星座的特質：創造、開始、源頭、純粹；土象星座的特質：實際、踏實、穩重、保守\n")
    text.insert(tk.INSERT,"摩羯很常過度壓抑自己，甚麼苦都往肚子裡吞，他們願意為了名利不計任何代價，再辛苦都會咬牙堅持，只為了成為典範受他人尊敬。\n")
    text.insert(tk.INSERT,"以上資料來自:https://wonderstarlife.com/constellations-date/\n\n")
    text.insert(tk.INSERT,"相處起來最合諧的星座： 金牛座、處女座；相處起來最有挑戰的星座： 牡羊座、天秤座\n")
    text.insert(tk.INSERT,"勤勞簡樸的摩羯適合重視物質的另一半，對土象星座來說麵包的價值遠遠高過愛情，所以摩羯會希望和另一半共同努力創造財富多過於遊山玩水，或是希望對方可以成為自己的靠山，為自己打點生活與提供溫馨舒適的生活環境。\n")
    text.insert(tk.END,"以上資料來自:https://wonderstarlife.com/constellation-matches/")
    text.pack()
    text.config(state=tk.DISABLED)
def click11():
    win1=tk.Tk()
    win1.geometry("1100x600")
    win1.title("水瓶座小百科")
    text=tk.Text(win1,font=("jf open 粉圓 1.1",20),padx=5,pady=5)
    text.insert(tk.INSERT,"水瓶座 星座日期 1月21日 - 2月18日\n")
    text.insert(tk.INSERT,"正面關鍵字： 獨立、創意、平等、博愛；負面關鍵字： 古怪、孤僻、冷漠、叛逆\n")
    text.insert(tk.INSERT,"水瓶座是固定星座，也是風向星座。固定星座的特質：頑固、專注、穩定、執著、風象星座的特質：理性、冷靜、靈活、輕巧\n")
    text.insert(tk.INSERT,"水瓶座有種遠離中心的特質，所以也代表他們善於創新與改革，也可以衍伸出反骨與叛逆的特質。\n")
    text.insert(tk.INSERT,"以上資料來自:https://wonderstarlife.com/constellations-date/\n\n")
    text.insert(tk.INSERT,"相處起來最合諧的星座： 天秤座、雙子座；相處起來最有挑戰的星座： 天蠍座、金牛座\n")
    text.insert(tk.INSERT,"喜歡跳躍思考的水瓶對陌生人都很友善，但是對自己的伴侶或是自己喜歡的對象就會顯得疏離，水瓶需要一個可以與他鬥智的對象，如果不聰明水瓶會覺得無趣，水瓶很喜歡學習新鮮的事物，會希望他的另一半可以給他空間做他喜歡的事情。\n")
    text.insert(tk.END,"以上資料來自:https://wonderstarlife.com/constellation-matches/")
    text.pack()
    text.config(state=tk.DISABLED)
def click12():
    win1=tk.Tk()
    win1.geometry("1100x600")
    win1.title("雙魚座小百科")
    text=tk.Text(win1,font=("jf open 粉圓 1.1",20),padx=5,pady=5)
    text.insert(tk.INSERT,"雙魚座 星座日期 2月19日 - 3月20日\n")
    text.insert(tk.INSERT,"正面關鍵字： 夢幻、救贖、犧牲、慈悲；負面關鍵字： 懶散、受害、可憐、上癮\n")
    text.insert(tk.INSERT,"雙魚座是變動星座，也是水象星座。變動星座的特質：靈活、變通、多元、多元；水象星座的特質：敏感、深情、浪漫、細膩\n")
    text.insert(tk.INSERT,"雙魚座十分純真而且愛幻想，浪漫的性格加上迷糊的個性總是會引發不少誤會，雙魚座都有相當不錯的感受力，他們就像是大海一樣可以輕易地感受到別人的情感。\n")
    text.insert(tk.INSERT,"以上資料來自:https://wonderstarlife.com/constellations-date/\n\n")
    text.insert(tk.INSERT,"相處起來最合諧的星座： 巨蟹座、天蠍座；相處起來最有挑戰的星座： 雙子座、射手座\n")
    text.insert(tk.INSERT,"浪漫迷糊的雙魚容易在愛情中吃虧，不過這也是因為雙魚的愛就是犧牲奉獻所致，雙魚會委屈自己成全愛人或重視的友人，雙魚需要的愛是心靈上的契合感，同時也需要一個精明、可以彌補他迷糊個性的對象。\n")
    text.insert(tk.END,"以上資料來自:https://wonderstarlife.com/constellation-matches/")
    text.pack()
    text.config(state=tk.DISABLED)

win=tk.Tk()
win.geometry("570x250")
win.title("星座小百科")
frame1=tk.Frame(win)
frame1.pack()
frame2=tk.Frame(win)
frame2.pack()
label=tk.Label(frame1,text="歡迎查詢十二星座! !請點選下列標籤查詢",fg="white",
        bg="black",font=("jf open 粉圓 1.1",20),padx=5,pady=5)
label.pack()
btt1=tk.Button(frame2,text="牡羊座",font=("jf open 粉圓 1.1",15),width=10,command=click1)
btt1.grid(row=1,column=0,padx=5,pady=5)
btt2=tk.Button(frame2,text="金牛座",font=("jf open 粉圓 1.1",15),width=10,command=click2)
btt2.grid(row=1,column=1,padx=5,pady=5)
btt3=tk.Button(frame2,text="雙子座",font=("jf open 粉圓 1.1",15),width=10,command=click3)
btt3.grid(row=1,column=2,padx=5,pady=5)
btt4=tk.Button(frame2,text="巨蟹座",font=("jf open 粉圓 1.1",15),width=10,command=click4)
btt4.grid(row=1,column=3,padx=5,pady=5)
btt5=tk.Button(frame2,text="獅子座",font=("jf open 粉圓 1.1",15),width=10,command=click5)
btt5.grid(row=2,column=0,padx=5,pady=5)
btt6=tk.Button(frame2,text="處女座",font=("jf open 粉圓 1.1",15),width=10,command=click6)
btt6.grid(row=2,column=1,padx=5,pady=5)
btt7=tk.Button(frame2,text="天秤座",font=("jf open 粉圓 1.1",15),width=10,command=click7)
btt7.grid(row=2,column=2,padx=5,pady=5)
btt8=tk.Button(frame2,text="天蠍座",font=("jf open 粉圓 1.1",15),width=10,command=click8)
btt8.grid(row=2,column=3,padx=5,pady=5)
btt9=tk.Button(frame2,text="射手座",font=("jf open 粉圓 1.1",15),width=10,command=click9)
btt9.grid(row=3,column=0,padx=5,pady=5)
btt10=tk.Button(frame2,text="摩羯座",font=("jf open 粉圓 1.1",15),width=10,command=click10)
btt10.grid(row=3,column=1,padx=5,pady=5)
btt11=tk.Button(frame2,text="水瓶座",font=("jf open 粉圓 1.1",15),width=10,command=click11)
btt11.grid(row=3,column=2,padx=5,pady=5)
btt12=tk.Button(frame2,text="雙魚座",font=("jf open 粉圓 1.1",15),width=10,command=click12)
btt12.grid(row=3,column=3,padx=5,pady=5)
win.mainloop()