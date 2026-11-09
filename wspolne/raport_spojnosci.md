# Raport spójności pracy — przegląd nr 1

Stan na 2026-11-09. Przegląd wykonany na plikach w folderze projektu. Rozdziałów nie poprawiano; raport wskazuje zmiany i przypisuje je do plików.

Oparto się na: `wspolne/budzet_stron.md`, `wspolne/slownik.md` (niespójności **N1–N20**), `wspolne/rejestr_todo.md` (**A1–A21**, **B1–B16**). Tych pozycji nie powtarzano. Raport dodaje to, czego tam nie ma: pomiar objętości z kompilacji, ocenę stylu, mapę powtórzeń między rozdziałami, zgodność z wymaganiami WEFiM i nowe niezgodności (**B17–B24**, dopisane też do rejestru).

**Nie sprawdzono** repozytorium `W:\VAULT\Inzynierka\latex` (komputer był niedostępny): `chapters/01–06`, `frontmatter/` (streszczenia, wykaz skrótów), `body.tex`. Do sprawdzenia w następnym przeglądzie.

---

## 0. Najważniejsze wnioski

1. **Objętość:** istniejące teksty (wstęp, podstawy teoretyczne, fragment pomiarów emisji ze schematem) zajmują po kompilacji **23 strony**. Same podstawy teoretyczne mają **14 stron** przy budżecie 10. Przy obecnych proporcjach praca nie zmieści się w 50 stronach, jeśli rozdz. 3–5 mają osiągnąć zalecane 60–70 % objętości.
2. **Brakuje rdzenia pracy:** nie ma tekstu rozdziałów „Projekt”, „Realizacja”, widm EDS (weryfikacja celu wg opisu tematu), podsumowania, streszczeń ani celu i zakresu pracy w rozdz. 1. Teoria jest dziś najdłuższą częścią pracy, a wyniki własne mają ok. 6 stron.
3. **Trzy różne sformułowania celu pracy** (plik pracy, opis tematu v2, sprawozdanie) — trzeba wybrać jedno i z niego zbudować p. 1.2 i podsumowanie (B17).
4. **Treść teorii wyprzedza lub przeczy wynikom:** zapowiada wykres F–N i porównanie przed/po odgazowaniu (B4), twierdzi, że odgazowanie wykonywano przed pomiarami (B18), i przypisuje magnesowi zmniejszenie plamki (B3).
5. **Nowe pytanie merytoryczne:** w sesji z magnesem napięcie bramki osiągało 1600–1700 V przy napięciu targetu 1500 V (B20). Może to tłumaczyć nasycenie prądu i trzeba to wyjaśnić przed interpretacją wyników.
6. Styl językowy jest w większości zgodny z zasadami (bezosobowy, rzeczowy). Poprawki stylu są drobne i wymienione w p. 5.

---

## 1. Objętość — wynik kompilacji

Kompilacja LuaLaTeX trzech istniejących tekstów razem (`wstep_opcja_C.tex`, `podstawy_teoretyczne.tex`, schemat układu, `emisja_tresc.tex`) z parametrami wspólnej preambuły: A4, 12 pt, Times (TeX Gyre Termes), marginesy 30/25 mm, interlinia `\setstretch{1.1}`, rozdziały od nowej strony. Kompilacja przeszła bez błędów (po usunięciu preambuły z `uklad_pomiarowy_body.tex`, zob. N19). W PDF widocznych jest 9 czerwonych znaczników `\TODO`.

| Część | Strony (kompilacja) | Budżet | Różnica |
|---|---:|---:|---:|
| Rozdz. 1 Wstęp (opcja C, bez celu i zakresu) | 2 (tekst ok. 1,3) | 2,5 | do dopisania cel i zakres (ok. 1 str.) |
| Rozdz. 2 Podstawy teoretyczne i technologiczne | **14** | 10 | **+4** (bez planowanych 3 rysunków; z nimi ok. +5) |
| Schemat układu (rozdz. 4) | ok. 0,5 | część z 3,5 | ✅ |
| Fragment 5.1 (emisja, magnes) | ok. 6,5 | 6 | +0,5 (po przeniesieniu „Metody analizy zdjęć” i „Wniosków” mieści się) |
| **Razem istniejące** | **23** | | |

