# Wspólne zasoby pracy — bibliografia

Ten folder zawiera elementy wspólne dla wszystkich wątków pracy. Ten plik opisuje **bibliografię**; inne wspólne pliki (budżet stron, słownik, szablon, rejestr TODO) dopisują własne sekcje poniżej.

## 1. Jeden plik: `wspolne/bibliografia.bib`

- To **jedyne źródło prawdy** dla wszystkich rozdziałów. Rozdziały nie mają własnych `.bib`.
- Stan 2026-11-09: **50 pozycji** (47 z DOI sprawdzonym w Crossref; bez DOI: 2 rozprawy doktorskie i podręcznik van Griekena).
- Źródła scalenia: `literatura-wstep/literatura_wstep.bib` (39 poz.) oraz `W:\VAULT\Inzynierka\latex\bibliography\bibliografia.bib` z repozytorium LaTeX (20 poz., 9 z nich to duplikaty). `literatura_wstep.bib` zostaje bez zmian, ale **nie należy go już edytować**.
- Repozytorium LaTeX używa już wspólnego pliku: `latex\bibliography\bibliografia.bib` = kopia `wspolne/bibliografia.bib` (identyczna suma MD5). Poprzednia wersja: `latex\bibliography\bibliografia_backup_2026-11-09.bib`. Przy każdej zmianie wspólnego pliku kopię w repo trzeba nadpisać.

## 2. Zasady dopisywania źródeł

1. **Przed dodaniem** wyszukaj DOI i nazwisko w `bibliografia.bib` (`grep -i "<doi>" wspolne/bibliografia.bib`). Jeśli pozycja jest, użyj istniejącego klucza.
2. **Klucz:** `nazwisko pierwszego autora + rok + jedno słowo z tytułu`, małe litery, bez polskich znaków i myślników, np. `grzebyk2016lateral`, `urbanski2026xrf`. Przy dwóch pracach tego samego autora z tego samego roku słowo musi je rozróżniać.
3. **Metadane z Crossref** (`https://api.crossref.org/works/<DOI>`; z kontenera przez Firecrawl scrape, bo bezpośredni curl blokuje proxy). Nie przepisywać z pamięci.
4. **Pola wymagane:**
   - `@article`: author, title, journal, year, volume, (number), pages, doi
   - `@inproceedings`: author, title, booktitle, year, pages, doi
   - `@book`: author/editor, title, year, (edition), publisher, doi
   - `@incollection`: author, title, booktitle, year, pages, publisher, doi
   - `@phdthesis` / normy / strony WWW: author, title, school/organization, year, url + urldate dla WWW
5. **Formatowanie:** tytuł w podwójnych klamrach `{{...}}` (chroni wielkość liter), autorzy w formie `Nazwisko, Imię and ...`, polskie znaki wprost (UTF-8), zakresy stron z `--`, DOI bez prefiksu `https://doi.org/`, małe litery. Pozycje polskojęzyczne: `langid = {polish}`.
6. **Wstawiaj wpis alfabetycznie wg klucza.** Plik czyta wiele wątków; przed zapisem wczytaj go ponownie (ostatni zapis wygrywa) i dopisuj tylko swoje wpisy, nie nadpisuj całości starą kopią.
7. **Bez duplikatów:** jeden DOI = jeden klucz. Nie zmieniaj istniejących kluczy; jeśli to konieczne, dopisz zmianę do tabeli w sekcji 4.
8. Wpisy-zaślepki niedozwolone w tym pliku. Brakujące źródło oznacza się w tekście `\cite{TODO-opis}` i dopisuje do rejestru TODO.

## 3. Styl cytowań (propozycja)

Golden Standard (pkt 11) dopuszcza **PN-ISO 690 lub IEEE**, numerowany wykaz w kolejności cytowania albo alfabetyczny. Repozytorium LaTeX ma już ustawione biblatex + biber, styl IEEE. Propozycja: zostać przy tym.

```latex
\usepackage[backend=biber, style=ieee, sorting=none, maxnames=3, minnames=1,
            doi=true, url=false, isbn=false]{biblatex}
\addbibresource{bibliografia.bib}   % kopia/łącze do wspolne/bibliografia.bib
...
\printbibliography[title={Literatura}]
```

