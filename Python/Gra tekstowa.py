import time
import sys
import textwrap
from Tkinter import *
import random

#file = '000029e5.wav'
#root = Tk()
#pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load(file)

#tu beda przechowywane rozne zmienne:
x = 0 #tchorzostwo
z = 1 #zostal i nie polecial od razu
y = 0 #smierci do rozdzialu 5
e = 0 #eadger
zas = 0 #jaka zasadzka?
i = 0 #informacja
s = 0 #syn umiera (albo i nie)
m = 0 #misja
t = 1 #Trela
bla = 0 #bla bla bla
s = 0 #samowola
#kom = 0 #komusci sa dobrzy
j = 1
#l = 1.0  list


def papieska_ruletka():
    q = random.randint(0,9)
    if q == 0:
        return("Nie wiem")
    if q == 1:
        return("Nie moge powiedziec")
    if q == 2:
        return("Tak jak pan Jezus powiedzial")
    if q == 3:
        return("Tak")
    if q == 4:
        return("Co?")
    if q == 5:
        return("Jak najbardziej")
    if q == 6:
        return("Nie")
    if q == 7:
        return("Bo mi nie dali nigdy")
    if q == 8:
        return("Bardzo")
    if q == 9:
        return("Jest mozliwe")
    
def prin(x):
    x = textwrap.fill(x, 100)
    for y in x:
        sys.stdout.write ('%s'% y)
        sys.stdout.flush()
        time.sleep(0.015)
    print("")

def slowlowanie(x):
    x = textwrap.fill(x, 100)
    for y in x:
        sys.stdout.write ('%s'% y)
        sys.stdout.flush()
        time.sleep(0.15)
    print("")

Tekst101a = "20 IX 1939 rok\nRazem z moim ojcem dolaczylismy do Korpusu Ochrony Pogranicza. General Wilhelm Orlik-Ruckeman skoncentrowal zolnierzy na zachod od rzeki Styr. Moj ojciec jest oficerem, wiec dowiedzialem sie, ze Warszawa jest oblegana. Dowodztwo planowalo udac sie w strone Wlodawy by polaczyc sily z gen. Kleebergiem."
Tekst101c = "W oddzialach panuje chaos. Zolnierze albo panikuja na mysl o walce, albo jej pragna. Sam nie wiem, co o tym myslec, ale ojciec mowi, bym na razie zachowal spokoj i czekal na rozwoj wypadkow."
Tekst102a = "26 IX 1939 rok"
Tekst102b = "Dotarlismy do lasow w okolicy Ratna. Napotkalismy tu kolejne oddzialy sowietow, tym razem doszlo do kilku potyczek. Przez cala droge natrafialismy na zbrojne bandy wroga, dodatkowo ataki lotnicze - marsz nie jest latwy. juz pierwsze straty wsrod ludzi, a minely dopiero 2 dni drogi!"
Tekst103a = "29 IX 1939 rok"
Tekst103b = "Nie czuje sie najlepiej.  Co prawda nie ucierpialem fizycznie, ale psychicznie juz nie daje rady."
Tekst103c = "Wczoraj doszlo do pierwszej wiekszej walki. Na wojska wroga natrafilismy w wiosce Szack. Zaatakowalismy szybko, z samego rana. Po godzinie ruscy juz uciekali w poplochu! Zdobylismy osiem radzieckich czolgow oraz zaoparzenie (dzieki Bogu, bo nam juz zostaly resztki). Cieszylem sie wtedy jak nigdy w zyciu, lecz moj ojciec, bardziej niz ja doswiadczony, wiedzial, ze to jeszcze nie koniec. Jesszcze tego samego dnia sowieci, dzieki posilkom i wsparciu lotnictwa, ruszyli do kontrataku. Przez blad dowodcow brygady ''Polesie'' zostalismy zepchnieci za linie Bugu. Dzisiaj ostatni zolnierze wracaja z Szacka. Okolo 500 ludzi poleglo, zostalo rannych i wzietych do niewoli. Moj poczatkowy entuzjazm zostal brutalnie ostudzony, lecz ojciec mowi, ze niedlugo dojde do siebie."
Tekst104a = "1 X 1939 rok"
Tekst104b = "Sytuacja wyglada tragicznie. Wczoraj dostalismy wiadomosc z zachodu - Warszawa padla! Nie ochlonolem jeszcze po walkach w Szacku, gdy dotarla do mnie ta wiadomosc. Dodatkowe trudnosci poteguja rozpacz - setki kilometrow drogi przebyte, nam brakuje amunicji i jedzenia. Zewszad jestesmy otoczeni wrogami, a teraz nie mamy nawet dokad pojsc. Wszyscy na okolo panikuja. Coraz wiecej dezerterow pojawia sie w naszch szeregach, a mnie wciaz meczy mysl, czy do nich nie dolaczyc."
Tekst104c = "Dzisiejszego ranka doszlismy do Wytyczna, skad biegnie szlak komunikacyjny Lublin - Wlodawa. Jednak zanim ruszymy nim w dalsza droge, musimy zmierzyc sie z armia sowietow."
Tekst105a = "Czekasz na granicy lasu na wroga. Zimny pot splywa ci po karku, nerwowo sprawdzasz bron. Z niepokojem wypatrujesz nieprzyjaciela. Wreszcie sie pojawia. Bitwa sie rozpoczela."
Tekst105b = "Wsrod huku karabinow z przerazeniem patrzysz na wojska wroga. Kule przelatuja kolo twojej glowy, uderzaja w ziemie pod twoimi stopami. Nagle ogladasz sie za ramie i widzisz uciekajacych w pospiechu zolniezy."
Tekst107a = "Zucasz karabin i biegiem na zlamanie karku uciekasz za nimi. Nie patrzysz sie za siebie ani przed siebie. Po prostu biegniesz, az zgielk bitwy nie umilknie. Tulasz sie wtedy po okolicy szukajac swoich, przeklinajac siebie w duchu, ze stchorzyles i zostawiles ojca samego na polu bitwy. Po jakims czasie (dla ciebie byla to wiecznosc) zaczeli pojawiac sie pozostali czlonkowie twojego oddzialu. Wsrod nich spotykasz swojego ojca. Szczesliwy, ze zyje, bieniesz w jego strone, lecz on wita cie ostrymi slowami. Wyzuca ci tchorzostwo i brak lojalnosci wobec wlasnych rodakow. Obwinia cie za przegrana bitwe, za smierc tych dobrych zolnierzy poleglych dzisiejszego dnia. Z rozpacza sluchasz jego slow, gdyz w glebi duszy wiesz, ze ma racje."
Tekst107b = "Nie poddajesz sie i strzelasz dalej. Naokolo ciebie zolnierze umieraja, lecz widzisz, ze i wrogowie gina. Nie myslac wiecej skupiasz sie na walce."
Tekst108b = "Nagly bol przeszywa twoje ramie - zostales trafiony. Mgla zachodzi ci oczy, z krzykiem upadasz na kolano. Nieprzytomnie rozgladasz sie na boki. Juz chcesz uciekac, gdy po twojej lewej stronie zauwazasz swojego ojca, zbierajacego wokol siebie ludzi. Stwierdzasz, ze mimo rany mozesz jeszcze strzelac i..."
Tekst109a = "Nie mozesz walczyc w takim stanie. Decydujesz sie na odwrot. Gdy uciekasz slyszysz, ze zgielk bitwy umilkl. Twoja rana mocno krwawi, lecz chwile pozniej doganiaja cie inni zolnierze, w tym twoj ojciec. Jest on z ciebie dumny i, mimo porazki, cieszy sie, ze jestescie razem"
Tekst109b = "Biegiem, ile sil w nogach, rzucasz sie w strone ojca. Kule lataja wokol ciebie, ale nie zwracasz na to uwagi. W polowie drogi twoj ojciec odwraca glowe w twoja strone, wasze spojrzenia krzyzuja sie."

Tekst201a = "6 X 1939 rok"
Tekst201b = "Oddalilismy sie z ojcem od lini frontu na tyle daleko, ze jestesmy juz praktycznie bezpieczni. Choc nie mozna powiedziec, ze istnieje jeszcze jakis front - wojna sie juz de facto skonczyla. Przegralismy. Jedyne co nam teraz pozostaje to uciekac z tad. Naczelny  wodz E. Rydz-Smigly polecil nam dwie drogi ucieczki - Wegry i Rumunie.  Musielismy z ojcem ustalic, gdzie udac sie teraz."
Tekst202a = "I wlasnie wtedy rozstalismy sie. Od ostatnich kilku dni nie moglismy sie dogadac, wiec i ta rozmowa nie mogla byc latwa. Jednak nigdy nie sadzilem, ze tak to sie skonczy. Ojciec kategorycznie chcial jechac do Rumunii, by tam dolaczyc do wladz polskich. Ja mu jednak mowilem, ze rzad nie zostanie tam, ale bedzie uciekal dalej na zachod - do Francji, badz Wielkiej Brytanii. A tam bezpieczniej przez Wegry. Probowalem go jeszcze dlugo przekonac, lecz widac bylo, ze on juz podial decyzje.  W pewnym momencie przerwal mi i powiedzial: ''Nie bedziesz decydowal za mnie! Nie jestes jeszcze wystarczajaco dorosly, by decydowac nawet za siebie! Chcesz znow tchorzyc i uciekac - prosze bardzo! Jednak beze mnie!'' Po tych slowach trzasnal drzwiami i wyszedl. Bylem tak zszokowany i tak zly, ze przez nastepne  20 minut chodzilem tam i z powrotem po namiocie, zlorzeczac na niego w myslach. Wtedy szedl nagle do srodka oficer Jan Askaldowicz. Przyjzal mi sie uwaznie, po czym rzekl '' Twoj ojciec mnie tu przyslal. Poprosil mnie, bym ruszyl do Wegier razem z toba. Zgodzilem sie, wiec zbieraj sie - za godzine wyruszamy.''"
Tekst202b = "Rozmowa nie byla prosta, poniewaz nie zgadzalismy sie ze soba. Ojciec kategorycznie chcial jechac do Rumunii, by tam dolaczyc do wladz polskich. Ja mu jednak mowilem, ze rzad nie zostanie tam dlugo, a bedzie uciekal dalej na zachod - do Francji, badz Wielkiej Brytanii. A tam bezpieczniej przez Wegry. Sytuacja byla patowa. I wtedy powiedzial do mnie ''Synu, udowodniles mi juz, ze jestes mezczyzna, twoja rana na ramieniu zdaje sie to potwierdzac. Sam mozesz wiec decydowac o swoim losie. Ja wybieram sie do Rumunii, to juz postanowilem. Podejdz do mnie, gdy zdecydujesz'' Po tych slowach wyszedl."
Tekst203a = "Decyzja byla trudna, lecz (w twoim przekonaniu) sluszna. Ojciec przyjal wiadomosc z kamienna twarza, jak zawsze. Zyczyl mi powodenia w podrozy i zyczyl mi, bysmy sie jeszcze kiedys spotkali. Na odchodnym polecil mi jeszcze swojego znajomego, oficera Askaldowicza, ktory rowniez ucieka przez Wegry. ''Powinien byc dla ciebie milym towarzyszem podrozy'' rzekl, po czym kazdy udal sie w swoja strone."
Tekst203b = "Momentalnie wybiegles z namiotu, goniac go, zanim odejdzie za daleko. Gdy usluszal twoja decyzje, nie kryl radosci. Godzine pozniej razem wyruszyliscie w kolejna podroz"
Tekst204a = "Towarzystwo (jak sie okazalo) twej bratniej duszy bardzo podnioslo cie na samopoczuciu. Mimo, ze juz zdobyl stopien podporucznika, byl zaledwie 4 lata starszy od ciebie. Dogadywaliscie sie swietnie, co pomagalo w znoszeniu trudow drogi. A ta nie byla latwa. Permanentne uczucie glodu doskwieralo niemilosiernie, znosiliscie to jednak z godnoscia. Zreszta, wkrotce dotarliscie nad granice polsko-wegierska. Zauwazyliscie duzo oddzialow sowieckich obsadzajacych granice, jednak wciaz bylo ich za malo, by calkowicie zagrodzic przejscie, szybko sie wiec przedostaliscie na druga strone. Potem poszlo juz latwo. Dolaczyliscie do grupki polskich zolnierzy w obozie internowania tak jak wy udajacych sie na zachod. Z tych ''obozow'' mozna bylo w kazdej chwili wyjsc, totez juz w polowie listopada, idac przez Jugoslawie i Wlochy, dotarlismy do Polskich Sil Zbrojnych we Francji. Jedyne czego zalowales, to tego, ze nie udalo ci sie wziac ze soba ojca."
Tekst204b = "Podroz okazala sie byc o wiele ciezsza, niz sie spodziewaliscie. Bardzo szybko zaczelo brakowac wam jedzenia. Rodzilo to pospiech. Jednak naokolo roilo sie wrecz od sowietow, szukajacych uciekinierow, takich jak wy. Twoj ojciec nie oszczedzal jednak ani siebie, ani ciebie. Twoja rana zaczela dawac sie we znaki, jednak nic o tym nie mowiles, gdyz nie chciales spowalniac marszu. Okazalo sie to jednak dla was zguba. Nieuwaga na granicy spowodowala, ze wpadliscie w zasadzke wroga. Pojmanych i spetnych wywiezli was wglab Rosji. Nie wiecie, gdzie dokladnie jesescie, jednak nie spodziewacie sie zbyt przyjaznej okolicy. W koncu zamykaja was, razem z innymi jencami, w obozie pracy."
Tekst204b1 = "Okrutne traktowanie sprawilo, ze twoj stan pogarszal sie z dnia na dzien. Lecz dopoki twoj ojciec byl z toba, dawales rade. Jednak i jego ci odebrali. Chory, wynedznialy, daleko od domu i zupelnie sam zmarles w zimnej celi gulagu..."
Tekst205a = "23 I 1940 rok"
Tekst206a = "Nie jest ze mna najlepiej. Po dotarciu do Paryza moja rana zaczela mi dokuczac. Po tygodniu lezalem juz sparalizowany w lozku. Na szczescie Janek mial rodzine w Paryzu, wiec mialem sie gdzie zatrzymac. Lezac w lozku mialem czas na rozmyslenia. Bardzo martwilem sie o mojego ojca - powinien juz byc. Na razie wszyscy probuja mnie pocieszac, jednak nie moge przestac o tym myslec. Nie wiem, co robic dalej. Nowy rzad zaczyna zbierac armie, ale nie jestem przekonany, czy to jakos pomoze. Zwatpilem w sens dalszej walki. Bo co moge ja, zolnierzyk nie mogacy samodzielnie trzymac karabinu?"
Tekst206b = "Martwie sie o ojca. Nie rozstalismy sie w zbyt przyjaznych stosunkach, wiec nie wybaczylbym sobie, gdyby umarl, uwazajac mnie za niedojzale dziecko. By nie myslec o tym, oraz by udowodnic swoja przydatnosc, postanowilem dolaczyc do Wojska Polskiego we Francji. Janek jest ze mna. Rozmawialismy troche na temat dalszych wydarzen. On jest nastawiony optymistycznie, jednak ja nie moge pozbyc sie watpliwosci."
Tekst207a = "15 IV 1940 rok"
Tekst208a = "Im wiecej czasu mijalo, im dluzej ojciec wciaz sie nie pojawial, tym bardziej zrospaczony sie stawales. Depresja wpedzila cie w alkoholizm. Mimo ze twoja rana juz wyzdrowiala, ty dalej siedziales w domu. W koncu Janek postanowil zainterweniowac. ''Nie mozesz ciagle siedziec w domu! Tam na zewnatrz trwa wojna. Hitler ruszyl na polnoc. Twoj ojciec nie chcialby bys tak skonczyl. Wes sie w garsc! Wciaz werbuja ochotnikow do wyruszenia na walki do Norwegii. Idziesz ze mna?"
Tekst208b = "Ojca dalej nie ma. Ostatnie dni byly bardzo ciezkie. Czuje sie coraz gorzej. Na szczescie wysylaja mnie do Norwegii - Hitler wreszcie wkonal ruch. Byc moze gdy znow rusze do walki poczuje sie lepiej"
Tekst209a = "''Zostaw mnie w spokoju! Idz walcz sobie za tych zdrajcow!'' Wyzucilem go z jego wlasnego mieszkania i zamknalem sie na cztery spusty. Chyba tylko z litosci nie wyzucil mnie pod most."
Tekst209a1 = "On pojechal na wojne do Norwegii, a tymczasem wojna przyszla do Francji. Ty jednak nawet tego nie zauwazyles. Dzien w dzien pijany lezales na kanapie w salonie, ruszajac sie czasem tylko po to, by cos zjesc. Gdy zapasy jedzenia sie skonczyly, postanowiles wyjsc i cos kupic. Wpadles pod samochod tuz po wyjsciu z domu..."
Tekst209b = "Po chwili milczenia odpowiedzialem ''Masz racje. Daj mi jeden dzien''"

Tekst31 = "8 V 1940 rok"
Tekst32 = "Wreszcie, po dlugich przygotowaniach, wyruszylismy na front. Wyladowalismy w porcie Harstad. Piekno norweskiego krajobrazu z poczatku mnie zafascynowalo. Jednak szybko otrzasnalem sie z zachwytu. Nie przyplynalem tu by podziwiac widoki. Wkrotce mrozny polnocny klimat wdal sie we znaki. Mimo poczatku maja temperatura wacha sie w okolicach 10 stopni Celsjusza. Jednak pogoda nie jest naszym najgrozniejszym wrogiem."
Tekst33 = "27 V 1940 rok"
Tekst34 = "Dolaczylem do 2 batalionu stacjonujacego rejonie Melik i Sorviku. Przez trzy ostatnie tygodnie obserwowalismy pozycje nieprzyjaciela, czekajac, az alianci przygotuja sie do ataku. Jednak, tuz przed rozoczeciem ataku, dowodztwo podielo decyzje o ewakuacji ze wzgledu na sytuacje we Francji, ktora ,wkrotce po naszym przybyciu tutaj, tj. 10 maja, zostala zaatakowana przez niemcow. Mimo to general Bethuart postanowil przed wycofaniem sie zdobyc Narwik. W tym celu nasza Brygada ma za zadanie zaatakowac pozycje niemieckie na polwyspie Ankenes. Wedlug naszego wywiadu wrogiego przyczulka broni ok. 400 zolnierzy, jednak ich pozycje sa dobrze przygotowane i zamaskowane, w dodatku chronione przez pole minowe. Zadanie to nie bedzie latwe."
Tekst35 = "3 VI 1940 rok"
Tekst36 = "Udalo nam sie! Zmusilismy niemcow do odwrotu! Bitwa trwala jednak na tyle dlugo, ze 1 batalion zdolal dotrzec do Narwiku dopiero 29 maja, czyli juz po zdobyciu miasta. Alianci docenili nasz wklad w cala bitwe - general Bethouart telefonicznie pogratulowal naszemu dowodcy sukcesow bojowych. Wszyscy swietowali nasze pierwsze wspolne zwyciestwo nad III Rzesza. Teraz wesola atmosfera nieco przygasla, gdyz przygotowujemy sie do powrotu do Francji. Informacja o inwazji byla dla nas szokujaca. Niektorzy nawet twierdza, ze nie ma juz gdzie wracac, jednak po ostatnim zwyciestwie ciezko jest myslec pesymistycznie."
Tekst37 = "26 VI 1940 rok"
Tekst38 = "Ten wpis pisze dzien po kapitulacji Francji. Jak sie zapewne domyslasz, sytuacja jaka tam zastalismy, byla gorsza niz przypuszczalismy. Wyladowalismy W Bretanii 8 czerwca i od razu natrafilismy na ogromne oddzialy wroga. Po kilku ciezkich bitwach zrozumielismy, ze nie mamy szans. Cala brygada rozproszyla sie. Wiekszosc, w tym ja i Janek, udala sie na wyspy brytyjskie. Reszta dolaczyla do nowo powstalego francuskiego ruchu oporu. Znow nie czuje sie za dobrze. Gdzie nie uciekne, wojna zawsze mnie dopadnie. Zdalem sobie rowniez sprawe z tego, ze juz nie mam szans na spodkanie ojca - przynajmniej w najblizszy czasie. Minelo zbyt dlugo czasu od naszego rozstania, by ciagle byl w drodze. Musialo go cos bardzo powaznego zatrzymac. Mam nadzieje, ze przynajmniej zyje, nawet jesli w niewoli..."

