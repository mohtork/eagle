import psutil
import os
import db
import socket

class Resources():
	def hostname(self):
        	self.hostname=(socket.gethostname())
        	return self.hostname

	def ListPartitions(self):
		self.partitions_list = []
		self.path_list = []
		partitions = psutil.disk_partitions()
		for partition in partitions:
			self.partitions_list.append(partition[1])
		return self.partitions_list

	def PartitionUsage(self, partitions):
		self.partition = []
		self.total= []
                self.used = []
		self.free = []
                self.percent = []
		for partition in partitions:
			usage = psutil.disk_usage(partition)
			total , used , free , percent = usage
			self.partition.append(partition)
			self.total.append(total // (2**30))
			self.used.append(used // (2**30))
			self.free.append(free // (2**30))
			self.percent.append(percent)
			
			
		return self.partition, self.total, self.used, self.free , self.percent

	def MapDiskUsage(self):
		MapUsage = self.PartitionUsage(self.ListPartitions())
		Dict = {}
		y=0
		self.disk, self.total , self.used, self.free, self.percent = MapUsage[0], MapUsage[1], MapUsage[2], MapUsage[3],  MapUsage[4]
		Dict = dict(zip(self.disk, zip(self.total, self.used, self.free, self.percent)))
		return Dict		
		
	def MemoryUsage(self):
		memory=psutil.virtual_memory()
		meminfo={}
		meminfo['total']=memory.total/1024/1024
		meminfo['available']=memory.available/1024/1024
		meminfo['used']=memory.used/1024/1024
		meminfo['free']=memory.free/1024/1024
		meminfo['percent']=memory.percent
		meminfo['buffers']=memory.buffers/1024/1024
		meminfo['cached']=memory.cached/1024/1024
		meminfo['active']=memory.active/1024/1024
		meminfo['inactive']=memory.inactive/1024/1024
		return meminfo

	def Swap(self):
		swap=psutil.swap_memory()
		swapinfo={}
		swapinfo['total']=swap.total/1024/1024
		swapinfo['used']=swap.used/1024/1024
		swapinfo['free']=swap.free/1024/1024
		swapinfo['percent']=swap.percent
		return swapinfo
			
	def LoadAvarage(self, interval):
		self.interval=interval
		return os.getloadavg()[interval]


x = Resources()

