import psutil

def health_check():
    cpu_threshold = float(input("Enter CPU Threshold: "))
    disk_threshold = float(input("Enter Disk Threshold: "))
    memory_threshold = float(input("Enter Memory Threshold: "))

    current_cpu = psutil.cpu_percent(interval=1)
    current_disk = psutil.disk_usage('/').percent
    current_memory = psutil.virtual_memory().percent

    print("\n------- SYSTEM HEALTH CHECK REPORT ---------------")

    if current_cpu > cpu_threshold:
        print(f"CPU is HIGH: {current_cpu}%")
    else:
        print(f"CPU is OK: {current_cpu}%")

    if current_disk > disk_threshold:
        print(f"Disk is HIGH: {current_disk}%")
    else:
        print(f"Disk is OK: {current_disk}%")

    if current_memory > memory_threshold:
        print(f"Memory is HIGH: {current_memory}%")
    else:
        print(f"Memory is OK: {current_memory}%")


# Run the script
health_check()