Tekst41a = "8 XI 1940 rok"
Tekst41b = "Znalazlem dom w Anglii i do tej pory w nim mieszkam. Przygarnal mnie i Janka jeden z pilotow angielskich. Bardzo mily czlowiek, jednak nie widujemy sie zbyt czesto, poniewaz niemcy poszli za ciosem i w lipcu rozpoczeli nalot wysp. Na szczescie brytyjski RAF, razem z naszymi dywizjonami odparl najezdzcow. Byly to najgorsze miesiace w moim zyciu. Na moich oczach rogrywala sie bitwa mogaca roztrzygnac losy tej wojny, a ja moglem sie jej tylko biernie przygladac. By czyms sie zajac zaczalem chodzic na kursy jezyka angielskiego. Nie dolaczylem do wojska, poniewaz chce wrocic do Polski, by tam rozpoczac walke z okupantem. Jest to na razie poz moim zasiegiem, wiec probuje chociaz troche wynagrodzic mojemu gospodarzowi jego dobroc, zaczynajac pracowac. Do tego jednak musze umiec sie porozumiewac - przynajmniej na poziomie podstawowym."
Tekst42a = "26 II 1941 rok"
Tekst42b = "U mnie wszystko w porzadku. Znalazlem dobrze platna prace, wiec moge juz sam sie utrzymywac. Wlasnego mieszkania jeszcze, co prawda, nie mam, ale co sie odwlecze, to nie uciecze. Sledze jeszcze sytuacje w wojnie, jednak nie wiem, czy wroce na front. Nie wiem tez, czy bede w stanie wrocic do domu, bo szala zwyciestwa nie jest przechylona na nasza strone. Wygrana bitwa o Anglie nie zmienia duzo w naszym polozeniu, poniewaz jestesmy de facto zamknieci na tych wyspach. Linia frontu calkowicie oddalila sie juz od Polski, pewnie niepredko tam wroci. Hitler skupil sie na poludniu - dolaczyl niedawno do Mussoliniego w Afryce. Mimo to Janek dolaczyl do armii - jako oficerowi moze bedzie mu latwiej cos osiagnac. Byc moze jeszcze kiedys sie spodkamy. Niestety musze juz konczyc pisac. Niedlugo zaczynaja sie moje lekcje angielskiego - mimo iz umiem juz dosyc dobrze poslugiwac sie tym jezykiem, wciaz widac roznice miedzy mna, a rodowitymi brytyjczykami."
Tekst43a = "7 VII 1941 rok"
Tekst43b = "Znow jestem wojsku. Decyzje podjalem pod koniec czerwca, gdy z gazety dowiedzialem sie, ze III Rzesza wypowiedziala wojne Zwiazkowi Radzieckiemu! To jest nasza szansa. Historia lubi sie powtarzac. Jak w 1914, nasi zaborcy zaczeli walczyc miedzy soba, a wiadomo, ze gdzie dwoch sie bije, tam trzeci korzysta! Napisalbym cos wczesniej, gdyby nie to, ze od razu zaczalem przygotowania. Nie chce bowiem walczyc razem z brytyjczykami, chce walczyc w Polsce! Poza tym musialem zalatwic wiele spraw osobistych, takich jak zwolnienie sie z pracy i rozliczenie sie z moim wynajemca. Myslalem, ze znalezienie armii, ktora mialaby realne szanse na walczenie w Polsce nie bedzie latwe, jednak dzieki pewnym znajomosciom szybko trafilem na slad oddzialu spadochroniarzy, nazywajacych siebie cichociemnymi. Jest to grupa wyspecjalizowanych komandosow, zrzucanych na terenie kraju, w celu wspomozenia naszego Panstwa Podziemnego. Zostala zalozona przez kapitana Macieja Kalenkiewicza, za pozwoleniem Naczelnego Wodza, 20 czerwca ubieglego roku. Odbyly sie juz pierwsze zrzuty, najwczesniejszy w nocy z 15 na 16 stycznia. Do szkolenia mogl przystapic kazdy ochotnik, jednak nie kazdy zdawal. Zajeca sa bardzo wymagajace zarowno pod wzgledem fizycznym, jak i psychicznym. Oprocz wspinaczki na 5 metrowe sciany czy walki ucza nas tez jeszcze przetrwania w lesie, jezyka niemieckiego oraz naszej legendy - nowej tozsamosci, ktora musimy znac tak dobrze, jak swoja prawdziwa. Dodatkowo zadbali o takie szczegoly, jak praktyki z zawodow, ktore niby wykonujemy. Oczywiscie najwazniejszym punktem szkolenia jest kurs spadochroniarski, ktory odbywa sie w Largo House przy 4. Brygadzie Kadrowej zwanym ''Malpim Gajem''. Jest to bardzo nowy budynek, zbudowany okolo miesiaca temu z funduszy oficerow brygady. Ciezko mi jest porzucac zwyczajne zycie na rzecz ciezkich treningow, ale tak naprawde o tym marzylem - by wrocic do Ojczyzny. Poza tym, jest mozliwe, ze spotkam tam ojca."
Tekst44a = "7 VII 1942 rok"
Tekst44b = "Juz od dokladnie roku nic nie pisalem, a to ze wzgledu, ze nie dzialo sie do tego czasu nic szczegolnego. Wciaz trenuje i, biorac pod uwage moje postepy, dlugo to jeszcze potrwa. Cwiczenia sa niewiarygodnie wymagajace. Z trwoga patrze na wydarzenia na swiecie. W Afryce wciaz trwaja przepychanki z niemcami - tydzien temu armia brytyjska zatrzymala marsz Afrika Korps na Aleksandrie pod El Alameine. Na razie zdolali odepchnac wroga, ale sytuacja wciaz jest nieroztrzygnieta. Po nieudaniej Operacji Barbarossa, Hitler prubuje dobic ZSRR po raz drugi. Tym razem udal sie na Kaukaz. Bitwa o Woroniez, rozpoczeta 23 czerwca, skonczyla sie wczoraj porazka wojsk radzieckich. Tym razem sowietom zima moze nie pomoc. Za to po drugiej stronie swiata rozpoczela sie nowa wojna. 7 grudnia roku ubieglego japonczycy zbombardowali baze amerykanow Pearl Harbour na Hawajach. Od tamtej pory Stany Zjednoczone tocza walki na dwoch frontach i idzie im to calkiem sprawnie. Jednak widac wyraznie, ze wojna osiaga juz swoj punkt kulminacyjny - to, co zaczelo sie w Polsce przed trzema laty teraz dzieje sie na calym swiecie. Z dobrych wiadomosci jest to, ze Janek tez dolaczyl do cichociemnych. Znudzilo mu sie patrolowanie szkockiego wybrzeza razem z 1 Dywizja Pancerna, wiec postanowil dolaczyc do mnie. Postanowilismy juz, ze wylecimy razem, wiec mozliwe, ze bede musial troche na niego zaczekac, choc kto wie - on nie mial tak dlugiej przerwy, co ja."
Tekst45a = "15 IV 1943 rok"
Tekst45b = "Dostalismy pozwolenie na zrzut! Wreszcie mozemy leciec! Trening przyniosl oczekiwany skutek. Jestem w doskomalej formie. Gorzej z niemieckim. Nie uczylem sie go wczesniej praktycznie wogole. Zwyczajnie mi sie nie chcialo. Ciagle myli mi sie z angielskim, co nie ulatwia nauki. Teraz jednak place za to. Testy przeszedlem sciagajac - nie wiem, jakim cudem mi sie to udalo, ale zdalem. Janek jest nastawiony do tego troche sceptycznie, mowi, ze powinnismy jeszcze troche poczekac. Jednak ja chce juz leciec! III Rzesza slabnie - Zostala juz prawie calkowicie wyparta z Afryki, po bitwie pod Stalingradem znow zostali wyparci i mozliwe, ze niedlugo zaczna sie cofac. Mozliwe, ze wojna zbliza sie do konca."
Tekst46a = "Dlatego postanowilem leciec - nie ma czasu do stracenia! Dawno nie czulem takiej euforii! Lecimy w okolice Wilna. Mamy za zadanie wspomoc tamte oddzialy partyzantow. Zrzut odbedzie sie za dwa dni - do tego czasu mamy sie przygotowac. Nie moge sie juz doczekac."
Tekst46b = "Mimo to trzeba dzialac z rozsadkiem. Przez nastepne dwa miesiace skupie sie tylko na niemieckim i powinienem nadrobic zaleglosci. Chwila zwloki chyba bardzo nie zaszkodzi."
Tekst47a = "20 VIII 1943 rok"
Tekst47b = "Bylo ciezko, ale teraz na pewno jestem gotow. Przez ostatnie miesiace mowilem tylko po niemiecku -  prawdziwa katorga! Jednak to juz za mna - najwazniejsze to co przede mna. Wysylaja nas w okolice Wilna, jednak juz wiadomo, ze po przylocie bedziemy misieli sie jeszcze udac do Warszawy, by tam pomoc jednej z grup. Szczerze mowiac nigdy nie bylem w Warszawie, wiec jestem bardzo ciekawy wygladu stolicy, choc teraz, podczas okupacji, moze nie byc to mily widok. Tak czy siak juz jutro wylatujemy. Nie moge sie juz doczekac."

Tekst51a = "22 VIII 1943 rok"
Tekst52a = "Wyladowalismy bezpiecznie w okolicach Zanarocza. To tutaj swoja baze ma powstaly oddzial partyzancki pod dowodcem Antoniego Burzynskiego ps ''Kmicica''. Oddzial dziala juz od stycznia, w tej chwili liczy okolo 200 zolnierzy. Po przywitaniu sie i krotkiej rozmowie dowiedzialem sie o ostatnich akcjach oddizalu w Malych i Zodziszkach, oraz o planowanej wspolnej akcji z radzieckimi partyzantami w Madziole. Osobiscie nie podoba mi sie, ze oddzial utrzymuje tak bliskie stosunki z komunistami. Fakt, ze moja pierwsza walke stoczyem wlasnie z ZSRR sprawia, ze juz nigdy nie bede mogl im zaufac. Pozniej zjedlismy porzadny obiad i po krotkim odpoczynku ruszylismy w strone Warszawy."
Tekst51b = "18 IV 1943 rok"
Tekst52b = "Wyladowalismy bezpiecznie w okolicach Zanarocza. To tutaj swoja baze ma niedawno powstaly oddzial partyzancki. Dowodca oddzialu jest Antonii Burzynski ps. ''Kmicic''. Porucznik strescil nam sytuacje - trzy dni temu zaatakowali niemiecka staje kolejowa, niszczac urzadzenia stacyjne oraz zdobywajac bron i amunicje. Byl to tak naprwde chrzest bojowy oddzialu. Niepodobaja mi sie stosunki tutejszego oddzialu z partyzantami sowieckimi. 'Kmicic' probowal zyc z nimi w zgodzie, uwazam jednak, ze to blad. Fakt, ze moja pierwsza walke stoczyem wlasnie z komunistami sprawia, ze juz nigdy nie bede mogl im zaufac."
Tekst53a = "22 VIII 1943 rok"
Tekst53b = "Czuje sie tu swietnie. Moc znow znalezc sie w tym miejscu, moc poroumiewac sie w swoim wlasnym jezyku, przebywac ze swoimi rodakami - tego mi tak brakowalo we Francji i Wielkiej Brytanii. Dla tych rzeczy warto opuscic wygody zycia codziennego. Zreszta, nie jest tak zle. Nie zyjemy w pieciogwiastkowych hotelach, ale nie narzekam. Zaczynam doceniac prace, jaka wlozylem podczas treningu, poniewaz jest mi ona teraz niezmiernie przydatna. Zaprzyjaznilem sie rowniez z ''Kmicicem''. Razem uczestniczylismy juz w dwoch akkcjach - w nocy z 1 na 2 sierpnia zaatakowalismy niemiecki posterunek w Dunilowiczach. Zabilismy kilku niemcow, zdobylismy kilka sztuk pistoletow maszynowych PM-84, karabiny przeciwpancerne, amunicje oraz zywnosc. Kolejna akcja byla wieksza. Rowniez w nocy, z 14 na 15 sierpnia zaatakowalismy zaloge miasteczka Zodziszki. Stanowilo ja 50 zandarmow niemieckich i 80 policjantow niemieckich. Miasteczko udalo sie opanowac bez strat wlasnych. Zdobylismy oczywiscie bron, amunicje, ale i umundurowanie i zywnosc.  Wszystko szlo po naszej mysli. Oddzial liczy juz okolo 200 zolnierzy. Jest to dla nas wielki sukces. Dostalem jednak informacje, ze ja i Janek mamy sie udac do Warszawy i wspomoc znajdujaca sie tam grupe AK. Szkoda mi opuszczac 'Kmicica', ale rozkaz to rozkaz. Misja ma potrwac 2 tygodnie, po czym bede mogl wrocic tutaj. W gruncie rzeczy to nawet sie ciesze, ze bede mogl zobaczyc Warszawe. Nigdy tam nie bylem, a slyszalem, ze jest piekna. Choc podczas okupacji moze to byc przykry widok."
Tekst53c = "Przed odjazdem zegnasz sie jeszcze z 'Kmicicem'. Porucznik podziekowal ci za pomoc i wyrazil nadzieje, ze niedlugo sie jeszcze spotkacie."
Tekst53d = "-Szkoda, ze musisz jechac. Przydalbys sie podczas akcji na Madziole."
Tekst53e = "- Rzeczywiscie szkoda."
Tekst53f = "- Do zobaczenia wiec."
Tekst54a = "- Do zobaczenia"
Tekst54b = "- Mam do ciebie jeszcze jedna prosbe."
Tekst54c = "- Slucham."
Tekst55a = "- Uwazaj na siebie."
Tekst55b = "- Nie ufaj komunistom. Najlepiej wogole przestan z nimi rozmaniac. Nie ufam Markowowi."
Tekst55c = "- Nie moge tego zrobic. Markow jest mi potrzebny. W ten czwartek spotykam sie z nim, by ustalic plany akcji Madziol."
Tekst55d = "- Nie potrzebujecie ich pomocy. Nie jest tego warta. Soweci moga znow wbic nam noz w plecy, jak to zrobili na poczatku wojny. W dodatku z pewnoscia sa bardzo osmieleni zblizajaca sie Armia Czerwona. Prosze cie ostatni raz - nie ufaj im!"
Tekst55e = "- Dobrze. Nie zaufam - powiedzial po chwili - postaram sie zorganizowac akcje samodzielnie."
Tekst56 = "Po tych slowach uscisneliscie sobie dlonie na pozegnanie, a ty z Jankiem ruszyliscie w strone Warszawy."
Tekst501data = "23 VIII 1943 rok"
Tekst501 = "Przybywasz do Warszawy. Tutaj rozstajesz sie z Jankiem, ktory ma sie udac do Pragi, podczas gdy ty idziesz na Wole. Masz sie spotkac z Aleksandrem Enderem na skrzyzowaniu ulicy Bema i Dworskiej o godzinie 12:00. Gdy juz jestes na miejscu, okolo wyznaczonej godziny podchodzi do ciebie mezczyzna."
Tekst501a = "- Przepraszam pana, ktora godzina?"
Tekst501b = "- Wydaje mi sie, ze juz czas."
Tekst501c = "- Chyba ma pan racje"
Tekst501d = "Po tej wymianie hasel uscisneliscie sobie dlonie."
Tekst501e = "- Nazywam sie Aleksander Ender, ale chyba juz pan to wie."
Tekst501f = "- Witam, Leon Rozbicki, milo mi."
Tekst501g = "Udaliscie sie w strone Wolskiej."
Tekst501h = "- Jak sie panu podoba Warszawa?"
Tekst501i = "- Naprawde piekne miasto. Bylem juz w Paryzu i Londynie, jednak to miejsce najbardziej przypadlo mi do gustu."
Tekst501j = "- Tylko troche tu za duzo cudzoziemcow, co nie?"
Tekst501k = "- Prawda - zasmiales sie - Dlugo pan tu mieszka?"
Tekst501l = "- Od czterech lat. Przyjechalem tu na studia, ale wojna pokrzyzowala moje plany."
Tekst501m = "Mijacie ulice Klaczkowska."
Tekst501n = "- Gdzie moge sie zatrzymac?"
Tekst501o = "- Dostales mieszkanie przy ulicy Staszica. Zmierzamy teraz w jej kierunku."
Tekst501p = "- Dlaczego nie spotkalismy sie w tamtym miejscu?"
Tekst501r = "- Chcialem ci troche pokazac miasto, a poza tym..."
Tekst501s = "Podchodzi do was trzech gestapowcow."
Tekst501t = "-Kontrola dokumentow, poprosze o panskie dowody osobiste."
Tekst501u = "Z lekkim niepokojem podajesz podrobiony dowod i czekasz na reakcje. Policjant przyglada ci sie chwile, po czym oddaje ci je. Jednak z papierami Endera jest cos nie tak."
Tekst501w = "- Pan pojdzie z nami."
Tekst501y = "Przerazony Ender probuje sie tlumaczyc, lecz nic to nie zmienia. Wystraszonym wzrokiem patrzy na ciebie. Wiesz, ze tlumaczenia nic w tej sytuacji nie pomoga. Rozgladasz sie. Na skrzyzowaniu zauwazasz karetke gestapo. Jedynym wyjsciem jest..."
Tekst502a = "Wyciagasz noz ukryty pod kurtka i szybkim ruchem precinasz gestapowcowi tetnice szyjna. Zaskoczony pada, bryzgajac krwia po chodniku. Ender, rownie zaskoczony, co dwoch pozostalych hitlerowcow, zaczyna biec w strone Siedmiogrodzkiej. Nazisci w samochodzie jeszcze sie nie zorientowali, jednak pozostali zandarmii sa poza zasiegiem twojego noza. Postanawiasz wiec..."
Tekst502b = "Bezradnie patrzysz, jak gestapowcy zabieraja Endera ze soba. Wiesz, ze nie mogles nic zrobic. Nie wiedzac, co zrobic, postanawiasz pojsc na ul. Staszica. Nie wiedzac nawet, ktory to jest budynek, krazysz po drodze. Na szczescie znajduja cie inne osoby z oddzialu Endera rowniez znajace haslo. Opowiadasz im o wpadce przed chwila, w czasie gdy oni zaprowadzaja cie do twojego nowego mieszkania."
Tekst503a = "Huk strzalow roznosi sie po calej ulicy. Nie ma watpliwosci, ze teraz wszyscy niemcy w promieniu 500 metrow beda cie gonic. Przebiegasz przez ulice, doganiajac Endera. Wbiegajac w Siedmiogrodzka dostrzegasz katem oka, ze karetka juz jedzie w twoja strone..."
Tekst503b = "Postanawiasz nie ryzykowac i zwyczajnie uciekasz. Dwoch niemcow jeszcze strzela do ciebie, ale nie zamierza cie gonic. Zanim karetka zorientowala sie kogo ma scigac, wy juz biegliscie zaulkiem w strone ulicy Kleczkowskiej. Tam Ender zaprowadzil cie do zaprzyjaznionej apteki. Okazalo sie, ze oberwal w noge, jednak dzieki adrenalinie mogl biec dalej. Teraz jednak rana powalila go. Po opatrzeniu rany aptekarz zadzwonil po kogos, by odebrali was stad, gdyz nie bylo tam bezpiecznie. Chwile pozniej juz jechaliscie samochodem w strone twojego nowego mieszkania."
Tekst504a = "Szybki skret w zaulek eliminuje pojazd z poscigu, jednak to jeszcze nie koniec. Nazisci widzieli, gdzie skrecasz, wiec juz po chwili poczules na karku oddech szesciu z nich. Moglbys dawno im uciec, gdyby nie to, ze musisz czekc na Endera. Nie ma on najlepszej kondycji. Caly zaulek ma okolo 100 metrow dlugosci, jednak na lewo widzisz zakret. Wybierasz..."
Tekst504b = "Szybko wbiegliscie do kamienicy. Jednak okazal sie to fatalny pomysl. Nazisci widzieli gdzie idziesz, wiec wkrotce wejscie i zarazem jedyne wyjscie bylo oblegane przez szesciu zandarmow. Postanowiles walczyc do konca, gdyz poddac sie nie bylo sensu. Ustanowiliscie sie z Enderem u szczytu schodow  i z tamtad strzelaliscie do wrogow. Nim skonczyla wam sie amunicja, padlo dwoch, nozem zarznoles trzeciego. Jednak nim dopadles czwartego, zdazyl on wpakowac ci caly magazynek w piers..."
Tekst505a = "Znow wybiegasz na ulice, tym razem jest to ul. Kleczkowska. Po lewej masz drzwi Apteki. Na przeciwko, po drugiej stronie drogi, sa drzwi do jednego z blokow. Co sil w nogach biegniesz..."
Tekst505b = "Jednak za pozno dostrzegasz, ze jest to slepy zaulek. Nim zdolales zawrocic, gestpowcy juz was dopadli. Zostajesz rozstrzelany w cieniu warszawskich budynkow..."
Tekst506b = "Szybko znikneliscie z pola widzenia Gestapo i wbiegliscie do apteki. Farmaceuta, z poczatku zdziwiony, najwyrazniej zrozumial, o co chodzi. Szybko zaprowadzil was do tylniego wyjscia, a sam wrocil za lade. Okazalo sie, ze drzwi prowadza na slepy zaulek, odchodzacy od tego, w ktorym dopiero co byliscie. Cicho przekradasz sie do wyjscia na ulice Kleczkowska. Na lewo widzisz dwoch niemcow biegnacych zdloz ulicy. Innych nie widzisz, znaczy to, ze pewnie przeszukuja apteke. Idziesz wiec na prawo. Znow jestescie na ul. Bema. Po prawej widzisz tlum ludzi przygladajacy sie miejscu zbrodni. Oddalasz sie od tamtego miejsca i jak najszybciej wchodzisz do jakiejkolwiek kamienicy."
Tekst506c = "- O Matko Boska! Udalo nam sie! Zyjemy!"
Tekst506d = "- Znales tego aptekarza?"
Tekst506e = "- Tak... Zaopatrywal nasz oddzial w opatrunki. Teraz przez nas bedzie mial duze klopoty. Dlaczego w ogole tam pobiegles?"
Tekst506f = "- Spontaniczna decyzja. Krotko mowiac, mielismy szczescie."
Tekst506g = "- Cholernie duzo szczescia! Ze tez ta kontrola musiala sie napatoczyc..."
Tekst506h = "- Zostawiles tam swoj dowod osobisty!"
Tekst506i = "- Nie martw sie. Wszystkie informacje tam byly falszywe, lacznie z data urodzenia."
Tekst506j = "- Co teraz robimy?"
Tekst506k = "- Jezeli chcemy jeszcze dzisiaj stad wyjsc, powinnismy zrobic to zanim zjedzie sie tu pol miasta."
Tekst506a = "Juz byles w polowie drogi, gdy gestapowcy otwieraja ogien. Dwie kule przebijaja ci pluca. Padasz na samym srodku ulicy. Po 2 minutach umierasz, tonac we wlasnej krwi."
Tekst511a  = "W srodku juz czekal na ciebie podporucznik AK Teodor Pajewski. Wiadomosc o zatrzymaniu Endera bardzo go zmartwila."
Tekst511a1 = "- Nasza sytuacja tu jest trudna. Kazdy czlowiek jest na wage zlota. Nie mozemy sobie pozwolic na bledy."
Tekst511a2 = "- Mial lewe papiery. Gestapo rozpoznalo je."
Tekst511a3 = "Komendant zafrasowal sie jeszcze bardziej."
Tekst511a3 = "- Widziales te dokumenty? Widziales cos, co moglo zwrocic uwage gestapowcow?"
Tekst511a4 = "- Nie."
Tekst511a5 = "- Coz, nic nie mogles zrobic. Zostawmy to na razie. To moje zmartwienie. Ty na razie ciesz sie z nowego mieszkania. Bardzo sie nam tutaj przydasz. Twoje bagaze juz przybyly. Twoj przyjaciel, Jan Askaldowicz, przywiozl je jakies pol godziny temu. Pozdrawia cie. Podejdz do mnie jutro, szykuje sie dla ciebie zadanie."
Tekst511b  = "W srodku juz czekal na was podporucznik AK Teodor Pajewski. Gdy zobaczyl krwawiacego Endera, zmarszczyl brwi."
Tekst511b1 = "- Co sie do diaska stalo!?"
Tekst511b2 = "- Zandarmii rozpoznali moje lewe papiery. Rozycki mnie uratowal przed wiezieniem."
Tekst511b3 = "- Cholera, masz krew na rekach!"
Tekst511b4 = "- Zabilem jednego z nich nozem. Po cichu, zeby nie zwrocic uwagi karetki gestapo."
Tekst511b5 = "- Taka akcja w bialy dzien... Dobrze sie to nie skonczy. Jednak na razie nie masz sie czym martwic. Bagaz juz przybyl. Twoj przyjaciel, Jan Askaldowicz, przywiozl je jakies pol godziny temu. Pozdrawia cie. Przyda ci sie dzisiaj odpoczynek, bo jutro bede mial dla ciebie duzo roboty. Ender na jakis czas jest zwolniony z wszelkich dzialan z oczywistych powodow."
Tekst511c  = "Wreszcie docieracie na miejsce. W srodku juz czekal na was podporucznik AK Teodor Pajewski. Nie byl zadowolonny."
Tekst511c1 = "- Coscie najleprzego narobili! Cholera, cale miasto trabi o tej strzelaninie. Poza tym, zamkneli Fabickiego."
Tekst511c2 = "- Kogo?"
Tekst511c3 = "- Atekarza, ktory wam pomogl. Dlaczego w ogole zaczeliscie strzelanine?"
Tekst511c4 = "- Zandarmii rozpoznali moje lewe papiery. Rozycki mnie uratowal przed wiezieniem."
Tekst511c5 = "- Cholera, masz krew na rekach!"
Tekst511c6 = "- Zabilem jednego z nich nozem. Reszte zastrzelilem."
Tekst511c7 = "Komendant przyjrzal wam sie z zaciekawieniem."
Tekst511c8 = "-Naprawde, zaimponowales mi. Nie jestes nawet drasniety! Niezle was tam wyszkolili w Anglii. Bardzo sie nam przydasz w tej chwili. Nasza sytuacja tu jest trudna. Kazdy czlowiek jest na wage zlota. Ender jest uziemiony na jakis czas, gdyz musi czekac na nowe dokumenty. Zglos sie do mnie jutro. Mam zadanie odpowiednie dla ciebie."

