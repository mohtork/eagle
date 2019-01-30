#!/usr/bin/python
from datetime import datetime
import socket
import time
import os

from tools import resources as res
from tools import domain as do
from tools import db
import config as cf
import messages as msg
import alerts as alert



x = res.Resources()
hostname=(socket.gethostname())
date=time.time()
today=datetime.now()
hour=today.hour
minute=today.minute
sslValidate_cron=str(hour)+":"+str(minute)
ssl_schedule=cf.yamls['ssl_validate']['job_time']


def GetDisks():
	values=[]
	for k, v in cf.yamls['disks'].items():
		values.append(v)
	return values

def GetCpuAvg():
	interval=cf.yamls['cpu']['cpu_avg_interval']
	try:
		if interval==1:
			cpu_avg=x.LoadAvarage(0)
		elif interval==5:
			cpu_avg=x.LoadAvarage(1)
		elif interval==15:
			cpu_avg=x.LoadAvarage(2)
		return cpu_avg
	except:
		return 'cpu_avg_interval not configured well'

def CpuMsg():
	avarage=GetCpuAvg()
	warn=cf.yamls['cpu']['warning']
	crit=cf.yamls['cpu']['critical']
	cpu_q=db.db.search(db.query['cpu'])
	if len(cpu_q)<1:
		record=db.DB('cpu', 'avarage' , avarage, 'False')
		db.db.insert(record)
	else:		
		cpu_q=(cpu_q[-1])
		p=cpu_q['cpu']['avarage']
		f=cpu_q['cpu']['flag']
		if p>= crit:
			danger=msg.CpuLoadAvg(str(avarage), hostname)[2]
			alert.Slack(danger, 'Alarm', 'danger', 'high', str(date))
			record=db.DB('cpu', 'avarage' , avarage, 'True')
			db.db.insert(record)
		if p >= warn and p < crit:	
			warning=msg.CpuLoadAvg(str(avarage), hostname)[1]
			alert.Slack(warning, 'Alarm', 'warning', 'medium', str(date))
			record=db.DB('cpu', 'avarage' , avarage, 'True')
			db.db.insert(record)
		if p < warn and f== db.flag:
			normal=msg.CpuLoadAvg(str(avarage), hostname)[0]
			alert.Slack(normal, 'Alarm', 'good', 'low', str(date))
			record=db.DB('cpu', 'avarage' , avarage, 'False')
			db.db.insert(record)
		if p < warn and f!= db.flag:
			nothing="Will do notning"
def MemoryMsg():
	memory=x.MemoryUsage()
	percent=memory['percent']
	warn=cf.yamls['memory']['warning']
	crit=cf.yamls['memory']['critical']
	memory_q=db.db.search(db.query['memory'])
	if len(memory_q)<1:
		record=db.DB('memory', 'percent' , percent, 'False')
		db.db.insert(record)
	else:
		memory_q=(memory_q[-1])
		p=memory_q['memory']['percent']
		f=memory_q['memory']['flag']
		if p >= crit:
			danger=msg.MemoryPercent(memory['percent'], hostname)[2]
			alert.Slack(danger, 'Alarm', 'danger', 'high', str(date))
			record=db.DB('memory', 'percent' , percent, 'True')
			db.db.insert(record)
		if p >= warn and p < crit:
			warning=msg.MemoryPercent(memory['percent'], hostname)[1]
			alert.Slack(warning, 'Alarm', 'warning', 'medium', str(date))
			record=db.DB('memory', 'percent' , percent, 'True')
			db.db.insert(record)
		if p < warn and f== db.flag:
			normal=msg.MemoryPercent(memory['percent'], hostname)[0]
			alert.Slack(normal, 'Alarm', 'good', 'low', str(date))
			record=db.DB('memory', 'percent' , percent, 'False')
			db.db.insert(record)
		if p < warn and f!= db.flag:
			nothing="Will do notning"

def SwapMsg():
	swap=x.Swap()
	percent=swap['percent']
	warn=cf.yamls['swap']['warning']
	crit=cf.yamls['swap']['critical']
	swap_q=db.db.search(db.query['swap'])
	if len(swap_q)<1:
		record=db.DB('swap', 'percent' , percent, 'False')
		db.db.insert(record)
	else:
		swap_q=(swap_q[-1])
		p=swap_q['swap']['percent']
		f=swap_q['swap']['flag']
		if p>= crit:
			danger=msg.SwapPercent(swap['percent'], hostname)[2]
			alert.Slack(danger, 'Alarm', 'danger', 'high', str(date))
			record=db.DB('swap', 'percent' , percent, 'True')
			db.db.insert(record)
		if p >= warn and p < crit:
			warning=msg.SwapPercent(swap['percent'], hostname)[1]
			alert.Slack(warning, 'Alarm', 'warning', 'medium', str(date))
			record=db.DB('swap', 'percent' , percent, 'True')
			db.db.insert(record)
		if p < warn and f== db.flag:
			normal=msg.SwapPercent(swap['percent'], hostname)[0]
			alert.Slack(normal, 'Alarm', 'good', 'low', str(date))
			record=db.DB('swap', 'percent' , percent, 'False')
			db.db.insert(record)
		if p < warn and f!= db.flag:
			nothing="Will do notning"
