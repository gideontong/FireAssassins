# Fire Assassins

As a side note, this project has now been deprecated. You can still download and browse the code, but it is no longer being maintained. If you'd like to submit a pull request, it'll be reviewed and accepted, but the code should continue to work as is, given the docs.

You can visit Gideon Tong's homepage [here](https://gideontong.com), his GitHub page [here](https://www.github.com/gideontong), or download the repository for Fire Assassins [here](https://www.github.com/gideontong/FireAssassins).

## What is water assassins? 

Water assassins is a game played by many high schools where people are given targets that they must eliminate in order to progress to the next round. The variant played by Westlake High School's class of 2019 involved teams of 5 that were given random target lists that were also of 5 players. With 320 people playing and a $10 entrance fee, the prize pool was $3,200 and is split 7 ways, between the winning team and the two organizers. The rules are given in a "constitution" of sorts and the targets were distributed via Instagram, where minigames and kills were also announced, as well as other pertinent information related to the game.

## Backstory

The [target list randomizer](CreateTargets.py) was written by Ethan O., a person who also participated in playing water assassins, thus raising suspicions that he may have cheated in writing the program in order to give himself or his team an advantage. As a result, the organizers posted the code in a video on an Instagram story, leading [Gideon Tong](https://www.github.com/gideontong) to realize that it may be possible to actually find the original target list. Thus, this code repository was created, a name based on the idea that this was uncharted territory and he was "playing with fire" as he tried to gain himself an advantage in a real-world game by using knowledge of computer systems.

This idea was developed in the first 48 hours of the game by Gideon Tong, who therorized it must be possible to reverse the order of a pseudo-random generator, even if it were not to be simple or trivial. However, it is believed that the process of doing so is trivial, and is a brute force attack in its worse case scenario.

## Technical Explanation

There is no such thing as randomness, and as a result, the random library in Python uses the [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister) in order to generate pseudo-random numbers. However, there are some repositories that already exist that can predict the next value of the Mersenne Twister, and thus the original sequence and key [given a certain n values from the sequence](https://github.com/fx5/not_random). Of course, to some extent, the Mersenne Twister will pass the series of [diehard tests](https://en.wikipedia.org/wiki/Diehard_tests) but we must consider that the published code contains the list of teams and members hardcoded in, which means that no randomness is invovled in the original sequence. In fact, we do not have to infer the order of the original sequence, we are given in.

We also know other things, like the fact that the order is a permutation given in an array, as well as what Python function was used to generate it. We also know 5 targets that we were given, meaning that we should be able to accurately predict five values, or a combination thereof (if we cannot assume its order) from the target list we have. In addition, we know the targets that other teams have if other teams share it with us or if they get a kill and it is announced on Instagram. Therefore, with each successive amount of data we gain, although we are losing time to solve the rest of the array, we also decrease the amount of entropy left to predict the rest of the targets.

Assuming we use the worst case scenario (but also the easiest one to write a program for), we must brute force the generator. However, we know that the seed for the generator, if left blank, is the current time the program is run. Therefore, we can infer based on social media clues as well as the time we were given our target list the time range that the list of teams was generated, thus decreasing the amount of entropy and limiting the target space for the search area of the seed that we are looking for.