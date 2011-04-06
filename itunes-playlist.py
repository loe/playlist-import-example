#!/usr/bin/env python

PLAYLIST_NAME="My Top Rated"
PLAYLIST_DESCRIPTION="Imported from iTunes"

import sys, logging
from playlistcreator import PlaylistCreator
pc = PlaylistCreator()
if not pc.authenticated:
  print 'You need to authenticate by running ./authenticate.py first'
  sys.exit(0)

logging.basicConfig(level=logging.WARNING)


from ScriptingBridge import *
itunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
playlist = itunes.sources()[0].playlists().objectWithName_(PLAYLIST_NAME)
itunes_tracks = playlist.tracks()
rdio_tracks = []
for track in itunes_tracks:
    #logging.info("%s - %s" % (track.artist().encode("ascii", "replace"), track.name().encode("ascii", "replace")))
    rdio_tracks.append((track.artist(),track.name()))

pc.make_playlist(PLAYLIST_NAME, PLAYLIST_DESCRIPTION, rdio_tracks)
