import numpy as np
from openpyxl import Workbook
from openpyxl.chart import ScatterChart, Reference, Series
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.drawing.image import Image as XImg
wb=Workbook(); b=Font(bold=True); hdr=PatternFill('solid',fgColor='DDE6F0')
def head(ws,row,vals):
    for i,v in enumerate(vals,1):
        c=ws.cell(row,i,v); c.font=b; c.fill=hdr; c.alignment=Alignment(wrap_text=True,vertical='top')
# 1 parametry
ws=wb.active; ws.title='Parametry'
P=[('Data pomiaru','12.06.2026, ok. 12:18–12:30 (znaczniki czasu na zdjęciach)'),
('Napięcie targetu U_T','4000 V (zasilacz HV, zrzut ekranu 12:18)'),
('Napięcie bramki U_B','1000 V'),
('Elektronika detektora','KETEK DPP2 (cyfrowy procesor impulsów), oprogramowanie KETEK ProSpect v1.1.36'),
('Typ detektora','nieznany; DPP2 współpracuje zwykle z detektorami SDD KETEK (VITUS) – do potwierdzenia'),
('Peaking time','0,50 µs'),('Base gain','2,980'),('Fine gain trim','1,000'),
('Liczba kanałów MCA','8192'),('Zakres dynamiczny','80 keV'),('Szerokość kanału','10 eV/kanał'),
('Progi','Trigger 30, Baseline 0, Energy 0'),
('Tryb','Continuous + Resume: widmo kumulowane, kolejne zdjęcia to stany pośrednie jednego pomiaru'),
('Czas martwy','52–54 % (bardzo wysoki; widoczne piki sumacyjne)'),
('Źródło danych','10 zdjęć ekranu (20260612_121840 … 20260612_124231); arkusz Widmo_digitalizacja odczytany z ujęcia końcowego (live 100 s)')]
head(ws,1,['Parametr','Wartość'])
for i,(k,v) in enumerate(P,2): ws.cell(i,1,k); ws.cell(i,2,v)
ws.column_dimensions['A'].width=28; ws.column_dimensions['B'].width=100
# 2 akwizycja
ws=wb.create_sheet('Akwizycja')
rows=[('20260612_122544',22.171,10.266,5040564,490.9824,227.3498,54,153885,''),
('20260612_122619',43.479,20.332,9861175,484.9997,226.8010,53,297351,''),
('20260612_122715',83.342,39.801,18751443,471.1350,224.9952,52,558820,''),
('20260612_122749',104.877,49.896,23632607,473.6387,225.3369,52,704657,''),
('20260612_122828',127.218,60.004,28739902,478.9694,225.9109,53,851449,''),
('20260612_122931',169.439,79.847,38296488,479.6237,226.9192,53,1110902,'zdjęcie nieostre – wartości z niepewnym odczytem'),
('20260612_123004',189.226,89.432,42723806,477.7227,225.7823,53,1223050,''),
('20260612_123036',210.699,100.053,47493933,474.6894,225.4109,53,1333605,'ujęcie końcowe, podstawa digitalizacji')]
head(ws,1,['Zdjęcie','Real time [s]','Live time [s]','Events','ICR [kcps]','OCR [kcps]','Dead time [%]','Zliczenia w kanale 1,49 keV (kursor)','Zliczenia 1,49 keV / live time [1/s]','Przyrost 1,49 keV / Δlive [1/s]','Uwagi'])
for i,r in enumerate(rows,2):
    for j,v in enumerate(r[:8],1): ws.cell(i,j,v)
    ws.cell(i,9,f'=H{i}/C{i}'); ws.cell(i,10,'' if i==2 else f'=(H{i}-H{i-1})/(C{i}-C{i-1})'); ws.cell(i,11,r[8])