- Numeracja w kolejności pierwszego cytowania (`sorting=none`), w tekście `[1]`, `[2–4]`.
- `\cite{a,b,c}` dla kilku źródeł naraz, cytowanie przed kropką: „…emisji polowej [3].”
- Alternatywa, gdyby promotor zażądał PN-ISO 690: `style=iso-numeric` (pakiet `biblatex-iso690`); `.bib` nie wymaga zmian.
- Nie mieszać `natbib`/`bibtex` z biblatex.

## 4. Lista zmienionych kluczy

Klucze z `literatura_wstep.bib` przeniesiono 1:1, więc `\cite` w `podstawy-teoretyczne/podstawy_teoretyczne.tex` działają bez zmian.

Klucze ze starego `.bib` w repozytorium LaTeX, które przestały istnieć (w repo cytowany był tylko `\cite{TODO}`, więc nic się nie psuje, ale tych kluczy nie używać):

| Stary klucz (repo) | Nowy klucz |
|---|---|
| `urbanski2026mems` | `urbanski2026phd` |
| `urbanski2024detection` | `urbanski2023detection` (artykuł ukazał się w 2023 r., t. 31) |
| `urbanski2024memssource` | `urbanski2024memscompatible` |
| `parmee2015cnt` | `parmee2015cntxray` |
| `yue2002cnt` | `yue2002cntxray` |
| `castaing1951` | `castaing1951sondes` (dodane słowo wg konwencji) |

Nowe pozycje z repozytorium (klucze bez zmian): `newbury2006sdd`, `newbury2013quantitative`, `newbury2015sddeds`, `vangrieken2002handbook`, `gatti1984driftchamber`, `lechner1996sdd`, `rose2009electronguns`, `senturia2001microsystem`, `madou2018microfabrication`, `grzebyk2013micropump` (+ DOI i strony z Crossref). Lista „do rozważenia” ze starego pliku jest przeniesiona jako komentarz na końcu `bibliografia.bib`.

Poprawki treści (bez zmiany kluczy):

| Klucz | Zmiana |
|---|---|
| `urbanski2023detection` | dodano volume 31, number 3, pages e146554 (Crossref) |
| `szyszka2025massspec` | dodano number 7, poprawiono nazwę czasopisma na „Przegląd Komunikacyjny” (czasopismo nie ma tomu) |
| `urbanski2026phd` | dodano `langid = {polish}`, pełną nazwę wydziału i promotora |
| `jeong2013focused`, `heo2012miniature`, `urbanski2023target` | w starym pliku repo były błędne imiona autorów (Jun-Wook, Jeong Min, Michał Białas); zostały wersje zgodne z Crossref (Jin-Woo, Jun Mok, Marcin) |

### Klucze zastępcze `TODO-…` we wstępie (`wstep-zagajenie/*.tex`) → klucze docelowe

| Klucz tymczasowy | Zamienić na |
|---|---|
| `TODO-insitu` | `gellert2015apxs,blake2012chemin` |
| `TODO-apxs` | `rieder2003apxs,campbell2012apxs` |
| `TODO-pixl` | `allwood2020pixl` |
| `TODO-urbanski` | `urbanski2024memscompatible,urbanski2023target,urbanski2026xrf` |
| `TODO-mems` | brak źródła (MEMS w elektronice użytkowej, np. przegląd rynku/podręcznik MEMS, do znalezienia); prace PWr `grzebyk2015selfpackaged,grzebyk2016lateral,grzebyk2017pumps` pasują dopiero do zdania o MEMS na PWr |
| `TODO-apollo` | brak źródła w bibliografii (do znalezienia) |
| `TODO-budzet` | brak źródła (masa/moc przyrządów misji, do znalezienia) |
| `TODO-sklad` | brak źródła (skład powierzchni ciał niebieskich, do znalezienia) |
| `TODO-...` | szablonowy znacznik, usunąć |

## 5. Uwagi

- Golden Standard zaleca min. 20–30 pozycji; bibliografia ma 50, czyli wymóg jest spełniony (w wykazie znajdą się tylko pozycje rzeczywiście cytowane).
- Docelowo można zarządzać plikiem przez Zotero + Better BibTeX (eksport do tego pliku), z tymi samymi kluczami.

---

# Budżet stron

Plik `wspolne/budzet_stron.md`: tabela stron, słów i rysunków dla każdego rozdziału (suma 50 stron A4 z częścią wstępną, literaturą i załącznikami), wykaz przekroczeń i zasady dla wątków. Przed oddaniem rozdziału porównaj jego objętość z budżetem; zmiany budżetu zapisuj w tym pliku z datą.

