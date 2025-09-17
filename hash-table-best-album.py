def solution(genres, plays):    
    answer = []
    genre_total = {}
    genre_songs = {}
  
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total[g] = genre_total.get(g, 0) + p
        genre_songs.setdefault(g, []).append((p, i))
      
    for g in sorted(genre_total, key=genre_total.get, reverse=True):
        songs = sorted(genre_songs[g], key=lambda x: (-x[0], x[1]))
        answer.extend([i for _, i in songs[:2]])

    return answer