Kalibracja przelicznika budżetu: tekst ma ok. 6100 słów na 23 stronach, rozdz. 2 ok. 3700 słów na 14 stronach, czyli **ok. 270 słów na stronę w rozdziale z wieloma wzorami i nagłówkami**, a nie 400. Wynika to z 48 podsekcji i 17 wyróżnionych równań. Wniosek dla budżetu: w rozdziałach z rysunkami i wzorami liczyć ok. 300 słów/str.; rozdz. 2 przy 10 stronach powinien mieć ok. **2700–3000 słów** (dziś 3700) i nie więcej niż 15–18 podsekcji.

Prognoza całości przy obecnych tekstach i budżecie dla brakujących części: 6 (część wstępna) + 2,5 + 14 + 6,5 (rozdz. 3) + 3,5 (rozdz. 4) + 13 (rozdz. 5) + 1,5 + 3 (literatura) + 1 (zał. A) = **ok. 51 stron bez rezerwy**. Limit 50 stron jest więc osiągalny tylko po skróceniu rozdz. 2 do budżetu.

---

## 2. Zgodność z wymaganiami PWr / WEFiM (Golden Standard)

| Wymaganie | Stan | Uwagi |
|---|---|---|
| Strona tytułowa wg wzoru, tytuł = APD | ✅ | Tytuł identyczny w pliku pracy, opisie tematu i sprawozdaniu (rejestr, sekcja C). Uzupełnić `\supervisor{}` (A19). |
| Streszczenie PL + EN, tożsame z APD | ❌ brak w plikach projektu | Termin APD 18.12.2026 (A20). |
| Spis treści | ✅ automatyczny | |
| Wykaz skrótów i oznaczeń | ⚠️ | Treść gotowa w `slownik.md` p. 2–3; brak pliku `.tex`. |
| Wstęp z uzasadnieniem tematu | ✅ | Opcja C. |
| **Cel i zakres pracy** | ❌ | Opcja C nie zawiera celu ani zakresu (co wchodzi, co nie). Zob. B17. |
| Wprowadzenie teoretyczne | ⚠️ | Za długie (p. 1), brak rysunków (Golden Standard: „czytelne schematy blokowe i rysunki”). |
| Prace własne 60–70 % | ❌ | Dziś ok. 30 % istniejącego tekstu. Rozdz. 3, 4 (poza schematem) i widma EDS nie istnieją (A15, A16). |
| Wyniki na wykresach + interpretacja + porównanie z literaturą | ⚠️ | Fragment 5.1 ma wykresy i interpretację, ale **nie porównuje wyników z literaturą** (np. progi emisji i prądy z rozprawy Urbańskiego, `grzebyk2017magnetic`). Dodać 2–3 zdania z cytowaniem. |
| Podsumowanie nawiązujące do celów | ❌ brak | „Wnioski” z 5.1 przenieść do rozdz. 6 (budżet). |
| Literatura min. 20–30 poz., jednolity format | ✅ | 39 pozycji we `wspolne/bibliografia.bib`, IEEE. Wstęp nadal ma klucze `TODO-…` (A9). |
| Rysunki numerowane w rozdziale, podpis pod; tabele — podpis nad | ✅ | We fragmencie 5.1 poprawnie; wspólna preambuła ustawia numerację. |
| Podpis „opracowanie własne” / „na podstawie [x]” | ⚠️ | Jest tylko przy schemacie. Dodać przy zdjęciach plamek („opracowanie własne”) i przy rysunkach przerysowanych z rozprawy. |
| Druk dwustronny | ✅ | `main.tex` w repo; `openany` vs `openright` — budżet, p. 1. |
| Bez kopiowania bez cytowania (JSA) | ⚠️ | Wstęp i opis tematu mają identyczny akapit o dyscyplinie (własny tekst, bez ryzyka). Rysunki z `knowledge/Inzynierka/images/` nie mogą trafić do pracy wprost (latex-workflow). |

---

## 3. Uwagi do rozdziałów

### 3.1. Rozdz. 1 — Wstęp (`wstep-zagajenie/wstep_opcja_C.tex`)