Tekst1a = "24 VIII 1943 rok"
Tekst1b = "Przychodzisz do dowodcy o umowionej porze. Od razu zaczyna ci streszczac cala sprawe."
Tekst1b1 = "-Moj oddzial od dawna szykuje zasadzke na Clausa von Stauffenberga, jednak ciagle brakuje nam o nim informacji. Twoim zadaniem jest dowiedziec sie, kiedy najdogodniej jest go zaatakowac i z jak duza eskorta sie porusza. Informacje te mozesz zdobyc od Klausa Schmidta, zandarma, ktorego udalo nam sie porwac przed trzema dniami. Znajduje sie on teraz w piwnicy - trwa juz jego przesluchanie. Pojdz tam jak najszybciej. Informacje o eskorcie von Stauffenberga mozesz uzyskac od informatora. Umowilismy sie na spotkanie 26, czyli za dwa dni, na cmentarzu prawoslawnym przy ulicy Wolskiej. Pojdz tam, ale sam, gdyz nasz szpicel jest nieco podejrzliwy."
Tekst1b2 = "Udajesz sie wiec do piwnicy i nim wchodzisz do srodka, juz slyszysz krzyki..."
Tekst1b3 = "Zblizajac sie do celi glos nasila sie. Otwierasz dzrzwi i widzisz wysokiego bruneta nachylonego nad postacia na krzesle. Mezczyzna patrzy na ciebie i, ocierajac krople potu z czola mowi:"
Tekst1b4 = "-Twarda sztuka. Mecze go juz dwie godziny, a ten tylko jeczy - podaje ci rekawiczki i, wychodzac, dodaje - Moim zdaniem to tylko stata czasu..."
Tekst1b5 = "Slyszysz trzask drzwi i skupiasz zwrok na wymeczonym gestapowcu. Jest w polowie rozebrany, a na swoim smuklym ciele ma wiele drobnych ran, z ktorych saczy sie krew. Jego twarz jest cala w siniakach, a nos skrzywiony. Podnosi twarz i patrzy ci sie w oczy. Przechodza cie delikatne ciarki i pojawia sie pytanie, czy jest to jednak nadal czlowiek, czy juz tylko puste cialo."
Tekst1b6 = "-Powiedz mi wszystko co wiesz o Clausie von Stauffenbergu lub bede musial dokonczyc robote mojego poprzednika."
Tekst1b7 = "Nie wyglada jakby chcial odpowiedziec i po prostu odwraca wzrok."
Tekst2a  = "Zakladasz rekawiczki i piescia uderzasz go w twarz, powtarzajac pytanie. Klaus pluje krwia, lecz nie widac nawet grymasu na jego twarzy. Stwierdzasz, ze to nadal za malo celujesz teraz w zebra. Zaczyna krzyczec z bolu i widzisz, ze ma problem ze zlapaniem oddechu. Pomiedzy jekami mozna uslyszec jakies slowa, ktore brzmia jak imiona. Zastanawiasz co dalej mozesz zrobic."
Tekst2b  = "Nie chcesz robic mu wiecej krzywdy, lecz misja jest priorytetem. Idziesz po szklanke z woda i obmywasz go nia zeby zlagodzic bol tylu ran. Siadasz przed nim i pytasz, jak ma na imie, lecz on wciaz odwraca wzrok. Zaczynasz go zagadywac, pytac, co robil w przeszlosci, czy ma jakas rodzine. Nie przynosi to zadnych rezulatatow."
Tekst3c  = "Jedyne co przychodzi ci na mysl to po prostu rozmowa, nawet jesli ma nie przyniesc szybko rezultatow. W pewnym momencie Klaus przerywa mi."
Tekst3c1 = "- Po co mam ci cokolwiek mowic, co?"
Tekst3c2 = "- Zeby przezyc."
Tekst3c3 = "- Jak wy mnie nie zabijecie, zrobia to moi."
Tekst3c4 = "Usmiechasz sie. Wreszczie zaczal romawiac. Wspominasz, ze mozesz zalatwic mu azyl, jesli tylko wszstko ci powie. Pytasz sie, kiedy mozecie zaatakowac Clausa i czy wie moze cos jeszcze."
Tekst3c5 = "- Wydaje mi sie, ze najlepiej 29 wieczorem. Wyjezcza wtedy do swojej rodziny w Piasecznie. I tak mi na nim nie zalezy, a uwazam nawet, ze zasluguje na kare. Zajmijcie sie nim, ale prosze, oszczedzcie innych. Oni nic nie zrobili. Ale strzeszcie sie. Claus wie wiecej, niz sadzicie. Przygotowal zasadzke na waszego informatora. Jest jednak zbyt pewny siebie, a to moze go zgubic."
Tekst3c6 = "Zostawiasz wieznia i mowisz mu, ze nie musi sie o nic bac. Idziesz zdac raport."
Tekst3a  = "Grozisz, ze jezeli natychmiast nie zacznie wspolpracowac, cala jego rodzina zostanie zamordowana. Klaus tepym wzrokiem wpatruje sie w twoje buty."
Tekst3b  = "Masz tego dosc. Wychodzisz z pokoju i idziesz do malej kuchni, by zabrac buteleczke z octem. Wracasz do wieznia i jescze raz patrzysz na jego poranione cialo. Otwierasz butelke i wylewasz jej zawartosc na mala szmatke, po czym przyciskasz mu ja do klatki piersiowej. Mezczyzna krzyczy z bolu i przygryza wargi. Po chwili dalszych meczarni zaczyna plakac i wrzeszczy, zeby przestac. Na chwile odpuszczasz i pozwalasz mu mowic."
Tekst3b1 = "- Blagam! Blagam, przestan! P-powiem wszystko co wiem!"
Tekst3b2 = "- Mow, kiedy von Stauffenberg bedzie najlatwiejszym celem."
Tekst3b3 = "- Wydaje mi sie, ze 27! Moze byc... Nie jednak 29 bedzie lepszy. Tak! Jestem tego pewien, ze 29... wyjezdza wtedy do swojej rezydencji w Piasecznie. Bedzie ze swoja rodzina, calkowicie sam! Nie wiem nic wiecej, przysiegam... Tylko juz wiecej nie bij..."
Tekst3b4 = "Wylewasz na niego szklanke wody, zeby zlagodzic choc troche bol i zostawiasz go w sali. Zadowolony z rezultatu idziesz zdac raport."
Tekst4a  = "Z przyzwyczajenia klniesz po niemiecku. Zandarm, na dzwiek jego ojczystego jezyka ocknal sie gwaltownie z odretwienia, rozgladajac sie na wszystkie strony. Zaskoczony, postanawiasz wykorzystac pobudzenie twojego wieznia i stawiasz mu ultimatum. Reszta  rozmowy odbywa sie po niemiecku"
Tekst4a1 = "-To jest twoja ostatnia szansa! Nie chce cie bic, ale nie dajesz mim wyboru. Musze wiedziec wszystko o von Stauffenbergu."
Tekst11  = "26 VIII 1943 rok"
Tekst11a = "Wiedzac o zasadzce podeslales szpiclowi informacje o zmianie lokalizacji spotkania. Nowe miejsce to kamienica nieopodal cmentarza. Idziesz do niej wczesniej niz wedlug planu, zeby upewnic sie o bezpieczenstwie. Budynek jest dosc stary i opusczony, ale idealny na tajne spotkanie. Wchodzisz do jednego pokoj i siadasz na starej lawie, czekajac na informatora. Nagle slyszysz kroki. Ktos wchodzi do budynku."
Tekst11b = "Udajesz sie na cmentarz o umownionej godzinie, jednak przed wejsciem zauwazasz dwoch gestapowcow. Zdajesz sobie sprawe, ze cmentarz jest pewnie caly obstawiony, a informator moze byc w srodku. Nie masz wyjscia, musisz..."
Tekst12a = "W drzwiach staje niemiecki zolnierz i, zaskoczony, siega po pistolet. Szybkim ruchem chwytasz belke lezaca obok zanim ten cokolwiek zrobi i uderzasz go w glowe. Policjant pada na ziemie, tracac przytomnosc. Sprawnie zwiazujesz go sznurem lezacym obok i kneblujesz usta. Przy okazji przeszukujesz go i znajdujesz portfel w niezla sumka. Nieprzytomnego Niemca zamykasz w skladziku w piwnicy."
Tekst12b = "Stajac w drzwiach zauwazasz jak po schodach wchodzi niemiecki zolnierz. Wiesz, ze nie uda ci sie uciec, ale mozesz sie jeszcze schowac. Wskakujesz miedzy zdemolowane meble i chowasz sie w szczelinie. Starasz sie uspokoic i czekasz, az Niemiec opusci budynek. Wchodzi do pokoju i sie po nim rozglada, lecz nie jest chyba zbyt skurpulatny w tym co robi, bo nie znajduje cie i wycofuje sie w strone wyjscia. Po chwili wychodzisz z ukrycia"
Tekst12c = "...stad odejsc. Nie mozesz nic zrobic"
Tekst12d = "...wejsc do srodka i jakos ocalic szpicla. Ta informacja moze zawazyc na powodzeniu calej misji, nie mozesz jej stracic! Zakradasz sie wiec od tylu, przeskakujac mur. Gdy ostroznie zblizasz sie do miejsca spotkania, po drugiej stronie rzedu grobow, jakies 20 metrow od ciebie, zauwazasz swoj cel w towarzystwie trzech Niemcow. Zrezygnowany informator wlasnie zostaje skuty w kajdanki."
Tekst13a = "Gdy wracasz do pokoju, wewnatrz stoi juz mezczyzna ubrany w szary plaszcz. Nie masz watpliwosci, ze to twoj informator, siadacie wiec i rozpoczynacie rozmowe"
Tekst13a1 = "- Dzien dobry. Czy masz dla mnie informacje na temat Clausa von Stauffenberga?"
Tekst13a2 = "- Oczywiscie. A czy ma pan dla mnie pieniadze?"
Tekst13a3 = "Pytanie to calkowicie cie zaskoczylo. Pieniadze? Prawda, ze za informacje czesto sie placi, ale on o zadnej zaplacie wczesniej nie wspominal. Juz chciales sie klucic, gdy przypominasz sobie o pieniadzach Niemca. Kompletnie ci na nich nie zalezalo, wiec dales mu je. Sknerus, uradowany, wreszcie zaczal mowic"
Tekst13b = "Wygladasz przez okno i widzisz, ze policjant, wychodzac, natrafil na czlowieka w szarym plaszczu. Obaj mezczyzni zaczeli ze soba rozmawiac. Sadzac po gestykulacji nie jest to zwyczajna pogadanka. Mezczyzna moze byc rownie dobrze informatorem, co cywilem."
Tekst13c = "Nie ma czasu do stracenia. Kozystajac z zaskoczenia powinno ci sie udac zastrzelic wszystkich zandarmow, zanim ci wyciagna bron. Lecz twoj plan zawodzi. Jeden z Niemcow od poczatku trzymal w reku bron, wiec zdazyl pociagnac za spust, nim kula go dosiegnela. Szpicel padl na ziemie martwy, z dziura w glowie. Nie majac juz nic wiecej do roboty w tym miejscu, uciekasz do kwatery glownej."
Tekst13d = "Kucasz jeszcze bardziej i obserwujesz sytuacje. Grupa ruszyla: jeden zandarm z przodu, z tylu dwoch, a wiezien miedzy nimi. Po przyjrzeniu im sie zauwazasz w rece pierwszego pistolet. Udaja sie w strone wyjscia. Wyprzedzasz ich i chowasz sie za drzewem rosnacym blisko sciezki, ktora ida. Dokladnie powtarzajac sobie caly plan w glowie, czekasz az nadejda. Gdy pierwszy z Niemcow zaczyna cie mijac, wyskakujesz zza drzewa - nozem rozcinasz blizszemu szyje, reszte zabijasz z pistoletu, zanim w ogole pomysla o siegnieciu po bron. Bez zatrzymywania sie zabierasz z ciala kluczyki do kajdanek i ciagniesz skonfundowanego informatora na tyly cmentarza. Po uwolnieniu go i zaprowadzeniu w bezpieczne miejsce rozpoczynacie rozmowe."
Tekst14a = "W pewnym momencie rozmowcy rzucili sie na siebie. Z przerazeniem zobaczyles, ze zandarm trzyma w reku pistolet. Szybko biegniesz, by ich rozdzielic, lecz spuzniasz sie. Cywil dostal trzy razy w brzuch. Jednym strzalem w glowe zabijasz Niemca i podbiegasz do umierajacego. To z pewnoscia byl twoj informator, lecz teraz nie powie ci juz nic. Nie pozesz go ocalic, wiec..."
Tekst14b = "Od razu biegniesz, by pomoc mu. Gdy wybiegles z budynku, obaj juz sie bili. Wyciagasz swoj noz i unieszkodliwiasz Niemca."
Tekst14b1 = "-Nic ci ne jest?"
Tekst14b2 = "- N-nie. Ty pewnie jestes z AK. To mnie szukasz. Uratowales mi zycie. Nie wiem, jak ci dziekowac."
Tekst14b3 = "- Nie ma sprawy. Czy masz dla mnie informacje na temat Clausa von Stauffenberga?"
Tekst14b4 = "- Tak, oczywiscie. Wszystko ci powiem, tylko, jesli mozna, w srodku."
Tekst14b5 = "Gdy tylko sprzatnales cialo zandarma, obaj usiedliscie na lawce i rozpoczeliscie rozmowe"
Tekst15a  = "...skracasz jego cierpienia. Potem od razu, co sil w nogach uciekasz, zanim zobacza cie nadbiegajacy gestapowcy."
Tekst15b  = "... porzucasz go w tym miejscu. Od razu, co sil w nogach uciekasz, zanim zobacza cie nadbiegajacy gestapowcy."
Tekst16  = "Dowiedziales sie, ze Claus nigdy nie jest sam. Praktycznie zawsze jezdzi za nim cywilny samochod pelen Niemcow. Szczerze podziekowales za tak wazna informacje i udales sie do kwatery glownej."
Tekst21 = "29 VIII 1943 rok"
Tekst22a = "Wszystko jest dopiete na ostatni guzik. Na akcjie bierzesz czterech ludzi, gdyby cos poszlo nie tak. Kazdy z czlonkow twojego oddzialu zna plan na pamiec. Ruszyliscie do Piaseczna o takiej porze, by znalezc sie pod domem von Stauffenberga po zmroku. Gdy byliscie juz na miejscu nadszedl czas na ostatnia narade."
Tekst22b = "Pomimo ze nie udalo ci sie zdobyc informacji od informatora, poprowadzisz te akcje. Sadzac po tym, co powiedzial ci Schmidt nie powinna to byc trudna misja. Ze soba bierzesz dwoch ludzi: Znicza i Kreta. Obaj znaja plan dzialania na pamiec. Ruszyliscie do Piaseczna o takiej porze, by znalezc sie pod domem von Stauffenberga po zmroku. Gdy byliscie juz na miejscu nadszedl czas na ostatnia narade."
Tekst23a  = "Wybila godzina 20. Okolica byla pusta, posanowiliscie wiec sie troche zabawic. Gdy zlokalizowaliscie pojazd z ochrona Clausa, dwoch ludzi, Znicz i Kret, podlozylo pod podwozie ladunki wybuchowe. Po minucie noc rozswietlila kula ognia powstala w miejscu, w ktorym przed chwila znajdowal sie samochod. To byl dla was sygnal do rozpoczecia akcji. Rysiek zostal przed domem, natomiast ty i Husarz wywazyliscie drzwi i weszliscie do srodka. Nagle, z lewej strony ktos cie zaatakowal. Powaliles go na ziemie. Tym kims okazal sie byc 16-letni chlopak, najpewniej syn Stauffenberga. Zostawilsm go z Husarzem, a sam wbiegles do salonu. Tam znalazles Clausa. Stal kolo stolu, przy ktorym piec minut temu spozywal kolacje. Gdy na ciebie spojzal, zamurowalo go z przerazenia. Wycelowales mu w glowe i powiedziales"
Tekst23a1 = "- W imieniu Polskiego Panstwa Podziemnego skazuje cie na smierc za wyrzadzone zbrodnie."
Tekst23a2 = "Pociagnales za spust. Kula trafila von Stauffenberga prosto miedzy oczy. Nim cialo osunelo sie na ziemnie, ty juz wyszedles z pokoju. Zadanie bylo wykonane, mozna bylo wracac do Warszawy."
Tekst23b  = "Wybila godzina 20. Okolica byla pusta, posanowiliscie wiec sie troche zabawic. Gdy zlokalizowaliscie pojazd z ochrona Clausa, dwoch ludzi, Znicz i Kret, podlozylo pod podwozie ladunki wybuchowe. Po minucie noc rozswietlila kula ognia powstala w miejscu, w ktorym przed chwila znajdowal sie samochod. To byl dla was sygnal do rozpoczecia akcji. Rysiek zostal przed domem, natomiast ty i Husarz wywazyliscie drzwi i weszliscie do srodka. Nagle, z lewej strony ktos cie zaatakowal. Strzeliles w tamta strone dwa razy. Pod twoje nogi padlo cialo 16-letniego chlopaka, najpewniej syna Stauffenberga. Nakazales Husarzowi zostac na korytarzu, a sam wbiegles do salonu. Tam znalazles Clausa. Stal kolo stolu, przy ktorym piec minut temu spozywal kolacje. Gdy na ciebie spojzal, zamurowalo go z przerazenia. Wycelowales mu w glowe i powiedziales"
Tekst23b1 = "- W imieniu Polskiego Panstwa Podziemnego skazuje cie na smierc za wyrzadzone zbrodnie."
Tekst23b2 = "Pociagnales za spust. Kula trafila von Stauffenberga prosto miedzy oczy. Nim cialo osunelo sie na ziemnie, ty juz wyszedles z pokoju. Zadanie bylo wykonane, mozna bylo wracac do Warszawy."
Tekst23c  = "Wybila godzina 20. Okolica byla pusta, oprocz jednego przechodnia i paru samochodow zaparkowanych przy ulicy. Bez zwloki postanowiliscie rozpoczac akcje. Znicz zostal przed domem, natomiast ty i Kret wywazyliscie drzwi i weszliscie do srodka. Nagle, z lewej strony ktos cie zaatakowal. Powaliles go na ziemie. Tym kims okazal sie byc 16-letni chlopak, najpewniej syn Stauffenberga. Zostawilsm go z Kretem, a sam wbiegles do salonu. Tam znalazles Clausa. Stal kolo stolu, przy ktorym piec minut temu spozywal kolacje. Gdy na ciebie spojzal, zamurowalo go z przerazenia. Wycelowales mu w glowe i powiedziales"
Tekst23c1 = "- W imieniu Polskiego Panstwa Podziemnego skazuje cie na smierc za wyrzadzone zbrodnie."
Tekst23c2 = "Pociagnales za spust. Kula trafila von Stauffenberga prosto miedzy oczy. Nim cialo osunelo sie na ziemnie, ty juz wyszedles z pokoju. Zadanie bylo wykonane, mozna bylo wracac do Warszawy. Jednak nagle uslyszales strzaly, dobirgajace z zewnatrz. Wyjrzales przez okno i zobaczyles, jak Znicz pada na ziemie, krwawiac z trzech ran naraz. W jednym z aut ukrytych bylo czterech niemcow, ktorzy szli teraz w twoim kierunku. Zaczeliscie z Kretem strzelac do nich, ukryci za oknem, jednak nim zabiliscie wszyskich, twoj towarzysz oberwal w piers. Po chwili zaczal intensywnie pluc krwia. Pomogles mu wyjsc z domu, przejsc nad martwym juz Zniczem i dojsc do waszego auta. Tylko we dwojke odjechaliscie z powrotam w strone Warszawy."
Tekst23d  = "Wybila godzina 20. Okolica byla pusta, oprocz jednego przechodnia i paru samochodow zaparkowanych przy ulicy. Bez zwloki postanowiliscie rozpoczac akcje. Znicz zostal przed domem, natomiast ty i Kret wywazyliscie drzwi i weszliscie do srodka. Nagle, z lewej strony ktos cie zaatakowal. Strzeliles w tamta strone dwa razy. Pod twoje nogi padlo cialo 16-letniego chlopaka, najpewniej syna Stauffenberga. Nakazales Kretowi zostac na korytarzu, a sam wbiegles do salonu. Tam znalazles Clausa. Stal kolo stolu, przy ktorym piec minut temu spozywal kolacje. Gdy na ciebie spojzal, zamurowalo go z przerazenia. Wycelowales mu w glowe i powiedziales"
Tekst23d1 = "- W imieniu Polskiego Panstwa Podziemnego skazuje cie na smierc za wyrzadzone zbrodnie."
Tekst23d2 = "Pociagnales za spust. Kula trafila von Stauffenberga prosto miedzy oczy. Nim cialo osunelo sie na ziemnie, ty juz wyszedles z pokoju. Zadanie bylo wykonane, mozna bylo wracac do Warszawy. Jednak nagle uslyszales strzaly, dobirgajace z zewnatrz. Wyjrzales przez okno i zobaczyles, jak Znicz pada na ziemie, krwawiac z trzech ran naraz. W jednym z aut ukrytych bylo czterech niemcow, ktorzy szli teraz w twoim kierunku. Zaczeliscie z Kretem strzelac do nich, ukryci za oknem, jednak nim zabiliscie wszyskich, twoj towarzysz oberwal w piers. Po chwili zaczal intensywnie pluc krwia. Pomogles mu wyjsc z domu, przejsc nad martwym juz Zniczem i dojsc do waszego auta. Tylko we dwojke odjechaliscie z powrotam w strone Warszawy"

