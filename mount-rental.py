def check_mount_rental(time_used, time_purchased):
    if time_used >= time_purchased:
        return print("overtime charged")
    else:
        return print("no charges yet")
check_mount_rental(5,10)
check_mount_rental(30,10)