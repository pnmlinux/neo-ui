import os, time, datetime, psutil

#Kernel Version
def kernel():
    os.system("cat /proc/version > version.txt")
    pnm_version_file = open("version.txt","r")
    pnm_text = pnm_version_file.read()
    kernel_version = pnm_text.split("(")[0]
    pnm_version_file.close()
    os.system("rm version.txt")
    return kernel_version

#CPU
#cpu line layout : "model name	: "
def cpu():
    os.system("cat /proc/cpuinfo > cpu.txt")
    cpu_file = open("cpu.txt","r")
    cpu_model = cpu_file.read()
    cpu_name = cpu_model.split("model name	: ")
    text = open("cpu.txt","w")
    text.write(cpu_name[1])
    text.close()
    text2 = open("cpu.txt","r")
    cpu = text2.readline()
    text.close()
    os.system("rm cpu.txt")
    return cpu

#GPU 
#GPU line        product: Whistler LE [ 
#GPU Command lshw -C display
def gpu():
    os.system("lshw -C display > gpu.txt")
    gpu_file = open("gpu.txt","r")
    gpu_text = gpu_file.read()
    gpu_version = gpu_text.split("product:")
    gpu = gpu_version[1].split("Whistler LE")[1].split("vendor:")[0]
    gpu_file.close()
    os.system("rm gpu.txt")
    return gpu


#DE
def desktopenv():
    os.system("echo $XDG_CURRENT_DESKTOP > de.txt")
    de_file = open("de.txt","r")
    de = de_file.read()
    de_file.close()
    os.system("rm de.txt")
    return de

#MEMORY
#Mem Code totalmem=0; for mem in /sys/devices/system/memory/memory*; do [[ "$(cat ${mem}/online)" == "1" ]] && totalmem=$((totalmem+$((0x$(cat /sys/devices/system/memory/block_size_bytes))))); done && ram=$((totalmem/1024**3))

def mem():
    cmd = 'totalmem=0; for mem in /sys/devices/system/memory/memory*; do [[ "$(cat ${mem}/online)" == "1" ]] && totalmem=$((totalmem+$((0x$(cat /sys/devices/system/memory/block_size_bytes))))); done && ram=$((totalmem/1024**3)) && echo $ram >ram.txt'

    os.system(cmd)

    ram_file = open("ram.txt","r")
    ramf = ram_file.readline()
    ram_file.close()
    ramf1 = open("ram.txt","w")
    ramf1.write(ramf)
    ramf1.close()
    ram_file = open("ram.txt","r")
    ram = ram_file.readline()
    ram_file.close()
    os.system("rm ram.txt")
    return ram


def oslogo():
    os.system("ls /usr/share/icons|grep logo.png > icon.txt")
    logo_file = open("icon.txt","r")
    oslogo = "/usr/share/icons/"+logo_file.readline()
    return oslogo

#UPTIME

#In main script because a dynamic function bro :D

