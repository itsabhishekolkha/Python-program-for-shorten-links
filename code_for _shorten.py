#code to shorten link by abhishek olkha
import pyshorteners
link=input("enter the link you want to short")
short=pyshorteners.Shortener()
url=short.tinyurl.short(link)
print("\nShorted link is:",url)