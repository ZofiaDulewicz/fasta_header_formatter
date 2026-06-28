import re

#Wzorce do wyłuskania danych z nagłówka
WZORZEC_NUMER = re.compile(r'([A-Z]{1,3}_?\d{4,9})(?:\.\d+)?')  #Szuka identyfikatora 1–3 wielkie litery, opcjonalny podkreślnik, potem 4–9 cyfr, na końcu ignoruje wersję po kropce
WZORZEC_NAZWA = re.compile(r'\b([A-Z][a-zA-Z-]+)\s+([a-z][a-zA-Z.-]+)\b') #pierwszy wyraz zaczyna się wielką literą, dalej litery lub myślnik, drugi wyraz małą literą(rodzaj, może mieć kropki lub myślnik (gatunek)

def skracaj(naglowek: str) -> str:
    #Zwraca >Rodzaj_gatunek_Numer dla podanego nagłówka w pliku fasta
    tekst = naglowek[1:].strip()  #obcina >, strip() ścina białe znaki z brzegów. Zostaje sam tekst

    # Numer z NCBI
    dopas_num = WZORZEC_NUMER.search(tekst)
    numer = dopas_num.group(1) if dopas_num else 'XXX'  #Próbuje znaleźć accession number. Jeśli znalazł, bierze go z grupy 1 (już bez .1), jeśli nie znalazł, awaryjnie używa XXX żeby miał stały format

    # Rodzaj i gatunek
    dopas_tax = WZORZEC_NAZWA.search(tekst)
    if dopas_tax:
        rodzaj, gatunek = dopas_tax.group(1), dopas_tax.group(2)
    else:
        slowa = [s for s in re.split(r'\s+', tekst) if re.search(r'[A-Za-z]', s)]
        rodzaj = slowa[0] if len(slowa) > 0 else 'Genus'
        gatunek = slowa[1] if len(slowa) > 1 else 'species'

    #Próbuje znaleźć parę Rodzaj gatunek, jeśli znalazł bierze obie grupy. Jeśli nie prymitywnie dzieli tekst po białych znakach i bierze pierwsze dwa. jeśli nawet tego nie ma, daje awaryjne Genus i species

    gatunek = gatunek.replace('.', '')
    return f'>{rodzaj}_{gatunek}_{numer}'

#Usuwa kropki z nazwy gatunkowej i składa wynik w zadanej kolejności

def przerob_fasta(plik_we: str, plik_wy: str) -> None:
    with open(plik_we, 'r', encoding='utf-8') as f_in, open(plik_wy, 'w', encoding='utf-8') as f_out:
        for linia in f_in:
            if linia.startswith('>'):
                f_out.write(skracaj(linia) + '\n')
            else:
                f_out.write(linia if linia.endswith('\n') else linia + '\n')

#Otwiera plik wejściowy do czytania i wyjściowy do pisania. Jeśli linia zaczyna się od >, traktuje ją jako nagłówek fasta i zamienia przez funkcje skracaj
#Jeśli to sekwencja, przepisuje 1:1, pilnując żeby na końcu była nowa linia


plik_we = r'plik_wejsciowy_test'
plik_wy = r'wsadowy_poprawa_test.txt'

# wywołanie funkcji
przerob_fasta(plik_we, plik_wy)
print(f'Gotowe! Plik zapisano jako: {plik_wy}')