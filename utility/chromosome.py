from music21 import *
import random
import os
import json
from utility.constants import KEY_SIGNATURES, WEIGHTS_SAME_MAJOR_TONALITY, WEIGHTS_SAME_MINOR_TONALITY, COEFFICIENTS_SAME_MAJOR_TONALITY, COEFFICIENTS_SAME_MINOR_TONALITY, COEFFICIENTS_MODULATION
import sys

VOICE_MAPPING = {
    "Soprano": 3,
    "Alto": 2,
    "Tenor": 1,
    "Bass": 0,
}

class Chromosome:
    """
    In this context, a chromosome is a certain harmonization of the
    input melody that has either been built while initializing the
    population or obtained by crossover/mutation during the
    algorithm's epochs.
    """
    def __init__(self, melody, voice):
        self.melody = melody
        self.voice = voice

        self.keySignature = self.melody.analyze("key")
        key_tonic = str(self.keySignature).split()[0]
        key_mode = str(self.keySignature).split()[1] # Major or minor
        key_scale = None # self.keySignature.getScale()
        if key_mode == "major":
            key_scale = scale.MajorScale(key_tonic)
        elif key_mode == "minor":
            key_scale = scale.MinorScale(key_tonic)
            # key_scale = scale.HarmonicMinorScale(key_tonic)
        else:
            print("Should never happen...")
            sys.exit(1)
        key_scale_pitches = scale.Scale.extractPitchList(key_scale, comparisonAttribute="pitchClass")
        self.diatonic_notes = [scale_pitch.name for scale_pitch in key_scale_pitches]

        self.chords = []

        # Key signatures list (for modulation detection)
        self.chordKeySignatures = []

        self.voice_idx = VOICE_MAPPING[self.voice]

        self.soprano = stream.Part()
        self.soprano.id = "Soprano"
        self.alto = stream.Part()
        self.alto.id = "Alto"
        self.tenor = stream.Part()
        self.tenor.id = "Tenor"
        self.bass = stream.Part()
        self.bass.id = "Bass"

        self.score = stream.Score()
        self.score.append([
            self.soprano,
            self.alto,
            self.tenor,
            self.bass,
        ])


    def harmonize(self):
        """
        Harmonizes input melody by assigning, for each note of the
        input melody, a note to every other part (besides the
        one specified in input) as to create a chord
        """

        measure_num = 1
        measure_offset = 0
        global_note_offset = 0

        for meas in self.melody:
            bass_line = []
            tenor_line = []
            alto_line = []
            soprano_line = []

            for n in meas.notes:
                bass, tenor, alto, soprano = self._get_random_chord(n)

                # Save the notes
                bass_note = n.transpose(bass)
                tenor_note = n.transpose(tenor)
                alto_note = n.transpose(alto)
                soprano_note = n.transpose(soprano)

                #print(measure_num, [bass_note.nameWithOctave, tenor_note.nameWithOctave, alto_note.nameWithOctave, soprano_note.nameWithOctave])

                # Add them to respective lines
                bass_line.append(bass_note)
                tenor_line.append(tenor_note)
                alto_line.append(alto_note)
                soprano_line.append(soprano_note)

                # Also add each chord to chord list
                # self.chords.append((bass_note, tenor_note, alto_note, soprano_note))
                self.chords.append(
                    chord.Chord([
                        bass_note,
                        tenor_note,
                        alto_note,
                        soprano_note,
                    ])
                )


            # For each part-line pair
            for part, line in zip([self.bass, self.tenor, self.alto, self.soprano], [bass_line, tenor_line, alto_line, soprano_line]):
                note_offset = 0
                # Create a new measure
                new_measure = stream.Measure(number=measure_num)

                # Add clef, key signature and time signature objects to first measure
                """
                if measure_num == 1:
                    # clef
                    if part.id == "Bass":
                        part_clef = clef.BassClef()
                    elif part.id == "Tenor":
                        part_clef = clef.TenorClef()
                    elif part.id == "Alto":
                        part_clef = clef.AltoClef()
                    elif part.id == "Soprano":
                        part_clef = clef.SopranoClef()

                    new_measure.insert(offsetOrItemOrList=0, itemOrNone=part_clef)

                    # key signature
                    melody_tonic = str(self.keySignature).split()[0]
                    melody_mode = str(self.keySignature).split()[1]
                    new_measure.insert(offsetOrItemOrList=0, itemOrNone=key.Key(melody_tonic, melody_mode))

                    # time signature
                    new_measure.insert(offsetOrItemOrList=0, itemOrNone=meter.TimeSignature("4/4"))
                """

                # Fill it with the notes from the current line
                for n in line:
                    new_measure.insert(offsetOrItemOrList=global_note_offset + note_offset, itemOrNone=n)
                    note_offset += 1

                # And add it to the current part
                part.insert(offsetOrItemOrList=measure_offset, itemOrNone=new_measure)

            measure_num += 1
            measure_offset += 4
            global_note_offset += 4


    def _check_chord_contains_voice_idx(self, curr_chord):
        return curr_chord[self.voice_idx] == 0 \
            or curr_chord[self.voice_idx] == 12 \
            or curr_chord[self.voice_idx] == -12

    def get_note_num_from_node_str(self, note_str):
        num = 0
        if note_str.lower() == "c":
            num = 0
        if note_str.lower() == "c#":
            num = 1
        if note_str.lower() == "d-":
            num = 1
        if note_str.lower() == "d":
            num = 2
        if note_str.lower() == "d#":
            num = 3
        if note_str.lower() == "e-":
            num = 3
        if note_str.lower() == "e":
            num = 4
        if note_str.lower() == "f":
            num = 5
        if note_str.lower() == "f#":
            num = 6
        if note_str.lower() == "g-":
            num = 6
        if note_str.lower() == "g":
            num = 7
        if note_str.lower() == "g#":
            num = 8
        if note_str.lower() == "a-":
            num = 8
        if note_str.lower() == "a":
            num = 9
        if note_str.lower() == "a#":
            num = 10
        if note_str.lower() == "b-":
            num = 10
        if note_str.lower() == "b":
            num = 11
        return num

    def get_all_available_chords_from_scale(self, notes_str):
        num = 0
        notes = []
        for note_str in notes_str:
            num = self.get_note_num_from_node_str(note_str)
            notes.append(num)
        all_chords = []
        for i in range(len(notes)):
            chord_tria = [
                notes[i],
                notes[(i + 2) % len(notes)],
                notes[(i + 4) % len(notes)],
            ]
            chord_quad = [
                notes[i],
                notes[(i + 2) % len(notes)],
                notes[(i + 4) % len(notes)],
                notes[(i + 6) % len(notes)],
            ]
            all_chords.append(chord_tria)
            all_chords.append(chord_quad)
        # print("#####################")
        # print("notes")
        # print(notes)
        # print("all chords")
        # for x in all_chords:
        #     print(x)
        # TODO: Use circulant matrix
        alls_inversions = []
        for chord in all_chords:
            if len(chord) == 3:
                alls = [
                    [
                        chord[0],
                        chord[1],
                        chord[2],
                        chord[0],
                    ],
                    [
                        chord[0],
                        chord[1],
                        chord[2],
                        chord[1],
                    ],
                    [
                        chord[0],
                        chord[1],
                        chord[2],
                        chord[2],
                    ],
                ]
            else:
                alls = [chord]
            for x in alls:
                alls_inversions.extend([
                    [
                        x[0],
                        x[1],
                        x[2],
                        x[3],
                    ],
                    [
                        x[1],
                        x[2],
                        x[3],
                        x[0],
                    ],
                    [
                        x[2],
                        x[3],
                        x[0],
                        x[1],
                    ],
                    [
                        x[3],
                        x[0],
                        x[1],
                        x[2],
                    ],
                ])
            # TODO: Keep going from here...
            # Se sono tre: raddoppio di tutte le note per avere lista quattro
            # Hai lista quattro: rivolti (all possible rounds)
        # print("all inversions")
        # for x in alls_inversions:
        #     print(x)
        # print()

    def _get_available_chords(self, note):
        available_chords = []

        note_str = note.pitch.name
        key_str = str(self.keySignature)

        # If note n is diatonic, choose a random chord that contains it among diatonic ones
        # Load note chord atlas
        note_chord_atlas_path = os.path.join(".\\utility\\chord_atlases", note_str + "_chord_atlas.json")
        with open(note_chord_atlas_path, "r") as file:
            note_chord_atlas = json.load(file)

        # Pick a randon chord containing the note
        if note_str in self.diatonic_notes:
            # Diatonic note
            for curr_chord in note_chord_atlas[key_str]:
                if self._check_chord_contains_voice_idx(curr_chord):
                    available_chords.append((curr_chord, self.keySignature))
            # TODO: Use this instead of calculated files
            self.get_all_available_chords_from_scale(self.diatonic_notes)
            # if note_str == "C":
            #     print("###################")
            #     for x in available_chords:
            #         print(x)
            #     print("###################")
        else:
            # Non-diatonic note
            for key_signature in KEY_SIGNATURES:
                for curr_chord in note_chord_atlas[key_signature]:
                    if self._check_chord_contains_voice_idx(curr_chord):
                        key_tonic, key_mode = key_signature.split(" ")
                        key_obj = key.Key(key_tonic, key_mode)
                        available_chords.append((curr_chord, key_obj))

        return available_chords

    def _get_random_chord(self, note):
        available_chords = self._get_available_chords(note)
        chosen_chord, chosen_chord_key = random.choice(available_chords)
        self.chordKeySignatures.append(chosen_chord_key)
        # print(f"chosen_chord: {chosen_chord}, chosen_chord_key: {chosen_chord_key}")
        return (*chosen_chord, )


    def _get_harmonic_value_same_key(self, curr_chord, next_chord, curr_key):
        curr_key_mode = str(curr_key).split()[1]
        weights_dict = WEIGHTS_SAME_MAJOR_TONALITY if curr_key_mode == "major" else WEIGHTS_SAME_MINOR_TONALITY
        coefs_dict = COEFFICIENTS_SAME_MAJOR_TONALITY if curr_key_mode == "major" else COEFFICIENTS_SAME_MINOR_TONALITY

        print(curr_chord, next_chord)
        weix = weights_dict[curr_chord]
        print(weix)

        w_i = weix[next_chord]
        a_i = coefs_dict[curr_chord][next_chord]
        print(w_i, a_i)

    def _get_harmonic_value_modulation(curr_chord, next_chord, curr_key):
        pass

    def _harmonic_evaluation(self):
        evaluation = 0
        for i in range(len(self.chords)-1):
            curr_chord = self.chords[i]
            next_chord = self.chords[i + 1]

            curr_key = self.chordKeySignatures[i]
            next_key = self.chordKeySignatures[i + 1]

            curr_degree = roman.romanNumeralFromChord(curr_chord, curr_key).romanNumeralAlone
            next_degree = roman.romanNumeralFromChord(next_chord, curr_key).romanNumeralAlone

            # Same key
            if curr_key == next_key:
                print(f"curr_chord: {curr_chord}, curr_key: {curr_key}")
                print(f"next_chord: {next_chord}, next_key: {next_key}")
                self._get_harmonic_value_same_key(curr_degree, next_degree, curr_key)

            # Different key (modulation)
            else:
                print("c1 and c2 are in different keys")

            print()
        return evaluation


    def _melodic_evaluation(self):
        evaluation = 0
        return evaluation


    def _evaluate(self):
        eval_harmonic = self._harmonic_evaluation()
        eval_melodic = self._melodic_evaluation()
        return (
            eval_harmonic,
            eval_melodic,
        )
