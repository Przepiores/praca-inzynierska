# Rozdział 3 — Projekt i wykonanie prototypu: plan akapitów

Stan: 2026-11-09, wersja 1. Kris podał układ warstw (od dołu: emiter z CNT, szkło 1 mm, bramka, szkło, target; szkic dośle). Napisano 3.1 i 3.2 w `projekt-prototypu/projekt.tex` (podgląd: `projekt-prototypu/rozdzial3_podglad.pdf`), rys. 3.1 jest poglądowy do podmiany po szkicu. T1 częściowo zamknięte (brak: położenie magnesu, grubość drugiego szkła).
Plik LaTeX docelowo: `projekt-prototypu/projekt.tex` (`\chapter{Projekt i~wykonanie prototypu}`, `\label{ch:projekt}`), podpinany w `wspolne/rozdzialy/03_projekt.tex`.

## 0. Założenia planu

- **Budżet:** 6,5 str. (`budzet_stron.md`). Przy kalibracji z `raport_spojnosci.md` (ok. 300 słów/str. w rozdziałach z rysunkami) daje to ok. **1500 słów tekstu + 4 rysunki + 2 tabele**. Budżet przewidywał 1 tabelę i 1900 słów; druga tabela (parametry procesów) zastępuje ok. 300 słów opisu, więc bilans stron się nie zmienia.
- **Podział z rozdz. 2:** rozdz. 2.1 opisuje *zasady* (fotolitografia, KOH i kąt 54,74°, utlenianie, bonding anodowy, bonding w próżni). Rozdz. 3 podaje tylko *to, co zrobiono w tej pracy*: wymiary, maski, parametry, kolejność, wyniki kontroli. Przy każdej technice jedno odesłanie `p.~\ref{...}`, bez powtarzania teorii.
- **Podział z rozdz. 4:** komora próżniowa, zasilacze laboratoryjne, obwód E–B–T, spektrometr i biegunowość napięć opisuje rozdz. 4. Rozdz. 3 kończy się na gotowym prototypie z kontaktami elektrod.
- **Podział z rozdz. 5:** żadnych wyników emisji ani widm. Wyjątek: kontrola jakości wykonania (wymiary po trawieniu, wygląd połączeń), bo to wynik procesu, a nie badań.
- **Terminologia wg `slownik.md`:** emiter (E), bramka (B, przy pierwszym użyciu „bramka (elektroda ekstrakcyjna)”), target (T), magnes ogniskujący (magnes trwały NdFeB), nakraplanie CNT, płyta grzejna, bonding anodowy, struktura krzemowo-szklana, niehermetyczna. Napięcia $U_\mathrm{B}$, $U_\mathrm{T}$; odległość emiter–bramka $d$.
- Czasy: przeszły bezosobowy („zaprojektowano”, „wytrawiono”); stan obecny i rozwiązanie docelowe rozdzielone wprost.

## 1. Struktura i budżet

| Podrozdział | Strony | Słowa | Rys./tab. |
|---|---:|---:|---|
| (wprowadzenie, bez nagłówka) | 0,1 | 40 | – |
| 3.1 Założenia projektowe i koncepcja struktury | 1,0 | 230 | rys. 3.1 |
| 3.2 Dobór materiałów i grubości elementów (szkło 1 mm) | 0,7 | 180 | tab. 3.1 |
| 3.3 Projekt emitera, bramki i targetu | 0,8 | 260 | – |
| 3.4 Projekt masek fotolitograficznych | 0,9 | 200 | rys. 3.2 |
| 3.5 Wytwarzanie elementów krzemowych: fotolitografia i trawienie | 1,3 | 280 | rys. 3.3, tab. 3.2 |
| 3.6 Wykonanie elementów szklanych | 0,3 | 90 | – |
| 3.7 Nanoszenie emitera CNT | 0,4 | 110 | – |
| 3.8 Bonding anodowy i montaż prototypu | 1,0 | 290 | rys. 3.4 (para zdjęć) |
| **Razem** | **6,5** | **≈ 1500** | **4 rys., 2 tab.** |