| # | Miejsce | Problem | Zmiana |
|---|---|---|---|
| W1 | brak | Brak p. 1.2 „Cel i zakres pracy” (Golden Standard p. 1, budżet). | Dopisać ok. 1 str.: cel główny (jedno brzmienie, B17), cele szczegółowe (aspekt badawczy i inżynierski z pliku pracy, w czasie przeszłym/teraźniejszym, nie „zostanie zaprojektowane”), zakres: co jest poza pracą (hermetyzacja, zasilacz, detektor — B7), krótki układ pracy (rozdz. 2–6). |
| W2 | l. 22–29 | „nie jest w tych zastosowaniach stosowane” — zbyt kategoryczne wobec projektów miniaturowych SEM cytowanych w rozdz. 2 (B15). | „…nie jest stosowane w przyrządach, które dotychczas wykorzystano w misjach”. |
| W3 | l. 28–30 vs rozdz. 2 l. 686–689 | Ta sama myśl o naturalnej próżni na Księżycu/planetoidach. | Zostawić we wstępie jedno zdanie, w rozdz. 2 tylko dane liczbowe (ciśnienie, Mars) z odwołaniem „(zob. rozdz. 1)” albo usunąć z rozdz. 2. |
| W4 | l. 56–66 vs rozdz. 2 l. 717–730 | Ostatni akapit wstępu (autonomiczna praca, sterowanie emisją, identyfikacja linii przed wysłaniem danych) powtarza niemal słowo w słowo koniec podsekcji „Elektronika zasilania i sterowania”. | Zostawić we wstępie (uzasadnienie zgodności z kierunkiem), w rozdz. 2 usunąć ostatnie dwa zdania. Podsekcja i tak ma trafić do rozdz. 3 (budżet). |
| W5 | l. 36–38 | „wymiary rzędu centymetrów i masa rzędu gramów” — dane źródła Urbańskiego (B9). | Przypisać z cytowaniem. |
| W6 | l. 19–21 | APXS i PIXL opisane i we wstępie, i w rozdz. 2 („Porównanie z przyrządami…”). | Opis przyrządów tylko w jednym miejscu: wstęp (stan techniki) albo 5.4 (budżet). W rozdz. 2 usunąć. |
| W7 | l. 38 | „W niniejszej pracy” | Dopuszczalne raz (N20). |
| W8 | cały | Klucze `\cite{TODO-…}` | Zamienić wg tabeli w `wspolne/README.md` (A9). |

### 3.2. Rozdz. 2 — Podstawy teoretyczne i technologiczne (`podstawy-teoretyczne/podstawy_teoretyczne.tex`)

Skróty i przeniesienia zalecone w budżecie (p. 3) są zasadne i tu ich nie powtarzano. Dodatkowo:

| # | Miejsce | Problem | Zmiana |
|---|---|---|---|
| T1 | l. 273–275 | „przed pomiarami źródło odgazowuje się przez wygrzewanie (w tej pracy ok. 200 °C)” — sugeruje, że odgazowanie było przed wszystkimi pomiarami; według 5.1 było tylko przed jedną sesją (B18). | „W pracy jedną z sesji pomiarowych poprzedzono odgazowaniem w ok. 200 °C (rozdz. \ref{sec:emisja-magnes}).” |
| T2 | l. 346–352 | Teza o wpływie magnesu (B3). Propozycja brzmienia: | „Wpływ magnesu na kształt plamki w badanym prototypie przedstawiono w rozdz.~\ref{sec:emisja-magnes}.” — i usunąć zdanie o zwiększeniu prądu i średnicy. |
| T3 | l. 534–541 („Charakterystyka prądowo-napięciowa emitera”) | Opis metodyki, nie teorii; zapowiada F–N i „przed i po odgazowaniu”, których w wynikach nie ma (B4). | Przenieść do rozdz. 4 (metodyka) i zapowiadać tylko to, co jest w rozdz. 5. |
| T4 | l. 254–264 („Wywołanie emisji w badanym układzie”) | Opis własnego układu i pomiaru prądu w rozdziale teorii; powiela schemat i rozdz. 4. | Zostawić 2 zdania (rola $U_\mathrm{B}$ i $U_\mathrm{T}$), pomiar prądu przez 100 kΩ przenieść do rozdz. 4. Zastąpić „rozdz. \TODO{nr}” odwołaniem `\ref` (A8). |
| T5 | l. 299–313 | Podsekcja „Napięcia w układzie” dubluje T4 (ta sama rola $U_\mathrm{B}$/$U_\mathrm{T}$) i opisuje pomiar prądów (B12). | Scalić z T4 w jedną podsekcję. |
| T6 | l. 443–446, 288–297, 719–720 | Wszystkie przykłady liczbowe dla 15 kV, zakres 10–20 kV; w pomiarach emisji $U_\mathrm{T}$ = 1,5–2 kV (N1/B1). | Po ustaleniu $U_\mathrm{T}$ dla widm przyjąć jeden zakres (np. 10–18 kV jak w opisie tematu) i jedną wartość przykładową. |
| T7 | l. 345–349 | „magnes trwały NdFeB umieszczony pod katodą z emiterem” — „katoda” niezgodna ze słownikiem (emiter), położenie magnesu sprzeczne z notatką (B6). | „pod emiterem” po potwierdzeniu położenia (A17). |
| T8 | l. 732–741 („Bezpieczeństwo pracy”) | Formy nakazowe („należy zachować odległość”) — instrukcja BHP, nie treść pracy. | Usunąć (budżet) lub 1 zdanie w rozdz. 4. |
| T9 | cały | 0 rysunków na 14 stronach. | Dodać 2–3 własne rysunki zastępujące tekst: schemat procesu MEMS (zamiast wyliczanki kroków), przekrój źródła E–B–T z magnesem i liniami pola, schemat relaksacji (linie Kα/Kβ). |
| T10 | l. 646–648 | Zdanie o braku analizy ilościowej + TODO (A6). | Po potwierdzeniu: jedno zdanie w rozdz. 4 lub 5, w rozdz. 2 tylko definicja analizy jakościowej. |
| T11 | l. 11 | Tytuł rozdziału „Podstawy teoretyczne i technologiczne” vs plan „Wprowadzenie teoretyczne” (B13). | Zostawić obecny tytuł (lepiej opisuje treść) i zaktualizować plan w Golden Standard/repo. |

