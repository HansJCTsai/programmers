# Best Album

Source: [Programmers - Best Album](https://programmers.co.kr/learn/courses/30/lessons/42579)

---

## Problem

A music streaming service wants to release a “best album” that contains the most popular songs, selected by genre.  
Each song is identified by a unique number, and the selection rules are:

1. Genres with a higher total play count come first.  
2. Within a genre, songs with more plays come first.  
3. If two songs within a genre have the same play count, the one with the smaller ID comes first.  
4. For each genre, pick up to two songs.  

### Constraints
- `genres[i]` is the genre of song `i`.  
- `plays[i]` is the number of plays for song `i`.  
- `genres` and `plays` have the same length, between 1 and 10,000.  
- The number of distinct genres is less than 100.  
- If a genre has only one song, include just that one.  
- The total play counts of different genres are all distinct.  

### Example

| genres | plays | return |
|--------|-------|--------|
| [classic, pop, classic, classic, pop] | [500, 600, 150, 800, 2500] | [4, 1, 3, 0] |

**Explanation:**

- The `classic` genre has 1,450 plays in total:  
  - ID 3: 800 plays  
  - ID 0: 500 plays  
  - ID 2: 150 plays  

- The `pop` genre has 3,100 plays in total:  
  - ID 4: 2,500 plays  
  - ID 1: 600 plays  

So the final best album is `[4, 1, 3, 0]`.

---

## Explanation

We can use a **hash map** to group songs by genre and then reorder them according to the given rules.  

- Genres are sorted by the **total play count** of all songs they contain (descending).  
- Songs within a genre are sorted by **play count** (descending), and if tied, by **song ID** (ascending).  
