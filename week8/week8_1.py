playlist = [
    ("Bad Guy", "Billie Eilish", 194),
    ("Peaches", "Justin Bieber", 198),
    ("Attention", "NewJeans", 168),
    ("Poker Face", "Lady Gaga", 235),
    ("Love Story", "Taylor Swift", 231),
    ("Happier Than Ever", "Billie Eilish", 298),
    ("Stay", "Justin Bieber", 141),
    ("Hype Boy", "NewJeans", 178),
    ("Bad Romance", "Lady Gaga", 295),
    ("Anti-Hero", "Taylor Swift", 200),
    ("September", "Earth, Wind & Fire", 215),
    ("I Love You So", "The Walters", 178),
    ("IRIS OUT", "Kenshi Yonezu", 152),
    ("Just the Two of Us", "Bill Withers", 232),
    ("Don’t Look Back in Anger", "Oasis", 278),
    ("OMG", "NewJeans", 213),
    ("Bad Guy", "Billie Eilish", 194),
    ("Peaches", "Justin Bieber", 198),
    ("Love Story", "Taylor Swift", 231),
    ("IRIS OUT", "Kenshi Yonezu", 152),
    ("OMG", "NewJeans", 213),]

playlist = list(set((title, artist, sec) for title, artist, sec in playlist))

playlist.sort(key=lambda x: (x[1], x[0]))

print(f"{'title':25} {'artist':25} {'sec':>10}")
print("-" * 65)
for title, artist, sec in playlist:
    print(f"{artist:25} {title:25} {sec:>10}")
print()    
prev_artist = None

print(f"{'title':25} {'artist':25} {'sec':>10}")
print("-" * 65)
for title, artist, sec in playlist:
    if artist != prev_artist and prev_artist is not None:
        print()  
    print(f"{artist:25} {title:25} {sec:>10}")
    prev_artist = artist

total_sec = 0
for title, artist, sec in playlist:
    total_sec += sec
total_hours = total_sec // 3600
total_minutes = (total_sec % 3600) // 60
total_seconds = total_sec % 60
total_time = f"{total_hours}:{total_minutes:02d}:{total_seconds:02d}"
print(f"Total Duration:{total_time}")