# Słownik i oznaczenia

Plik `wspolne/slownik.md`: nazewnictwo elementów układu (emiter E, bramka B, target T), wykaz skrótów, symbole i jednostki ($U_\mathrm{B}$ — napięcie ekstrakcyjne, $U_\mathrm{T}$ — napięcie przyspieszające, $I_\mathrm{e}$, $I_\mathrm{B}$, $I_\mathrm{T}$), terminy preferowane i zakazane („relaksacja”, nie „rekombinacja” dla atomu), zasady stylu bezosobowego oraz lista niespójności N1–N20 w istniejących tekstach. Nowy termin lub symbol dopisuje się najpierw do słownika.

---

# Rejestr TODO i niezgodności

Plik `wspolne/rejestr_todo.md`: (A) miejsca do uzupełnienia i (B) sprzeczności liczb, nazw i faktów między rozdziałami, z kolumnami nr, rozdział/plik, opis, kto, status. Wątek, który znajdzie brak lub sprzeczność, dopisuje wiersz na końcu tabeli (bez przenumerowania); po rozstrzygnięciu zmienia status na `zamknięte` z krótkim opisem. Przed zapisem wczytaj plik ponownie.

---

# Szablon LaTeX (wspólny dla całej pracy)

Stan 2026-11-09. Skompilowano w kontenerze (TeX Live 2023, LuaLaTeX + biber): **`main.pdf` ma 33 strony**, w tym rozdziały 3, 4, 6 i załącznik A jako puste szkielety z `\TODO`. Bez błędów; ostrzeżenia tylko o 4 brakujących kluczach `TODO-…` we wstępie (mapowanie w sekcji 4 wyżej).

## Pliki

| Plik | Rola |
|---|---|
| `main.tex` | plik główny: klasa, kolejność części, `\input` rozdziałów |
| `szablon/preambula.tex` | pakiety i format: marginesy, czcionka, interlinia, numeracja, podpisy, siunitx, biblatex |
| `szablon/makra.tex` | `\TODO`, odwołania, `\rysunek`, oznaczenia ze słownika, `\inputBezPreambuly` |
| `szablon/strona_tytulowa.tex` | strona tytułowa + strona streszczeń wg wzoru WEFiM `inz_pl_w12n.docx` |
| `frontmatter/dane_pracy.tex` | **jedyne miejsce na metadane** (autor, opiekun, tytuł PL/EN, rok, streszczenia, słowa kluczowe) |
| `frontmatter/wykaz_skrotow.tex` | wykaz skrótów i oznaczeń przepisany ze `slownik.md` (sekcje 2 i 3.1) |
| `frontmatter/podziekowania.tex` | opcjonalne, domyślnie wyłączone w `main.tex` |
| `rozdzialy/0X_*.tex`, `A_*.tex` | „wrappery” rozdziałów, które wczytują istniejące pliki z innych folderów |
| `.latexmkrc` | `latexmk main.tex` → LuaLaTeX + biber, pliki pomocnicze w `build/` |

Kompilacja: `latexmk main.tex` w folderze `wspolne/` (albo `lualatex main`, `biber main`, 2× `lualatex main`). Overleaf: Menu → Compiler → **LuaLaTeX**; trzeba wgrać też foldery, z których czytają wrappery (ścieżki `../`).

## Format (wymogi PWr/WEFiM)