Tekst521a = "6 IX 1943 rok"
Tekst521b = "Zycie w Warszawie jest cudowne - z pewnoscia bys tu zostal, gdyby nie twoja obietnica, ze wrocisz.  A czas powrotu sie zbliza. Zaczales sie nawet juz pakowac."
Tekst521c = "Od zakonczenia akcji w Piasecznie ciagle byles przy Krecie, lecz, niestety, chlopak po dwoch dniach zmarl w skutek odniesionych ran. Nie czules sie z tym najlepiej. Caly twoj oddzial zginal poczas pierwszej misji. Jednak starasz sie o tym nie myslec. Czas powrotu sie zbliza. Zaczales sie juz nawet pakowac."
Tekst522a = "Jednak podporucznik Pajewski ma dla ciebie jeszcze jedno zadanie. Nakazal ci sie spotkac w domu Endera przy ulicy Pawia. Czesto tam ostatnio jezdziles, odwiedzajac go. To bezczynne siedzenie w domu dobijalo go. Jestes siekaw, dlaczego spotykacie sie akurat tam. Gdy wchodzisz do srodka, obaj juz tam byli. Komendant przemowil perwszy."
Tekst522a1 = "- Nie bede owijal w bawelne. Wsrod nas jest zdrajca. Zebralismy sie tutaj, poniewaz baza nie jest juz do konca bezpieczna. Zaufalem tylko wam. Leonowi, bo jest z zewnatrz, a Aleksandrowi, poniewaz wiem, ze ciebie nie da sie niczym przekupic. Ender, wiem ze chcalbys wreszcie cos zrobic, jednak bardziej przydasz mi sie na miejscu. To Rozbicki bedzie dzialal w polu. Tyle mam wam do powiedzenia, reszte ustalcie miedzy soba."
Tekst522a2 = "Po tych slowach wyszedl."
Tekst522a3 = "- Zdrajca? U nas?"
Tekst522a4 = "- Masz jakies podejrzenia?"
Tekst522a5 = "- Nie... Nie wiem... Musze pomyslec."
Tekst522a6 = "- Nachodzilo cie ostatnio gestapo?"
Tekst522a7 = "- Nie. Nikt nie przychodzil. -zamyslil sie na moment - Jezeli chodzi o podejrzanych, to jest jeden. Tadeusz Trela. Na co dzien pracuje z szkopami, wiec ma kontakty. Mialby tez motyw - w oddziale niezbyt go lubia, poza tym nie jest zbyt bogaty."
Tekst522a8 = "- Masz jakies dowody?"
Tekst522a9 = "- Oczywiscie, ze nie. Gdybym mial, powiedzialbym je duzo wczesniej."
Tekst522a10 = "- Od dawna z nimi pracuje?"
Tekst522a11 = "- Od ponad roku."
Tekst522a12 = "- Wiec ten niemiec, ktorego niedawno przesluchiwlismy powinien go znac."
Tekst522a13 = "- Racja. Od niego mozesz zaczac. Ja moge ci tylko zyczyc powodzenia. Slyszales dowodce."
Tekst522a14 = "- Szkoda. Przydalbys mi sie bardzo."
Tekst522a15 = "Wychodzisz, udajac sie w strone kwatery glownej."
Tekst522b = "Jednak podporucznik Pajewski ma dla ciebie jeszcze jedno zadanie. Komendant osobiscie przyszedl do twojego domu. Wygladal na zmeczonego. Gdy tylko wszedl, od razu zaczal mowic."
Tekst522b1 = "- Nie bede owijal w bawelne. Wsrod nas jest zdrajca. Tobie jedynemu ufam, poniewaz jestes z zewnatrz. Chcialbym, zebys zajal sie nim. Nie musze chyba mowic, kto jest glownym podejzanym..."
Tekst522b2 = "Oczywiscie rozumiesz, o co mu chodzi. Mowi o Enderze, ktory przed czterema dniami zostal wypuszczony z wiezienia. Przez to wszystkie podejzenia spadaja na niego, ale ty sadzisz inaczej. Od czasu jego wyjscia odwiedzasz go czesto w domu i poznaliscie sie juz dosc dobrze."
Tekst522b3 = "- Nie masz innych podejrzanych?"
Tekst522b4 = "- Mam, ale uwazaj. Nie bron Endera za wszelka cene. Jest jeszcze Tadeusz Trela. Na co dzien pracuje z szkopami, wiec teoretycznie ma kontakty. Ale to sa tylko przypuszczenia. Skup sie na faktach, a te sa dosyc jednoznaczne. O akcji na ulicy Ogrodowej wiedzialy tylko osoby z oddzialu. Plan zostal ustalony tuz przed aresztowaniem Aleksandra, a niemcy ewidentnie wiedzieli o wszystkim. Stracilismy pieciu dobrych zolniezy. Nie chce, by ich ofiara poszla na marne..."
Tekst522b5 = "Po tych slowach wyszedl. Postanawiasz jeszcze raz przesluchac Schmidta. O Enderze nie bedzie nic wiedzial, zostal zlapany wczesniej, ale moze powie ci cos o Treli."
Tekst522c  = "Caly oddzial Pajewskiego urzadzil pozegnalna impreze dla ciebie. Akcja w Piasecznie przez dlugi czas bedzie dla nich symbolem walki i wyrtwalosci, ktorej czasem im brakuje. Na nastepny dzien jeszcze raz uscisnales dlon podporucznikowi oraz Enderowi, z ktorym szczerze sie zaprzyjazniles, i wyjechales w droge powrotna w strone Wilna."
Tekst522d  = "Pozegnales sie z podporucznikiem oraz z Enderem. Obaj podziekowali ci za pomoc, ktora im okazales. Reszta oddzialu tez cie zegnala, lecz czesc z nich obwiniala cie za smierc ich kolegi. Jednak te wydarzenia byly juz za toba. Nastepnego dnia razem z Leszkiem oposciliscie Warszawe."
Tekst523a  = "Zgodnie z twoja obietnica Schmidt nie jest juz wiezniem. Od kilku dni czeka jeszcze na przydzial w jakims innym miescie, gdyz tutaj zbyt wiele osob go zna. Znajdujesz go w malym pokoiku, w ktorym tymczasowo nocuje. Teraz, po tych paru dniach normalnego traktowania zmienil sie nie do poznania - przybral na masie, oczy odzyskaly blask. Jednak wciaz kazdy ruch sprawial mu pewna trudnosc."
Tekst523a1 = "- A, to ty. Dawno sie nie widzielismy. Dotrzymales obietnicy, wiec jestem ci chyba winny jakies podziekowania."
Tekst523a2 = "- Nie ma za co. Staram sie dotrzymywac umow. Teraz jednak zmowu potrzebuje twojej pomocy"
Tekst523b  = "Znow spotykasz sie z Klausem. Jego rany zabliznily sie o waszego ostatniego spotkania. Gdy wszedles do jego celi, lezal na pryczy, lecz na twoj widok szybko sie wyprostowal. Byl strasznie wychudzony, jeszcze bardziej niz ostatnio. W milczeniu wpatrywaliscie sie sobie w oczy."
Tekst523b1 = "- Znow potrzebuje twojej pomocy. Mam nadzieje, ze tym razem dojdziemy do porozumienia szybciej, niz ostatnio."
Tekst523b2 = "Schmidt zadrzal lekko na wspomnienie tamtych chwil i szybko rzekl - Nie mam ochoty na spory. Jezeli tego potrzebujesz, odpowiem ci na wszystkie pytania. Tylko miejmy to juz za soba."
Tekst524 = "Na wszelki wypadek zaczynasz wypytywac o Endera, jednak zgodnie z twoimi przypuszczeniami Niemiec nic o nim nie wie. Wtedy skupiasz sie na Treli. Dowiadujesz sie o nim wielu rzeczy. Rzeczywiscie czesto bywal na Alei Szucha, wykonujac kilka prac dla Niemcow. Zainteresowales sie szczegolnie wiadomoscia, ze tuz przed schwytaniem Schmidta podejrzany czesto udawal sie do gabinetu samego obersturmbannfuhrera Reinera. Klaus nie znal tematu rozmow, ale to nic dziwnego - w koncu byl tylko zandarmem, nie mogl sluchac takich rzeczy. Tadka widywal przypadkowo, ale zapamietal go, poniewaz kiedys wykonywal on dla niego pewna sprawe. Probujesz wyciagnac z niego jeszcze pare informacji, ale bezskutecznie. On juz wiecej nie wie."
Tekst525a  = "Udajesz sie jeszcze do ludzi z oddzialu, by ich wypytac o Trele. Byles ciekaw, jakie zdanie maja o nim jego koledzy. A te nie byly zbyt przychylne. Tadeusz byl odludkiem. Rzadko przebywal z innymi, moze dlatego, ze nie umial mowic zbyt dobrze po polsku - byl polakiem, ale urodzonym i wychowanym w Czechoslowacji. Do Polski przeprowadzil sie 5 lat temu, a wciaz mieszal czeski z polskim. W dodatku ciagle kontakty ze szwabami nie dzialaly na jego korzysc. Jego jedynym przyjacielem byl Gabicki, poniewaz znali sie jeszcze sprzed wojny. Tylko on nie powiedzial zlego slowa na Trele. Nie wiesz, co o tym wszystkim myslec. Niby wszysto jest logiczne, ale wciaz masz watpliwosci, czy wiedzac tylko tyle mozesz wydac na niego wyrok. Nie wiesz, skad moglbys dowiedziec sie czegos wiecej, postanawiasz..."
Tekst526a = "...nie ryzykowac. Zdrajca moze w kazdej chwili wsypac was wszyskich, musisz wiec dzialac szybko. Postanawiasz zastawic na Trele zasadzke. Umawiasz sie z nim przez telefon w ogrodach Ulrycha za pol godziny. Dojezdzasz tam jak najszybciej mozesz i ukrywasz sie w poblizu miejsca spotkania. Tadeusz przyszedl o umowionej godzinie i , czekajac, stanal do ciebie plecami. Wyszedles z cienia drzewa, za ktorym sie ukrywales, wyciagnales bron, przystawiles mu ja w tyl glowy i wyrecytowales:"
Tekst526a1 = "- W imieniu Polski Podziemnej jestes skazany na smierc za zdrade Ojczyzny"
Tekst526a2 = "Zaczales juz naciskac spust, gdy Trela gwaltownie sie odwrocil, reka odpychajac lufe od siebie. Kula, zamias w glowe, trafila go w ramie. Wrzasnal z bolu i rzucil sie do ucieczki. Nim jednak przebiegl dziesiec metrow, padl na ziemie, trafiony w plecy. Powoli podszedles do niego jednoczesnie przeladowywujac bron. Mezczyzna lezal w kaluzy krwi, z grymasem olbrzymiego bolu na twarzy. Wciaz czolgal sie w strone ulicy. Dobiles go jednym strzalem...     "
Tekst526a3 = "Po wykonaniu zadania poszedles do mieszkania Endera, by poinformowac go o wykonanej misji."
Tekst526b  = "...nie ryzykowac. Zabijanie ludzi na slepo nie jest dobrym rozwiazaniem. Postanawiasz najpierw pojsc do Endera po rade."
Tekst527a  = "Wchodzisz po schodach do mieszkania Endera. Juz masz dzwonic do dzwi, gdy ze srodka dochodza cie odglosy rozmowy. Z przerazeniem zdajesz sobie sprawe, ze slyszysz jezyk niemiecki. Gestapowcy przyszli do Endera. Nie rozumiesz, o czym rozmawiaja, ale mowia spokojnie. Liczac na to, ze sytuacja jest pod kontrola, wchodzisz na polpietro wyzej. Po jakims czasie gestapowiec wychodzi, a ty mozesz wejsc do srodka."
Tekst527a1 = "- Leon? Co tutaj robisz?"
Tekst527a2 = "- Co sie stalo? Dlaczego byl tu ten gestapowiec?"
Tekst527a3 = "- Zdrajca mu cos o mnie sypnal. Na szczescie jeszcze nie zamierzaja mnie przymknac, ale robi sie niebezpiecznie. Czy uporales sie juz ze zdrajca?"
Tekst527b  = "Wchodzisz po schodach do mieszkania Endera. Juz masz dzwonic do dzwi, gdy ze srodka dochodza cie odglosy rozmowy. Odruchowo zaczales nasluchiwac. Po chwili zaczales rozrozniac poszczegolne slowa. Osoby w srodku mowiom po niemiecku. Ender rozmawia z gestapowcem. Jednak tresc ich rozmowy zmrozila ci krew w zylach. Mowili o zasadzce na Kwatere Glowna! To Ender od poczatku byl zdrajca. Co sil w nogach pobiegles, by zlozyc raport Pajewskiemu."
Tekst528a  = "- Tak, juz po nim."
Tekst528a1 = "Ender patrzyl sie na ciebie przez chwile w milczeniu."
Tekst528a2 = "- Doskonale. Czyli zagrozenie mamy z glowy. Uff, juz sie balem, ze wyniknie z tego cos zlego."
Tekst528a3 = "- Ale na pewno jestes bezpieczny? Gestapo tak po prostu ci odpusci?"
Tekst528a4 = "- Na to bym nie liczyl. Bede musial wyjechac z Warszawy. Moze pojade z toba? Kto wie. Na razie chodzmy do komendanta zdac mu raport."
Tekst528a5 = "Ruszyliscie razem do Kwatery Glownej. Podporucznik Pajewski przyjal wiadomosc o zdrajcy z wiela ulga. Rozpoczeliscie od razu male przyjecie pozegnalne dla ciebie. Wszyscy musieli docenic twoja pomoc. Gdy wszyscy byli juz lekko pijani, nagle a dzwiami rozlegly sie strzaly. Drzwi otworzyly sie z hukiem, a do srodka wpadlo dwoch niemcow, ktorzy zaczeli strzelac do wszystkiego, co sie rusza. Szybko schowales sie za stolem i zdjales obu wrogow. Rozgladnales sie, by obejrzec straty. Zginelo szesc osob, w tym podporucznik Pajewski. Endera nigdzie nie widziales. Slyszac, ze na dole jest wiecej szkopow, zaczales szukac innego wyjscia. Pozostalo ci tylko czterech ludzi, trzech mialo wiec pilnowac drzwi, a ty i czwarty zaczeliscie sie rozgladac. Jedyna droga ucieczki bylo okno. Gdy tylko je otworzyles, nadciagnela kolejna fala niemcow. Reszta oddzialu zgodzila sie poswiecic, bys mogl uciec. Nie chciales im na to pozwolic, ale oni juz podieli decyzje. Chcieli umrzec tu, przy swoim dowodcy. Ty jeszcze nie mogles zginac, poniewaz obiecales Kmicicowi, ze wrocisz. Wyskoczyles wiec przez okno i opusciles Warszawe najszybciej jak mogles."
Tekst528b  = "- Nie. Zdrajca wciaz jest nieznany."
Tekst528b1 = "Ender patrzyl sie na ciebie przez chwile w milczeniu."
Tekst528b2 = "- To nie dobrze. Bardzo nie dobrze. Obawiam sie, ze nie zdolamy sie juz dowiedziec, kto jest zdrajca."
Tekst528b3 = "- Trela jest wciaz podejzany."
Tekst528b4 = "- Ale nie jestes na tyle pewien, ze jest winny, by go zabic. To juz koniec naszego oddzialu. Kazdy z nas musi pojsc w swoja strone. Kazda kryjowka jest teraz zagrozona nie ma innego wyjscia."
Tekst528b5 = "Telefonicznie poinformowales porucznika Pajewskiego o obecnej sytuacji. Zgodzil sie z nami, lecz glos mu drzal. Musial sie zalamac - stracil wlasnie to wszystko, co tak dlugo i pieczolowicie budowal. Jednak cala nasza trojka wiedziala, ze tak trzeba zrobic. Pozegnales sie z komendantem z przeczuciem, ze juz nigdy wiecej go nie zobaczysz. Pozostalo ci juz tylko wracac na Wilenszczyzne. Zaproponowales Enderowi, by pojechal z toba, ale odmowil. Musi cos jeszcze tutaj zalatwic. Uscisneliscie sobie serdecznie dlonie i rozstaliscie sie. Sam udales sie w droge powrotna."
Tekst528c  = "Komendant, slyszac te wiadomosc, byl nawet bardziej zdziwiony niz ty. Wstrzasnelo to nim do glebi. Jednak nadal byl w stanie kierowc oddzialem. Ewakuacja kwatery troche im zajela, ale uporaliscie sie z tym dosc sprawnie."
Tekst528c1 = "- Mam do ciebie jeszcze jedna prosbe. Tym razem juz ostatnia, przysiegm ci. Chce, bys zabil Aleksandra Endera. Kazdy zdrajca powinien zostac ukarany. Mozemy sie juz nie spotkac, wiec pozegnam sie juz teraz. Bardzo nam pomogles swoim przyjazdem tutaj, nie tylko podczas zamachu na von Stauffenberga, ale i teraz, kiedy ocaliles caly oddzial odnajdujac szpicla. To byl dla mnie zaszczyt, by pracowac z kims takim jak ty."
Tekst528c2 = "Uscisneliscie sobie dlonie na porzegnanie, a ty ruszyles na swoja ostatnia juz misje w Warszawie."
Tekst528c3 = "Zastales go w jego mieszkaniu. Gdy cie zobaczyl, od razu zasypal cie pytaniami"
Tekst528c4 = "- I jak, znalazles zdrajce? Zabiles go?"
Tekst528c5 = "- Znalazlem, ale jeszcze nie zabilem."
Tekst528c6 = "- Co? Dlaczego? - zaczal pytac, lecz gdy spojzal w twoje oczy zbladl nagle - Nie sadzisz chyba, ze to ja jestem zdrajca?"
Tekst528c7 = "- Slyszalem, o czym rozmawiales z gestapowcem pol godziny temu."
Tekst528c8 = "Ender zaczal otwierac usta, to znow je zamykac. Nie mogl znalezc slow. W koncu poddal sie i spuscil glowe."
Tekst528c9 = "- Masz racje. Oczywiscie masz racje. To ja zdradzilem. To ja stchorzylem."
Tekst528c10 = "- Zaufalem ci. Wszyscy ci ufali! Jak mogles cos takiego zrobic? Dlaczego to zrobiles?"
Tekst528c11 = "- Stchorzylem, ratowalem wlasna skore. Tak bardzo nie chcialem umierac, ze wolalem zdradzic wszystkie bliskie mi osoby, tylko po to, by ocalic moje nedzne zycie..."
Tekst528c12 = "Przystawiles mu bron do czola, lecz on patrzyl sie w podloge."
Tekst528c13 = "Spojrz mi prosto w oczy. Spojrz mi w oczy. SPOJRZ! - Ender podniosl wzrok. Przez chwile tak staliscie w milczeniu."
Tekst528c14 = "- W imieniu Polskiego Panstwa Podziemnego skazuje cie na smierc za zdrade Ojczyzny."
Tekst528c15 = "Ender przez cala przemowe twardo patrzyl ci sie w oczy. Nie mogles zniesc juz tego wzroku. Odwrociles glowe i pociagnales za spust. Krotki huk i dzwiek upadajacego ciala. Juz bylo po wszyskim...     "
Tekst528c16 = "Juz nic wiecej nie zatrzymuje cie w Warszawie. Oddzial Pajewskiego rozproszyl sie po calym miescie. Sam udales sie w droge powrotna w strone Wilna."
Tekst528d  = "Mimo ze komendant przewidywal taka mozliwosc, wiadomosc ta wstrzasnelo to nim do glebi. Jednak nadal byl w stanie kierowc oddzialem. Ewakuacja kwatery troche im zajela, ale uporaliscie sie z tym dosc sprawnie."
Tekst528d1 = "- Mam do ciebie jeszcze jedna prosbe. Tym razem juz ostatnia, przysiegm ci. Chce, bys zabil Aleksandra Endera. Kazdy zdrajca powinien zostac ukarany. Mozemy sie juz nie spotkac, wiec pozegnam sie juz teraz. Bardzo nam pomogles swoim przyjazdem tutaj, nie tylko podczas zamachu na von Stauffenberga, ale i teraz, kiedy ocaliles caly oddzial odnajdujac szpicla. To byl dla mnie zaszczyt, by pracowac z kims takim jak ty."
Tekst528d2 = "Uscisneliscie sobie dlonie na porzegnanie, a ty ruszyles na swoja ostatnia juz misje w Warszawie."
Tekst528d3 = "Zastales go w jego mieszkaniu. Gdy cie zobaczyl, od razu zasypal cie pytaniami"
Tekst528d4 = "- I jak, znalazles zdrajce? Zabiles go?"
Tekst528d5 = "- Znalazlem, ale jeszcze nie zabilem."
Tekst528d6 = "- Co? Dlaczego? - zaczal pytac, lecz gdy spojzal w twoje oczy zbladl nagle - Nie sadzisz chyba, ze to ja jestem zdrajca?"
Tekst528d7 = "- Slyszalem, o czym rozmawiales z gestapowcem pol godziny temu."
Tekst528d8 = "Ender zaczal otwierac usta, to znow je zamykac. Nie mogl znalezc slow. W koncu poddal sie i spuscil glowe."
Tekst528d9 = "- Masz racje. Oczywiscie masz racje. To ja zdradzilem. To ja stchorzylem."
Tekst528d10 = "- Zaufalem ci! Jak mogles cos takiego zrobic? Dlaczego to zrobiles?"
Tekst528d11 = "- Stchorzylem, ratowalem wlasna skore. Tak bardzo nie chcialem umierac, ze wolalem zdradzic wszystkie bliskie mi osoby, tylko po to, by ocalic moje nedzne zycie..."
Tekst528d12 = "Przystawiles mu bron do czola, lecz on patrzyl sie w podloge."
Tekst528d13 = "Spojrz mi prosto w oczy. Spojrz mi w oczy. SPOJRZ! - Ender podniosl wzrok. Przez chwile tak staliscie w milczeniu."
Tekst528d14 = "- W imieniu Polskiego Panstwa Podziemnego skazuje cie na smierc za zdrade Ojczyzny."
Tekst528d15 = "Ender przez cala przemowe twardo patrzyl ci sie w oczy. Nie mogles zniesc juz tego wzroku. Odwrociles glowe i pociagnales za spust. Krotki huk i dzwiek upadajacego ciala. Juz bylo po wszyskim...     "
Tekst528d16 = "Juz nic wiecej nie zatrzymuje cie w Warszawie. Oddzial Pajewskiego rozproszyl sie po calym miescie. Sam udales sie w droge powrotna w strone Wilna."
Tekst531 = "7 IX 1943 rok"
Tekst532 = "Jedziemy z Jankiem do Zanarocza, by dolaczyc juz na stale do Kmicica. Jestesmy teraz juz w polowie drogi do celu, dlatego moge przysiasc i cos napisac. To byly bardzo meczace dwa tygodnie."
Tekst533a = "Juz pierwszego dnia uczestniczylem w strzelaninie na ul. Bema. Ledwo uszedlem wtedy z zyciem. Na szczescie nic mi sie nie stalo."
Tekst533b = "Juz pierwszego dnia bylem swiatkiem aresztowania - mnie tez o malo co nie przymkneli. Na szczescie nic mi sie nie stalo."
Tekst534a = "Potem nie bylo lepiej. Przez moj wlasny blad stracilem dwoch dobrych ludzi podczas zamachu na Clausa von Stauffenberga. Ciezko mi z tym teraz zyc."
Tekst534b = "Potem juz bylo troche lepiej.  Misja zamachu na Clausa von Stauffenberga, ktora mi zlecono, poszla wrecz idealnie - zadnych strat wlasnych. Wiekszosc czasu potem swietowalismy zwyciestwo."
Tekst535a = "Sama koncowke poswiecilem na zwiedzanie miasta - naprawde zakochalem sie w tym miescie. Gdy tylko bede mogl, wroce tam na dluzej."
Tekst535b = "Jednak najgorsze zostalo na koniec. W szeregach oddzialu pojawil sie szpieg, przez ktorego caly oddzial musial zostac rozwiazany. Przynajmniej zdrajca otrzymal sprawiedliwa kare."
Tekst535c = "Jednak najgorsze zostalo na koniec. W szeregach oddzialu pojawil sie szpieg, przez ktorego caly oddzial musial zostac rozwiazany. Niestety zdrajca zdolal najpewniej uciec."
Tekst535d = "Jednak najgorsze zostalo na koniec. W szeregach oddzialu pojawil sie szpieg. Ja niesprawiedliwie osadzilem jednego z czlonkow oddzialu, podczas gdy prawdziwy zdrajca jest na wolnosci. Przeze mnie wszyscy teraz nie zyja."

