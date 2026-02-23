import requests;

payload = \
{
    "request_number": "REQ4379395",
    "ritm_number": "RITM4385572",
    "email": "qa.bufp@packages.com.pk",
    "role": "UL Supplier External User",
    "environment": "Production",
    "country": "PK - Pakistan"
};

response = requests.post\
(
    "http://127.0.0.1:8000/process_request",
    json = payload
);

print(response.json());