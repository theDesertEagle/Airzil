from urllib.request import urlretrieve, urlopen
from os import path
from re import findall

class ExternDataController():
    """Handles all tasks related to acquiring external datasets
    """

    @staticmethod
    def download(source_url, dest_path):
        """Downloads one file (dataset) from a specified URL linking to the file (dataset)
        Args: 
            source_url: URL linking to the file from where it is to be downloaded
            dest_path: Local path of the file which is to be downloaded, including its new name
        
        Returns:
            True: Indicates that the file already exists (or) the file has been downloaded successfully
            False: Indicates that the file was never downloaded

        Raises:
            Exception: Reason why the file download failed    
        """
        if path.exists(dest_path): 
            print('[.] ' + dest_path + ' already exists.')
            return True
        else:
            try:
                urlretrieve(source_url, dest_path)
                print('[+] ' + path.basename(dest_path) + ' has been downloaded and placed in the ' + path.dirname(dest_path) + ' directory.')
                return True

            except Exception as e:
                print('[-] An error occured ... \n ')
                print(e)
                return False

    @staticmethod
    def search_zipcodes(url, logic=b'\d{5}', zipcode_range=(10000, 15000)):
        """Searches for a set of zipcodes (particularly for New York City in this case)
        Args:
            url: URL linking to a website with listed zipcodes
            logic: Regex pattern as a byte-string which will match all potential zipcodes; default case matches a 5-digit zipcode
            zipcode_range: Tuple with zip code range described as (inclusive_smallest, exclusive_highest) as per the state in consideration;
                default - All valid zipcodes in New York Codes lie in 10000 <= zipcodes < 15000 range; as per link: [https://en.wikipedia.org/wiki/List_of_ZIP_Code_prefixes]

        Returns:
            set: All extracted zipcodes      
        """                    
        html = urlopen(url).read()

        # Extracts regex pattern containig potential zipcodes as ybte strings  
        # 
        return set([str(code) for code in list(map(lambda code_byte: int(code_byte.decode('utf-8')), findall(b'\d{5}', html))) if code >= 10000 and code < 15000])