8 podsekcji, bez podpodsekcji (dla porównania: rozdz. 2 ma ich za dużo, zob. raport spójności).

## 2. Plan akapitów

### Wprowadzenie do rozdziału (bez nagłówka, 0,1 str.)
- **W1.** Dwa zdania: rozdział opisuje projekt struktury krzemowo-szklanej źródła elektronów i kolejne etapy jej wytworzenia aż do zmontowanego prototypu; zasady procesów omówiono w p.~\ref{sec:technologia}, stanowisko w rozdz.~\ref{ch:stanowisko}.

### 3.1 Założenia projektowe i koncepcja struktury (1,0 str., rys. 3.1)
- **1.1 Wymagania.** Zwięzła lista wymagań wynikających z celu pracy: wytworzenie wiązki elektronów przez emisję polową z CNT przy $U_\mathrm{B}$ rzędu 1 kV, przyspieszenie do energii wzbudzającej linie lekkich pierwiastków (w prototypie $U_\mathrm{T}$ do 4 kV, docelowo 10–18 kV), izolacja elektryczna elektrod przy tych napięciach, wykonanie wyłącznie procesami MEMS dostępnymi w laboratorium, zgodność materiałów z bondingiem anodowym, możliwość późniejszej hermetyzacji.
- **1.2 Koncepcja.** Stos warstw: krzemowy emiter – szkło dystansowe – krzemowa bramka z aperturą – szkło dystansowe – target (nośnik próbki / luminoforu); magnes ogniskujący NdFeB umieszczony na emiterze. Krótko, czym konstrukcja różni się od źródła RTG z rozprawy~\cite{urbanski2026phd}: wiązka pada bezpośrednio na próbkę na targecie (EDS, a nie target transmisyjny), brak zintegrowanej mikropompy i elektrody ogniskującej, ogniskowanie wyłącznie magnetyczne. \TODO{T1, T2}
- **1.3 Opis rys. 3.1.** Przekrój struktury (własny rysunek TikZ, nie kopia z rozprawy) z oznaczeniami E, B, T, odległością $d$, grubościami szkła, położeniem magnesu i kierunkiem wiązki. Akapit tylko prowadzi czytelnika po rysunku i wskazuje, który element pełni którą funkcję.
- **1.4 Doprowadzenie napięć (1–2 zdania).** Każda elektroda krzemowa ma osobny kontakt; sposób zasilania i biegunowość opisano w rozdz.~\ref{ch:stanowisko}. \TODO{T3}

### 3.2 Dobór materiałów i grubości elementów (0,7 str., tab. 3.1)
- **2.1 Krzem.** Płytki Si (100), bo kształt emitera i otworów wynika z trawienia anizotropowego (p.~\ref{subsec:koh}); krzem jako materiał konstrukcyjny i przewodzący elektrod. Konkretne dane płytek: grubość, typ, rezystywność, polerowanie. \TODO{T4}
- **2.2 Szkło 1 mm (punkt obowiązkowy).** Szkło borokrzemowe o grubości 1 mm jako dystansownik i izolator. Uzasadnienie grubości: (a) wytrzymałość na przebicie i upływ powierzchniowy przy $U_\mathrm{T}$ do kilku kV, docelowo kilkunastu kV (szacunek natężenia pola $U_\mathrm{T}/\SI{1}{\milli\metre}$), (b) ustalenie odległości bramka–target i emiter–bramka, (c) sztywność mechaniczna i łatwość obróbki, (d) dostępność standardowej grubości. Konsekwencja: długa droga wiązki sprzyja jej rozbieganiu się, co uzasadnia zastosowanie magnesu ogniskującego (odesłanie do p.~\ref{...} w rozdz. 2.3). \TODO{T5}
- **2.3 Tab. 3.1.** Zestawienie elementów struktury: element | materiał | grubość | wymiary zewnętrzne | otwór/apertura | funkcja. Tekst nie powtarza wartości z tabeli.