### 3.3. Fragment 5.1 — Wpływ magnesu na emisję (`emisja-magnes-pomiary/emisja_tresc.tex`)

Oznaczenia ($U\to U_\mathrm{B}$, $U_\text{target}\to U_\mathrm{T}$, sesje N/M, $I\to L$, jednostki) są w N3–N5, N17, N18. Dodatkowo:

| # | Miejsce | Problem | Zmiana |
|---|---|---|---|
| E1 | l. 26, 32 | Nazwy plików roboczych w tekście pracy: „arkusz *Book1*, seria 1”, „arkusz *magnez\_emisja*” (B19). | Usunąć; opisać serie przez warunki pomiaru (data, $U_\mathrm{T}$, magnes tak/nie, odgazowanie). |
| E2 | tab. `tab:emisja-iv`, l. 29–33, wnioski | Sesja M: $U_\mathrm{B}$ do 1700 V przy $U_\mathrm{T}$ = 1500 V; dla $U_\mathrm{B}\ge U_\mathrm{T}$ target nie przyspiesza elektronów względem bramki, które przejmuje prąd (B20). | Wyjaśnić z autorem konwencję napięć (A13, B1). Jeśli $U_\mathrm{B}$ przekraczało $U_\mathrm{T}$, uwzględnić to w interpretacji nasycenia ok. 200 µA i nie przypisywać nasycenia tylko brakowi odgazowania. |
| E3 | l. 136, wzór `eq:nadmiar-niebieskiego` | Symbol $e$ (nadmiar niebieskiego) koliduje z ładunkiem elementarnym $e$ z rozdz. 2 (B21). | Np. $b_\mathrm{n}$ albo $\Delta B$; dopisać do słownika. |
| E4 | l. 154–163, 324 | Współczynnik korelacji $r$ — ten sam symbol co promień ostrza i $r_\mathrm{L}$ w rozdz. 2. | Dopuszczalne, jeśli przy pierwszym użyciu napisać „współczynnik korelacji Pearsona $r$”; dopisać do słownika. |
| E5 | l. 158 | „Warto zauważyć” (N17). | „W sesji M słaba plamka jest widoczna już przy…” |
| E6 | cały | Brak porównania z literaturą (Golden Standard, checklista). | 2–3 zdania: próg i prąd emisji vs rozprawa Urbańskiego / `krysztof2022emitter`; efekt magnesu vs `grzebyk2017magnetic` (tam też liczba 50 % → 5 %, B10). |
| E7 | „Metoda analizy zdjęć”, „Wnioski” | Metodyka i wnioski w rozdziale wyników. | Przenieść do rozdz. 4 i 6 (budżet). |
| E8 | rys. `fig:emisja-sbs`, `fig:emisja-mg-skrajne`, `fig:emisja-pelne` | Zdjęcia bez dopisku o źródle. | Dodać „(opracowanie własne)”. Rozważyć usunięcie `fig:emisja-pelne` (ok. 0,4 str.), jeśli zabraknie miejsca. |
| E9 | seria 2 | Tekst podaje „\SIrange{1}{400}{\micro A}” jako fakt, choć jednostka i warunki serii 2 są niepotwierdzone (A11). | Do czasu potwierdzenia oznaczyć `\TODO` w tekście, nie tylko w rejestrze. |

### 3.4. Rozdz. 4 — schemat układu (`uklad-pomiarowy/`)

