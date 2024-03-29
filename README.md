6\. Cztery w rzędzie 
*(https://en.wikipedia.org/wiki/Connect_Four)*

Opis zadania

-   Okno wyświetlające siatkę 7 kolumn x 6 wierszy, przycisk nad każdą kolumną, informację "Tura gracza 1" lub "Tura gracza 2", przycisk do resetowania gry oraz rozwijalną listę wyboru reguł gry.

-   Początkowo pola siatki są puste.

-   Gracze na zmianę wrzucają monety do wybranych przez siebie kolumn.

-   Pola w których jest moneta gracza 1 są czerwone, pola z monetami gracza 2 są żółte (tkinter, Canvas, [*http://stackoverflow.com/a/12254442*](http://stackoverflow.com/a/12254442)).

-   Gracze wybierają kolumnę klikając przycisk nad nią.

-   Wygrywa gracz który pierwszy ustawi cztery monety w linii (poziomo, pionowo lub po skosie).

-   Gdy gra się kończy, wyświetlane jest okienko z napisem 'Wygrał gracz 1" lub "Wygrał gracz 2", zależnie kto wygrał grę. Możliwe jest zresetowanie planszy bez zamykania głównego okna.

-   Reprezentacja reguł gry ma być realizowana poprzez hierarchię Mas. Klasa bazowa definiuje między innymi funkcję wirtualną ktoWygral() nadpisywaną w klasach pochodnych. Realizowane powinny być przynajmniej dwa zestawy reguł, jako dwie klasy pochodne.

Testy

1.  Wykonanie po dwa ruchy przez każdego z graczy - monety spadają nadół pola gry lub zatrzymują się na już wrzuconym żetonie.

2.  Ułożenie pionowej linii monet przez jednego gracza - oczekiwanainformacja o jego wygranej.

3.  Ułożenie poziomej linii monet przez drugiego gracza - oczekiwanainformacja o jego wygranej.

4.  Ułożenie skośnej linii przez dowolnego gracza - oczekiwanainformacja o jego wygranej.

1.  Zapełnienie pola gry tak, że żaden gracz nie ułożył linii -oczekiwana informacja o remisie.

2.  Ułożenie linii dłuższej niż 4 przez jednego z graczy - oczekiwana informacja o jego wygranej. \[c\]\[c\]\[c\]\[ \]\[cl\[c\]\[c\]\[k\]\[z\]\[2\]\[ \]\[z\]\[ż\]\[ż\] &lt;- w następnym mchu gracz żółty wrzuci monetę w środkową kolumnę.

1.  Próba wrzucenia monety do zapełnionej kolumny - oczekiwana informacja o błędzie.

GitHub:
[Kkoonnrr/Connect\_Four(github.com)](https://github.com/Kkoonnrr/Connect_Four)
