
def DiskPercent(partition, percent, hostname):
	normal="Normal ! "+partition +" is normal on "+ hostname
	warning="Warning! "+partition +' has reached '+ str(percent)+ '%'+' on '+ hostname
	danger="Critical! "+partition +' has reached '+ str(percent)+ '%'+' on '+ hostname
	return normal, warning, danger

def MemoryPercent(percent, hostname):
	normal="Normal ! Memory usage returned to normal on " +hostname
	warning="Warning ! the memory usage has reached "+str(percent)+"% on "+hostname
	danger="Critical ! the memory usage has reached "+str(percent)+"% on "+hostname 
	return normal, warning , danger

def SwapPercent(percent, hostname):
	normal="swap is normal on " +hostname
	warning="Warning ! The swap usage has reached "+str(percent)+"% on "+hostname
	danger="Critical ! The swap usage has reached "+str(percent)+"% on "+hostname
	return normal, warning, danger

def CpuLoadAvg(avarage, hostname):
	normal="Normal ! Avarage cpu is normal ! " +" on "+hostname
	warning="Warning ! Average cpu load is "+str(avarage)+" on "+hostname
	danger="Critical ! Average cpu load is "+str(avarage)+" on "+hostname
	return normal, warning, danger

def UrlUp(domain):
	up=domain+" is up"
	down=domain+" is down"
	notvalid=domain+" is not valid"
	return up, down, notvalid

def SslChek(domain, days):
	valid="SSL is valid for "+domain
	expired=domain+" SSL will expire in "+str(days)+" days"
	return valid, expired