for c,w in zip('ABCDEFGHIJK',[18,12,12,12,11,11,11,18,18,18,44]): ws.column_dimensions[c].width=w
ch=ScatterChart(); ch.title='Stabilność częstości zliczeń'; ch.x_axis.title='Czas rzeczywisty [s]'; ch.y_axis.title='kcps'; ch.style=13
x=Reference(ws,min_col=2,min_row=2,max_row=9)
for col,name in [(5,'ICR'),(6,'OCR')]:
    s=Series(Reference(ws,min_col=col,min_row=2,max_row=9),x,title=name); s.marker.symbol='circle'; ch.series.append(s)
ch.width=18; ch.height=8; ws.add_chart(ch,'B12')
# 3 linie
ws=wb.create_sheet('Identyfikacja_linii')
head(ws,1,['E piku (digitalizacja) [keV]','Wysokość [zliczenia/10 eV]','Linia','E tabelaryczna [keV]','Różnica [eV]','Interpretacja'])
L=[(1.26,519000,'Mg Kα',1.254,'magnez – składnik próbki/stopu Al (do potwierdzenia, zob. słownik N8)'),
(1.48,1333605,'Al Kα',1.486,'główna linia; wysokość z kursora ProSpect'),
(1.74,841000,'Si Kα',1.740,'krzem (struktura MEMS / próbka)'),
(2.98,26300,'Al Kα + Al Kα',2.972,'pik sumacyjny (pile-up), czas martwy 53 %'),
(3.22,22000,'Al Kα + Si Kα',3.226,'pik sumacyjny'),
(3.46,10800,'Si Kα + Si Kα',3.480,'pik sumacyjny')]
for i,(e,h,l,t,n) in enumerate(L,2):
    ws.cell(i,1,e); ws.cell(i,2,h); ws.cell(i,3,l); ws.cell(i,4,t); ws.cell(i,5,f'=ROUND((A{i}-D{i})*1000,0)'); ws.cell(i,6,n)
ws.cell(9,1,'Energie linii: tabela Bruker (zdjęcie 20260612_124231). Dokładność digitalizacji ok. ±20 eV. Brak tła powyżej ok. 4 keV zgodny z granicą Duane’a–Hunta E_max = e·U_T = 4 keV.')
for c,w in zip('ABCDEF',[16,16,16,16,12,70]): ws.column_dimensions[c].width=w
# 4 widmo
ws=wb.create_sheet('Widmo_digitalizacja')
d=np.loadtxt('spektrum_dig.csv',delimiter=',',skiprows=1)
head(ws,1,['E [keV]','Zliczenia / 10 eV (przybliżone)'])
for i,(e,c) in enumerate(d,2): ws.cell(i,1,float(e)); ws.cell(i,2,int(round(c)))
ws.cell(1,4,'Uwaga: wartości odczytane z fotografii ekranu (korekcja perspektywy, krok 20 eV), dokładność ok. ±2 % wysokości i ±20 eV. Do pracy należy wyeksportować oryginalne widmo z ProSpect (File → Save, plik .mca/.csv).').alignment=Alignment(wrap_text=True)
ws.column_dimensions['D'].width=60
ch=ScatterChart(); ch.title='Widmo EDS, U_T = 4 kV, U_B = 1 kV, live 100 s'; ch.x_axis.title='E [keV]'; ch.y_axis.title='Zliczenia / 10 eV'; ch.style=13
n=len(d)+1
s=Series(Reference(ws,min_col=2,min_row=2,max_row=n),Reference(ws,min_col=1,min_row=2,max_row=n),title='widmo'); s.marker.symbol='none'; s.smooth=False
ch.series.append(s); ch.x_axis.scaling.min=0; ch.x_axis.scaling.max=6; ch.width=24; ch.height=12; ch.legend=None
ws.add_chart(ch,'D4')
# 5 wykresy png
ws=wb.create_sheet('Wykresy')
for img,a in [('/mnt/project-files/widma-eds/widmo_eds_4kV.png','A1'),('/mnt/project-files/widma-eds/stabilnosc_zliczen.png','A38')]:
    im=XImg(img); im.width*=0.55; im.height*=0.55; ws.add_image(im,a)
wb.save('/mnt/project-files/widma-eds/widmo_eds_4kV.xlsx')
