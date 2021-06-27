# Testing

## Unit testing 

### Tested thing

    - unittesting has been done for both data structures
    - also some functions have been tested for their base case, otherwise due to randomness/creation of files have been left untested due to difficulty of testing

### Coverage

![Coverage](/pictures/coverage_final.png)

## Rightness of Output

### Methodology

 - Tested by listening to the output by ear, placing emphasis on these charecteristics
    - Quality: Does it sound good?
    - Originality: Does the created piece sound different enough from the training data
 - These charesteristics were given a grade from 1 to 10
    - For quality this means that 1 is a horrid mess that cannot be considered music, 5 is something that doesn't sound repulsive and could be considered musical and 10 is something that could be considered to be produced by an actual musician
    - For Originality 1, is a copy of a training piece, 5 has a parts of the training data (different pieces) but also has some originality, and 10 is something not closely related to the training data but can sound similar
 - These charesteristics were tested by creating 4 sets with different degrees of markov chains, with three pieces for each degree, the degrees were 2, 4, 6, and 8

### 2nd degree
 
 - Quality
    - The created pieces seem detached and chaotic, for this reason the quality can be considered poor, but not worse as there is some harmony 2/10
 - Originality
    - They seemed to work as part chaotic part like a scale pratice for this reason the originality score is 9/10
 - General
    - Alltought there was some harmony the pieces themselves seemed a bit chaotic and directionless, also the first had a duration of over 24 minutes

### 4th degree

 - Quality
    - There still exist some chaotic parts but there is greater harmony and the pieces seem more structured hence a score 4/10
 - Originality
    - Part chaotic and did not sound like the training data hence score 9/10
 - General
    - More direction and better harmony seems like an improvement


### 6th degree

 - Quality
    - As expected some chaos exist in the pieces but harmony and melodies have somewhat imporved compared to 4th degree, score is 6/10
 - Originality
    - Some recognizable parts have emerged, meaning some originality has been lost hence the score is 8/10
 - General
    - More direction and better harmony seems like an improvement (same as transition from 3rd to 4th degree)

### 8th degree

 - Quality
    - Compared to 6th degree the quality has greatly increased and number of harmonic melodies ha grown, score is 7/10
 - Originality
    - Some recognizable parts have emerged, meaning some originality has been lost more tha in the 6th degree hence the scoreis 7/10
 - General
    - Good direction and harmony, only the mediocer time creation holds the pieces back

## Results analysis

Results are as expected, the quality tends to increase with the degree but originality suffers 

(The test files are the current files in the created directory in from TestXDegreeY.midi)