Tekst61 = "8 IX 1943 rok"
Tekst62a  = "Nie mam dobrych wiesci. W Zanaroczu wydarzyla sie tragedia. Gdy dotarlismy na miejsce, okazalo sie, ze baza OP Kmicica zostala zaatakowana. W poblizu lezaly rozerwane zwloki jednego z partyzantow. Wygladalo na to, ze popelnil samobojstwo, wysadzajac sie granatem. Nie bylo innych sladow walki, wiec pewnie sie poddali. Zaczalem szukac kogos, kto moglby powiedziec mi, co tu sie stalo. W wiosce znalazlem Ursusa, ktoremu udalo sie uciec razem z Szpagatem i Dlugim. Opowiedzial mi o wszystkim. Kmicic udal sie do Markowa, przywodcy sowieckich partyzantow. Jednak juz z tamtad nie wrocil. Zamiast tego, 26 sierpnia zostali napadnieci przez rosjan. Poddali sie, nie stawiajac oporu. Tylko Brzozka nie chcal trafic zywy w rece wroga. To jego cialo widzialem. Nastepnego dnia wszyscy zostali przesluchani, a nastepnie podzieleni na dwie grupy. Z pierwszej utworzony zostal nowy oddzial, podlegly polskiemu dowodztwu w Moskwie, druga grupa zostala rozstrzelana w lesie. Z tej wlasnie grupy uciekli trzej partyzanci. Sam Kmicic prawdopodobnie juz nie zyje. Teraz nie wiemy z Leszkiem, co robic. Na razie probujemy skontaktowac sie z innymi polskimi oddzialami w okolicy."
Tekst62a1 = "14 IX 1943 rok"
Tekst62a2 = "Dolaczylismy do druzyny Maksa, przynajmniej na razie. Dwa dni temu pomoglismy im w akcji na Chojeckowszczyznie. Ostrzelalismy bande rabunkowa dzialajaca na tamtym terenie. Nie zdolalismy jej wyeliminowac, gdyz zabraklo nam amunicji. Ogolnie sytuacja z zasobami w tym oddziale jest krytyczna. Zaczyna brakowac jedzenia. Dlatego dowodca oddzialu zaproponowal nam uklad. Mamy zalozyc z Leszkiem nasz wlasny oddzial partyzancki, ktory utworzymy z 50 ludzi przekazanych nam z grupy Maksa. Raczej przystaniemy na ten plan. Reorganizacja powstalych brygad zajmie okolo doby. My w tym czasie wymyslamy sobie pseudonimy, jakie sobie nadamy. Janek wybral sobie ''Zaglobe'', a ja "
Tekst62b  = "Nie mam dobrych wiesci. W Zanaroczu wydarzyla sie tragedia. Gdy dotarlismy na miejsce, okazalo sie, ze baza OP Kmicica zostala zaatakowana. Wszedzie wokol lezaly trupy polakow, bialorusinow i rosjan. Bylem przerazony tym widokiem. Udalem sie do wioski, by tam zasiegnac jezyka, ale po drodze wpadlem na resztki oddzialu. Kmicica nie bylo wsrod nich, ale zyje. Udal sie z kilkunastoma zolnierzami na Chojeckowszczyznie, by tam wspomoc druzyne Maksa, walczaca z bandami rabunkowymi. Od ocalalych dowiedziales sie, co sie stalo. Na szczescie porucznik Burzynski posluchal mojej rady i nie poszedl na umowione spotkanie z Markowem. Mimo to, 26 sierpnia, sowieci napadli ich. Kmicic osobiscie dowodzil obrona, jednak byla to beznadziejna walka. Komunisci mieli troche lepszy sprzet, a w dodatku duza przewage liczebna. Po bardzo krwawej potyczce polacy wycofali sie, porzucajac baze. Kmicic chcial ukryc sie i poczekac na mnie, jednak Markow nie odpuscil i dalej go szukal. Dlatego musial uciekac. Jednak zostawil mi okolo 50 ludzi i misje, by utworzyc swoj wlasny oddzial. Bylem zszokowany taka decyzja. Nie mam doswiatczenia w dowodzeniu tak duza grupa ludzi. Jednak nalezalo sprobowac. Reorganizacja brygady potrwa troche czasu. W tym czasie z Jankiem wymyslamy sobie pseudonimy, jakie sobie nadamy. On wybral sobie ''Zaglobe'', a ja "
Tekst62c  = "Nie mam dobrych wiesci. W Zanaroczu wydarzyla sie tragedia. Gdy dotarlismy na miejsce, okazalo sie, ze baza OP Kmicica zostala zaatakowana. W poblizu lezaly rozerwane zwloki jednego z partyzantow. Wygladalo na to, ze popelnil samobojstwo, wysadzajac sie granatem. Nie bylo innych sladow walki, wiec pewnie sie poddali. Zaczalem szukac kogos, kto moglby powiedziec mi, co tu sie stalo. W wiosce znalazlem Ursusa, ktoremu udalo sie uciec razem z Szpagatem i Dlugim. Opowiedzial mi o wszystkim. Kmicic udal sie do Markowa na umowione spodkanie, jednak juz z tamtad nie wrocil. Zamiast tego, 26 sierpnia zostali napadnieci przez rosjan. Poddali sie, nie stawiajac oporu. Tylko Brzozka nie chcal trafic zywy w rece wroga. To jego cialo widzialem. Nastepnego dnia wszyscy zostali przesluchani, a nastepnie podzieleni na dwie grupy. Z pierwszej utworzony zostal nowy oddzial, podlegly polskiemu dowodztwu w Moskwie, druga grupa zostala rozstrzelana w lesie. Z tej wlasnie grupy uciekli trzej partyzanci. Sam Kmicic prawdopodobnie juz nie zyje. Teraz nie wiemy z Leszkiem, co robic. Na razie probujemy skontaktowac sie z innymi polskimi oddzialami w okolicy."
Tekst62c1 = "14 IX 1943 rok"
Tekst62c2 = "Dolaczylismy do druzyny Maksa, przynajmniej na razie. Dwa dni temu pomoglismy im w akcji na Chojeckowszczyznie. Ostrzelalismy bande rabunkowa dzialajaca na tamtym terenie. Nie zdolalismy jej wyeliminowac, gdyz zabraklo nam amunicji. Ogolnie sytuacja z zasobami w tym oddziale jest krytyczna. Zaczyna brakowac jedzenia. Dlatego dowodca oddzialu zaproponowal nam uklad. Mamy zalozyc z Leszkiem nasz wlasny oddzial partyzancki, ktory utworzymy z 50 ludzi przekazanych nam z grupy Maksa. Raczej przystaniemy na ten plan. Reorganizacja powstalych brygad zajmie okolo doby. My w tym czasie wymyslamy sobie pseudonimy, jakie sobie nadamy. Janek wybral sobie ''Zaglobe'', a ja "
Tekst63 = "Jestem bardzo podekscytowany tym, ze bede dowodca wlasnego oddzialu. Zrownalem sie tym samym stopniem z porucznikiem Askaldowiczem. Jestem ciekaw, jak poradze sobie w tej roli."
Tekst601 = "3 I 1944 rok"
Tekst602 = "Nasz oddzial rosnie w sile. Do tej pory bylismy za slabi, by atakowac w pojedynke, wiec kooperowalismy z innymi brygdami. Uczestniczylismy miedzy innymi w polowaniu na rabusiow i konfidentow w Soroku i Tatarach w dniach 19-24 wrzesnia oraz w rozbiciu wiezienia w Wormianach 5 listopada. Razem z OP Gorala uwolnilismy wtedy kilku Zydow i miejscowych rolnikow. Zniszczylismy rowniez niemiecka dokumentacje. Teraz nasz oddzial liczy ok 170 zolnierzy, jestesmy niezle uzbrojeni i zaopatrzeni. Teraz, gdy zima sie zaczyna, o jedzenie bedzie coraz trudniej, ale wszyscy sa dobrej mysli. Jednak ja nie ciesze sie tak bardzo, jak powinienem. Wciaz dochodza do mnie niepokojace informacje z domu - ponoc na Wolyniu trwaja teraz walki miedzy polakami, a ukraincami. Udalo mi sie namowic Leszka, bysmy sie tam udali i zweryfikowali sytuacje. Co prawda nie mamy pozwolenia od dowodztwa, ale postaramy sie z tym uporac jak najszybciej."
Tekst603 = "14 I 1944 rok"
Tekst604 = "Prawda okazala sie byc o wiele bardziej brutalna, niz ci sie wydawalo. W kazdej niemal wsi do ktorej zagladasz znajdujesz ciala polakow, zabitych w okrutny sposob. Jestes swiatkiem prawdziwej czystki etnicznej. W koncu trafiasz do miejscowosci, gdzie znajdujesz wyjatkowo duzo trupow - kobiet przebitych widlamy, dzieci nabitych na plot, mezczyzn bez glow. Po zobaczeniu tego wszystkiego..."
Tekst605a = "...poczules tak silna nienawisc, jak jeszcze nigdy w zyciu. Spontanicznie chwyciles za bron i zaczales strzelac do wszystkich naokolo. Wkrotce twoj oddzial przylaczyl sie do ciebie. Po chwili cala wies plonela, a krew z cial zabitych wiesniakow zalala cala droge. Dlugo wpatrywales sie w ten widok, myslac, ze sprawiedliwosc zostala wymierzona."
Tekst605b = "...odszedles stad jak najszybciej. Nie mozesz zniesc patrzenia na te okropienstwa."
Tekst606 = "Dwa dni pozniej obozowaliscie w lesie. Zaopatrzenie dawno wam sie skonczylo, juz dzien nie mieliscie. Nagle podeszlo do ciebie czterech twoich zolniezy, niosacych trzy kuty i kosz pelen jaj."
Tekst6061 = "- Skad to macie?"
Tekst6062 = "- Odebralismy wiesniakom. Spojrz, jakie sa tluste!"
Tekst607a  = "- Co wy sobie myslicie! Cywili sie nie okrada."
Tekst607a1 = "- To byla ukrainska rodzina. Mordercow chcesz bronic?"
Tekst607b = "- Dawaj, upieczemy je!"
Tekst607b1 = "Po wspanialej uczcie wszyscy poczuli sie syci, pierwszy raz od dawna. Rozlozyles sie wygodnie na lawce i zaczales rozmyslac, co bys zjadl na deser..."
Tekst608a  = "Oczywiscie nie chciales. Milczales chwile, przygladajac sie kurom. Rzeczywiscie byly tluste"
Tekst608a1 = "- Dobra, nie marudz juz. Dawaj, upieczemy je!"
Tekst608a2 = "Po wspanialej uczcie wszyscy poczuli sie syci, pierwszy raz od dawna. Rozlozyles sie wygodnie na lawce i zaczales rozmyslac, co bys zjadl na deser..."
Tekst608b  = "- Znam ich lepiej niz ty! Wychowalem sie tu i wiem, ze wiekszosc z nich przynajmniej nas toleruje. Nie mozna generalizowac i wrzucac wszystkich ludzi do jednego worka"
Tekst608b1 = "Mimo ze byles okropnie glodny, kazales im odniesc wszystko z powrotem. Czasem bycie dobrym wymaga poswiecen. Po calym oddziale przeszedl pomruk niezadowolenia, ale nikt niepowiedzial nic na glos."
Tekst609data = "23 I 1944 rok"
Tekst609a  = "Doszedles do wsi Kopanka. To jest twoj ostatni przystanek. Nie zdolasz dojsc juz do domu. Wyruszyles o bardzo zlej porze. Caly twoj oddzial gloduje juz od 3 dni. Wszyscy sa poddenerwowani i chca wracac do domu. Jednak jestescie juz na tyle niedaleko, ze ktos ze wsi zgodzi sie dostarczyc chociaz list. Gdy juz zaczynasz dobijac targu z jakims wiesniakiem, nagle slyszysz za soba huk wystrzalu. To twoi ludzie wlasnie dokonali egzekucji kobiety. Obok kleczy starszy czlowiek, placzac nad martwym cialem. Krzyczysz w ich strone. Zauwazasz, ze zabojstwa dokonali ci sami, co tydzien temu sprawili wam taka uczte."
Tekst609a1 = "- Ej! Co wy tam robicie?"
Tekst609a2 = "- Cholerna ukrainka nie chciala dac nam zarcia! - wrzasnal przywodca bandy"
Tekst609a3 = "Nim zdazyles mu odpowiedziec, starzec przeklul go widlami. Zolnierz zacharczal przerazliwie i kaszlnal krwia. Padl na kolana, lecz nim tamten zdazyl go dobic, zostal rozstrzelany przez pozostalych. Trzy trupy lezaly tuz obok siebie. Cala wioska zareagowala gwaltownie. Wszyscy zaczeli krzyczec, niektorzy nawt lapac za bron. Mimo ze nie zdazyles wyslac listu, nakazujesz wszystkim jak najszybszy odwrot..."
Tekst609b  = "Znow mijasz miejscowosc, w ktorej popelniono tyle zbrodnii. Gdy zaczales sobie przypominac wszystkie okropnosci, jakie tam widziales, z lasu zaczal cie ostrzeliwywac oddzial UPA. Nim wszyscy zdazyliscie skryc sie do rowu przy drodze, mnostwo was padlo. Wymiana ognia trwala jeszcze pare minut, gdy banda ukrainska nagle zniknela, rownie szybko, co sie pojawila. Nad droga zawisla glucha cisza. Jak tylko upewniliscie sie, ze juz po wszystkim, zaczeliscie liczyc straty. Gdy chodziles wsrod zwlok swoich podkomendnych, nagle zauwazyles, ze na ziemi lezy Janek. Twaz mial cala we krwi, oberwal kula prosto w oko. Kleknales przy jego ciele i zaczales plakac..."
Tekst609c  = "Doszedles do wsi Kopanka. To jest twoj ostatni przystanek. Nie zdolasz dojsc juz do domu. Wyruszyles o bardzo zlej porze. Caly twoj oddzial gloduje juz od 3 dni. Wszyscy sa poddenerwowani i chca wracac do domu. Jednak jestescie juz na tyle niedaleko, ze ktos ze wsi zgodzi sie dostarczyc chociaz list. Na szczescie udaje ci sie kogos znalezc. Szczesliwy, ze udaje ci sie chociaz tyle zrobic, udajesz sie w droge powrotna."
Tekst610a  = "Bedac juz blisko twojej bazy zauwazasz opartego o drzewo umierajacego rosjanina."
Tekst610b  = "Bedac juz blisko twojej bazy zauwazasz opartego o drzewo umierajacego rosjanina. Podchodzac blizej poznajesz Markowa! Nie zastanawiajac sie, co on tu robi, postanawiasz..."
Tekst611a  = "... go zabic. Musisz pomscic OP Kmicica. Poza tym, jest zdrajca, a kazdy zdrajca musi umrzec. Gdy cie zauwaza, wytrzeszcza z przerzenia oczy. Nim cokolwiek powie, przykladasz mu pistolet w skron i strzelasz."
Tekst611b  = "...uratowac go. Wiesz, ze zemsta do niczego nie prowadzi. Poza tym, przed paroma dniami byles swiatkiem zbyt okrutnych wydarzen. Nie chciales zyc w takim swiecie, postanowiles wiec go zmienic - chocby w tej chwili. Podczas opatrywania rany Markow zemdlal, nie byles pewien, czy z bolu, czy ze strachu. To nie mialo juz znaczenia..."