- Klasa `mwrep` (polska typografia, ta sama baza co `dyplompwr`), 12 pt, A4, **druk dwustronny** (`twoside`), rozdziały od dowolnej strony (`openany`, zgodnie z budżetem stron).
- Czcionka: Times New Roman, a gdy jej brak (Linux) metryczny klon TeX Gyre Termes; matematyka TeX Gyre Termes Math.
- Marginesy: 25 mm, od strony grzbietu 30 mm. Tekst wyjustowany, wcięcie także pierwszego akapitu.
- Interlinia: `\setstretch{1.1}` ≈ 1,15 w Wordzie (≈ 400 słów/str., jak w `budzet_stron.md`). Zmiana: `\interlinia` na górze `preambula.tex`.
- Numer strony w **górnym zewnętrznym rogu** (wymóg dziekanatu dla egzemplarza archiwalnego), bez żywej paginy; strona tytułowa bez numeru, ale liczona jako 1.
- Kolejność części wg strony WEFiM „Zasady edytowania pracy”: strona tytułowa, streszczenie PL, abstract EN, podziękowania, spis treści, wykaz skrótów, wstęp/cel, teoria, prace własne, podsumowanie, literatura, dodatki. (Golden Standard ma podziękowania przed streszczeniem; wydział podaje odwrotnie, przyjęto kolejność wydziałową.)
- Rysunki „Rys. 3.1.” (podpis pod), tabele „Tab. 3.1.” (podpis nad), wzory (3.1) po prawej, wszystko w obrębie rozdziału.
- Bibliografia: biblatex + biber, `style=ieee`, `sorting=none`, plik `wspolne/bibliografia.bib` (sekcja 3 wyżej).
- Wersja dla promotora (jednostronna): w `main.tex` `twoside` → `oneside`.
- Wersja do oddania: odkomentować `\wersjaFinalnatrue` w `main.tex` — każdy pozostawiony `\TODO` zatrzyma kompilację.

## Makra (zawsze z `szablon/makra.tex`, nie definiować w rozdziałach)

| Makro | Wynik |
|---|---|
| `\TODO{…}` | czerwone `[TODO: …]` + ostrzeżenie w logu (`grep "TODO:" build/main.log` daje listę) |
| `\rysref{fig:x}`, `\tabref{}`, `\wzorref{}`, `\rozdzref{}`, `\pref{}`, `\zalref{}` | „rys.~3.1”, „tab.~…”, „wzór~(2.3)”, „rozdz.~…”, „p.~…”, „zał.~…” |
| `\angielski{Carbon Nanotubes}` | „ang. *Carbon Nanotubes*” (`\ang` jest zajęte przez siunitx) |
| `\rysunek[szer]{plik}{podpis}{etykieta}` | cały blok `figure` |
| `\opracowanieWlasne`, `\naPodstawie{klucz}`, `\zrodlo{klucz}` | dopiski w podpisach |
| `\tabjedn{$\UB$}{\volt}` | nagłówek kolumny „$U_\mathrm{B}$ [V]” |
| `\UB \UT \Ie \IB \IT \RT \RB \Ezero \Ec \me \kB \FL \RKO`, `\dd` | oznaczenia ze słownika (p. 3.1–3.2), w trybie matematycznym |
| `\Ka \Kb \La` | K$\alpha$, K$\beta$, L$\alpha$ („Si~\Ka”) |
| `\si{\ju}` | jednostka umowna „j.u.” |
| `\inputBezPreambuly{plik}` | wstawia rysunek zapisany jako osobny dokument (`\documentclass…\begin{document}`) bez zmian w pliku |
| `\figdir`, `\datadir` | katalog zdjęć/danych fragmentu; wrapper ustawia przez `\renewcommand` |

Liczby i jednostki: `\SI`, `\SIrange`, `\si`, `\num` (już używane) działają; ustawienia siunitx są tylko w preambule — **usunąć `\sisetup`, `locale=DE` i `\providecommand{\TODO}` z kopii rozdziałów** przy przenoszeniu (w obecnych plikach `\providecommand` nie szkodzi). Etykiety: `ch:`, `sec:`, `subsec:`, `fig:`, `tab:`, `eq:`, `zal:`.

## Podłączenie istniejących rozdziałów

Istniejące pliki **nie zostały zmienione**. Każdy rozdział ma wrapper w `rozdzialy/`, który je wczytuje:

