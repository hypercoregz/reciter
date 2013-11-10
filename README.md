#reciter
Provides a simple way to recite or dictate.

##License

MIT License.

##Features

* [√] Recite with infinite turns.
* [√] Only recite things you were answered wrong until you've fully mastered them.
* [ ] Show the correct answer under your answer (default) or not.
* [√] Recite reversely or randomly. Your favor!
* [√] Fully supports UTF-8.
* [ ] Error handling on the way.

##Usage

reciter.py [-h] [-r] [-R] file

* `-h` *show the help text*
* `file` *the dictionary you want to recite (format: see below)*
* `-r` *reversely recite (ignored when using with "-R")*
* `-R` *randomly recite*

##File Format

* type: plain text
* extension: anything
* format: `word meaning`
* example:
<pre>
apologize thank
inform tell
candy sweet
lecture speech
</pre>
