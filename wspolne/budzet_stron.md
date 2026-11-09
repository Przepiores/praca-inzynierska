# Budżet stron pracy inżynierskiej

Stan na 2026-11-09. Limit: **50 stron A4 łącznie** (strona tytułowa, streszczenia, spis treści, wykaz skrótów, rozdziały, literatura i załączniki). Każdy wątek pisze swój rozdział w ramach poniższego budżetu; przy przekroczeniu skraca tekst, a nie przesuwa nadmiar na inne rozdziały.

## 1. Założenia przeliczeniowe

- Format wg Golden Standard: A4, 12 pt, marginesy 25 mm, tekst wyjustowany, szablon `dyplompwr`.
- **1 strona czystego tekstu ≈ 400 słów** (interlinia ok. 1,15). Przy interlinii 1,5 to tylko ok. 330 słów, więc wartości trzeba skalibrować po pierwszej kompilacji całości (zadanie wątku kontroli spójności).
- Rysunek o szerokości strony z podpisem ≈ 0,4 str., para rysunków (`subcaption`) ≈ 0,5 str., tabela ≈ 0,25 str., równanie wyróżnione ≈ 0,08 str., nagłówek podrozdziału ≈ 0,06 str.
- Kalibracja: fragment `emisja-magnes-pomiary/emisja_tresc.tex` (ok. 1400 słów, 6 rysunków, 2 tabele) daje 6 stron w `emisja_porownanie.pdf`, co zgadza się z powyższymi przelicznikami.
- **Puste strony:** przy druku dwustronnym z opcją `openright` każdy rozdział zaczyna się na stronie nieparzystej, co może dodać do 5 pustych stron. Budżet zakłada `openany` (rozdziały od dowolnej strony); jeśli promotor lub dziekanat wymaga `openright`, trzeba zdjąć te strony z rezerwy i z rozdziału 2.

## 2. Tabela budżetu

