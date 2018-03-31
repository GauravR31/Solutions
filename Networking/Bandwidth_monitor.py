import psutil
import time

def main():
	interval = input("Enter time interval to monitor data in seconds ")

	old_sent_value = 0
	old_recv_value = 0

	while True:
		sent = psutil.net_io_counters().bytes_sent
		received = psutil.net_io_counters().bytes_recv

		if old_sent_value:
			curr_sent = sent - old_sent_value
			curr_recv = received - old_recv_value

			print("KB sent in last {} sec: {}".format(interval, show_stat(curr_sent)))
			print("KB received in last {} sec: {}".format(interval, show_stat(curr_recv)))

		old_sent_value = sent
		old_recv_value = received

		time.sleep(interval)

def show_stat(value):
	return float(value/1024)

if __name__ == '__main__':
	main()