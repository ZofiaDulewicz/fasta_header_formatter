# fasta_header_formatter
Skrypt w Pythonie do automatycznego formatowania i skracania nagłówków sekwencji FASTA z bazy NCBI.

Proste narzędzie napisane w Pythonie, służące do standaryzacji nagłówków plików FASTA pobieranych z bazy NCBI. 

Oryginalne nagłówki sekwencji pobierane z baz danych są często długie i zawierają wiele nadmiarowych informacji. Ten skrypt automatycznie wyłuskuje z nich najważniejsze dane taksonomiczne oraz identyfikatory i zamienia je na zwięzły format: `>Rodzaj_gatunek_NumerAccession`. Narzędzie znacznie ułatwia przygotowywanie przejrzystych danych wsadowych do przyrównań sekwencji (sequence alignment).

# Jak to działa?
Skrypt wykorzystuje bibliotekę wyrażeń regularnych (`re`) do identyfikacji wzorców w tekście (nazwy gatunkowe, numery akcesyjne). Przetwarza plik wejściowy linia po linii, podmieniając wyłącznie nagłówki i zachowując oryginalne sekwencje nukleotydowe lub aminokwasowe bez zmian.

## Sposób użycia
Skrypt obsługuje się z poziomu wiersza poleceń. Uruchom program, podając ścieżkę do pliku wejściowego (`-i`) oraz wyjściowego (`-o`):

`python ncbi_header_cleaner.py -i plik_wejsciowy.fasta -o gotowy_wynik.fasta`
