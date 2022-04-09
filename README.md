Sphinx gettext bug with napoleon
=================================

This repo demonstrates a bug with gettext+napoleon on Sphinx.

When a directive is included within parameter/return signatures that get processed by napoleon, it confuses gettext and makes the result untranslatable.

Running
```bash
cd docs
PYTHONPATH=$(cd .. && pwd) make html
```
or
```powershell
$env:PYTHONPATH="$(pwd)"; docs/make html
```

produces .pot files that contain these, derived with autodoc from the [module](foobar/__init__.py):

```
#: ../../../foobar/__init__.py:docstring of foobar.documented_function:3
msgid "Whether the duck should be small or not.  .. warning::     This duck is very small."
msgstr ""

#: ../../../foobar/__init__.py:docstring of foobar.documented_function:3
msgid "Whether the duck should be small or not."
msgstr ""

#: ../../../foobar/__init__.py:docstring of foobar.documented_function:6
msgid "This duck is very small."
msgstr ""
```
```
#: ../../../foobar/__init__.py:docstring of foobar.documented_function:9
msgid "A nice `picture of a duck`__.  .. _picture_of_a_duck: https://upload.wikimedia.org/wikipedia/commons/5/51/Mandarin.duck.arp.jpg __ picture_of_a_duck_"
msgstr ""

#: ../../../foobar/__init__.py:docstring of foobar.documented_function:9
msgid "A nice `picture of a duck`__."
msgstr ""
```

Despite both the 'unclean' and 'clean' versions both being present, only the first (unclean) version actually gets used, making these strings untranslatable as anything other than removing the directives either results in them appearing in the resulting document 'as is' (e.g. not parsed), or Sphinx kicking out an error.
