# latexmk: LuaLaTeX + biber, pliki pomocnicze w build/
$pdf_mode = 4;            # 4 = lualatex
$lualatex = 'lualatex -interaction=nonstopmode -file-line-error -synctex=1 %O %S';
$bibtex_use = 2;          # biber, usuwany przy -c
$aux_dir = 'build';
$out_dir = '.';
