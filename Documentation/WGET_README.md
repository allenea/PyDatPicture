https://bitbucket.org/techtonik/python-wget/src


This (Python-WGET-Master) is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

----------------------------------------------------------------------------- 

Usage
=====
'''
  python -m wget [options] <URL>

  options:
    -o --output FILE|DIR   output filename or directory
'''

API Usage
=========
'''
  >>> import wget
  >>> url = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3'
  >>> filename = wget.download(url)
  100% [................................................] 3841532 / 3841532>
  >> filename
  'razorback.mp3'
'''
The skew that you see above is a documented side effect.
Alternative progress bar:

  >>> wget.download(url, bar=bar_thermometer)


## ChangeLog
============
2.2 (2014-07-19)
 * it again can download without -o option

2.1 (2014-07-10)
 * it shows command line help
 * -o option allows to select output file/directory

   * download(url, out, bar) contains out parameter

2.0 (2013-04-26)
 * it shows percentage
 * it has usage examples
 * it changes if being used as a library

   * download shows progress bar by default
   * bar_adaptive gets improved algorithm
   * download(url, bar) contains bar parameter
     * bar(current, total)
   * progress_callback is named callback_progress

1.0 (2012-11-13)
 * it runs with Python 3

0.9 (2012-11-13)
 * it renames file if it already exists
 * it can be used as a library

   * download(url) returns filename
   * bar_adaptive() draws progress bar
   * bar_thermometer() simplified bar

0.8 (2011-05-03)
 * it detects filename from HTTP headers

0.7 (2011-03-01)
 * compatibility fix for Python 2.5
 * limit width of progress bar to 100 chars

0.6 (2010-04-24)
 * it detects console width on POSIX

0.5 (2010-04-23)
 * it detects console width on Windows

0.4 (2010-04-15)
 * it shows cute progress bar

0.3 (2010-04-05)
 * it creates temp file in current dir

0.2 (2010-02-16)
 * it tries to detect filename from URL

0.1 (2010-02-04)
 * it can download file


Release Checklist
=================

| [ ] update version in wget.py
| [x] update description in setup.py
| [ ] python setup.py check -mrs
| [ ] python setup.py sdist upload
| [ ] tag hg version

-- 
anatoly techtonik <techtonik@gmail.com>
