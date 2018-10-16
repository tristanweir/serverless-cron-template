import requests
import time


class ObservatoryScanner():
    def __init__(self):
        self.session = requests.Session()
        self.api_url = 'https://http-observatory.security.mozilla.org/api/v1'

    def scan(self, host):
        # Initiate the scan
        results = {}
        analyze_url = self.api_url + '/analyze?host=' + host
        results['scan'] = self.session.post(analyze_url, data=None).json()

        # Wait for the scan to complete, polling every second
        results['tests'] = self.__poll(results['scan']['scan_id'])
        results['host'] = host
        return results

    def __poll(self, scan_id):
        url = self.api_url + '/getScanResults?scan=' + str(scan_id)
        while True:
            resp = self.session.get(url).json()
            # This means we got our results back, so return them!
            if 'content-security-policy' in resp:
                return resp

            time.sleep(1)


### How to use me? ###
url = "mozilla.org"
scanner = ObservatoryScanner()
results = scanner.scan(url)
######################
