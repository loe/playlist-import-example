#!/usr/bin/env python

PLAYLIST_NAMES=["My Top Rated"] # Supports a list
PLAYLIST_DESCRIPTION="Imported from iTunes"

import sys, logging
from playlistcreator import PlaylistCreator
from ScriptingBridge import *

pc = PlaylistCreator()
if not pc.authenticated:
  print 'You need to authenticate by running ./authenticate.py first'
  sys.exit(0)

logging.basicConfig(level=logging.WARNING)

for playlist_name in PLAYLIST_NAMES:
  itunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
  playlist = itunes.sources()[0].playlists().objectWithName_(playlist_name)
  itunes_tracks = playlist.tracks()
  rdio_tracks = []
  for track in itunes_tracks:
    #logging.info("%s - %s" % (track.artist().encode("ascii", "replace"), track.name().encode("ascii", "replace")))
    rdio_tracks.append((track.artist(),track.name()))

  if rdio_tracks:
    pc.make_playlist(playlist_name, PLAYLIST_DESCRIPTION, rdio_tracks)