Tekst71 = "3 II 1944 rok"
Tekst72 = "Wczoraj wrocilismy do Zanarocza. Wszyscy bardzo dotkliwie odczuli dni wedrowki. Pare osob zmarlo z glodu. W dodatku dowodztwo jest bardzo niezadowolone, ze udalismy sie tam bez zezwolenia. Za kare nasz oddzial zostal wcielony do 3 Brygady pod dowodztwem kapitana Gracjana Froga ''Szczerbca''"
Tekst73a = "Dodatkowo zostalem zdegradowany do stopnia podporucznika. Przynajmniej zgodzili sie na pogrzeb Janka z wszystkimi honorami. Zabralismy jego cialo ze soba. Nie moglem pozwolic, by zostal pochowany na tamtej przekletej ziemi."
Tekst73b = "Na szczescie Jankowi udalo sie nieco zlagodzic sytuacje. Nie zostalismy przyajmniej zdegradowani."
Tekst74 = "14 VI 1944 rok"
Tekst75 = "Nasz okreg zaczal sie przygotowywac do rozpoczecia akcji ''Burza'' na Wilenszczyznie. Cala akcja trwa juz na Wolyniu i Podolu. Jest to reakcja na przekroczenie przedwojennej granicy przez Armie Czerwona. Dowodztwo zaczelo laczenie oddzialow w trzy wieksze zgromadzenia. My dolaczylismy do Zgrupowania nr 1 pod dowodztwem majora Antoniego Olechnowicza ''Pohoreckego''. Dowodca naszegom okregu, podpulkonik ''Wilk'' Skierowal nas pod Wilno i przygotowal do ataku na miasto z zewnatrz. Takiego zgrupowania naszych sil nie widzialem juz od bardzo dawna. Juz niedlugo wojna wreszcie sie skonczy."
Tekst76 = "5 VII 1944 rok"
Tekst77 = "Armia Czerwona jest coraz blizej. Za okolo trzy dni dojdzie juz do miasta i wlasnie wtedy zaatakujemy. Mamy wyraznie zaznaczyc, ze Polska wciaz walczy, ze to my tutaj rzadzimy! Plan akcji juz zostal potwierdzony. Nasze zgrupowanie zaatakuje od wschodu. Wszyscy sie juz niecierpliwia. Jeszcze nie widzialem ich tak podekscytowanych. Nareszcie znow wrocilismy na front."
Tekst701 = "7 VII 1944 rok"
Tekst702 = "Ze wzgledu na szybkie zblizanie sie Armii Czerwonej, Wilk postanowil przyspieszyc rozpoczecie operacji ''Ostra Brama'' o dobe. Zdolano skoncentrowac tylko 1 z 3 przewidzianych w planie oddzialow uderzeniowych. Zaatakowaliscie o godzinie 7, od poludniowego wschodu. Ruszyles do walki razem z Brygada 8, jednak wszelkie wasze dzialania blokowal pociag pancerny w rejonie stacji Kolonia Wilenska. Brygada 8 zalegla w kotlinie na przeciwko betonowego bunkra, lecz wam udalo sie przejsc rzeke Wilejke, dotrzec do Belmontu, Zarzecza, a nawet Traktu Batorego."
Tekst703a = "Podczas walk na Trakcie twoja flanka zaczela przegrywac. Niemcy wciaz ostrzeliwali wasze pozycje z mozdziezow. Ryk karabinow oraz huk wybuchow roznosil sie po calej ulicy. Nagle, tuz obok ciebie wybuchl granat, raniac cie odlamkami. Walczac z bolem w krwawiacej nodze probowales sie wycofac do budynku, lecz wtedy pocisk przelecial ci przez lewy bark na wylot. Padles na ziemie zalany krwia..."
Tekst703b = "Podczas walk na Trakcie twoja flanka zaczela przegrywac. Niemcy wciaz ostrzeliwali wasze pozycje z mozdziezow. Ryk karabinow oraz huk wybuchow roznosil sie po calej ulicy. Nagle, tuz obok Askaldowicza wybuchl granat, raniac go odlamkami. Widzisz, jak czolga sie w strone budynku. Reszta juz sie wycofala sie. Jezeli zaraz stad nie uciekniesz, zginiesz. Jestes za daleko Janka, by zdazyc do niego dobiec. Jest on jednak juz bardzo blisko schronu, gdyby tylko mial troche wiecej czasu..."
Tekst704a = "Wiesz, co masz zrobic. Mimo ze zostales juz calkowicie sam, wciaz strzelasz w strone Niemcow, utrzymujac ich w odpowiedniej odleglosci. Trwa to pare chwil, lecz w koncu trafiaja cie. Padasz na plecy i powoli zaczynasz sie wykrwawiac, lecz nim straciles przytomnosc, widzisz jeszcze, ze Jankowi udaje sie przezyc..."
Tekst704b = "Jednak jest juz dla niego za pozno. Uciekasz w strone schronu, mijajac setki kul i chyba tylko Bogu zawdzieczasz, ze jeszcze zyjesz. Janek jednak nie mial tyle szczescia..."
Tekst705  = "Utrzymujecie ta pozycje do nastepnego dnia, gdy dolaczyli do was sowieci. Wasze sily sa bardzo przezedzone, wiec postanawiacie wycofac sie do rejonu Szwajcar."
Tekst706a  = "...budzisz sie w lozku, a nad toba stoi... Twoj ojciec! Na jego widok wstajesz gwaltownie, lecz zaraz padasz z powrotem, sparalizowany ogromnym bolem w ranie po postrzale."
Tekst706a1 = "- Spokojnie, spokojnie. Zaraz ci pomoge - powiedzial, podajac ci dlon."
Tekst706a2 = "- Skad sie tu wziales?"
Tekst706a3 = "- Przybylem tu razem z sowietami. Uczestniczylem w walce o Wilno, a gdy sie dowiedzialem, ze lezysz tutaj ranny, od razu tu przyszedlem."
Tekst706a4 = "- Nie moge uwierzyc, ze cie spotkalem! Tyle lat minelo. Stracilem juz nadzieje! Ale dlaczego trzymasz z sowietami?"
Tekst706a5 = "- Po drodze do Rumunii trafilem do ich niewoli. Wypuscili mnie po niecalym roku, gdy polacy podpisali porozumienie z ZSRR. Chcialem wtedy dolaczyc do wojsk polsich, jednak nie zdazylem. Czekalem wiec na kolejna okazje. I wtedy dowiedzialem sie o zdradzie polskiego rzadu i jego kolaboracjach z Hitlerem - wtedy zdalem sobie sprawe, ze jedyna szansa na wyzwolenie Polski jest walka wspolnie ze Zwiazkiem Radzieckim, dlatego wstapilem do Armii Czerwonej."
Tekst706a6 = "- O czym ty mowisz, jaka zdrada!?"
Tekst706a7 = "- Ciszej, nie mow takich rzeczy jak nie wiesz! Caly czas byles oklamywany! Na szczescie znalazlem cie, nim AK zabralo cie stad"
Tekst706a8 = "- A co sie z nimi stalo?"
Tekst706a9 = "- Czesc z nich uciekla, reszta zostala rozbrojona - widzac zdziwienie rozetke na twojej twarzy szybko dodaje - Spokojnie, mi mozesz przeciez zaufac. Sowieci chca nam pomoc, w koncu mamy jeden wspolny cel - pokonac Hitlera. Nie masz sie o co bac"
Tekst706a10 = "Wciaz nie jestes przekonany tym, co mowi twoj ojciec, jednak nie chcesz go opuszczac, a nie masz jak dolaczyc z powrotem do AK, postanawiasz wiec isc razem z nim..."
Tekst706b  = "Po pieciu dniach Wilno juz bylo zdobyte. Wszedzie zaczeto wywieszac polskie flagi. Widok byl przepiekny i, mimo iz Janek zginal, swietowales razem z innymi, gdyz i on przyczynil sie do tego zwyciestwa. Polegl, ale z bronia w reku, z honorem. Wszyscy na nowo odzyskali nadzieje na zwyciestwo w wojnie i niepodleglosc. Jednak nie trwalo to dlugo. Wkrotce po pokonaniu Niemcow Armia Czerwona zaczela podmieniac bialo-czerwone flagi na sowieckie. W dodatku oddzialy NKWD przystapily do rozbrajania polskiej armii. Gdy tylko sie o tym dowiedziales, zechciales sie ewakulowac razem z armia pplk Macieja Kalenkiewicza ''Kotwicza'', zalorzyciela grupy cichociemnych, ktory rowniez przeszedl kurs i zrzucil sie do Polski. Jednak najpierw miales spotkac sie z kims w jednym z wojskowych barakow stojacych w okolicy. Na wszelki wypadek wziales bron. Gdy wszedles do srodka, zobaczyles swojego ojca."
Tekst706b1 = "- Tata? Skad sie tu wziales?"
Tekst706b2 = "- Przybylem tu razem z sowietami. Uczestniczylem w walce o Wilno, a gdy sie dowiedzialem, ze ty rowniez tutaj jestes, zorganizowalem to spokanie."
Tekst706b3 = "- Nie moge w to uwierzyc! Tyle lat minelo. Stracilem juz nadzieje! Ale dlaczego trzymasz z sowietami?"
Tekst706b4 = "- Po drodze do Rumunii trafilem do ich niewoli. Wypuscili mnie po niecalym roku, gdy polacy podpisali porozumienie z ZSRR. Chcialem wtedy dolaczyc do Armii Andersa, jednak nie zdazylem. Czekalem wiec na kolejna okazje. Lecz wtedy dowiedzialem sie o zdradzie polskiego rzadu i jego kolaboracjach z Hitlerem - zdalem sobie sprawe, ze jedyna szansa na wyzwolenie Polski jest walka wspolnie ze Zwiazkiem Radzieckim, dlatego wstapilem do Armii Czerwonej."
Tekst706b5 = "Nie mogles uwierzyc w to, co slyszysz. Twoj wlasny ojciec, ten sam, ktory uczyl cie przez cale zycie, ktory cie wychowywal, dal sie tak omamic! Juz chciales cos powiedziec, gdy do srotka wszedl jakis czlowiek."
Tekst706b6 = "- To jest Yuri, czlowiek, ktoremu zawdzieczam wszystko. To on mnie namowil do wstapienia do Armii."
Tekst706b7 = "A wiec to wszystko jego sprawka."
Tekst706b8 = "- Ojcze, co ty za glupoty wygadujesz! Przeciez AK walczy z Hitlerem! Opamietaj sie!"
Tekst706b9 = "- Caly czas byles oklamywany! Nie widzisz? AK to zdrajcy!"
Tekst706b10 = "- Bylem swiatkiem ataku radzieckich partyzantow na polski OP. To sowieci sa zdrajcami! Mozesz mi przeciez zaufac."
Tekst706b11 = "Twoj ojciec zaczal sie wahac. Patrzyl to na ciebie, to na Yuriego. Teraz to on musi podjac decyzje..."
Tekst707a  = "- Nie. Nie moge. Nie jestes jeszcze wystarczajaco dojrzaly, by obiektywnie ocenic sytuacje."
Tekst707a1 = "- Nie przekonasz mnie. Nie dolacze do komunistow!."
Tekst707a2 = "Patrzyliscie na siebie w milczeniu. Nagle Yuri powiedzial cos do twojego ojca, a ten, jakby ze smutkiem, przytaknal mu."
Tekst707a3 = "- Nie moge pozwolic na to, by moj wlasny syn walczyl przeciw ojczyznie. Przykro mi, ale zmusiles mnie do tego... - powiedzial to i wycelowal w ciebie pistolet. Zareagowales bezwarunkowo. Jedna reka odsunales lufe od siebie, a druga wbiles mu noz w krtan. Twoj ojciec padl na kolana, patrzac sie na ciebie ze zdziwieniem i nienawiscia w oczach. Bez zatrzymywania sie, z furia rzuciles sie na Yuriego i poderznales mu gardlo. Po chwili, obaj lezeli juz na ziemii martwi. Gdy ochlonales i obaczyles ten widok, uciekles stamtad jak najszybciej. Pobiegles do Kalenkiewicza jak najszybciej i opusciles Wilno. Jednak tamten pokoj bedzie ci sie snic juz do konca zycia."
Tekst707b  = "- Kocham cie, synu. I dlatego pojde z toba."
Tekst707b1 = "Gdy rosjanin to uslyszal, ryknal z wscieklosci i rzucil sie na twego ojca. Zareagowales bezwarunkowo. Popchnales go na sciane i wbiles mu noz w brzuch. Chwile pozniej lezal martwy na ziemi. Jak najszybciej uciekliscie z tamtad i udaliscie sie do Kalenkiewicza. Kilka godzin pozniej opusciliscie Wilno."
Tekst708 = "Opusciliscie miasto 14 lipca, by udac sie w strone Puszczy Rudnickiej. Po dotarciu na miejsce, okolo 18 tysiecy zolnierzy i cywili zgromadzonych na miejscu zostalo podzielonych na mniejsze bandy z rozkazem udania sie na Bialystok. NKWD ruszylo za waszym oddzialem dowodzonym przez Kotwicza. Kilkukrotnie musieliscie odpierac oblawy sowietow, co zmusilo was do ponownego cofniecia sie w las. Tam przesiedzieliscie caly miesiac, podczas gdy rosjanie probowali was okrazyc. By przejsc przez linie wroga, podzieliliscie sie na jeszcze mniejsze grupy. Wasz nowy 36-osobowy oddzial udal sie na poludniowy zachod. Jednak nie udalo sie wam uciec oblawie. Swoj ostatni boj stoczyliscie w lesniczowce Surkonty. Tylko jeden z was ocalal, jednak nie byles to ty..."

