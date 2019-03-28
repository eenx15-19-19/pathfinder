class TestIgen:
    # antal rader och kolumner i matrisen
    rows = 4
    cols = 4
    matrix = [['0000' for col in range(4)] for row in range(4)]
    # lista med rows*cols antal element
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    # index för matris
    row = 0
    col = 0

    # börjar hantera första 'raden' i listan
    current_row = 1

    # flyttar alltid vänster 1 pga nollindexering, ökar när vi backar i raden
    move_left = 1

    print(matrix)

    for k in range(len(list)):

        # index på element i listan
        index = cols * current_row

        # flytta vänster 1 pga nollindexering + 1 till för varje redan tillagt element
        number = list[index - move_left]

        matrix[row][col] = number

        # flytta ner en rad
        row = row + 1

        # om vi når botten av matrisen, flytta upp till toppen igen
        if row > rows - 1:
            row = 0
            current_row = current_row + 1
            col = col + 1
            # om
            if col > cols - 1:
                col = 0

            # byter vi rad ska denna nollställas
            move_left = 0

            # backa en gång för varje avklarat element
        move_left = move_left + 1

    print(matrix)