### 3.3 Projekt emitera, bramki i targetu (0,8 str.)
- **3.1 Emiter.** Geometria emitera (ostrze / obszar pod CNT), obliczenia wymiarów z etapu 2 sprawozdania: związek szerokości okna w masce z wysokością i kształtem ostrza przy kącie \ang{54.74} (bez wyprowadzania, odesłanie do p.~\ref{subsec:koh}). \TODO{T6}
- **3.2 Bramka.** Średnica/bok apertury i odległość $d$ od emitera; szacunek średniego natężenia pola $U_\mathrm{B}/d$ i porównanie z polem potrzebnym do emisji z CNT po uwzględnieniu współczynnika $\beta$ (jedno równanie albo odesłanie do równania F–N w rozdz. 2.2). Kompromis: mała apertura zwiększa pole, ale przechwytuje część wiązki (prąd bramki $I_\mathrm{B}$). \TODO{T7}
- **3.3 Target.** Element, na który pada wiązka: materiał, sposób umieszczenia próbki i warstwy luminoforu (obserwacja kształtu wiązki, rozdz. 5.1), odległość od bramki. \TODO{T8}
- **3.4 Magnes ogniskujący.** Magnes trwały NdFeB położony na emiterze; parametrów (gatunek, wymiary, indukcja) nie określono, dlatego opis jest jakościowy; zasada działania w rozdz. 2.3. Jedno zdanie, że elektrony padające na magnes mogą wzbudzać linie Fe, Nd, Ni (zapowiedź dla interpretacji widm w rozdz. 5.2).

### 3.4 Projekt masek fotolitograficznych (0,9 str., rys. 3.2) — punkt obowiązkowy
- **4.1 Zestaw masek.** Ile masek wykonano i do którego elementu/etapu służy każda (np. maska emitera, maska otworów bramki, ewentualnie maska dla strony spodniej), rodzaj maski (chromowa / foliowa), narzędzie projektowe. \TODO{T9}
- **4.2 Reguły projektowe.** Jak wymiary okien przeliczono z docelowych wymiarów po trawieniu: poszerzenie o $2h/\tan\ang{54.74}$ dla wnęk, podtrawianie wypukłych narożników przy ostrzach i ewentualne struktury kompensacyjne, tolerancja justowania. Jedno zdanie, że zasada wynika z p.~\ref{subsec:koh}.
- **4.3 Rozkład na płytce.** Liczba struktur na płytce, znaczniki justowania, linie cięcia, struktury testowe do kontroli głębokości trawienia. \TODO{T10}
- **4.4 Rys. 3.2.** Widok masek (eksport z programu projektowego) lub ich fragmentów z wymiarami kluczowych okien.

### 3.5 Wytwarzanie elementów krzemowych: fotolitografia i trawienie (1,3 str., rys. 3.3, tab. 3.2) — punkty obowiązkowe
- **5.1 Sekwencja procesu.** Kolejność kroków jako rys. 3.3 (przekroje płytki po każdym etapie, TikZ): mycie płytek → wytworzenie warstwy maskującej (SiO$_2$ / Si$_3$N$_4$) → fotolitografia → otwarcie okien → trawienie KOH → usunięcie maski → cięcie. Akapit opisuje tylko decyzje, nie kroki znane z rozdz. 2.1. \TODO{T11}
- **5.2 Fotolitografia.** Zastosowany fotorezyst, wirowanie, wygrzewanie, naświetlanie (urządzenie, czas), wywoływanie, trawienie warstwy maskującej; parametry w tab. 3.2, w tekście tylko to, co wymagało dobrania (np. czas naświetlania, justowanie dwustronne). \TODO{T12}
- **5.3 Trawienie w KOH.** Stężenie, temperatura, czas, uzyskana szybkość i głębokość; sposób kontroli końca trawienia; zjawiska, które pojawiły się w praktyce (podtrawienie narożników, chropowatość dna, pęcherze wodoru, ewentualnie trawienie z jednej strony w uchwycie). \TODO{T13}
- **5.4 Kontrola jakości.** Pomiar wymiarów po trawieniu (mikroskop optyczny / profilometr) i porównanie z projektem z p. 3.4; ewentualne zdjęcie mikroskopowe emitera jako część rys. 3.4. Odchyłki i ich wpływ na odległość $d$. \TODO{T14}
- **5.5 Tab. 3.2.** Parametry wszystkich procesów w jednym miejscu: fotolitografia, trawienie warstwy maskującej, KOH, nakraplanie CNT, bonding anodowy.

