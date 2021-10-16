import speedtest
import logging
import time


class NetworkMonitor:
    def __init__(self):
        # start logging
        logging.basicConfig(
            filename='test.log',
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p'
        )
        # get valid interval from user
        while True:
            try:
                self.interval = float(input('Interval (Minutes): '))
            except ValueError:
                print('Not a valid interval')
            else:
                logging.debug(f'Network Monitor Started. Interval set to {self.interval}')
                break
        # test connection
        # RUNS INDEFINITELY AT SET INTERVAL
        while True:
            self.test_connection()
            time.sleep(60 * self.interval)

    def as_mbps(self, speed_in_bits: float):
        # converts the bits to megabits
        return round(speed_in_bits / 1_000_000, 2)

    def test_connection(self):
        # appends Download and Upload results to log file
        print('Running test...')
        results = speedtest.Speedtest()
        logging.debug(f'Download: {self.as_mbps(results.download())} Mbit/s')
        logging.debug(f'Upload: {self.as_mbps(results.upload())} Mbit/s')
        print('Test complete')


if __name__ == '__main__':
    NetworkMonitor()
