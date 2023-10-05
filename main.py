import os
import random


class Wrap:
    __left = None
    __right = None

    def __init__(self, left=None, right=None):
        self.__left = left
        self.__right = right
        return

    def __getitem__(self, item):
        if self.__left is None or self.__right is None:
            return None
        elif self.__left <= item < self.__right:
            return item
        else:
            return self.__left + (item - self.__left) % (self.__right - self.__left)


def is_enharmonic(input_str, standard):
    inl = input_str.lower()
    stl = standard.lower()
    if len(input_str) == 1:
        return inl == stl
    elif (stl == 'c' and inl == 'b#') or \
            (stl == 'b' and inl == 'cb') or \
            (stl == 'f' and inl == 'e#') or \
            (stl == 'e' and inl == 'fb'):
        return True
    else:
        return inl in stl


key = ['C', '(C#/Db)', 'D', '(D#/Eb)', 'E', 'F', '(F#/Gb)', 'G', '(G#/Ab)', 'A', '(A#/Bb)', 'B']
chord_type = [['maj', 'min', 'dim', 'aug', 'sus2', 'sus4'], ['maj7', 'min7', 'm7b5', 'dim7', '7', 'mM7', 'maj7#5']]
chord_composition = \
    [  # semitones to root
        [  # triad chord
            [0, 4, 7],  # maj
            [0, 3, 7],  # min
            [0, 3, 6],  # dim
            [0, 4, 8],  # aug
            [0, 2, 7],  # sus2
            [0, 5, 7],  # sus4
        ],
        [  # seventh chord
            [0, 4, 7, 11],  # △7
            [0, 3, 7, 10],  # m7
            [0, 3, 6, 10],  # ø
            [0, 3, 6, 9],  # o
            [0, 4, 7, 10],  # 7
            [0, 3, 7, 11],  # mM7
            [0, 4, 8, 11]  # △7+5
        ]
    ]
tones_of_chord = [3, 4]
specific_types = [len(chord_type[i]) for i in range(0, len(chord_type))]
inversion_name = ['原位', '第一转位', '第二转位', '第三转位']

while True:
    root = random.randrange(0, len(key))
    chord_general_type = random.randrange(0, len(chord_type))
    chord_specific_type = random.randrange(0, specific_types[chord_general_type])
    inversion = random.randrange(0, tones_of_chord[chord_general_type])
    tone_wrapper = Wrap(0, tones_of_chord[chord_general_type])
    key_wrapper = Wrap(0, len(key))

    os.system("cls")
    print("%s%s%s:" % (key[root], chord_type[chord_general_type][chord_specific_type], inversion_name[inversion]))
    tones = input().split(' ')
    success = True
    if tones[0] == 'exit':
        break
    elif len(tones) != tones_of_chord[chord_general_type]:
        success = False
    else:
        for i in range(0, tones_of_chord[chord_general_type]):
            if not is_enharmonic(tones[i], key[key_wrapper[
                    root + chord_composition[chord_general_type][chord_specific_type][tone_wrapper[inversion + i]]]]):
                success = False
    if success:
        print('正确')
    else:
        for i in range(0, tones_of_chord[chord_general_type]):
            print(key[key_wrapper[
                root + chord_composition[chord_general_type][chord_specific_type][tone_wrapper[inversion + i]]]],
                  end=' ')
        print()
    os.system('pause')