| Rozdział (etykieta) | Wrapper | Źródło | Co zrobić w źródle przy najbliższej edycji |
|---|---|---|---|
| 1. Wstęp (`ch:wstep`) | `01_wstep.tex` | `wstep-zagajenie/wstep_opcja_C.tex` | dodać `\label{ch:wstep}` po `\chapter`; podmienić klucze `TODO-…` (sekcja 4); dopisać „Cel i zakres pracy” jako `\section` |
| 2. Podstawy (`ch:podstawy`) | `02_podstawy.tex` | `podstawy-teoretyczne/podstawy_teoretyczne.tex` | nic — kompiluje się bez zmian; usunąć `\providecommand{\TODO}` (zbędne) |
| 3. Projekt i wykonanie (`ch:projekt`) | `03_projekt.tex` | brak | wątek rozdziału tworzy własny plik z `\chapter` i podmienia treść wrappera na `\input{../folder/plik}` |
| 4. Stanowisko i metodyka (`ch:stanowisko`) | `04_stanowisko.tex` | `uklad-pomiarowy/uklad_pomiarowy_body.tex` (schemat) | wrapper wstawia schemat przez `\inputBezPreambuly`, z podpisem z `rysunek_w_pracy.tex` poprawionym wg słownika (N6, N9: $R_\mathrm{T}$, „prototyp analizatora EDS”). `rysunek_w_pracy.tex` nie jest używany (ma złą ścieżkę `figures/uklad_pomiarowy/`). W `uklad_pomiarowy_body.tex` brakuje `\end{document}` — dlatego nie da się go wstawić zwykłym `\input` ani pakietem `standalone` |
| 5. Badania (`ch:badania`) | `05_badania.tex` | `emisja-magnes-pomiary/emisja_tresc.tex` (od `\section`) | wrapper ustawia `\figdir`/`\datadir` na `../emisja-magnes-pomiary/…`; poprawki symboli wg słownika N3–N5 |
| 6. Podsumowanie (`ch:podsumowanie`) | `06_podsumowanie.tex` | brak | przenieść tu „Wnioski” z `emisja_tresc.tex` (budżet) |
| Zał. A (`zal:zasilanie`) | `A_zasilanie.tex` | brak | – |

Nowy rozdział: plik w swoim folderze, zaczyna się od `\chapter{…}\label{ch:…}`, bez preambuły; podgląd budować przez `main.tex` (można chwilowo zakomentować inne `\input`), a nie przez osobny `\documentclass`. Ścieżki rysunków względem `wspolne/` (`../folder/plik`) albo przez `\figdir`.

## Porównanie z repozytorium `W:\VAULT\Inzynierka\latex` (sprawdzone 2026-11-09)

Repo to szkielet z 17.09.2026 (wszystkie pliki poza `.bib` mają tę datę), więc treści nowszej niż w plikach projektu w nim nie ma. Przeniesiono:

| Z repo | Dokąd | Uwagi |
|---|---|---|
| `\titlen` (tytuł EN) | `frontmatter/dane_pracy.tex` | „Development, implementation and testing of a miniature MEMS-based EDS analyzer for space applications”; sprawdzić zgodność z APD |
| `frontmatter/streszczenie.tex`, `abstract_en.tex` | `dane_pracy.tex` (`\pracaStreszczenie`, `\pracaAbstract`) | wersje robocze, z `\TODO` na wyniki liczbowe |
| `chapters/01_wstep.tex`: cel, aspekt badawczy i inżynierski | `rozdzialy/01_wstep.tex`, `\section{Cel i zakres pracy}` (`sec:cel`) | przepisane bezosobowo; „Zgodność z kierunkiem” pominięta (jest w opcji C) |
| `main-roboczy.tex` (oneside, interlinia 1,5) | `main-roboczy.tex` | wspólna treść w `main-tresc.tex`; 35 str. |
| `bibliography/bibliografia.bib` | `bibliografia.bib` | scalił już wątek bibliografii (50 pozycji) |

Nie przeniesiono, celowo:
- `dyplompwr.cls` i `logopwr/` — strona tytułowa Wydziału Chemicznego; jest wzór WEFiM.
- Numeracja rzymska części wstępnej — dziekanat numeruje wszystkie strony od pierwszej, ciągle.
- Wykaz skrótów z repo (HV, keV, ESD) — słownik zakazuje HV/ESD; obowiązuje `frontmatter/wykaz_skrotow.tex`.
- Słowa kluczowe z repo (7) — WEFiM wymaga 3–6; zostało 6.
- Nagłówki rozdziałów 2–6 z repo (wzorcowy spis treści) — struktura idzie za `budzet_stron.md`; etykiety z repo (`ch:teoria`, `ch:realizacja`, `app:schematy`) nie są nigdzie używane.
- `config/packages.tex`: `locale=DE`, kolorowe linki, `listings`, `longtable` — zastąpione `szablon/preambula.tex` (`listings`/`longtable` można dopisać, jeśli będą potrzebne).

Repo można teraz zastąpić zawartością `wspolne/` (plus foldery rozdziałów) albo przestać go używać; `wspolne/` jest aktualnym źródłem.