grob0="                     _..-----.._"
grob1="                  .-             ``-."
grob2="               _-`                   `-_"
grob3="             .'7                         `."
grob4="           .` /                           \""
grob5="          /  /                             \""
grob6="         /  |                               \""
grob7="        ;  /                                 \""
grob8="       /  ;                                   ;"
grob9="       |  |  ______ _______ _______ _______    \""
grob10="      |  | |  ____ |_____| |  |  | |______    |"
grob11="      |  | |_____| |     | |  |  | |______    |"
grob12="      |  |                                    |"
grob13="      |  |                                    |"
grob14="      |  |  _____  _    _ _______  ______     |"
grob15="      |  | |     |  \  /  |______ |_____/     |"
grob16="      |  | |_____|   \/   |______ |    \_     |"
grob17="      |  |                                    |"
grob18="      |  |                                    |"
grob19="      |  |                                    |"
grob20="      |  |                                    |"
grob21="      |  |                                    |"
grob22="      |  |                                    |"
grob23="      |  |                                    |"
grob24="      |  |                                    |"
grob25="      |  |                                    |"
grob26="      |  |                                    |"
grob27="      |  |                                    |_"
grob28="      |  |                          ____....---`___."
grob29=" __..-J_ |        ______....---`_`_`_...----````_.-|"
grob30="/`\\.____...---'''__....-----`_`_`.`-----```````   |"
grob31="|\ `/...-----'''``_...----````          __...----``|"
grob32="| `Y|\----````````       _____..-----````"
grob33=" \ |||        ___...---``_...---`````"
grob34="  `\|.----``_`...---`````"
grob35="    `--````"

grob = (grob0,grob1,grob2,grob3,grob4,grob5,grob6,grob7,grob8,grob9,grob10,grob11,grob12,grob13,grob14,grob15,grob16,grob17,grob18,grob19,grob20,grob21,grob22,grob23,grob24,grob25,grob26,grob27,grob28,grob29,grob30,grob31,grob32,grob33,grob34,grob35,)



granat = "Granat wybucha pod toba, odrywajac ci nogi."
tekstwybor = "Co zrobisz? Wybierz "
ucieczkaiwalka = "1 - ucieczka, 2 - walka"
ucieczkaipodejscie = "1 - uciekasz, 2 - podchodzisz do ojca"
wegryirumunia = "1 - zostawiasz Ojca i jedziesz do Wegier, 2 - jedziesz z Ojcem do Rumunii"
zostaniidz = "1 - zostajesz sam w domu, 2 - idziesz dalej!"
lecizostan = "1 - lecisz, 2 - jednak zostajesz"
paiprosba = "1 - ''do zobaczenia'', 2 - ''mam do ciebie jeszcze jedna prosbe''"
uwazajinieufaj = "1 - ''uwazaj na siebie'', 2 - ''nie ufaj komunistom''"
zabijiodejdz = "1 - zabijasz, 2 - odchodzisz"
zastrzeliuciekaj = "1 - zastrzel pozostalych, 2 - uciekaj za Enderem"
uciekajiuciekaj = "1 - uciekaj w zaulek, 2 - uciekaj do kamienicy"
prostoizakret = "1 - droga prosto, 2 - zakret"
aptekaiblok = "1 - do apteki, 2 - do bloku"
silairozmowa = "1 - uzywasz sily, 2 - rozmawiasz"
grozbaitortura = "1 - grozisz, 2 - torturujesz"
odejscieiwejscie = "1 - odchodzisz, 2 - wchodzisz do srodka"
uratujiczekaj = "1 - ratujesz informatora, 2 - czekasz"
czekajisprawdz = "1 - czekaj, 2 - sprawdz kto to"
czekajipomoz = "1 - czekasz na rozwoj wydarzen, 2 - biegniesz pomoc"
dobijiuciekaj = "1 - dobijasz, 2 - uciekasz"
postronniizasadzka = "Mowisz im: 1 - ''Uwazajcie na postronnych'', 2 - ''Uwazajcie na zasadzke''"
treleiender = "1 - zabijasz Trele, 2 - idziesz za Enderem"
zniszcziodejdz = "1 - niszczysz wioske, 2 - odchodzisz czym predzej"
bidaijedzenie = "1 - nie okrada sie wiesniakow, 2 - zarcie!"
zostawipomoz = "1 - zostawiasz, 2 - pomogasz"
zabijiuratuj = "1 - zabijasz, 2 - ratujesz"
poswiecenieiucieczka = "1 - poswiecasz sie, 2 - uciekasz"

print("")
print("")
slowlowanie("Rozdzial 1 - ''Poczatek przygody''")
wait = raw_input("By przejsc dalej nacisnij enter")
print("")
print("")
prin(Tekst101a)
time.sleep(1)
prin(Tekst101c)
wait = raw_input("")
print("")
prin(Tekst102a)
time.sleep(1)
prin(Tekst102b)
wait = raw_input("")
print("")
prin(Tekst103a)
time.sleep(1)
prin(Tekst103b)
prin(Tekst103c)
wait = raw_input("")
print("")
prin(Tekst104a)
time.sleep(1)
prin(Tekst104b)
prin(Tekst104c)
wait = raw_input("")
print("")
prin(Tekst105a)
prin(Tekst105b)
time.sleep(3)
print("")
prin(tekstwybor)
prin(ucieczkaiwalka)
while True:
    wybor = raw_input()
    if wybor == '1':
        prin(Tekst107a)
        x = x + 1
        break
    elif wybor == '2':
        prin(Tekst107b)
        prin(Tekst108b)
        time.sleep(3)
        prin(tekstwybor)
        prin(ucieczkaipodejscie)
        while True:
            wybor = raw_input()
            if wybor == '1':
                prin(Tekst109a)
                break
            elif wybor == '2':
                prin(Tekst109b)
                time.sleep(3)
                slowlowanie(granat)
                for a in grob:
                    print a
                wait = raw_input("KONIEC")
                sys.exit(0)
            else:
                prin("Musisz wpisac 1 lub 2!")
        break
    elif wybor == '2137':
        prin(papieska_ruletka())
    else:
        prin("Musisz wpisac 1 lub 2")
print("")
slowlowanie("Koniec rozdzialu 1.")
time.sleep(5)
wait = raw_input("Idziesz dalej?")

for a in range(30): #liczba kolumn
    print("")

slowlowanie("Rozdzial 2 - ''Ucieczka''")
time.sleep(3)
print("")
print("")
prin(Tekst201a)
time.sleep(1)
prin(Tekst201b)
wait = raw_input("")
print("")
if x == 1:
    prin(Tekst202a)
    wait = raw_input("")
    print("")
    prin(Tekst204a)
    wait = raw_input("")
    print("")
    prin(Tekst205a)
    wait = raw_input("")
    print("")
    prin(Tekst206b)
    print("")
    wait = raw_input("")
    print("")
    prin(Tekst207a)
    time.sleep(1)
    prin(Tekst208b)
else:
    prin(Tekst202b)
    time.sleep(3)
    prin(tekstwybor)
    prin(wegryirumunia)
    while True:
        wybor = raw_input()
        if wybor == '1':
            prin(Tekst203a)
            wait = raw_input("")
            print("")
            prin(Tekst204a)
            wait = raw_input("")
            print("")
            prin(Tekst205a)
            time.sleep(1)
            prin(Tekst206a)
            print("")
            wait = raw_input()
            prin(Tekst207a)
            time.sleep(1)
            prin(Tekst208a)
            time.sleep(3)
            prin(tekstwybor)
            prin(zostaniidz)
            while True:
                wybor = raw_input()
                if wybor == '1':
                    prin(Tekst209a)
                    wait = raw_input()
                    print("")
                    slowlowanie("GAME OVER")
                    for a in grob:
                        print a
                    wait = raw_input("KONIEC")
                    sys.exit(0)
                elif wybor == '2':
                    prin(Tekst209b)
                    break
                elif wybor == '2137':
                    prin(papieska_ruletka())
                else:
                    prin("Musisz wpisac 1 lub 2")
            break
        if wybor == '2':
            prin(Tekst204b)
            wait = raw_input()
            prin(Tekst204b1)
            print("")
            slowlowanie("GAME OVER")
            for a in grob:
                print a
            wait = raw_input("KONIEC")
            sys.exit(0)
        elif wybor == '2137':
            prin(papieska_ruletka())
        else:
            prin("Musisz wpisac 1 lub 2")

time.sleep(3)
prin(tekstwybor)
prin(zostaniidz)
while True:
    wybor = raw_input()
    if wybor == '1':
        prin(Tekst209a)
        break
    elif wybor == '2':
        prin(Tekst209b)
        break
    elif x == '2137':
        print("")
        prin(papieska_ruletka())
        print("")
    else:
        prin("Musisz wpisac 1 lub 2")

print("")
slowlowanie("Koniec Rozdzialu 2.")
time.sleep(5)
wait = raw_input("Idziesz dalej?")

for a in range(30): #liczba kolumn
    print("")

slowlowanie("Rozdzial 3 - ''Upadek''")
time.sleep(3)
print("")
print("")
prin(Tekst31)
time.sleep(1)
prin(Tekst32)
wait = raw_input("")
print("")
prin(Tekst33)
time.sleep(1)
prin(Tekst34)
wait = raw_input("")
print("")
prin(Tekst35)
time.sleep(1)
prin(Tekst36)
wait = raw_input("")
print("")
prin(Tekst37)
time.sleep(1)
prin(Tekst38)
wait = raw_input("")
print("")
slowlowanie("Koniec Rozdzialu 3.")
time.sleep(5)
print("")
wait = raw_input("Idziesz dalej?")

for a in range(30): #liczba kolumn
    print("")

slowlowanie("Rozdzial 4 - ''Cichociemni''")
time.sleep(3)
print("")
print("")
prin(Tekst41a)
time.sleep(1)
prin(Tekst41b)
wait = raw_input("")
print("")
prin(Tekst42a)
time.sleep(1)
prin(Tekst42b)
wait = raw_input("")
print("")
prin(Tekst43a)
time.sleep(1)
prin(Tekst43b)
wait = raw_input("")
print("")
prin(Tekst44a)
time.sleep(1)
prin(Tekst44b)
wait = raw_input("")
print("")
prin(Tekst45a)
time.sleep(1)
prin(Tekst45b)
time.sleep(3)
prin(tekstwybor)
prin(lecizostan)
while True:
    wybor = raw_input()
    if x == '1':
        prin(Tekst46a)
        z = 0
        break
    elif x == '2':
        prin(Tekst46b)
        print ("")
        prin(Tekst47a)
        time.sleep(1)
        prin(Tekst47b)
        break
    elif x == '2137':
        prin(papieska_ruletka())
    else:
        prin("Musisz wpisac 1 lub 2")

slowlowanie("Koniec Rozdzialu 4.")
time.sleep(5)
print("")
wait = raw_input("Idziesz dalej?")

for a in range(30): #liczba kolumn
    print("")

slowlowanie("Rozdzial 5 - ''Warszawa''")
time.sleep(3)
print("")
print("")
if z == 0:
    prin(Tekst51b)
    time.sleep(1)
    prin(Tekst52b)
    print("")
    wait = raw_input()
    prin(Tekst53a)
    time.sleep(1)
    prin(Tekst53b)
    prin(Tekst53c)
    prin(Tekst53d)
    prin(Tekst53e)
    prin(Tekst53f)
    time.sleep(3)
    prin(tekstwybor)
    prin(paiprosba)
    while True:
        wybor = raw_input()
        if wybor == '1':
            prin(Tekst54a)
            print("")
            prin(Tekst56)
            break
        elif wybor == '2':
            prin(Tekst54b)
            prin(Tekst54c)
            time.sleep(3)
            prin(tekstwybor)
            prin(uwazajinieufaj)
            while True:
                if wybor == '1':
                    prin(Tekst55a)
                    kom = 0
                    break
                elif wybor == '2':
                    prin(Tekst55b)
                    prin(Tekst55c)
                    prin(Tekst55d)
                    prin(Tekst55e)
                    kom = 1
                    break
                elif wybor == '2137':
                    prin(papieska_ruletka())
                else:
                    prin("Musisz wpisac 1 lub 2")
            prin(Tekst56)
        elif wybor == '2137':
            prin(papieska_ruletka())
        else:
            prin("Musisz wpisac 1 lub 2")
elif z == 1:
    prin(Tekst51a)
    time.sleep(1)
    prin(Tekst51b)

prin(Tekst501data)
prin(Tekst501)
prin(Tekst501a)
prin(Tekst501b)
prin(Tekst501c)
prin(Tekst501d)
prin(Tekst501e)
prin(Tekst501f)
prin(Tekst501g)
prin(Tekst501h)
prin(Tekst501i)
prin(Tekst501j)
prin(Tekst501k)
prin(Tekst501l)
prin(Tekst501m)
prin(Tekst501n)
prin(Tekst501o)
prin(Tekst501p)
prin(Tekst501r)
prin(Tekst501s)
prin(Tekst501t)
prin(Tekst501u)
prin(Tekst501w)
prin(Tekst501y)
time.sleep(5)
prin(tekstwybor)
prin(zabijiodejdz)
while True:
    wybor = raw_input()
    if wybor == '1':
        prin(Tekst502a)
        time.sleep(3)
        prin(tekstwybor)
        prin(zastrzeliuciekaj)
        while True:
            wybor = raw_input()
            if wybor == '1':
                prin(Tekst503a)
                time.sleep(3)
                prin(tekstwybor)
                prin(uciekajiuciekaj)
                while True:
                    wybor = raw_input()
                    if wybor == '1':
                        prin(Tekst504a)
                        time.sleep(3)
                        prin(tekstwybor)
                        prin(prostoizakret)
                        while True:
                            wybor = raw_input()
                            if wybor == '1':
                                prin(Tekst505a)
                                time.sleep(3)
                                prin(tekstwybor)
                                prin(aptekaiblok)
                                while True:
                                    wybor = raw_input()
                                    if wybor == '1':
                                        prin(Tekst506b)
                                        prin(Tekst506c)
                                        prin(Tekst506d)
                                        prin(Tekst506e)
                                        prin(Tekst506f)
                                        prin(Tekst506g)
                                        prin(Tekst506h)
                                        prin(Tekst506i)
                                        prin(Tekst506j)
                                        prin(Tekst506k)
                                        wait = raw_input()
                                        print("")
                                        prin(Tekst511c)
                                        prin(Tekst511c1)
                                        prin(Tekst511c2)
                                        prin(Tekst511c3)
                                        prin(Tekst511c4)
                                        prin(Tekst511c5)
                                        prin(Tekst511c6)
                                        prin(Tekst511c7)
                                        prin(Tekst511c8)
                                        e = 2
                                        break
                                    elif wybor == '2':
                                        prin(Tekst506a)
                                        y = 1
                                        break
                                    elif wybor == '2137':
                                        prin(papieska_ruletka())
                                    else:
                                        prin("Musisz wpisac 1 lub 2")
                                break
                            elif wybor == '2':
                                prin(Tekst505b)
                                y = 1
                                break
                            elif wybor == '2137':
                                prin(papieska_ruletka())
                            else:
                                prin("Musisz wpisac 1 lub 2")
                        break
                    elif wybor == '2':
                        prin(Tekst504b)
                        y = 1
                        break
                    elif wybor == '2137':
                        prin(papieska_ruletka())
                    else:
                        prin("Musisz wpisac 1 lub 2")
                    break
            elif wybor == '2':
                prin(Tekst503b)
                prin(Tekst511b)
                prin(Tekst511b1)
                prin(Tekst511b2)
                prin(Tekst511b3)
                prin(Tekst511b4)
                prin(Tekst511b5)
                e = 1
                wait = raw_input()
                break
            elif wybor == '2137':
                prin(papieska_ruletka())
            else:
                prin("Musisz wpisac 1 lub 2")
        break
    elif wybor == '2':
        prin(Tekst502b)
        prin(Tekst511a)
        prin(Tekst511a1)
        prin(Tekst511a2)
        prin(Tekst511a3)
        prin(Tekst511a4)
        prin(Tekst511a5)
        e = 0
        wait = raw_input()
        break
    elif wybor == '2137':
        prin(papieska_ruletka())
    else:
        prin("Musisz wpisac 1 lub 2")
        
