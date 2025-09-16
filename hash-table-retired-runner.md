# Find the Participant Who Did Not Finish

**Source:** [https://programmers.co.kr/learn/courses/30/lessons/42576](https://programmers.co.kr/learn/courses/30/lessons/42576)

## Problem Description

Numerous runners have participated in a marathon. However, exactly one runner did not finish the race.

You are given two string arrays: `participant` and `completion`. The `participant` array contains the names of the runners who joined the race, and the `completion` array contains the names of those who finished.

Your task is to write a `solution` function that returns the name of the participant who did not complete the marathon.

## Constraints

- The number of participants will be between 1 and 100,000, inclusive.
- The length of the `completion` array is always one less than the length of the `participant` array.
- Participant names are composed of 1 to 20 lowercase English letters.
- Participants may share the same name.

## Input/Output Examples

| `participant`                                         | `completion`                               | `return`   |
| :---------------------------------------------------- | :----------------------------------------- | :--------- |
| `["leo", "kiki", "eden"]`                             | `["eden", "kiki"]`                         | `"leo"`    |
| `["marina", "josipa", "nikola", "vinko", "filipa"]`   | `["josipa", "filipa", "marina", "nikola"]` | `"vinko"`  |
| `["mislav", "stanko", "mislav", "ana"]`               | `["stanko", "ana", "mislav"]`              | `"mislav"` |

## Explanation of Examples

- **Example #1**
  "leo" is in the `participant` list but not in the `completion` list, which means he did not finish.

- **Example #2**
  "vinko" is in the `participant` list but not in the `completion` list, which means he did not finish.

- **Example #3**
  There are two participants named "mislav" in the `participant` list, but only one in the `completion` list. This means one of the participants named "mislav" did not finish the race.
