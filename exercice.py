#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from structs import Queue, Stack


def reverse_data(data: list = None):
    # TODO: Demander 10 valeurs à l'utilisateur,
    # les stocker dans une structure de données,
    # et les retourner en ordre inverse, sans utiliser de liste.
    stack , MAX = Stack() , 10

    if data is None:
        stack.put_many(input(f"Entrez la valuer {i} ici -> ") for i in range(MAX))
    
    reversed_data = [ stack.get() for _ in range(MAX) ]

    return reversed_data


def delete_nth_from_stack(data: Stack, position: int) -> Stack:
    # TODO: Supprimer le énième (position) élément de data et retourner la nouvelle structure de données.
    for i in range(len(data)) :
        if i == (len(data) - position) :
            print(f"L'element a supprimer est {data.get()} a la position {position}.")
            data.get()
        else :
            data.put(data.get())

    new_stack = Stack()
    new_stack.put_many(data.get() for _ in range(len(data)))
   
    return new_stack


def delete_nth_from_queue(data: Queue, position: int) -> Queue:
    # TODO: Supprimer le énième (position) élément de data et retourner la nouvelle structure de données.
    # something weird with this function
    for i in range(len(data)) :
        if i == position :
            print(f"L'element a supprimer est {data.get()} a la position {position}.")
            data.get()
        else :
            data.put(data.get())
    return data


def sort_stack(data: Stack) -> Stack:
    # TODO: Retourner la séquence triée
    data_list = [data.get() for _ in range(len(data))]
    data.put_many(sorted(data_list))
    return data


def sort_queue(data: Queue) -> Queue:
    # TODO: Retourner la séquence triée
    data_list = [data.get() for _ in range(len(data))]
    data.put_many(sorted(data_list))
    return data


def string_and_structs(string: str) -> tuple:
    # TODO: Parcourez la chaîne de caractères.
    # Si le caractère est une lettre, on l'ajoute dans fifo.
    # Sinon, on retire un élément de fifo pour l'insérer dans lifo.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    fifo, lifo = Queue(), Stack()
    for letter in string :
        if letter in alphabet :
            fifo.put(letter)
        else :
            lifo.put(fifo.get())

    return fifo, lifo


def main() -> None:
    #print("On inverse des données...")
    #print(f"Résultat: {reverse_data()}")

    '''n = 4
    lifo = Stack()
    lifo.put_many([i for i in range(20)])
    print(f"On retire l'élément à la position {n} de la pile et on obtient: {delete_nth_from_stack(lifo, n)}")

    n = 6
    fifo = Queue()
    fifo.put_many([i for i in range(20)])
    print(f"Avant -> {fifo}")
    print(f"On retire l'élément à la position {n} de la file et on obtient: {delete_nth_from_queue(fifo, n)}")

    lifo = Stack()
    lifo.put_many([randint(0, 1000) for _ in range(20)])
    print(f"On ordonne une pile: {sort_queue(lifo)}")

    fifo = Queue()
    fifo.put_many([randint(0, 1000) for _ in range(20)])
    print(f"On ordonne une file: {sort_stack(fifo)}")'''

    sequence = "te!eYy.E6e/T"
    print(f"Le résulat de la manipulation de la séquence: {string_and_structs(sequence)}")


if __name__ == '__main__':
    main()