if y == 1:
    prin("Na cale szczescie jestem laskawy i cie oszczedze. Na przyszlosc postaraj sie nie ginac. Masz teraz cale 15 sekund na przemyslenie swojego zachowania")
    time.sleep(15)
    prin(Tekst501data)
    prin(Tekst501)
    prin(Tekst501a)
    prin(Tekst501b)
    prin(Tekst501c)
    prin(Tekst501d)
    prin(Tekst501e)
    prin(Tekst501f)
    prin(Tekst501g)
    prin(Tekst501h)
    prin(Tekst501i)
    prin(Tekst501j)
    prin(Tekst501k)
    prin(Tekst501l)
    prin(Tekst501m)
    prin(Tekst501n)
    prin(Tekst501o)
    prin(Tekst501p)
    prin(Tekst501r)
    prin(Tekst501s)
    prin(Tekst501t)
    prin(Tekst501u)
    prin(Tekst501w)
    prin(Tekst501y)
    time.sleep(5)
    prin(tekstwybor)
    prin(zabijiodejdz)
    while True:
        wybor = raw_input()
        if wybor == '1':
            prin(Tekst502a)
            time.sleep(3)
            prin(tekstwybor)
            prin(zastrzeliuciekaj)
            prin(Tekst503b)
            prin(Tekst511b)
            prin(Tekst511b1)
            prin(Tekst511b2)
            prin(Tekst511b3)
            prin(Tekst511b4)
            prin(Tekst511b5)
            e = 1
            wait = raw_input()
            break
        elif wybor == '2':
            prin(Tekst502b)
            prin(Tekst511a)
            prin(Tekst511a1)
            prin(Tekst511a2)
            prin(Tekst511a3)
            prin(Tekst511a4)
            prin(Tekst511a5)
            e = 0
            wait = raw_input()
            break
        elif wybor == '2137':
           prin(papieska_ruletka())
        else:
            prin("Musisz wpisac 1 lub 2")

print("")
prin(Tekst1a)
time.sleep(1)
prin(Tekst1b)
prin(Tekst1b1)
prin(Tekst1b2)
prin(Tekst1b3)
prin(Tekst1b4)
prin(Tekst1b5)
prin(Tekst1b6)
prin(Tekst1b7)
time.sleep(3)
prin(tekstwybor)
prin(silairozmowa)
while True:
    wybor = raw_input()
    if wybor == '1':
        prin(Tekst2a)
        prin(tekstwybor)
        prin(grozbaitortura)
        while True:
            wybor = raw_input()
            if wybor == '1':
                prin(Tekst3a)
                if z == 1:
                    prin(Tekst4a)
                    prin(Tekst4a1)
                    prin(Tekst3c1)
                    prin(Tekst3c2)
                    prin(Tekst3c3)
                    prin(Tekst3c4)
                    prin(Tekst3c5)
                    prin(Tekst3c6)
                    zas = 1
                elif z == 0:
                    time.sleep(3)
                    prin(Tekst3b)
                    prin(Tekst3b1)
                    prin(Tekst3b2)
                    prin(Tekst3b3)
                    prin(Tekst3b4)
                break
            elif wybor == '2':
                prin(Tekst3b)
                prin(Tekst3b1)
                prin(Tekst3b2)
                prin(Tekst3b3)
                prin(Tekst3b4)
                break
            elif wybor == '2137':
               prin(papieska_ruletka())
            else:
                prin("Musisz wpisac 1 lub 2")
        break
    elif wybor == '2':
        prin(Tekst2b)
        time.sleep(3)
        prin(tekstwybor)
        prin(silairozmowa)
        while True:
            wybor = raw_input()
            if wybor == '1':
                prin(Tekst2a)
                prin(tekstwybor)
                prin(grozbaitortura)
                while True:
                    wybor = raw_input()
                    if wybor == '1':
                        prin(Tekst3a)
                        if z == 1:
                            prin(Tekst4a)
                            prin(Tekst4a1)
                            prin(Tekst3c1)
                            prin(Tekst3c2)
                            prin(Tekst3c3)
                            prin(Tekst3c4)
                            prin(Tekst3c5)
                            prin(Tekst3c6)
                            zas = 1
                        elif z == 0:
                            time.sleep(3)
                            prin(Tekst3b)
                            prin(Tekst3b1)
                            prin(Tekst3b2)
                            prin(Tekst3b3)
                            prin(Tekst3b4)
                        break
                    elif wybor == '2':
                        prin(Tekst3b)
                        prin(Tekst3b1)
                        prin(Tekst3b2)
                        prin(Tekst3b3)
                        prin(Tekst3b4)
                        break
                    elif wybor == '2137':
                       prin(papieska_ruletka())
                    else:
                        prin("Musisz wpisac 1 lub 2")
                break
            elif wybor == '2':
                prin(Tekst3c)
                prin(Tekst3c1)
                prin(Tekst3c2)
                prin(Tekst3c3)
                prin(Tekst3c4)
                prin(Tekst3c5)
                prin(Tekst3c6)
                zas = 1
                wait = raw_input()
                break
            elif wybor == '2137':
               prin(papieska_ruletka())
            else:
                prin("Musisz wpisac 1 lub 2")
        break
    elif wybor == '2137':
       prin(papieska_ruletka())
    else:
        prin("Musisz wpisac 1 lub 2")

prin(Tekst11)
if zas == 1:
    prin(Teks11a)
    time.sleep(3)
    prin(tekstwybor)
    prin(czekajisprawdz)
    while True:
        wybor = raw_input()
        if wybor == '1':
            prin(Tekst12a)
            time.sleep(3)
            prin(Tekst13a)
            prin(Tekst13a1)
            prin(Tekst13a2)
            prin(Tekst13a3)
            time.sleep(3)
            prin(Tekst16)
            wait = raw_input()
            i = 1
            break
        elif wybor == '2':
            prin(Tekst12b)
            time.sleep(3)
            prin(Tekst13b)
            time.sleep(3)
            prin(tekstwybor)
            prin(czekajipomoz)
            while True:
                wybor = raw_input()
                if wybor == '1':
                    prin(Tekst14a)
                    time.sleep(3)
                    prin(tekstwybor)
                    prin(dobijiuciekaj)
                    while True:
                        wybor = raw_input()
                        if wybor == '1':
                            prin(Tekst15a)
                            wait = raw_input()
                            break
                        elif wybor == '2':
                            prin(Tekst15b)
                            wait = raw_input()
                            break
                        elif wybor == '2137':
                            prin(papieska_ruletka())
                        else:
                            prin("Musisz wpisac 1 lub 2")

                    break
                elif wybor == '2':
                    prin(Tekst14b)
                    prin(Tekst14b1)
                    prin(Tekst14b2)
                    prin(Tekst14b3)
                    prin(Tekst14b4)
                    prin(Tekst14b5)
                    time.sleep(3)
                    prin(Tekst16)
                    wait = raw_input()
                    i = 1
                    break
                elif wybor == '2137':
                   prin(papieska_ruletka())
                else:
                    prin("Musisz wpisac 1 lub 2")
            break
        elif wybor == '2137':
           prin(papieska_ruletka())
        else:
            prin("Musisz wpisac 1 lub 2")
elif zas == 0:
    prin(Tekst11b)
    time.sleep(3)
    prin(tekstwybor)
    prin(odejscieiwejscie)
    while True:
        wybor = raw_input()
        if wybor == '1':
            prin(Tekst12c)
            break
        elif wybor == '2':
            prin(Tekst12d)
            time.sleep(3)
            prin(tekstwybor)
            prin(uratujiczekaj)
            while True:
                wybor = raw_input()
                if wybor == '1':
                    prin(Tekst13c)
                    wait = raw_input()
                    break
                elif wybor == '2':
                    prin(Tekst13d)
                    time.sleep(3)
                    prin(Tekst16)
                    wait = raw_input()
                    i = 1
                    break
                elif wybor == '2137':
                   prin(papieska_ruletka())
                else:
                    prin("Musisz wpisac 1 lub 2")
            break
        elif wybor == '2137':
           prin(papieska_ruletka())
        else:
            prin("Musisz wpisac 1 lub 2")

print("")
prin(Tekst21)
time.sleep(1)
if i == 1:
    prin(Tekst22a)
elif i == 0:
    prin(Tekst22b)
prin(tekstwybor)
prin(postronniizasadzka)
while True:
    wybor = raw_input()
    if wybor == '1':
        if i == 1:
            prin(Tekst23a)
            prin(Tekst23a1)
            prin(Tekst23a2)
            wait = raw_input()
            m = 1
            s = 1
        elif i == 0:
            prin(Tekst23c)
            prin(Tekst23c1)
            prin(Tekst23c2)
            wait = raw_input()
            s = 1
        break
    elif wybor == '2':
        if i == 1:
            prin(Tekst23b)
            prin(Tekst23b1)
            prin(Tekst23b2)
            wait = raw_input() 
            m = 1
        elif i == 0:
            prin(Tekst23d)
            prin(Tekst23d1)
            prin(Tekst23d2)
            wait = raw_input()
        break
    elif wybor == '2137':
       prin(papieska_ruletka())
    else:
        prin("Musisz wpisac 1 lub 2")

print("")
prin(Tekst521a)
time.sleep(1)
if m == 1:
    prin(Tekst521b)
    wait = raw_input()
elif m == 2:
    prin(Tekst521c)
    wait = raw_input()

print("")
if e == 1:
    prin(Tekst522a)
    prin(Tekst522a1)
    prin(Tekst522a2)
    prin(Tekst522a3)
    prin(Tekst522a4)
    prin(Tekst522a5)
    prin(Tekst522a6)
    prin(Tekst522a7)
    prin(Tekst522a8)
    prin(Tekst522a9)
    prin(Tekst522a10)
    prin(Tekst522a11)
    prin(Tekst522a12)
    prin(Tekst522a13)
    prin(Tekst522a14)
    prin(Tekst522a15)
    wait = raw_input()
elif e == 0:
    prin(Tekst522b)
    prin(Tekst522b1)
    prin(Tekst522b2)
    prin(Tekst522b3)
    prin(Tekst522b4)
    prin(Tekst522b5)
    wait = raw_input()
elif e == 2:
    if m == 1:
        prin(Tekst522c)
        wait = raw_input()
    elif m == 0:
        prin(Tekst52d)
        wait = raw_input()

print("")
if zas == 1:
    prin(Tekst523a)
    wait = raw_input()
if zas == 0:
    prin(Tekst523b)
    wait = raw_input()

print("")
prin(Tekst524)
time.sleep(3)
prin(tekstwybor)
prin(treleiender)
while True:
    wybor = raw_input()
    if wybor == '1':
        prin(Tekst526a)
        wait = raw_input()
        t = 0
        break
    elif wybor == '2':
        prin(Tekst526a)
        wait = raw_input()
        t = 1
        break
    elif wybor == '2137':
       prin(papieska_ruletka())
    else:
        prin("Musisz wpisac 1 lub 2")

print("")   
if z == 0:
    prin(Tekst527a)
    prin(Tekst527a1)
    prin(Tekst527a2)
    prin(Tekst527a3)
    wait = raw_input()
    if t == 0:
        bla = 3
        prin(Tekst528a)
        prin(Tekst528a1)
        prin(Tekst528a2)
        prin(Tekst528a3)
        prin(Tekst528a4)
        prin(Tekst528a5)
        wait = raw_input()
    elif t == 1:
        bla = 2
        prin(Tekst528b)
        prin(Tekst528b1)
        prin(Tekst528b2)
        prin(Tekst528b3)
        prin(Tekst528b4)
        prin(Tekst528b5)
        wait = raw_input()
elif z == 1:
    bla = 1
    prin(Tekst527b)
    wait = raw_input()
    if e == 1:
        prin(Tekst528c)
        prin(Tekst528c1)
        prin(Tekst528c2)
        prin(Tekst528c3)
        prin(Tekst528c4)
        prin(Tekst528c5)
        prin(Tekst528c6)
        prin(Tekst528c7)
        prin(Tekst528c8)
        prin(Tekst528c9)
        prin(Tekst528c10)
        prin(Tekst528c11)
        prin(Tekst528c12)
        prin(Tekst528c13)
        prin(Tekst528c14)
        prin(Tekst528c15)
        prin(Tekst528c16)
        wait = raw_input()
    elif e == 0:
        prin(Tekst528d)
        prin(Tekst528d1)
        prin(Tekst528d2)
        prin(Tekst528d3)
        prin(Tekst528d4)
        prin(Tekst528d5)
        prin(Tekst528d6)
        prin(Tekst528d7)
        prin(Tekst528d8)
        prin(Tekst528d9)
        prin(Tekst528d10)
        prin(Tekst528d11)
        prin(Tekst528d12)
        prin(Tekst528d13)
        prin(Tekst528d14)
        prin(Tekst528d15)
        prin(Tekst528d16)
        wait = raw_input()

print("")
prin(Tekst531)
time.sleep(1)
prin(Tekst532)
print("")
if e == 0:
    prin(Tekst533b)
    wait = raw_input()
else:
    prin(Tekst533a)
    wait = raw_input()
if m == 1:
    prin(Tekst534b)
    wait = raw_input()
elif m == 0:
    prin(Tekst534a)
    wait = raw_input()
if e == 2:
    prin(Tekst535a)
    wait = raw_input()
if bla == 1:
    prin(Tekst535b)
    wait = raw_input()
elif bla == 2:
    prin(Tekst535c)
    wait = raw_input()
elif bla == 3:
    prin(Tekst535d)
    wait = raw_input()

print("")
slowlowanie("Koniec rozdzialu 5.")
time.sleep(5)
wait = raw_input("Idziesz dalej?")


for a in range(30): #liczba kolumn
    print("")

slowlowanie("Rozdzial 6 - ''Na Wolyn!''")
time.sleep(3)
print("")
print("")
prin(Tekst61)
time.sleep(1)
if z == 1:
    prin(Tekst62a)
    prin(Tekst62a1)
    prin(Tekst62a2)
    k = 0
elif kom == 1:
    prin(Tekst62b)
    k = 1
else:
    prin(Tekst62c)
    prin(Tekst62c1)
    prin(Tekst62c2)
while True:
    name = raw_input("Podaj pseudonim:")
    if len(name) > 0 and name.isalpha():
        break

print("")
prin(Tekst63)
wait = raw_input()
print("")
print("")
prin(Tekst601)
time.sleep(1)
print("")
prin(Tekst602)
wait = raw_input()
print("")
prin(Tekst603)
wait = raw_input()
print("")
prin(Tekst604)
time.sleep(3)
prin(tekstwybor)
prin(zniszcziodejdz)
while True:
    wybor = raw_input()
    if wybor == '1':
        prin(Tekst605a)
        r = 1
        s = s + 1
        break
    elif wybor == '2':
        prin(Tekst605b)
        r = 0
        break
    elif wybor == '2137':
       prin(papieska_ruletka())
    else:
        prin("Musisz wpisac 1 lub 2")

print("")
prin(Tekst606)
prin(Tekst6061)
prin(Tekst6062)
prin(tekstwybor)
prin(bidaijedzenie)
while True:
    wybor = raw_input()
    if wybor == '1':
        prin(Tekst607a)
        prin(Tekst607a1)
        time.sleep(3)
        if r == 0:
            prin(Tekst608b)
            prin(Tekst608b1)
            wait = raw_input()
        else:
            prin(Tekst608a)
            prin(Tekst608a1)
            prin(Tekst608a2)
            wait = raw_input()
            s = s + 1
        break
    elif wybor == '2':
        prin(Tekst607b)
        prin(Tekst607b1)
        wait = raw_input()
        s = s + 1
        break
    elif wybor == '2137':
       prin(papieska_ruletka())
    else:
        prin("Musisz wpisac 1 lub 2")

print("")
Tekst609data
time.sleep(1)
if s == 0:
    prin(Tekst609c)
    l = 1
else:
    prin(Tekst609a)
    prin(Tekst609a1)
    prin(Tekst609a2)
    prin(Tekst609a3)
    l = 0
if r == 0:
    prin(Tekst609b)
    j = 0

if z == 1:
    prin(Tekst610a)
    prin(tekstwybor)
    prin(zostawipomoz)
    while True:
        wybor = raw_input()
        if wybor == '1':
            markow = 0
            break
        elif wybor == '2':
            markow = 1
            break
        elif wybor == '2137':
           prin(papieska_ruletka())
        else:
            prin("Musisz wpisac 1 lub 2")
elif z == 0:
    prin(Tekst610b)
    prin(tekstwybor)
    prin(zabijiuratuj)
    while True:
        wybor = raw_input()
        if wybor == '1':
            prin(Tekst611a)
            markow = 0
            break
        elif wybor == '2':
            prin(Tekst611b)
            markow = 1
            break
        elif wybor == '2137':
           prin(papieska_ruletka())
        else:
            prin("Musisz wpisac 1 lub 2")

slowlowanie("Koniec Rozdzialu 6.")
time.sleep(5)
print("")
wait = raw_input("Idziesz dalej?")

for a in range(30): #liczba kolumn
    print("")

slowlowanie("Rozdzial 7 - ''Final''")
time.sleep(3)
print("")
print("")
prin(Tekst71)
time.sleep(1)
prin(Tekst72)
wait = raw_input()
print("")
if j == 1:
    prin(Tekst73b)
    wait = raw_input()
    print("")
elif j == 0:
    prin(Tekst73a)
    wait = raw_input()
    print("")

prin(Tekst74)
time.sleep(1)
prin(Tekst75)
wait = raw_input()
print("")
prin(Tekst76)
time.sleep(1)
prin(Tekst77)
wait = raw_input()
print("")
prin(Tekst701)
time.sleep(1)
prin(Tekst702)
wait = raw_input()
print("")
if j == 0:
    prin(Tekst703a)
    wait = raw_input()
    print("")
    A = 1
elif j == 1:
    prin(Tekst703b)
    time.sleep(3)
    prin(tekstwybor)
    prin(poswiecenieiucieczka)
    while True:
        wybor = raw_input()
        if wybor == '1':
            prin(Tekst704a)
            wait = raw_input("KONIEC")
            sys.exit(0)
        elif wybor == '2':
            prin(Tekst704b)
            prin(Tekst705)
            wait = raw_input()
            print("")
            j = 0
        elif wybor == '2137':
           prin(papieska_ruletka())
        else:
            prin("Musisz wpisac 1 lub 2")
if A == 1:
    prin(Tekst706a)
    prin(Tekst706a1)
    prin(Tekst706a2)
    prin(Tekst706a3)
    prin(Tekst706a4)
    prin(Tekst706a5)
    prin(Tekst706a6)
    prin(Tekst706a7)
    prin(Tekst706a8)
    prin(Tekst706a9)
    prin(Tekst706a10)
    wait = raw_input()
    print("")
    prin(Tekst707c)
    wait = raw_input("KONIEC")
    sys.exit(0)
else:
    prin(Tekst706b)
    prin(Tekst706b1)
    prin(Tekst706b2)
    prin(Tekst706b3)
    prin(Tekst706b4)
    prin(Tekst706b5)
    prin(Tekst706b6)
    prin(Tekst706b7)
    prin(Tekst706b8)
    prin(Tekst706b9)
    prin(Tekst706b10)
    prin(Tekst706b11)
    wait = raw_input()
    print("")
    if x == 1:
        prin(Tekst707a)
        prin(Tekst707a1)
        prin(Tekst707a2)
        prin(Tekst707a3)
    elif x == 0:
        prin(Tekst707b)
        prin(Tekst707b1)
    prin(Tekst708)
    wait = raw_input("KONIEC")
    sys.exit(0)
sys.exit(0)
