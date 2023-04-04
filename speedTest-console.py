import speedtest
import os

print("Measuring speed...")
print("please wait...")

servers = []
threads = 1

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()

downResult   = str(s.download(threads=threads) / 8 / 1024/ 1024)
uploadResult = str(s.upload(threads=threads) / 8 / 1024/ 1024)

print("Done!")

print( "Download: " + downResult + " | " + "Upload:" + uploadResult) 