def DiskMsg():
        partitions=GetDisks()
	warn=cf.yamls['disk']['warning']
	crit=cf.yamls['disk']['critical']
        for partition in partitions:
                percent = x.MapDiskUsage()[partition][3]
		disk=db.db.search(db.query[partition])
		if len(disk)<1:
			record=db.DB(partition, 'percent' , percent, 'False')
			db.db.insert(record)
		else:	
			disk=(disk[-1])
			p=disk[partition]['percent']
			f=disk[partition]['flag']
                	if p >= crit:
                        	danger=msg.DiskPercent(partition, percent, hostname)[2]
                        	alert.Slack(danger , 'Alarm', 'danger', 'high', str(date))
				record=db.DB(partition, 'percent' , percent, 'True')
				db.db.insert(record)
			if p >= warn and p < crit:
				warning=msg.DiskPercent(partition, percent, hostname)[1]
				alert.Slack(warning , 'Alarm', 'warning', 'medium', str(date))
				record=db.DB(partition, 'percent' , percent, 'True')
				db.db.insert(record)
			if p < warn and f== db.flag:
				normal=msg.DiskPercent(partition, percent, hostname)[0]
				alert.Slack(normal , 'Alarm', 'good', 'low', str(date))
				record=db.DB(partition, 'percent' , percent, 'False')
				db.db.insert(record)
			if p < warn and f!= db.flag:
				nothing="Will do notning"

def GetDomains(rule):
	domain=[]
	domains=cf.yamls[rule].items()
	for k, v in domains:
		domain.append(v)
	return domain
		

def DomainUptime():
	domains=GetDomains('uptime')
	for domain in domains:
		dom=db.db.search(db.query[domain])
		if len(dom) <1:
			record=db.DB(domain, 'status' , 'up', 'False')
			db.db.insert(record)
		else:
			dom=(dom[-1])
			f=dom[domain]['flag']
			try:
				health=do.url_uptime(domain)
                        	if health==502 or health==503 or health==504:
                                	down=msg.UrlUp(domain)[1]
					alert.Slack(down , 'Alarm', 'danger', 'high', str(date))
					record=db.DB(domain, 'status' , 'down', 'True')
					db.db.insert(record)
				if health in range(200,399) and f==db.flag:
					up=msg.UrlUp(domain)[0]
					alert.Slack(up , 'Alarm', 'good', 'normal', str(date))
					record=db.DB(domain, 'status' , 'up', 'False')
					db.db.insert(record)
				if health in range(200,399) and f!=db.flag:
					nothing="Will do notning"
			except do.requests.exceptions.ConnectionError:
				notvalid=msg.UrlUp(domain)[2]
				alert.Slack(notvalid , 'Alarm', 'warning', 'medium', str(date))		

def SslValidate():
	domains=GetDomains('ssl')
	norm=cf.yamls['ssl_validate']['normal']
	warn=cf.yamls['ssl_validate']['warning']
	for domain in domains:
		expire_date=do.ssl_check(domain)
		remaining= expire_date - today
		ssl_query=db.db.search(db.query[domain])
		if len(ssl_query) <1:
			record=db.DB(domain, 'remaining' , remaining.days, 'False')
			db.db.insert(record)
		else:
			ssl_query=(ssl_query[-1])
			f=ssl_query[domain]['flag']
			if remaining.days<warn:
				warning=msg.SslChek(domain, remaining.days)[1]
				alert.Slack(warning , 'Alarm', 'danger', 'high', str(date))
				record=db.DB(domain, 'remaining' , remaining.days, 'True')
				db.db.insert(record)
			if remaining.days>norm and f==db.flag:
				normal=msg.SslChek(domain, remaining.days)[0]
				alert.Slack(normal , 'Alarm', 'good', 'normal', str(date))
				record=db.DB(domain, 'remaining' , remaining.days, 'False')
				db.db.insert(record)
			if remaining.days>norm and f!=db.flag:
				nothing="Will do notning"						
			
			
def Main():
	CpuMsg()
	MemoryMsg()
	SwapMsg()
	DiskMsg()
	DomainUptime()
	if sslValidate_cron==ssl_schedule:
		SslValidate()

if __name__ == '__main__':
	Main()

