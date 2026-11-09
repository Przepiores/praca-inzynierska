# Widmo EDS, U_T = 4000 V, U_B = 1000 V (pomiar 12.06.2026)

Materiał do podrozdz. 5.2 (Widma EDS próbek), zob. `wspolne/budzet_stron.md`.

## Pliki
- `widmo_eds_4kV.xlsx`: arkusze Parametry, Akwizycja (8 stanów pośrednich pomiaru + wykres ICR/OCR), Identyfikacja_linii, Widmo_digitalizacja (E, zliczenia co 20 eV + wykres), Wykresy.
- `widmo_eds_4kV.pdf/.png`: wykres widma do pracy (`\includegraphics`), `stabilnosc_zliczen.pdf/.png`: ICR, OCR i zliczenia w kanale Al Kα w czasie.
- `widmo_eds_4kV_digitalizacja.csv`: widmo odczytane ze zdjęcia, `skrypty/`: digitalizacja (korekcja perspektywy homografią, błąd dopasowania osi ≤ 4 px) i wykresy.
- `zdjecia/`: oryginalne zdjęcia ekranu, tabela energii linii (Bruker) i nastawy zasilacza HV.

## Warunki pomiaru
- U_T = 4000 V, U_B = 1000 V (zasilacz HV, zrzut 12:18).
- Elektronika: KETEK DPP2, program KETEK ProSpect v1.1.36; peaking time 0,5 µs, 8192 kanały, zakres 80 keV, 10 eV/kanał. Typ detektora (prawdopodobnie SDD KETEK) do potwierdzenia.
- Widmo kumulowane (Continuous + Resume): real time 210,7 s, live time 100,1 s, 47,5·10⁶ zdarzeń, ICR ≈ 475 kcps, OCR ≈ 225 kcps, czas martwy 52–54 %.

## Wyniki (odczyt, dokładność ok. ±20 eV)
| Pik [keV] | Linia | E tabel. [keV] |
|---|---|---|
| 1,26 | Mg Kα | 1,254 |
| 1,48 | Al Kα (1 333 605 zliczeń w kanale 1,49 keV) | 1,486 |
| 1,74 | Si Kα | 1,740 |
| 2,98 / 3,22 / 3,46 | piki sumacyjne Al+Al / Al+Si / Si+Si | 2,972 / 3,226 / 3,480 |

- Tło hamowania zanika przy ok. 4 keV, zgodnie z granicą Duane'a–Hunta E_max = e·U_T.
- Piki sumacyjne wynikają z bardzo dużej częstości zliczeń (czas martwy > 50 %); do pracy zaleca się pomiar przy mniejszym prądzie wiązki lub większej odległości detektora.
- Częstość ICR/OCR stała w czasie (±2 %); średnia częstość w kanale Al Kα spada z 15,0·10³ do 13,3·10³ s⁻¹ (ok. 11 % w 200 s).

## Ograniczenia
Widmo pochodzi z fotografii ekranu, więc nadaje się do identyfikacji linii i do rysunku poglądowego. Do wersji ostatecznej należy wyeksportować oryginalne widmo z ProSpect (File → Save) i podmienić CSV, skrypt `skrypty/plot.py` zadziała bez zmian po podaniu nowego pliku.

Otwarte: skład próbki (Al? stop Al-Mg?), pochodzenie Mg Kα (zob. słownik, N8), czy pomiar był z magnesem, ciśnienie w komorze, prąd emisji podczas pomiaru.