Uwagi N6, N7, N9, N19 i B12 obejmują wszystko, co znaleziono. Wspólna preambuła ładuje pakiet `standalone`, więc N19 nie złamie już kompilacji, ale plik `uklad_pomiarowy_body.tex` i `schemat_ukladu.tex` są identyczne; zostawić jeden (B22).

### 3.5. Dokumenty poza pracą (opis tematu v2, sprawozdanie)

Nie wymagają zmian (są złożone), ale praca musi być z nimi zgodna albo świadomie od nich odejść: cel (B17), zakres napięć 10–18 kV (B1), Al Kα 1,487 keV (N10), linia Mg (B6), bonding (B2).

---

## 4. Mapa powtórzeń między rozdziałami

| Treść | Gdzie występuje | Gdzie zostawić |
|---|---|---|
| Naturalna próżnia na ciałach bez atmosfery | wstęp l. 28–30; rozdz. 2 l. 157–159, 686–689; opis tematu | wstęp (1 zdanie) + rozdz. 2 tylko liczby (Mars, Księżyc) |
| APXS, PIXL, CheMin | wstęp l. 19–21; rozdz. 2 l. 697–715 | wstęp (stan techniki) lub 5.4 |
| Autonomia, sterowanie emisją, identyfikacja linii przed wysłaniem danych | wstęp l. 56–66; rozdz. 2 l. 724–730 | wstęp |
| Rola $U_\mathrm{B}$ i $U_\mathrm{T}$, pomiar prądu przez 100 kΩ | rozdz. 2 l. 254–264 i 299–313; schemat; 5.1 | rozdz. 2: 2 zdania fizyki; rozdz. 4: pomiar |
| Odgazowanie przy 200 °C | rozdz. 2 l. 273–275; 5.1 l. 27–33, 82–84 | 5.1 (fakt), rozdz. 2 (dlaczego się odgazowuje) |
| Stanowisko pomiarowe | rozdz. 2 l. 523–532; schemat | rozdz. 4 |
| Detektor: typy Si(Li)/SDD/CdTe | rozdz. 2 l. 553–565; plan rozdz. 3.6 | rozdz. 2 (teoria) + rozdz. 4 (użyty model, A5) |
| Wnioski z pomiarów emisji | 5.1 „Wnioski” | rozdz. 6 |

---

## 5. Styl językowy

Ocena ogólna: **zgodny z zasadami projektu**. Teksty są bezosobowe („porównano”, „wyznaczono”, „opisano”), rzeczowe, bez pytań retorycznych i bez pierwszej osoby. „Relaksacja” dla atomu i „rekombinacja” tylko dla nośników w detektorze — poprawnie. Czasy: wyniki w przeszłym, fizyka w teraźniejszym — poprawnie.

Odstępstwa do poprawy:

| Plik | Miejsce | Uwaga |
|---|---|---|
| `emisja_tresc.tex` | l. 158 | „Warto zauważyć” (N17). |
| `emisja_tresc.tex` | l. 87–89 | „Prawdopodobnie dlatego w sesji M obserwuje się:” — hipoteza podana jako lista faktów; przy niepotwierdzonym A12 dopisać zastrzeżenie raz, na początku podrozdziału. |
| `podstawy_teoretyczne.tex` | l. 738–741 | Tryb nakazowy („należy zachować odległość”) — T8. |
| `podstawy_teoretyczne.tex` | l. 99, 153, 274, 350, 503, 645, 676 | „w tej pracy” — dopuszczalne, ale słownik zaleca „w pracy”; ujednolicić. |
| `podstawy_teoretyczne.tex` | wyliczenia | Wiele list `itemize` z pogrubionymi hasłami (termoemisja, detektory, parametry spektrometru, piki pozorne). W pracy dyplomowej lepiej czyta się 2–3 zdania ciągłego tekstu; skrócenie list da też część potrzebnych stron. |
| `wstep_opcja_C.tex` | l. 50 | „skład chemiczny” → „skład pierwiastkowy” (N11). |
| wszystkie | półpauzy | W tekście ciągłym `--` jako myślnik (np. `emisja_tresc.tex` l. 133 „tło (…) -- pomarańczowo-czerwoną”); dopuszczalne w polskiej typografii, ale zasady projektu każą unikać wtrąceń z myślnikiem — zamienić na przecinek lub dwukropek tam, gdzie to łatwe. |

---

## 6. Nowe niezgodności (dopisane do `rejestr_todo.md` jako B17–B24)