| # | Część | Cel | Strony | Rys./tab. | Słowa (tekst) | Powiązane pliki / wątki | Stan obecny | Ocena |
|---|---|---|---:|---|---:|---|---|---|
| – | Strona tytułowa + odwrocie | wymóg wydziałowy, tytuł zgodny z APD | 2 | – | – | `body.tex` w repo LaTeX | gotowa w szablonie | ✅ |
| – | Streszczenie PL + Abstract EN | tekst tożsamy z USOS-APD, 200–300 słów każde | 2 | – | 2 × 250 | `frontmatter/streszczenie.tex`, `abstract_en.tex` | szkic roboczy | ✅ |
| – | Podziękowania | opcjonalne | 0 | – | – | `frontmatter/podziekowania.tex` | pusta strona w szablonie | ⚠️ usunąć albo zmieścić w rezerwie |
| – | Spis treści | automatyczny | 2 | – | – | – | – | ✅ |
| – | Wykaz skrótów i oznaczeń | jedna tabela skrót → rozwinięcie | 1 | 1 tab. | – | `wspolne/` (słownik), `frontmatter/wykaz_skrotow.tex` | szkic | ✅ |
| **1** | **Wstęp** | motywacja, krótki stan techniki, cel i zakres, zgodność z kierunkiem | **2,5** | 0 | 1000 | `wstep-zagajenie/wstep_opcja_C.tex` (zatwierdzona), `literatura-wstep/przeglad_literatury_wstep.md`, `chapters/01_wstep.tex` | ok. 370 słów (opcja C) + cel/aspekty z `Praca inzynierska.md` ≈ 1,8 str. | ✅ zostaje ok. 0,7 str. na stan techniki |
| **2** | **Podstawy teoretyczne i technologiczne** | tylko teoria potrzebna do zrozumienia prototypu i wyników | **10** | 3 rys. | 3200 + ok. 12 równań | `podstawy-teoretyczne/podstawy_teoretyczne.tex`, `literatura-wstep/zagadnienia_do_opracowania.md` | ok. 3750 słów, 17 równań, 48 podsekcji, 0 rysunków ≈ 12,5 str.; z planowanymi rysunkami ≈ 14 str. | ❌ **przekroczenie ok. 4 str.** |
| 2.1 | Technologia wykonania struktur MEMS | materiały, utlenianie, fotolitografia, KOH, CNT, bonding (docelowo w próżni) | 2 | 1 | | | ok. 760 słów | ⚠️ +0,3 |
| 2.2 | Emisja polowa i emitery CNT | praca wyjścia, F-N, β, CNT, degradacja | 2 | 1 | | | ok. 580 słów, 4 równania | ✅ |
| 2.3 | Przyspieszanie i ogniskowanie wiązki | energia elektronu, siła Lorentza, soczewka magnetyczna | 1,5 | 0 | | | ok. 490 słów, 5 równań | ⚠️ +0,2 |
| 2.4 | Powstawanie promieniowania X | oddziaływanie e⁻ z materią, hamowanie, jonizacja, relaksacja, Moseley, EDS a XRF | 2,5 | 1 | | | ok. 750 słów, 5 równań | ⚠️ +0,3 |
| 2.5 | Spektrometria EDS | detektor, tor akwizycji, parametry, analiza widma | 1,5 | 0 | | | ok. 630 słów (bez części przeniesionych) | ⚠️ +0,4 |
| 2.6 | Próżnia i warunki kosmiczne | próżnia, warunki misji | 0,5 | 0 | | | ok. 180 słów | ⚠️ +0,2 |
| **3** | **Projekt i wykonanie prototypu** | koncepcja, emiter CNT z elektrodą ekstrakcyjną, elektroda przyspieszająca, magnes NdFeB, zasilanie HV, montaż | **6,5** | 4 rys., 1 tab. | 1900 | `chapters/03_*.tex`, `knowledge/.../Notatka - Jak dziala skonstruowany uklad RTG MEMS.md` | brak tekstu (nagłówki w szkielecie) | 🔲 do napisania |
| **4** | **Stanowisko pomiarowe i metodyka** | komora próżniowa, obwód E–B–T, spektrometr, metoda analizy zdjęć, niepewności | **3,5** | 3 rys. | 900 | `uklad-pomiarowy/` (schemat + `uklad_pomiarowy_body.tex`), `emisja-magnes-pomiary/analiza_obrazu.py` | schemat + ok. 280 słów ≈ 1,2 str. | ✅ |
| **5** | **Badania eksperymentalne** | wyniki i ich interpretacja (rdzeń pracy) | **13** | 10 rys., 3 tab. | 3000 | | | |
| 5.1 | Charakterystyki I-V i wpływ magnesu ogniskującego | I-V obu sesji, wpływ odgazowania, jasność a prąd, skupienie plamki | 6 | 6 rys., 2 tab. | | `emisja-magnes-pomiary/emisja_tresc.tex` | ok. 1500 słów, 6 rys., 2 tab. ≈ 6 str. | ✅ po przeniesieniu „Metody analizy zdjęć” do rozdz. 4 i „Wniosków” do rozdz. 6 zostaje ok. 5,4 str. |
| 5.2 | Widma EDS próbek | rejestracja i identyfikacja linii, rola magnesu | 4 | 3 rys., 1 tab. | | `widma-eds/` (widmo 4 kV, Excel, wykresy) | tekst `widma-eds/widma_tresc.tex` w rozdz. 5 (2026-11-09): ok. 2,5 str., 2 rys., 2 tab.; potrzebny eksport z ProSpect | ✅ zostaje ok. 1,5 str. na kolejne widma |
| 5.3 | Stabilność i powtarzalność emisji | zmiany prądu w czasie, różnice między sesjami | 1 | 1 rys. | | – | częściowo w 5.1 („Wpływ warunków źródła”) | 🔲 |
| 5.4 | Ocena pod kątem zastosowań kosmicznych | masa, moc, próżnia, porównanie z APXS/PIXL (odwołanie do 2.6, bez powtórzeń) | 1,5 | 1 tab. | | | „Porównanie z przyrządami” jest dziś w rozdz. 2 | 🔲 |
| 5.0 | Wprowadzenie do rozdziału | 2–3 zdania | 0,5 | | | | | |
| **6** | **Podsumowanie i wnioski** | realizacja celów, wkład własny, dalsze prace | **1,5** | 0 | 600 | `chapters/06_*.tex` | „Wnioski” z `emisja_tresc.tex` (160 słów) do przeniesienia | 🔲 |
| – | Literatura | IEEE, tylko pozycje cytowane | 3 | – | – | `wspolne/bibliografia.bib` | 39 pozycji ≈ 3 str. | ✅ przy ≤ 42 pozycjach |
| – | Załącznik A: schematy zasilania HV | jedyny załącznik | 1 | 1–2 rys. | – | `appendices/a_*.tex` | pusty | 🔲 |
| – | Załączniki B (zdjęcia), C (surowe dane) | – | 0 | – | – | `appendices/b,c` | puste | ⚠️ usunąć; 1 zdjęcie stanowiska do rozdz. 4, dane w repozytorium/na nośniku |
| – | **Rezerwa** | podziękowania, pływające rysunki, ewentualne `openright` | 2 | | | | | |
| | **RAZEM** | | **50** | | ≈ 11 100 | | | |

