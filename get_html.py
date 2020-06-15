"""gets a list of comma delimited urls as an input from a Jenkins job
and, loops over each url and prints the HTML of that url."""
import sys
import urllib.request

if __name__ == "__main__":
    urls = sys.argv[1]
    for u in urls.split(","):
        print(u)
        try:
            req = urllib.request.urlopen(u).read()
            print(req)
        except ValueError:
            print("There is an error when parsing html")
            sys.exit(0)

