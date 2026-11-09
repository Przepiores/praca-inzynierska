# Wspólny słownik, oznaczenia i zasady stylu

Obowiązuje wszystkie rozdziały pracy. Stan: 2026-11-09 (aktualizacja 15:30 po odpowiedziach autora, sekcja 0). Zebrano na podstawie: `knowledge/Inzynierka/Praca inzynierska.md`, Golden Standard, `opis-tematu-v2/opis_tematu_v2.tex`, `wstep-zagajenie/wstep_opcja_C.tex` (zatwierdzony), `podstawy-teoretyczne/podstawy_teoretyczne.tex`, `uklad-pomiarowy/*.tex`, `emisja-magnes-pomiary/emisja_tresc.tex`, `literatura-wstep/*.md`, sprawozdanie z postępów, notatki w `knowledge/`.
Nie sprawdzono repozytorium `W:\VAULT\Inzynierka\latex` (komputer był niedostępny), w tym `frontmatter/wykaz_skrotow.tex` — gotowy zamiennik: `wspolne/wykaz_skrotow.tex` (skróty + oznaczenia).

## 0. Fakty o prototypie potwierdzone przez autora (2026-11-09)

| Parametr | Wartość | Jak pisać w pracy |
|---|---|---|
| Napięcie przyspieszające | pomiary emisji: $U_\mathrm{T}=\SI{2000}{\volt}$ (sesja bez magnesu; z magnesem \SI{1500}{\volt}); **pomiary widm (12.06.2026): $U_\mathrm{T}=\SI{4000}{\volt}$, $U_\mathrm{B}=\SI{1000}{\volt}$**, tło hamowania kończy się przy ok. \SI{4}{\kilo\electronvolt} (granica Duane'a–Hunta, `widma-eds/README.md`), więc $E_0\approx\SI{4}{\kilo\electronvolt}$ | zawsze podawać, którego pomiaru dotyczy wartość; \SIrange{10}{18}{\kilo\volt} tylko jako parametr docelowy. Niepewność: czy $U_\mathrm{T}$ jest mierzone od emitera (wtedy $E_0=eU_\mathrm{T}$), czy bramka dodaje \SI{1}{\kilo\volt}; widmo wskazuje na pierwszy przypadek |
| Prąd w tabeli emisji | $I_\mathrm{e}$ = prąd emisji | symbol $I_\mathrm{e}$, nazwa „prąd emisji” |
| Połączenie elementów | bonding anodowy w atmosferze | „połączono bondingiem anodowym w atmosferze; struktura nie jest hermetyczna, badania prowadzono w komorze próżniowej” |
| Magnes | magnes trwały NdFeB umieszczony na emiterze, parametry nieznane | nie podawać indukcji ani wymiarów; „parametry magnesu nie były znane” jako ograniczenie w rozdz. pomiarów |
| Detektor spektrometru | elektronika KETEK DPP2 (program ProSpect), detektor najpewniej KETEK SDD — typ niepotwierdzony | „spektrometr z detektorem półprzewodnikowym (prawdopodobnie SDD) i procesorem impulsów KETEK DPP2”; nie pisać „SDD” jako pewnika |
| Ciśnienie w komorze | rzędu \SI{1e-5}{\hecto\pascal} | „\SI{1e-3}{\pascal} (\SI{1e-5}{\hecto\pascal})” |
| Naniesienie CNT | kompozyt CNT-PVP jak w rozprawie Urbańskiego, nakraplany pipetą na emiter na płycie grzejnej nagrzanej do \SI{240}{\celsius} | „nakraplanie kompozytu CNT-PVP” |

Zasada nadrzędna: **jedno pojęcie = jeden termin = jeden symbol** w całej pracy. Nowy termin lub symbol dopisuje się tutaj, zanim trafi do rozdziału.

---

## 1. Obiekty i elementy układu (nazewnictwo)

| Używać | Znaczenie | Nie używać / uwagi |
|---|---|---|
| **analizator EDS** (pełniej: miniaturowy analizator EDS w technologii MEMS) | przyrząd będący przedmiotem pracy | „analizator rentgenowski”, „układ RTG MEMS” w odniesieniu do własnego prototypu |
| **prototyp analizatora** | wykonany egzemplarz | „chip”, „urządzenie” (potocznie) |
| **źródło elektronów** | część analizatora: emiter + bramka + target | „działo elektronowe” — tylko dla SEM/klasycznych dział |
| **źródło RTG MEMS** (przy pierwszym użyciu: miniaturowe źródło promieniowania rentgenowskiego MEMS) | przyrząd z rozprawy P. Urbańskiego, punkt wyjścia pracy | nie nazywać tak własnego analizatora (zob. niespójność N9) |
| **emiter (E)** | mikroostrze krzemowe pokryte kompozytem CNT-PVP | „katoda” tylko w kontekście ogólnym: „zimna katoda” vs „katoda żarzona”; „katoda polowa” — unikać |
| **bramka (B)** | elektroda ekstrakcyjna z aperturą; przy pierwszym użyciu: „bramka (elektroda ekstrakcyjna)” | „grid”, „siatka”, „elektroda wyciągająca” |
| **target (T)** | elektroda przyspieszająca, na którą pada wiązka; w analizatorze nośnik badanej próbki / warstwy luminoforu | „anoda” (dopuszczalne tylko w opisie ogólnym lampy RTG) |
| **próbka** | badany materiał, na który pada wiązka (na targecie) | nie zamieniać „próbka” ↔ „target” w obrębie jednego akapitu |
| **magnes ogniskujący** (magnes trwały NdFeB) | element magnetycznego ogniskowania, umieszczony na emiterze | „magnes neodymowy” tylko jako dopowiedzenie przy pierwszym użyciu |
| **ekran luminescencyjny** (warstwa luminoforu na targecie) | do obserwacji kształtu wiązki | „ekran luminoforowy”, „fosfor” |
| **plamka** | ślad wiązki na ekranie | „plama”, „spot” |
| **komora próżniowa** | zewnętrzna komora, w której prowadzono badania | ciśnienie rzędu \SI{1e-3}{\pascal} (\SI{1e-5}{\hecto\pascal}) |
| **nakraplanie** CNT | sposób naniesienia emitera w prototypie: pipeta, płyta grzejna \SI{240}{\celsius} | „hot plate” → „płyta grzejna” |
| **mikropompa jonowo-sorpcyjna** | element docelowej struktury hermetycznej | — |
| **spektrometr rentgenowski** / **detektor** | przyrząd rejestrujący widmo | KETEK DPP2, detektor prawdopodobnie SDD (sekcja 0) |
| **stanowisko pomiarowe** | całość: komora, zasilacze, mierniki, spektrometr | „setup” |

## 2. Skróty (do wykazu skrótów i oznaczeń)

Przy pierwszym użyciu w tekście: pełna nazwa polska, skrót w nawiasie, rozwinięcie angielskie kursywą: „spektroskopia EDS (ang. *Energy Dispersive X-ray Spectroscopy*)”. Dalej tylko skrót.

| Skrót | Rozwinięcie (ang.) | Znaczenie (pol.) |
|---|---|---|
| APXS | Alpha Particle X-ray Spectrometer | spektrometr rentgenowski wzbudzany cząstkami alfa |
| CNT | Carbon Nanotubes | nanorurki węglowe |
| CNT-PVP | — | kompozyt nanorurek węglowych i poliwinylopirolidonu |
| DRIE | Deep Reactive Ion Etching | głębokie trawienie reaktywne jonowe |
| EDS | Energy Dispersive X-ray Spectroscopy | spektroskopia rentgenowska z dyspersją energii |
| F–N | Fowler–Nordheim | (wykres, równanie) Fowlera–Nordheima |
| FWHM | Full Width at Half Maximum | szerokość połówkowa |
| KOH | — | wodorotlenek potasu |
| MCA | Multichannel Analyzer | analizator wielokanałowy |
| MEMS | Micro-Electro-Mechanical Systems | mikrosystemy elektromechaniczne |
| NdFeB | — | stop neodym–żelazo–bor (magnes trwały) |
| PIXL | Planetary Instrument for X-ray Lithochemistry | przyrząd łazika Perseverance |
| PVP | Polyvinylpyrrolidone | poliwinylopirolidon |
| RTG | — | rentgenowski (tylko w nazwie „źródło RTG MEMS”) |
| SDD | Silicon Drift Detector | krzemowy detektor dryfowy |
| SEM | Scanning Electron Microscope | elektronowy mikroskop skaningowy |
| Si(Li) | — | detektor krzemowy kompensowany litem |
| TMAH | Tetramethylammonium Hydroxide | wodorotlenek tetrametyloamoniowy |
| UV | Ultraviolet | nadfiolet |
| WDS | Wavelength Dispersive X-ray Spectroscopy | spektroskopia z dyspersją długości fali |
| XRF | X-ray Fluorescence | fluorescencja rentgenowska (metoda) |
| ZAF | — | poprawki na liczbę atomową (Z), absorpcję (A), fluorescencję (F) |

Nie wprowadzać skrótów: HV/WN (pisać „wysokie napięcie”), ESD (pisać „desorpcja stymulowana elektronami”), „j.u.” wyjaśnić raz jako „jednostki umowne”. CheMin, MER, Curiosity, Perseverance — nazwy własne, bez rozwinięć w wykazie.

## 3. Symbole i jednostki

### 3.1. Wielkości układu pomiarowego (rdzeń pracy — obowiązkowe)

| Symbol | LaTeX | Znaczenie | Jednostka |
|---|---|---|---|
| $U_\mathrm{B}$ | `U_\mathrm{B}` | **napięcie ekstrakcyjne** (emiter–bramka) | V |
| $U_\mathrm{T}$ | `U_\mathrm{T}` | **napięcie przyspieszające** (emiter–target) | V, kV |
| $I_\mathrm{e}$ | `I_\mathrm{e}` | prąd emisji | µA |
| $I_\mathrm{B}$ | `I_\mathrm{B}` | prąd bramki | µA |
| $I_\mathrm{T}$ | `I_\mathrm{T}` | prąd targetu (prąd wiązki docierający do targetu) | µA |
| $R_\mathrm{T}$, $R_\mathrm{B}$ | | rezystory ograniczające w obwodzie targetu i bramki (\SI{100}{\kilo\ohm}) | kΩ |
| $U_{R_\mathrm{T}}$, $U_{R_\mathrm{B}}$ | | napięcia na rezystorach (pomiar prądu) | V |
| $p$ | | ciśnienie | Pa (hPa tylko w nawiasie, gdy źródło podaje hPa) |
| $T$ | | temperatura bezwzględna; w °C pisać słownie z jednostką | K, °C |
| $L$ | | jasność (intensywność) świecenia ekranu z analizy obrazu | j.u. |

Zamiast symbolu $U_\mathrm{acc}$ obowiązuje $U_\mathrm{T}$ (tak jest już w schemacie i w podstawach teoretycznych). Wartości napięć podaje się jako **moduły** (np. $U_\mathrm{T}=\SI{15}{\kilo\volt}$); biegunowość opisuje się raz, w rozdziale o układzie: emiter na potencjale ujemnym względem targetu.

### 3.2. Fizyka (podstawy teoretyczne)

| Symbol | Znaczenie | Jednostka |
|---|---|---|
| $\varphi$ | praca wyjścia | eV |
| $F$ | natężenie pola elektrycznego na powierzchni emitera (w równaniu F–N) | V/m |
| $\vec E$ | wektor natężenia pola elektrycznego (siła Lorentza) | V/m |
| $J$ | gęstość prądu emisji | A/m² |
| $\beta$ | współczynnik wzmocnienia pola | — |
| $d$ | odległość emiter–bramka | µm |
| $a$, $b$ | stałe Fowlera–Nordheima | — |
| $e$, $m_\mathrm{e}$, $c$, $h$, $k_\mathrm{B}$ | stałe fizyczne | — |
| $E_0$ | energia elektronów wiązki ($E_0=eU_\mathrm{T}$) | keV |
| $E$ | energia fotonu | keV |
| $E_\mathrm{c}$ | energia krytyczna (energia wiązania powłoki, krawędź absorpcji) | keV |
| $U_0$ | współczynnik nadnapięcia $E_0/E_\mathrm{c}$ (bezwymiarowy; mimo litery $U$ nie jest napięciem) | — |
| $\vec F_\mathrm{L}$ | siła Lorentza | N |
| $\vec B$, $B_z$ | indukcja magnetyczna | T |
| $r_\mathrm{L}$ | promień Larmora | mm |
| $f$ | ogniskowa soczewki magnetycznej | mm |
| $Z$, $A$, $\rho$ | liczba atomowa, masa atomowa, gęstość | —, g/mol, g/cm³ |
| $R_\mathrm{KO}$ | zasięg elektronów Kanayi–Okayamy | µm |
| $\omega$ | wydajność fluorescencji | — |
| $\lambda$ | długość fali promieniowania | nm |
| $\bar l$ | średnia droga swobodna | mm |
| $\varepsilon$ | średnia energia wytworzenia pary elektron–dziura w Si (3,6 eV) | eV |
| $\mathcal F$ | czynnik Fano | — |
| $N$ | liczba zliczeń | — |

### 3.3. Oznaczenia linii i pierwiastków

- Notacja Siegbahna: K$\alpha$, K$\beta$, L$\alpha$; w LaTeX makro `\Ka` = `K$\alpha$` (do wspólnego szablonu). Pierwiastek + linia ze spacją niełamliwą: `Si~\Ka`.
- Wartości energii linii (jedno źródło, tablice; nie podawać innych zaokrągleń):
  O K$\alpha$ 0,525 keV; Mg K$\alpha$ 1,254 keV; **Al K$\alpha$ 1,487 keV**; Si K$\alpha$ 1,740 keV; Ca K$\alpha$ 3,69 keV; Mn K$\alpha$ 5,90 keV; Fe K$\alpha$ 6,40 keV.
  Energie krytyczne: Si K 1,84 keV; Al K 1,56 keV; Fe K 7,11 keV.

### 3.4. Zapis liczb i jednostek

- Przecinek dziesiętny, w LaTeX zawsze przez `siunitx` (`\SI`, `\SIrange`, `\num`), jednostki makrami (`\kilo\volt`, `\micro\ampere`), nie tekstem „V”, „µA”. Ustawienia `siunitx` — we wspólnym szablonie.
- Zakresy: `\SIrange{10}{18}{\kilo\volt}`; w tekście bez LaTeX półpauza „10–18 kV”.
- Ciśnienie: Pa jako podstawowa jednostka; `\SI{1e-3}{\pascal}`.
- Wymiary: µm, mm; masa: g; temperatura procesu: °C.

## 4. Terminy preferowane i zakazane

| Używać | Nie używać | Uwagi |
|---|---|---|
| **relaksacja** atomu, przejście elektronowe | „rekombinacja” (dla atomu) | „rekombinacja” wyłącznie dla par elektron–dziura w detektorze |
| promieniowanie X | „promienie X”, „promieniowanie RTG” | przymiotnik: „rentgenowski” (spektrometr, lampa, widmo) |
| promieniowanie hamowania (przy 1. użyciu: *bremsstrahlung*) | „promieniowanie ciągłe” jako jedyna nazwa | |
| linie charakterystyczne / promieniowanie charakterystyczne | „fale charakterystyczne” | |
| **spektroskopia EDS** (metoda), **spektrometr** (przyrząd), **widmo** | „spektrometria EDS” zamiennie | WDS analogicznie |
| emisja polowa (przy 1. użyciu: zimna emisja polowa) | „emisja autoelektronowa”, „field emission” | |
| prąd emisji, prąd upływu, prąd targetu, prąd bramki | „prąd anody” | |
| napięcie ekstrakcyjne / napięcie przyspieszające | „napięcie bramki” zamiennie z ekstrakcyjnym bez symbolu | zawsze z symbolem przy pierwszym użyciu w rozdziale |
| wiązka elektronów | „wiązka elektronowa” zamiennie | |
| ogniskowanie magnetyczne / elektrostatyczne | „skupianie”, „zagęszczanie wiązki” | |
| bonding anodowy | „spajanie anodowe”, „bondowanie” | |
| odgazowanie (przez wygrzewanie w ok. 200 °C) | „wypiekanie”, „bake-out” | |
| skład pierwiastkowy | „skład chemiczny” | EDS daje pierwiastki, nie związki |
| analiza jakościowa / ilościowa | | |
| wzbudzenie (linii, próbki) | „wywalanie fotonów”, „bombardowanie” (potocznie) | |
| struktura krzemowo-szklana | „kanapka” | |
| hermetyczna / niehermetyczna | | prototyp: niehermetyczny, badania w komorze próżniowej; bonding w próżni: rozwiązanie docelowe |
| sesja pomiarowa, seria pomiarów | | oznaczenia sesji: zob. N4 |

## 5. Zasady stylu (wspólne)

1. Strona bezosobowa i formy na „-no/-to”: „wykonano”, „zmierzono”, „zaprezentowano na rys. 5.2”. Bez 1. i 2. osoby („wykonałem”, „Twoim”), bez „my”.
2. Czasy: opis własnych prac i pomiarów w czasie przeszłym („zmierzono”); fizyka, zasady działania, wnioski ogólne w teraźniejszym („prąd rośnie wykładniczo”).
3. Rzeczowo, jak w raporcie: bez pytań retorycznych, ozdobników i wtrąceń typu „warto zauważyć”, „należy podkreślić”, „bardzo”, „ogromny”, „przełomowy”. „W pracy” zamiast „W niniejszej pracy” (dopuszczalne raz we wstępie).
4. Akapit = jedna myśl. Zdania krótkie. Bez powtarzania treści innych rozdziałów: odsyłać przez `\ref` („p.~\ref{subsec:bonding}”, „rozdz.~\ref{ch:pomiary}”).
5. Odwołania: „rys.~\ref{}”, „tab.~\ref{}”, „wzór~\eqref{}”, „rozdz.”, „p.” (punkt). Małą literą w środku zdania, z tyldą.
6. Liczby z jednostką zawsze przez `siunitx`; „ok.” zamiast „około” i „~” przy przybliżeniach.
7. Nazwiska w nazwach praw i wzorów z półpauzą: równanie Fowlera–Nordheima, model Deala–Grove'a, wzór Kanayi–Okayamy, granica Duane'a–Hunta (w LaTeX `--`).
8. Terminy angielskie kursywą tylko przy pierwszym użyciu, z „ang.”.
9. Spójniki jednoliterowe z tyldą (`w~`, `z~`, `i~`, `a~`) — jak w istniejących plikach.
10. Podpisy: „opracowanie własne” lub „na podstawie [x]” przy rysunkach adaptowanych.

---

## 6. Niespójności znalezione w istniejących tekstach

Kolejność: od najistotniejszych merytorycznie. Plik/linia podane, żeby właściwy wątek mógł poprawić.

| # | Gdzie | Problem | Proponowana poprawka |
|---|---|---|---|
| N1 | `opis-tematu-v2` (cel), `podstawy_teoretyczne.tex` l. 288, 290, 443–446, 720; `emisja_tresc.tex` | **Rozstrzygnięte:** emisja przy $U_\mathrm{T}=\SI{2}{\kilo\volt}$ (\SI{1.5}{\kilo\volt} z magnesem), widma przy $U_\mathrm{T}=\SI{4}{\kilo\volt}$ ($E_0\approx\SI{4}{\kilo\electronvolt}$ z granicy Duane'a–Hunta). Podstawy liczą przykłady dla \SI{15}{\kilo\volt} i piszą, że „dobrze wzbudzane są linie K pierwiastków do żelaza” — przy \SI{4}{\kilo\volt} nieprawda. $U_0$ przy \SI{4}{\kilo\electronvolt}: Mg K ≈ 3,1, Al K ≈ 2,6, Si K ≈ 2,2 (dobre wzbudzenie); **Ca K (4,04 keV) i Fe K (7,11 keV) nie wzbudzają się**, z Fe widoczna co najwyżej Fe L$\alpha$ (0,705 keV). Weryfikacja celu przez Al K$\alpha$ jest w zasięgu (zmierzona). | Podstawy: przykłady przeliczyć dla \SI{4}{\kilo\volt} lub podawać oba przypadki (pomiar / docelowo \SIrange{10}{18}{\kilo\volt}); lista „O, Mg, Al, Si, Ca, Fe” → przy \SI{4}{\kilo\volt} tylko lekkie pierwiastki do Si (i K, Cl, S przy małym $U_0$). Zasięg Kanayi–Okayamy dla Si: ok. \SI{0.3}{\micro\metre} przy \SI{4}{\kilo\electronvolt}. Rozdział pomiarów: wyjaśnić, dlaczego napięcie było niższe od docelowego. |
| N2 | `podstawy_teoretyczne.tex` l. 350–352 vs `emisja_tresc.tex` (wnioski 5–6) | Podstawy twierdzą, że magnes „zwiększył prąd docierający do targetu i zmniejszył średnicę plamki”. Rozdział pomiarów mówi, że wzrostu prądu nie da się oddzielić od braku odgazowania, a średnicy plamki nie zmierzono. | Przepisać w podstawach na: „wpływ magnesu na kształt plamki przedstawiono w rozdz. \ref{}” — bez wniosków ilościowych w teorii. |
| N3 | `emisja_tresc.tex` (cały) vs `podstawy`, schemat | Napięcie ekstrakcyjne oznaczone jako $U$ (bez indeksu), napięcie targetu jako $U_\text{target}$ i $U_\text{t}$ (dwa warianty). | $U \to U_\mathrm{B}$, $U_\text{target}, U_\text{t} \to U_\mathrm{T}$. |
| N4 | `emisja_tresc.tex` | „Sesja B” (bez magnesu) koliduje z oznaczeniem bramki B. | Sesje: **N** (bez magnesu), **M** (z magnesem), seria 2 → **N2**. |
| N5 | `emisja_tresc.tex` l. 142 i wykresy | Intensywność świecenia oznaczona $I$ — ten sam symbol co prąd. | Intensywność: $L$ [j.u.]. |
| N6 | `podstawy` l. 262–264 vs schemat (`uklad-pomiarowy`) | Podstawy: „prąd emisji wyznaczano z napięcia na rezystorze 100 kΩ” (jeden), schemat ma dwa rezystory $R$ (target) i $R_\mathrm{B}$ (bramka). Prąd emisji = $I_\mathrm{B}+I_\mathrm{T}$ — nie jest jasne, który prąd podano w tab. emisji jako $I_e$. | Ustalić, co mierzono jako $I_\mathrm{e}$; $R \to R_\mathrm{T}$ w schemacie i podpisie. **Rozstrzygnięte:** w tabeli jest prąd emisji $I_\mathrm{e}$; w rozdz. o układzie pomiarowym jednym zdaniem opisać, z napięć na których rezystorach go wyznaczono. |
| N7 | `uklad-pomiarowy/schemat_ukladu.tex` | Etykieta „zasilacz 2 (bramka, $B_\mathrm{on}$)” — $B_\mathrm{on}$ nigdzie niezdefiniowane; komentarz „rezystor R i amperomierz”, a na schemacie woltomierz. | Usunąć $B_\mathrm{on}$ lub zdefiniować; poprawić komentarz. |
| N8 | `opis-tematu-v2` („Potencjalne przeszkody”) | „elektrony padające na … magnes, wzbudzające linie … Mg K$\alpha$” — magnes NdFeB nie zawiera magnezu (Nd, Fe, B; zwykle powłoka Ni). Arkusz pomiarów nazywa się `magnez_emisja` — możliwa pomyłka magnes/magnez. | W pracy pisać o liniach Fe/Ni (Nd L) od magnesu, chyba że w układzie jest element z Mg. Do potwierdzenia. |
| N9 | `uklad-pomiarowy/rysunek_w_pracy.tex` | Podpis: „…w miniaturowym źródle RTG MEMS” — dotyczy własnego prototypu. | „…w prototypie analizatora EDS”. |
| N10 | `opis-tematu-v2` vs `podstawy` l. 482 | Al K$\alpha$ = 1,486 keV vs 1,487 keV. | 1,487 keV (tab. 3.3). Opisu tematu nie trzeba już zmieniać. |
| N11 | `wstep_opcja_C.tex` l. 50, `opis-tematu-v2` | „skład chemiczny” — EDS daje skład pierwiastkowy. | „skład pierwiastkowy” w pracy. |
| N12 | `wstep_opcja_C.tex`, `opis-tematu-v2`, notatka EDS | Rozwinięcie EDS: „Energy Dispersive Spectroscopy” vs „Energy-Dispersive X-ray Spectroscopy”. | W pracy: *Energy Dispersive X-ray Spectroscopy* (wykaz skrótów). |
| N13 | `podstawy` l. 621 vs `wstep_opcja_C.tex` | „spektrometria z dyspersją energii (EDS)” vs „spektroskopia EDS”. | „spektroskopia”. |
| N14 | `podstawy` l. 137, 670 vs notatki | Ciśnienie raz w hPa, raz w Pa. | Pa, hPa w nawiasie przy cytowaniu źródła. |
| N15 | `podstawy` (wzory) | Kolizje symboli: $R$ = zasięg i rezystor; $\lambda$ = długość fali i droga swobodna; $\vec F$ = siła Lorentza i $F$ = pole w F–N; $i$ = prąd w Kramersie obok $I$. | $R_\mathrm{KO}$, $\bar l$, $\vec F_\mathrm{L}$, $I_\mathrm{T}$ (tab. 3.2). |
| N16 | sprawozdanie vs `podstawy` l. 152–160 | **Rozstrzygnięte:** bonding anodowy wykonano w atmosferze. | W podstawach zamienić „Elementy złożono bez zamknięcia próżniowego” na „Elementy połączono bondingiem anodowym w atmosferze, bez zamknięcia próżniowego” i usunąć TODO. W tym samym akapicie usunąć TODO o ciśnieniu: rzędu $10^{-5}$ (jednostka do potwierdzenia). |
| N21 | `podstawy` l. 109–118 | **Rozstrzygnięte:** emiter to kompozyt CNT-PVP jak w rozprawie Urbańskiego, nakraplany pipetą na płycie grzejnej \SI{240}{\celsius}. | Dopisać sposób naniesienia w prototypie i usunąć TODO l. 118. |
| N22 | `podstawy` l. 565, l. 532 | TODO „wpisać typ detektora”. | Wpisać: procesor impulsów KETEK DPP2, detektor prawdopodobnie KETEK SDD (do potwierdzenia u promotora). Model pomp, odległość i kąt detektora: zostawić w rejestrze TODO. |
| N23 | `podstawy` l. 345–349, `emisja_tresc.tex` | Magnes opisany jako „umieszczony pod katodą z emiterem” — zgodne z faktem (na emiterze), ale nie ma parametrów magnesu, więc nie można liczyć $r_\mathrm{L}$ ani $f$ dla układu. | Przykład liczbowy promienia Larmora (\SI{0.1}{\tesla}) oznaczyć jako szacunek dla typowego magnesu NdFeB, nie jako parametr układu. |
| N17 | `emisja_tresc.tex` l. 158 | „Warto zauważyć, że…” — wtrącenie niezgodne ze stylem. | Usunąć wtrącenie. |
| N18 | `emisja_tresc.tex` vs `podstawy` | Jednostki raz `\SI{100}{V}` i „µA” jako tekst, raz `\volt`, `\micro\ampere`; różne ustawienia `siunitx` (`locale=DE` vs `output-decimal-marker`). | Makra jednostek + jedno ustawienie we wspólnym szablonie. |
| N19 | `uklad-pomiarowy/uklad_pomiarowy_body.tex` | Plik przeznaczony do `\input` zawiera `\documentclass` i preambułę — złamie kompilację pracy. | Zostawić w nim tylko środowisko `circuitikz` (dla wątku szablonu). |
| N20 | `wstep_opcja_C.tex` l. 38 | „W niniejszej pracy” | Dopuszczalne raz we wstępie; w pozostałych rozdziałach „W pracy”. |

Otwarte nadal: **N8** (skąd Mg K$\alpha$ od magnesu w opisie tematu). Pozostałe pozycje mogą poprawiać wątki rozdziałów bez pytania autora.
