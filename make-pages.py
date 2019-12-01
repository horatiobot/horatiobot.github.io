#!/usr/bin/env python

import sys

def main():
    args = sys.argv[1:]

    if len(args) < 2:
        print "usage: make-pages.py [-n] <n-pages> <n-links-per-page>"
        return

    dry_run = False
    if args[0] == '-n':
        print '*** Dry run'
        dry_run = True
        args = args[1:]

    n_pages = int(args[0])
    n_links_per_page = int(args[1])

    # On December 1, these links were 1/1, 1/5, 2/1, 2/4, 2/6, 3/3 (page/place on page) from Google search of "ukraine server"

    link_to = ['https://www.wired.com/story/trump-ukraine-server-delusion-spreading/',
               'https://www.washingtonpost.com/outlook/2019/11/25/trumps-conspiracy-theory-about-server-threatens-election-security/',
               'https://www.cbsnews.com/news/senator-john-kennedy-says-he-was-wrong-to-say-ukraine-may-have-hacked-dnc-server/',
               'https://www.thedailybeast.com/gop-sen-john-kennedy-i-was-wrong-to-say-ukraine-may-have-hacked-dnc-server',
               'https://www.factcheck.org/2019/11/trump-repeats-false-ukraine-claims/',
               'https://www.cnn.com/videos/tv/2019/11/22/lead-kaitlan-collins-dnt-live-jake-tapper.cnn']

    page = '<html>\n<head>\n<title>\na page\n</title></head>\n<body>'
    for ilink in range(0, n_links_per_page):
        for link in link_to:
            page += '\n<a href="' + link + '">' + link + '</a><br/>'
    for ilink in range(0, n_pages):
        page += '\n<a href="page' + str(ilink) + '.html">page ' + str(ilink) + '</a><br/>'
    page += '\n</body>\n</html>\n'

    if dry_run:
        print page
    else:
        for ipage in range(0, n_pages):
            f = open('page' + str(ipage) + '.html', 'w')
            f.write(page)
            f.close()

main()
