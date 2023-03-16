import plistlib
import numpy as np
import matplotlib.pyplot as pyplot

fileNameExample = "Aests.xml"

def processXML(fileName):

    with open(fileName, "rb") as file:
        plist = plistlib.load(file)

    print("Finding duplicates in %s..." %fileName)

    tracks = plist['Tracks']
    trackNames = []
    playCount = []
    durations = []

    for trackID, track in tracks.items():
        try:
            trackNames.append(track['Name'])
            playCount.append(track ['Play Count'])
            durations.append(track['Total Time'])

        except:
            print("Big No No NO ")
            pass

        if playCount == []:
            print("No valid Plays Counts/Total Time data in %s." % fileName)
            return

    #Scatter Plot
    x = np.array(durations, np.int32)
    # convert to minutes
    x = x/60000.0
    y = np.array(playCount, np.int32)

    pyplot.subplot(2, 1, 1)
    pyplot.plot(x, y, 'o')
    pyplot.axis([0, 1.05 * np.max(x), -1, 110])

    pyplot.xlabel("Durations")
    pyplot.ylabel("Play Counts")

    #Histogram
    pyplot.subplot(2,1,2)
    pyplot.hist(x, bins=20)

    pyplot.xlabel("Durations")
    pyplot.ylabel("Play Counts")

    pyplot.show()

processXML(fileNameExample)



