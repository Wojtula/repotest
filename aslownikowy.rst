Algorytmy słownikowe
####################

Przykłady słownikowych algorytmów kompresji bezstratnej:
`LZ77 <https://pl.wikipedia.org/wiki/LZ77>`_,
`LZ78 <https://pl.wikipedia.org/wiki/LZ78>`_
`LZW <https://pl.wikipedia.org/wiki/LZW>`_.

Zasada działania polega w uproszczeniu na analizie tekstu, zbudowaniu słownika zawierającego
powtarzające się ciągi znaków, a następnie zastępowaniu powtarzających się sekwencji indeksami
wskazującymi wcześniejsze wystąpienia.

Przykład::

  The rain in Spain fails mainly on the plain. (44 znaki = 44 bajty)
  The rain <3,3>Sp<9,4>falls m<11,3>ly on t<34,3>pl<15,3>. (28 znaki + 5 kodów = 33 bajty)

Token <x,y> oznacza, że dana sekwwencja wystąpiła x znaków wcześniej i miała długość y znaków.
Aby zapisać *x* trzeba 6 bitów, na *y* 2 bity, w sumie 1 token zapisujemy w 1 bajcie.

Współczynnik kompresji w omówionym przykładzie: 33/44 * 100% = 75%


Ćwiczenie 1
***********

Poniżej wpisz skompresowane metodą słownikową podane zdanie. Oblicz i podaj również współczynnik kompresji::

  Moją pasją są kompresje i ich komputerowe wersje. (52znaki = 52 bajty)
  Moją pas<6,3>są kompre<15,2>e, i ich <16,4>uterowe wer<25,3> (37 znaków + 5 kodów = 42 bajty

  Współczynnik 42/52 = 81%
