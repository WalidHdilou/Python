def test_distinct(liste):
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[i] == liste[j]:
                return False
    return True

print(test_distinct([1, 5, 7, 9]))       
print(test_distinct([2, 4, 5, 5, 7, 9]))

