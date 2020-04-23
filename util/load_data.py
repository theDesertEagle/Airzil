#DEPRECATED DUE TO LACK OF TIME
import pandas as pd

class LoadDataController():
    """Handles all tasks related to loading datasets and optimizing memory  
    """
        
    def __init__(self):
        """Initializes the cache of standard (default) columns that a dataset will require when loaded
        Args: 
            [None]
        
        Returns:
            [None] 

        Raises:
            [None]    
        """                

        # Dicitonary with key = dataset, values = [list of standard columns, inclusive boolean indicator]
        self._standard_cols = {
            'airbnb': [ 
                [
                    'id',
                    'zipcode',
                    'property_type',
                    'room_type',
                    'accommodates',
                    'beds',
                    'bathrooms',
                    'bedrooms',
                    'amenities',
                    'neighbourhood_cleansed',
                    'neighbourhood_group_cleansed',
                    'state',
                    'latitude',
                    'longitude',
                    'is_location_exact',
                    'price',
                    'number_of_reviews',
                    'reviews_scores_rating',
                    'reviews_scores_accuracy',
                    'reviews_scores_cleanliness',
                    'reviews_scores_checkin',
                    'reviews_scores_communication',
                    'reviews_scores_location',
                    'reviews_scores_value',
                    'reviews_per_month',
                    'availability_30',
                    'availability_60',
                    'availability_90',
                    'availability_365'
                ], 
                True
            ],
            'zillow': [
                [
                    'RegionID', 
                    'City', 
                    'Metro', 
                    'CountyName'
                ],
                False
            ]                
        } 

    def _lowercase_set(self, lst):
        """Returns a set of lowercased column names which are strings; for error-proofing column-name cases while importing 
        Args: 
            lst: list of column names as strings
        
        Returns:
            Set: Lowercased column names as strings 

        Raises:
            Exception: [None]    
        """                
        
        return set(list(map(str.lower, lst)))

    def load(self, dataset_name, path, columns, inclusive):
        """Loads a dataset into memory
        Args: 
            dataset_name: String indicating the dataset to be loaded, i.e., 'zillow', 'airbnb' or 'states'
            path: Local path including the dataset's name
            columns: List of columns to be loaded; if given as string valued 'standard', all cached columns are loaded;
                    this argument does not matter if dataset_name = 'states'  
            inclusive: Boolean indicating the columns list given as argument are inclusive/exclusive while loading the dataset;
                    this argument does not matter if dataset_name = 'states'
        
        Returns:
            dataset: Dataset that is loaded 

        Raises:
            Exception: Reason why the dataset load failed    
        """
        try:
            # Flag standard columns as per the arguments passed 
            if isinstance(columns, str) and columns == 'standard':
                inclusive = self._standard_cols[] 
                standard_flag = True
            else: 
                standard_flag = False
             
            # Load states dataset if applicable
            if dataset_name == 'states':
                dataset = pd.read_csv(path, sep='\n', header=None, names=['stateids'])

            # Load Airbnb or Zillow dataset, as per applicability
            if inclusive:
                dataset = pd.read_csv(
                    path,
                    usecols=lambda col: col.lower() in self._lowercase_set(self._standard_cols[dataset_name] if standard_flag else columns),
                    low_memory=False if dataset_name == 'airbnb' else True            
                )
            else:
                dataset = pd.read_csv(
                    path,
                    usecols=lambda col: col.lower() not in self._lowercase_set(self._standard_cols[dataset_name] if standard_flag else columns),
                    low_memory=False if dataset_name == 'airbnb' else True            
                )
            print('[+] The ' + dataset_name + ' dataset has been loaded successfully.')
            return dataset

        except Exception as e:
            print('[-] An error occured ... \n')
            print(e)