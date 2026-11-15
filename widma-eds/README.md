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

---

# Oryginalne pliki .mca (miedz.zip, 2026-11-15)

Pliki KETEK ProSpect v1.1.36 (nagłówek tekstowy + 8192 kanały, zakres 80 keV) w `dane_mca/`:
- `2026-06-12_Al_4kV/1-5SERIA.mca`: oryginał widma 4 kV. `4SERIA.mca` = to samo, co na zdjęciach (real 210,7 s, live 100,05 s, 1 333 605 zliczeń w kanale Al Kα). Wykres `widmo_eds_4kV.pdf/png` jest teraz rysowany z tego pliku (digitalizacja ze zdjęć zostaje tylko jako archiwum).
- `2026-08-17_magnes/`: 1Pomiar1mA, 1Seria, 2SeriaBezMagnesu (tło kończy się ok. 4–4,5 keV; Mg/Al/Si). Jeszcze nieopisane.
- `2026-11-13/`: `miedz/` (miedz0 = dawny `miedz.mca` + miedz1–5), `olow/` (seria1–10), `final/` (s1–s10), `aluminium/` (= „Aluminium nowe”, seria1–11; seria11 to kopia seria10, seria2–3 czas martwy > 90 %).

## Kalibracja energii
Skala z pliku (kanał · 80/8192 keV) ma błąd wzmocnienia ok. 2 %: E = 1,02156·E_raw − 0,0184 keV (13.11; punkty: Al Kα, Pb Mα, Cr Kα, Fe Kα, Cu Kα; residua ≤ 3 eV). Dla 12.06: E = 1,02168·E_raw − 0,0008 keV (Mg, Al, Si).

## Wyniki 13.11 (`piki_13-11.csv`, `widma_materialy.pdf`)
- A „miedź”: Cu Lα 0,924, Cu Kα/Kβ, seria Te L (3,76/4,04/4,30/4,57), P 2,01, S 2,30, Cl 2,62, K 3,32, Si, Al.
- B ołów: Pb Mζ/Mα/Mγ; brak Pb L (E0 ≈ 10 keV < krawędź L3 13 keV).
- C „final”: Au M (1,66/2,13/2,41/2,79), Cr Kα/Kβ, Cu Lα/Kα. Częstość Au Mα w s1–s10: 1027–1096 /s.
- D aluminium: Al Kα, sumacyjny 2×Al, Mn Kα, Fe Kα (bez Mg i Si, inny stop niż 12.06).
- Tło hamowania kończy się ok. 10 keV → E0 ≈ 10 keV (U_T niezapisane w plikach).
- **Tlen**: brak piku O Kα (0,525 keV) w żadnym widmie; poniżej ok. 0,65 keV zliczenia ≈ 0 (okno detektora + próg). Pik 0,92 keV to Cu Lα.

Skrypt: `python3 -I skrypty_mca/widma_mca.py /mnt/project-files/widma-eds` (wymaga numpy, scipy, matplotlib). Widma jako CSV (E po korekcji; zliczenia): `widma_csv/`.
Tekst do pracy: `widma_materialy_tresc.tex` (podpięty w `wspolne/rozdzialy/05_badania.tex`).