Proporcja: prace własne (rozdz. 3–5) = 23 z 37 stron rozdziałów 1–6, czyli ok. 62 %, zgodnie z zaleceniem Golden Standard (60–70 %). Podstawy teoretyczne zajmują 27 % i nie mogą rosnąć kosztem wyników.

## 3. Przekroczenia i zalecenia

### Rozdział 2 (przekroczenie ok. 4 str., najważniejsze)

1. **Przenieść poza rozdział** (ok. 1 str.), bo dublują inne rozdziały:
   - „Stanowisko pomiarowe” i „Charakterystyka prądowo-napięciowa emitera” → rozdz. 4 i 5.1;
   - „Porównanie z przyrządami stosowanymi w misjach” → wstęp (stan techniki) i 5.4;
   - „Elektronika zasilania i sterowania” → rozdz. 3 (układ zasilania HV);
   - „Bezpieczeństwo pracy” → usunąć albo 1–2 zdania w rozdz. 4.
2. **Scalić podsekcje:** 48 podsekcji po 50–100 słów → ok. 15–18. Same nagłówki zajmują dziś ok. 2,5 str.
3. **Skrócić:** „Bonding anodowy” (260 → ok. 120 słów, jako rozwiązanie docelowe), „EDS a WDS” (100 → 2 zdania), „Target transmisyjny i odbiciowy” (80 → 1 zdanie lub usunąć), „Analiza ilościowa” (do 1 zdania: w pracy tylko analiza jakościowa), „Inne metody trawienia” (do 1 zdania).
4. Rysunki (3) dodawać tylko tam, gdzie zastępują tekst (np. schemat procesu MEMS zamiast opisu kroków).

### Rozdział 5.1

Fragment mieści się po przeniesieniu „Metody analizy zdjęć” (ok. 100 słów + równanie) do rozdz. 4 i „Wniosków” (160 słów) do rozdz. 6.

### Ryzyka

- **5.2 Widma EDS (4 str.)**: jest jedno widmo (4 kV, `widma-eds/`, 2026-11-09), odczytane ze zdjęć ekranu. Przed oddaniem rozdziału trzeba podmienić je na widmo wyeksportowane z ProSpect.
- Przelicznik 400 słów/str. trzeba potwierdzić pierwszą kompilacją całości w `dyplompwr`.

## 4. Zasady dla wątków

- Przed oddaniem rozdziału policz słowa, rysunki i tabele i porównaj z kolumną „Słowa” i „Rys./tab.”. Odchylenie do +10 % jest dopuszczalne, większe oznacza skracanie.
- Nie powtarzaj treści z innych rozdziałów: odwołuj się przez `\ref{}` (np. „zob. podrozdz.~\ref{...}”).
- Zmianę budżetu (przesunięcie stron między rozdziałami) zapisuj w tym pliku z datą, tak aby suma nadal wynosiła 50.

## 5. Historia zmian

- 2026-11-09: pierwsza wersja budżetu.
- 2026-11-09: 5.2 ma dane (widmo 4 kV w `widma-eds/`).
- 2026-11-09: 5.2 napisane (`widma-eds/widma_tresc.tex`, podpięte w `rozdzialy/05_badania.tex`); całość 37 str.
