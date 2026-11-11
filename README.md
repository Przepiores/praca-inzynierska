# Praca inżynierska — miniaturowy analizator EDS w technologii MEMS

Kopia robocza pracy z projektu (PWr, WEFiM). Źródłem prawdy są pliki w projekcie; to repozytorium jest kanałem synchronizacji z komputerem.

- `wspolne/main.tex` — plik główny (LuaLaTeX + biber: `latexmk main.tex` w `wspolne/`), opis szablonu w `wspolne/README.md`.
- Pozostałe foldery — treść rozdziałów wczytywana przez `wspolne/rozdzialy/*.tex`.
- `pdf/Praca_inzynierska_promotor.pdf` — wersja dla promotora (`wspolne/main-promotor.tex`): bez znaczników TODO i bez pustych podrozdziałów.
- `pdf/Praca_inzynierska.pdf` — najnowszy skompilowany PDF (nadpisywany przy każdej aktualizacji; poprzednie wersje w historii git).
- `synchronizuj.ps1` — na komputerze: `git pull` i kopia PDF do `Downloads\Praca_inzynierska_RRRR-MM-DD.pdf`.
