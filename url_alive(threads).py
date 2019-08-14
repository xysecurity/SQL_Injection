import socket
import asyncio
import sys
import queue
import threading
import requests
iplist=[]
class socket1():
	def __init__(self,i):
		self.i=i

		# print(target)
		

	def scan(self,ip,i):
		# print("start scan")

		# print(s.connect_ex((self.target,80)))
		# for i in range(1,100):
			# print(i)
		s=requests.get(ip,timeout=6)
		
		if s.status_code==200:
			# print(ip,'open')
			iplist.append(ip)


			
	def worker(self,q):
		while not q.empty():
			ip=str(q.get())
			if ('http' or 'https') in ip:
				ip=ip
			else:
				ip='http://'+ip
			print(ip)
			try:
				self.scan(ip,self.i)
			finally:
				q.task_done()
	# def main(self):
	# 	print("start to detect ",self.target)
	# 	loop=asyncio.get_event_loop()
	# 	tasks=[asyncio.ensure_future(self.scan(port)) for port in range(1,65536)]
	# 	loop.run_until_complete(asyncio.wait(tasks))
if __name__ == '__main__':
	print("Start testing the target port")
	# print("Example:['127.0.0.1','127.0.0.2'] 80")
	filename='ipsuccess.txt'
	q=queue.Queue()
	a=socket1(80)
	with open(filename,'rb') as f:
		for line in f.readlines():
			# print(line.decode()[:-2])
			q.put(line.decode()[:-2])
	# iplist=[]


	# for i in range(65535):
	# 	print(q.get())
	threads=[threading.Thread(target=a.worker,args=(q,)) for i in range(200)]
	list(map(lambda x:x.start(),threads))
	q.join()

	print("scan over")
	print(iplist)
	with open('ipsuccess.txt','w',encoding='utf-8') as f:
		for i in iplist:
			f.write(i+'\n')

	

	
	# for i in sys.argv:
	# 	iplist.append(i)
	# del iplist[0]
	# print(iplist)
	# port=int(sys.argv[1])
	# del iplist[-1]
	# print(port)
	
	# a.scan(80)
	# for i in range(1,100):
	# 	a.scan(i)
	