| nr | Opis | Kto |
|---|---|---|
| B17 | Trzy różne brzmienia celu: plik pracy (projekt źródła + analiza ogniskowania + ocena MEMS), opis tematu v2 (zakres 10–18 kV, weryfikacja liczbą fotonów Al Kα, porównanie z/bez magnesu), sprawozdanie („czy umożliwia detekcję i identyfikację pierwiastków”). | kris |
| B18 | Rozdz. 2 l. 273–275 sugeruje odgazowanie przed wszystkimi pomiarami; 5.1 — tylko przed jedną sesją. | wątek teorii |
| B19 | 5.1 zawiera nazwy plików roboczych (Book1, magnez_emisja). | wątek pomiarów |
| B20 | Sesja z magnesem: $U_\mathrm{B}$ do 1700 V przy $U_\mathrm{T}$ = 1500 V; wpływ na interpretację nasycenia prądu. | kris |
| B21 | Symbol $e$ (nadmiar niebieskiego) koliduje z ładunkiem elementarnym; $r$ (korelacja) z promieniami. | wątek słownika |
| B22 | `uklad_pomiarowy_body.tex` i `schemat_ukladu.tex` to ten sam rysunek w dwóch plikach. | wątek szablonu |
| B23 | Rozdz. 2: realna gęstość ok. 270 słów/str. (kompilacja), budżet zakłada 400; rozdz. 2 przekracza budżet o 4 str. | wątek budżetu |
| B24 | Powtórzenia wstęp ↔ rozdz. 2 (naturalna próżnia, APXS/PIXL, autonomia przyrządu) — zob. p. 4. | wątki wstępu i teorii |

---

## 7. Kolejność działań (propozycja)

1. **kris:** odpowiedzieć na pytania blokujące: B17 (cel), B1/B20 (napięcia), A14 (który prąd), A12 (odgazowanie), B2 (bonding), A15 (widma EDS).
2. **Wątek teorii:** skrócić rozdz. 2 do ok. 2800 słów i 15–18 podsekcji (budżet p. 3 + T1–T11).
3. **Wątek wstępu:** dopisać cel i zakres (W1), usunąć powtórzenia (W3–W6).
4. **Wątek pomiarów:** E1–E9 i oznaczenia ze słownika.
5. **Następny przegląd spójności:** po wstawieniu rozdziałów do repo `W:\VAULT\Inzynierka\latex` — kompilacja `main.tex` w `dyplompwr`, liczenie stron całości, kontrola `frontmatter/`.

---

## 8. Aktualizacja 2026-11-09 (po odpowiedziach kris, poprawiona 15:31: widma przy $U_\mathrm{T}$ = 4 kV)

