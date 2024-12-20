# graph-verticles-coloring

Program został napisany specjalnie do przedmiotu Techniki Algorytmiczne.

Problem: "Kolorowanie wierzchołków grafu"

Program tworzy excela z pomiarami dla dwóch algorytmów, optymalnego i algorytmu LF:

![image](https://user-images.githubusercontent.com/63360050/233190172-8ba2b142-c338-4a34-986a-5dbd3277bc60.png)

## Instalacja

Do działania potrzebny jest interpreter języka Python w wersji conajmniej 3.11.0

Aby zaintalować Pythona w systemie Windows należy wcisnąć `Win+R` następnie wpisać `powershell` a po odpaleniu konsoli
należy wpisac `python`, wtedy wyświetli się Microsoft Store z którego należy pobrać Pythona.

Dodatkowo należy zaintalować biblioteki wpisując w konsoli **Powershell**:

```
pip install -r requirements.txt
```

## Obsługa programu

Program polega na edycji funkcji zawartej w pliku `main.py` a następnie otworzeniu folderu w konsoli(`Shift+PPM` w
folderze i wybranie opcji `Otworz w terminalu`) i wpisanie:

```
python main.py
```


Po wykonaniu polecenia w tym samym folderze powinien wygenerować się domyślny plik test.xlsx

## Parametry

| Parametry        | Zastosowanie                                                                                                                                                                                                                                               | Obowiązkowy |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------:|
| `size=[W, K]`    | rozmiar macierzy, pierwszy argument to liczba wierzchołków `W` a drugi to liczba krawędzi `K`                                                                                                                                                              |     TAK     |
| `filename`       | podanie nazwy pliku .xlsx, nazwa musi zawierać poprawne rozszerzenie. W przypadku gdy plik istnieje dane zostaną dodane na koniec pliku. Wszystkie obliczenia i ingerencje w pliku nie należy umieszczać pod danymi gdyż program może nadpisać te komórki. |     NIE     |
| `importfilename` | nazwa importowanego grafu. Nazwa musi być z roszerzeniem .npy                                                                                                                                                                                              |     NIE     |
| `exporttoexcel`  | słuzy do wyłączania opcji eksportu do pliku excel. True eksportuje                                                                                                                                                                                         |     NIE     |
| `exporttofile`   | słuzy do włączania opcji eksportu wygenerowanego grafu. Opcja przydatna do analizy                                                                                                                                                                         |     NIE     |
| `printmatrix`    | służy do wyświetlania macierzy incydencji na ekran                                                                                                                                                                                                         |     NIE     |
| `printcolour`    | służy do wyświetlania metody pokolorowania wierzchołków na ekran                                                                                                                                                                                           |     NIE     |
| `printamount`    | służy do wyświetlania ilosci urzytych kolorów na ekran                                                                                                                                                                                                     |     NIE     |
| `printtime`      | służy do wyświetlania czas pracy algorytmów na ekran                                                                                                                                                                                                       |     NIE     |
| `printmemory`    | służy do wyświetlania ilości pamięci użytych przez algorytmy na ekran                                                                                                                                                                                      |             |
| `iterations`     | parametr mówiący ile badań ma przeprowadzić algorytm (Domyślnie 1)                                                                                                                                                                                         |     NIE     |

Parametry wystarczy odkomentować (usunąć znak `#`) oraz zmienić wartość w przypadku parametrów odnoszących się do nazwy
plików.
