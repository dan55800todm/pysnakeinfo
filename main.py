import tkinter as tk
import platform
import psutil

root = tk.Tk()
root.title("PySnakeInfo")
root.configure(bg="black")
root.geometry("600x600")
root.iconbitmap("bitmap.ico")

def show_system_info():
    info = "Processor: {}\n".format(platform.processor())
    info += "System: {} {}\n".format(platform.system(), platform.release())
    info += "Verison: {}\n".format(platform.version())
    info += "Architecture: {}\n".format(platform.architecture())
    info += "Processor information: {}\n".format(platform.machine())
    info += "User (or computer) name: {}\n".format(platform.node())
    info += "Platform version: {}\n".format(platform.platform())
    info += "System type: {}\n".format(platform.system())
    info += "Number of processor cores: {}\n".format(psutil.cpu_count(logical=False))
    info += "Total number of processor cores: {}\n".format(psutil.cpu_count(logical=True))

    disk_info = psutil.disk_partitions()
    for disk in disk_info:
        info += f"\nDisk {disk.device}"
        info += f"\n  Mountpoint: {disk.mountpoint}"
        try:
            disk_usage = psutil.disk_usage(disk.mountpoint)
            info += f"\n  Total space: {disk_usage.total/(1024*1024*1024):.2f} GB"
            info += f"\n  Used space: {disk_usage.used/(1024*1024*1024):.2f} GB"
            info += f"\n  Free space: {disk_usage.free/(1024*1024*1024):.2f} GB"
            info += f"\n  Percentage used: {disk_usage.percent}%"
        except PermissionError:
            info += f"\n  Insufficient permissions to access disk information"
    
    label_info.config(text=info)

btn = tk.Button(root, text="Get system information", command=show_system_info, bg="gray", fg="white", font=("Arial", 12))
btn.pack(pady=10)

label_info = tk.Label(root, text="", bg="black", fg="white", font=("Arial", 12))
label_info.pack(pady=10)

root.mainloop()
