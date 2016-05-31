import wget
import sys
import urllib

form = list()
dlink = list()

class GNUDollect():
        def __init__(self, base, program):
                self.base = base
                self.program = program

        def Pownload(self):
                global html
                global info
                global text
                global dvi
                global pdf
                global texi
                html = self.base + self.program + "/manual/" + self.program + ".html"
                info = self.base + self.program + "/manual/" + self.program + "-info.tar.gz"
                text = self.base + self.program + "/manual/" + self.program + ".txt"
                dvi  = self.base + self.program + "/manual/" + self.program + ".dvi.gz"
                pdf  = self.base + self.program + "/manual/" + self.program + ".pdf"
                texi = self.base + self.program + "/manual/" + self.program + ".texi.tar.gz"
                form = ['html','info','ascii','dvi','pdf','texi']
                dlink = [html, info, text, dvi, pdf, texi]
                print "[html/info/ascii/dvi/pdf/texi/all]"
                selection = raw_input()
                if selection == "all":
                        for name in xrange(6):
                                filename = wget.download(dlink[name])
                        print "\n"
                       # sys.exit(0)
                else:
                        print "helloo"
                        for name in xrange(6):
                                if selection == form[name]:
                                        print dlink[name]
                                        filename = wget.download(dlink[name])
                                        print "\n"
          		            
			        
  

#data = GNUDollect("http://www.gnu.org/software/", "mdk")
#dict = GNUDollect("http://puszcza.gnu.org.ua/software/", "dico")

#data.Pownload()
#dict.Pownload()
#data.Pownload()

def connectivity():
        check = "https://www.google.co.in"
        print "Internet Connectivity.........",
        try:
            data = urllib.urlopen(check)
            print "Available"
        except:
            print "Failed\n"
            sys.exit(0)



def archiving(formataccept):
        print "[Cpio/Gzip/Paxutils/Sharutils/Tar/Xorriso]"
        selection = raw_input()
        program = selection.lower()
        archive = GNUDollect("http://www.gnu.org/software/", program)
	archive.Pownload()



if len(sys.argv) > 1:
    if sys.argv[1] == "lv" and len(sys.argv) == 3:
        if int(sys.argv[2]) <= 9:
#            print "hello"
            i = int(sys.argv[2])
            connectivity()
            lva()
            sys.exit(0)
        elif int(sys.argv[2]) <= 18:
            #debug
            i = int(sys.argv[2])
            connectivity()
            lvb()
            sys.exit(0)
    elif sys.argv[1] == "oreilly":
        connectivity()
        selection = raw_input('programming/data \n')
        oreilly(selection)
        
    elif sys.argv[1] == "tldp":
        connectivity()
        tldp()
        
    elif sys.argv[1] == "floss":
        connectivity()
        floss()

    elif sys.argv[1] == "links":
        connectivity()
        links()
        
    elif sys.argv[1] == "gcc":
        connectivity()
        gcc()

    elif sys.argv[1] == "gdb":
        connectivity()
        gdb()
        
    elif sys.argv[1] == "archiving":
#        print "hello"
        connectivity()
        archiving("NULL")

    elif sys.argv[1] == "audio":
        connectivity()
        audio("NULL")

    elif sys.argv[1] == "database":
        connectivity()
        database()

    elif sys.argv[1] == "dictionaries":
        connectivity()
        dictionaries()

    elif sys.argv[1] == "doculation":
        connectivity()
        doculation()

    elif sys.argv[1] == "editor":
        connectivity()
        editor()
        
    elif sys.argv[1] == "education":
        connectivity()
        education()
        
    elif sys.argv[1] == "email":
        connectivity()
        email()

    elif sys.argv[1] == "font":
        connectivity()
        font()

    elif sys.argv[1] == "organization":
        connectivity()
        organization()

    elif sys.argv[1] == "game":
        connectivity()
        game()

    elif sys.argv[1] == "graphics":
        connectivity()
        graphics()

    elif sys.argv[1] == "health":
        connectivity()
        health()

    elif sys.argv[1] == "alltext":
        connectivity()
        alltext()
        
    else:
        print "\n LINUXVOICE COMPLETE \n"
        for i in xrange(18):
            if i == 0:
                continue
            if i <= 9:
                connectivity()
                lva()
            else:
                connectivity()
                lvb()

