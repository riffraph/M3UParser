import sys

class track():
    def __init__(self, length, title):
        self.length = length
        self.title = title

# # # song info lines are formatted like:
#EXTINF:419,Alice In Chains - Rotten Apple
# length (seconds), Song title
# # # file name - relative or absolute path of file
# ..\Minus The Bear - Planet of Ice\Minus The Bear_Planet of Ice_01_Burying Luck.mp3
def parseM3U(infile):
    print(infile)

    playlist = []
    song = track(None,None)

    checkedFormat = False
    with open(infile) as f:
        for line in f:
            line=line.strip()
            # check file format
            if not checkedFormat and line.startswith('#EXTM3U'):
                checkedFormat = True
            elif not checkedFormat:
                print("invalid file format")
                return 
            elif line.startswith('#EXTINF:'):
                # pull length and title from #EXTINF line
                length,title=line.split('#EXTINF:')[1].split(',',1)
                song = track(length, title)
                playlist.append(song);

    return playlist

# get the playlist file path from the first command line argument
def main():
    m3ufile=sys.argv[1]
    playlist = parseM3U(m3ufile)
    if playlist:
        for track in playlist:
            print(track.title)

if __name__ == '__main__':
    main()

