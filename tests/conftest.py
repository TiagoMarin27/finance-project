"""Pytest confuguration file"""

import pytest 


from finance_project.main import app
from fastapi.testclient import TestClient



@pytest.fixture
def test_client():
    return TestClient(app)


@pytest.fixture
def mock_expected_stocks_list():
    return  [
        {   

            "name": "Apple company", 
            "price": 102, 
            "code": "AAPL.US"
        },   
        { 
                    
            "name": "Microsoft company", 
            "price": 78, 
            "code": "MICRO.US"
        },
        {  
                    
            "name": "Google company", 
            "price": 92, 
            "code": "GGLE.US"
         }
            
    ]