Odpowiedzi kris: **pomiary emisji** (rozdz. 5.1) przy $U_\mathrm{T}$ = **2000 V**, **pomiary widm** przy $U_\mathrm{T}$ = **4000 V** i $U_\mathrm{B}$ = **1000 V**; tło promieniowania hamowania kończy się przy ok. 4 keV (granica Duane'a–Hunta), więc energia elektronów na próbce $E_0 \approx$ **4 keV**; detektor najpewniej SDD firmy KETEK; dane w `widma-eds/`; bonding anodowy **w atmosferze** (struktura niehermetyczna); magnes NdFeB **leży na emiterze**, parametry nieznane; typu detektora nie da się ustalić; ciśnienie w komorze ok. **1e-5 hPa** (= 1e-3 Pa); nanorurki naniesione **pipetą na emiter na płycie grzejnej w 240 °C**. Rejestr: A3, A5, A17 zamknięte, B1 i B25 zaktualizowane przez wątek rejestru.

Skutki dla uwag z tego raportu:

| Uwaga | Zmiana po odpowiedziach |
|---|---|
| T6, N1/B1, B25 | Energia wiązki przy widmach $E_0 \approx \SI{4}{\kilo\electronvolt}$ (potwierdzona końcem tła w widmie — warto to pokazać w rozdz. 5 jako pomiar granicy Duane'a–Hunta, opisany już w rozdz. 2 l. 419–426), a nie 15 keV. Rozdz. 4 musi jasno opisać obie wartości ($U_\mathrm{T}$ = 4000 V, $U_\mathrm{B}$ = 1000 V) i względem czego są liczone (B1). Współczynnik nadnapięcia $U_0=E_0/E_\mathrm{c}$: O K ≈ 7,5, Mg K ≈ 3,1, Al K ≈ 2,6, Si K ≈ 2,2 (dobre wzbudzenie); Ca K (4,04 keV) — niewzbudzana, Fe K i Cu K — **niewzbudzane**, widoczne mogą być tylko ich linie L (Fe L ok. 0,70 keV, Cu L ok. 0,93 keV). Rozdz. 2 przestawić z przykładów dla 15 kV na 4 kV: l. 286–297 (prędkość ok. $\SI{3.75e7}{\metre\per\second}$, poprawka relatywistyczna ok. 0,6 %), l. 401–405 (zasięg w Si przy 4 keV ok. 0,3 µm zamiast 3 µm), l. 443–447 („linie K do żelaza” → „linie K pierwiastków do ok. Si; Ca, Fe, Cu tylko linie L”). Napięcia 10–18 kV podawać wyłącznie jako docelowe napięcie przyrządu (l. 719–720, rozdz. 1, rozdz. 6). Przykład Fe w l. 435–436 i 477–478 (prawo Moseleya) można zostać, ale bez sugestii, że Fe K mierzono. |
| E-rozdz. 5.1 | Pomiary emisji przy 2000 V i widma przy 4 kV to różne serie — w rozdz. 4 i 5 podać warunki każdej serii osobno ($U_\mathrm{T}$, $U_\mathrm{B}$, magnes, odgazowanie), żeby czytelnik nie łączył nasycenia ok. 200 µA z warunkami pomiaru widm. |
| B20 | Nadal aktualne: tab. emisji podaje dla sesji z magnesem $U_\mathrm{T}$ = 1500 V i $U_\mathrm{B}$ do 1700 V. Potwierdzić, czy 2000 V dotyczy też tej sesji. |
| T7, B6 | „Magnes NdFeB umieszczony na emiterze” — poprawić l. 346–347 („pod katodą z emiterem”). Bez parametrów magnesu opis w rozdz. 3 tylko jakościowy; „0,1 T” w l. 331–333 oznaczyć jako przykład rzędu wielkości. Przy 4 keV elektrony padające na magnes mogą wzbudzić Fe L, Nd M, Ni L (powłoka) — uwzględnić przy interpretacji widm. |
| B2, rozdz. 2 l. 152–160 | Napisać wprost: „elementy połączono bondingiem anodowym w atmosferze; struktura nie jest hermetyczna, badania prowadzono w komorze próżniowej przy ciśnieniu ok. \SI{1e-3}{\pascal}”. Bonding w próżni zostaje rozwiązaniem docelowym. |
| A2, rozdz. 2 l. 109–118 | „Metodę termo-mechaniczną opracowaną w zespole” zastąpić własną procedurą: zawiesina CNT naniesiona pipetą na emiter na płycie grzejnej w 240 °C (szczegóły w rozdz. 4, w rozdz. 2 tylko zasada). Zdanie o odporności emitera na bonding zostawić. |
| A5, rozdz. 2 l. 553–565 | Detektor: najpewniej SDD firmy KETEK. W rozdz. 2 zostawić opis SDD (Si(Li) i CdTe skrócić do zdania), w rozdz. 4 podać producenta i typ z zastrzeżeniem, jeśli nie da się potwierdzić modelu, oraz zmierzoną FWHM z widm. |
| Wstęp (W1) i cel (B17) | Opis tematu opiera weryfikację celu na linii Al Kα (1,487 keV). Przy 4 kV Al K jest dobrze wzbudzana ($U_0 \approx 2{,}6$), więc to kryterium można zachować. W p. 1.2 i podsumowaniu zaznaczyć, że badania widm wykonano przy $U_\mathrm{T}$ = 4 kV, a 10–18 kV to zakres docelowy (kierunek dalszych prac). |

---

## 9. Przegląd repozytorium `W:\VAULT\Inzynierka\latex` (2026-11-09, 15:40)

Komputer był dostępny; pliki przeczytano bezpośrednio. Na komputerze nie ma LaTeX-a (brak `lualatex`/`latexmk`) ani repozytorium git, a w folderze nie ma żadnego skompilowanego PDF, dlatego objętość oceniono na podstawie kompilacji `wspolne/main.tex` (p. 9.3).

### 9.1. Czy wątki przeniosły swoją pracę do repozytorium? — **Nie.**

Wszystkie pliki rozdziałów i części wstępnej mają datę 17.09.2026 (szkielet z `latex-workflow.md`), a `bibliography/bibliografia.bib` 03.10.2026 (20 wpisów). Żadna z dzisiejszych prac nie trafiła do repo:

| Element | W repozytorium | Gotowe w folderze projektu |
|---|---|---|
| Rozdz. 1 Wstęp | stara wersja z `Praca inzynierska.md`: czas przyszły („zostanie zaprojektowane”), `\cite{TODO}`, „masa rzędu pojedynczych gramów” bez źródła | `wstep-zagajenie/wstep_opcja_C.tex` (zatwierdzona 08.11) |
| Rozdz. 2 | same nagłówki i komentarze `% TODO`; zawiera 2.1.2 „Oddziaływanie promieniowania X z materią”, które kris wyłączył | `podstawy-teoretyczne/podstawy_teoretyczne.tex` |
| Rozdz. 3–4 | nagłówki | brak tekstu (A16) |
| Rozdz. 5 | nagłówki; 5.4 „Rejestracja widma EDS próbki testowej (Cu, Si, Al, Fe)” — przy $U_\mathrm{T}$ = 4 kV linie K Cu i Fe nie są wzbudzane | `emisja-magnes-pomiary/emisja_tresc.tex`, `widma-eds/` |
| Rozdz. 6 | nagłówki | — |
| Streszczenie / Abstract | szkic bez wyników; abstract w czasie teraźniejszym („is built”), streszczenie w przeszłym | `wspolne/frontmatter/dane_pracy.tex` (TODO) |
| Wykaz skrótów | 10 pozycji: zawiera HV i ESD (słownik każe ich nie używać), „keV” (jednostka, nie skrót), „dryftowy” zamiast „dryfowy”, rozwinięcie EDS bez „X-ray” (N12) | `wspolne/frontmatter/wykaz_skrotow.tex` (ze słownika) |
| Bibliografia | 20 wpisów, stuby `urbanski_pub*` | `wspolne/bibliografia.bib` (39 wpisów, DOI z Crossref) |
| Strona tytułowa | `\supervisor{[TODO…]}` (A19); fonty URW niedostępne bez instalacji | `wspolne/szablon/strona_tytulowa.tex` (wg wzoru WEFiM `inz_pl_w12n.docx`) |
| Preambuła | `siunitx` z `locale=DE`, `luainputenc` (przestarzały przy LuaLaTeX), brak makra `\TODO` | `wspolne/szablon/preambula.tex`, `makra.tex` |

### 9.2. Dwa równoległe szkielety pracy — wymaga decyzji

Istnieją teraz dwie wersje „pliku głównego”, które się wykluczają:

| | Repo `W:\VAULT\Inzynierka\latex` | `wspolne/main.tex` |
|---|---|---|
| Klasa | `dyplompwr` (na bazie `mwrep`) | `mwrep` + własna strona tytułowa |
| Interlinia | 1,0 (archiwalna), 1,5 (robocza) | 1,1 |
| Marginesy | zewn. 20 mm, wewn. 35 mm | 25 mm, wewn. 30 mm (jak Golden Standard) |
| Treść | szkielet z września | wszystkie dzisiejsze rozdziały przez wrappery `rozdzialy/*.tex` |
| Kompiluje się | nie sprawdzono (brak LaTeX-a na komputerze) | tak, 33 strony |

Preambuły nie da się po prostu przenieść do repo: `dyplompwr.cls` sam ładuje `geometry` i `setspace`, więc `wspolne/szablon/preambula.tex` dałby tam konflikt opcji pakietu `geometry`. Liczba stron zależy od wyboru: interlinia 1,0 vs 1,1 to ok. 1 strona na 20, a wersja robocza `dyplompwr` (1,5) to ok. +25 %.

**Rekomendacja:** przyjąć `wspolne/` jako źródło prawdy (zgodne z Golden Standard co do marginesów, ma całą treść i wspólną bibliografię) i skopiować je do repo jako nową zawartość folderu `latex\`, a stary szkielet przenieść do `latex\_archiwum_wrzesien\`. Do tego czasu żaden wątek nie powinien edytować plików w repo.

### 9.3. Objętość wg `wspolne/main.pdf` (33 str., stan 10:55)

Część wstępna 5 str. (tytułowa, streszczenia, spis treści 2 str., wykaz skrótów), rozdz. 1 — 2 str., **rozdz. 2 — 13 str.** (budżet 10), rozdz. 3 i 4 — puste, rozdz. 5 — 7 str. (sam fragment 5.1), rozdz. 6 — pusty, literatura 2 str., zał. A — pusty. Potwierdza to wnioski z p. 1: do napisania zostało ok. 20 stron (rozdz. 3, 4, widma EDS, 6, streszczenia), a mieści się ok. 17, jeśli rozdz. 2 nie zostanie skrócony.
