import sys
import httplib
import urllib
import urllib2
import cookielib


def main():
    cj=cookielib.CookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 6.1; rv:29.0) Gecko/20100101 Firefox/29.0')]
    urllib2.install_opener(opener)

    #req = urllib2.Request("http://vote.jyb.cn/capa.php",urllib.urlencode({'act':'act'}))
    req = urllib2.Request("http://vote.jyb.cn/capa.php?act=act")
    req.add_header("Referer","http://vote.jyb.cn/vote2014jsyrkm.html")

    try:
        resp = urllib2.urlopen(req, timeout=10000)

        for index, cookie in enumerate(cj):
            cap=cookie

            #print word
            # print '[',index, ']';
    except Exception,e:
        print "time out here"


if __name__ == "__main__":
    main()