### 3.6 Wykonanie elementów szklanych (0,3 str.)
- **6.1 Szkło 1 mm.** Sposób wykonania otworów i kształtu dystansowników w szkle 1 mm (np. wiercenie, piaskowanie, cięcie laserowe, trawienie w HF), wymiary otworów względem apertury bramki, przygotowanie powierzchni do bondingu (czystość, płaskość, mycie). \TODO{T15}

### 3.7 Nanoszenie emitera CNT (0,4 str.)
- **7.1 Nakraplanie.** Skład zawiesiny (kompozyt CNT-PVP jak w~\cite{urbanski2026phd}: rodzaj CNT, rozpuszczalnik, stężenie), objętość i liczba kropli, emiter na płycie grzejnej \SI{240}{\celsius}, czas suszenia. Tylko parametry; zasada w p. 2.1. \TODO{T16}
- **7.2 Kolejność względem bondingu i ocena warstwy.** Czy CNT naniesiono przed, czy po bondingu (bonding wymaga ok. 300–450 °C, więc kolejność ma znaczenie dla trwałości warstwy), jak wyglądała warstwa (jednorodność, zasięg kropli poza ostrze), ograniczenia metody w porównaniu z metodą termo-mechaniczną. \TODO{T17}

### 3.8 Bonding anodowy i montaż prototypu (1,0 str., rys. 3.4) — punkt obowiązkowy
- **8.1 Kolejność łączenia.** Które pary krzem–szkło łączono i w jakiej kolejności, jak justowano elementy względem osi wiązki (apertura bramki nad emiterem). \TODO{T18}
- **8.2 Parametry i przebieg bondingu.** Bonding wykonano w atmosferze: temperatura, napięcie, czas, przebieg prądu bondingu (jeśli rejestrowany); ocena połączenia (wizualnie przez szkło, wytrzymałość). Parametry w tab. 3.2. \TODO{T19}
- **8.3 Montaż.** Umieszczenie magnesu NdFeB na emiterze, wykonanie kontaktów elektrycznych do E, B, T (np. klej przewodzący / pasta srebrowa / druty), naniesienie luminoforu i próbki na target, mocowanie w komorze (szczegóły komory w rozdz. 4). Wymiary i masa gotowego prototypu (dane własne, zob. A18). \TODO{T20}
- **8.4 Stan obecny i rozwiązanie docelowe.** Struktura jest niehermetyczna, ponieważ wszystkie połączenia wykonano w atmosferze; badania prowadzono w komorze próżniowej przy ok. \SI{1e-5}{\hecto\pascal} (rozdz.~\ref{ch:stanowisko}). Docelowo ostatnie połączenie wykonuje się bondingiem anodowym w próżni, a próżnię podtrzymuje mikropompa (trudności procesu opisano w p.~\ref{subsec:bonding}, tu bez powtórzeń). 3–4 zdania.
- **8.5 Rys. 3.4 (para zdjęć, `subcaption`).** (a) element krzemowy po trawieniu lub emiter z CNT pod mikroskopem, (b) zmontowany prototyp z magnesem i kontaktami.

## 3. Brakujące dane (\TODO) — do uzupełnienia przez kris

Najważniejsze (bez nich nie da się napisać rozdziału): **T1, T4, T6, T7, T9, T13, T18, T19**.

