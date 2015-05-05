# firefox2pass.py

This script migrates passwords from Firefox to
[pass](http://passwordstore.org/), in a format that is readable by
[passff](https://github.com/jvenant/passff).

1. Install [Password Exporter](https://addons.mozilla.org/de/firefox/addon/password-exporter/).
2. Go to its settings and export as CSV.
3. Run `python firefox2pass.py exported.csv`.

Licensed under the public domain.

## Contribution

I'm unlikely to ever use this script again, so only bugfixes are accepted. If
you want to add extra features, you'll have to maintain those yourself (I'll
give you commit rights for this repo).
