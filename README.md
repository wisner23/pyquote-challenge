
# Installing and Running

Python 3.5 is required.

    git clone https://github.com/wisner23/pyquote-challenge.git
    cd pyquote-challenge
    virtualenv env
    source env/bin/activate
    
    pip install -r requirements.txt
    python application.py
    
    # run test
    python -m unittest -v tests.quote_service_test


# Routes

    GET /quotes 
    GET /quotes/1 
    GET /quotes/random 

    GET /dashboard