| nr | podrozdział | potrzebna informacja |
|---|---|---|
| T1 | 3.1 | Pełny układ warstw od dołu do góry: ile elementów krzemowych i szklanych, czy jest osobna elektroda ogniskująca (elektrostatyczna) czy tylko magnes. Szkic odręczny wystarczy do narysowania rys. 3.1. |
| T2 | 3.1 | Czy elementy projektowano od zera, czy na bazie projektu z rozprawy Urbańskiego (które elementy przejęto, co zmieniono). |
| T3 | 3.1 | Jak wyprowadzono kontakty do E, B, T (pola kontaktowe na krzemie, klej przewodzący, druty). |
| T4 | 3.2 | Płytki Si: grubość, orientacja (zakładamy (100)), typ i rezystywność, jedno- czy dwustronnie polerowane. |
| T5 | 3.2 | Szkło 1 mm: typ (Borofloat 33?), dlaczego wybrano 1 mm (dostępność, izolacja, odległość), ile warstw szkła i gdzie. |
| T6 | 3.3 | Obliczenia wymiarów emitera ze sprawozdania (etap 2): kształt emitera (ostrze/płaszczyzna), wymiary okna w masce, wysokość ostrza. |
| T7 | 3.3 | Odległość emiter–bramka $d$ i wymiar apertury bramki. |
| T8 | 3.3 | Target: materiał, wymiary, jaki luminofor i jak naniesiony, gdzie leżała próbka do pomiaru EDS. |
| T9 | 3.4 | Ile masek, do czego każda, rodzaj (chrom/folia), w czym projektowano; najlepiej pliki/zrzuty masek do rys. 3.2. |
| T10 | 3.4 | Liczba struktur na płytce, znaczniki justowania, struktury testowe, sposób cięcia. |
| T11 | 3.5 | Warstwa maskująca do KOH: SiO$_2$ (termiczny?) czy Si$_3$N$_4$, grubość. |
| T12 | 3.5 | Fotolitografia: fotorezyst, obroty wirowania, wygrzewanie, czas naświetlania, wywoływacz, trawienie maski (BHF?). |
| T13 | 3.5 | KOH: stężenie, temperatura, czas, głębokość, uzyskana szybkość, problemy w trakcie. |
| T14 | 3.5 | Czy mierzono wymiary po trawieniu (mikroskop, profilometr) i czy są zdjęcia. |
| T15 | 3.6 | Jak wykonano otwory w szkle 1 mm. |
| T16 | 3.7 | Zawiesina CNT: rodzaj nanorurek, rozpuszczalnik, czy z PVP, stężenie, objętość/liczba kropli. |
| T17 | 3.7 | CNT naniesiono przed bondingiem czy po nim. |
| T18 | 3.8 | Kolejność łączenia elementów i sposób justowania. |
| T19 | 3.8 | Parametry bondingu w atmosferze: temperatura, napięcie, czas; czy wszystkie połączenia się udały. |
| T20 | 3.8 | Wymiary i masa gotowego prototypu, sposób mocowania magnesu, zdjęcia prototypu (do rys. 3.4). |

## 4. Sprawy do uzgodnienia z innymi rozdziałami

1. **Rozdz. 2.1 (wątek teorii):** akapit „W prototypie opisanym w tej pracy zastosowano prostszą metodę…” w „Nanoszenie emitera CNT” oraz akapit „Stan obecny” przy bondingu opisują prototyp, nie teorię. Proponuję przenieść je do 3.7 i 3.8 (rozdz. 2 zyska ok. 0,3 str., co pomaga w przekroczeniu budżetu).
2. **„Elektronika zasilania i sterowania” (dziś w rozdz. 2, budżet przenosi ją do rozdz. 3):** w prototypie użyto zasilaczy laboratoryjnych, a zasilacz nie wchodzi w zakres pracy (opis tematu, B7). Proponuję nie dawać jej do rozdz. 3: zasilacze opisać w rozdz. 4, a docelowy układ HV z pętlą sprzężenia zwrotnego w 1–2 zdaniach w rozdz. 6 („dalsze prace”). Rozdz. 3 nie potrzebuje wtedy załącznika A.
3. **Golden Standard p. 3.6 „Tor detekcji”** — w rozdz. 4, nie w 3.
4. Rysunki 3.1 i 3.3 rysowane od nowa w TikZ (nie kopiowane z rozprawy), z podpisem „opracowanie własne”; jeśli geometria bazuje na projekcie Urbańskiego, dopisać „na podstawie~\cite{urbanski2026phd}”.
