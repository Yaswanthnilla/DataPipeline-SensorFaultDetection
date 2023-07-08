
import os


# SECURITY_PROTOCOL="SASL_SSL"   #To establish a secure connection bw client and server
# SSL_MACHENISM="PLAIN"
# API_KEY = os.getenv('API_KEY',None)
# ENDPOINT_SCHEMA_URL  = os.getenv('ENDPOINT_SCHEMA_URL',None)
# API_SECRET_KEY = os.getenv('API_SECRET_KEY',None)
# BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER',None)
# # SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL',None)
# # SSL_MACHENISM = os.getenv('SSL_MACHENISM',None)
# SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY',None)
# SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET',None)



#Authentication related configs
SECURITY_PROTOCOL="SASL_SSL"   #To establish a secure connection bw client and server
SSL_MACHENISM="PLAIN"

#Cloud related keys
API_KEY = "XARC5HQR4CJSN4PV"
API_SECRET_KEY = "W5FGbfjR+6hjEOATqXLlw4vYw0bZVtL7SAQh49FDZJlxiZtUhvGZtnl+I0nSIwbs"
BOOTSTRAP_SERVER = "pkc-41p56.asia-south1.gcp.confluent.cloud:9092"

#Schema related keys
ENDPOINT_SCHEMA_URL  = "https://psrc-lzvd0.ap-southeast-2.aws.confluent.cloud"
SCHEMA_REGISTRY_API_KEY = "TWDMZPPHOFXKGWRN"
SCHEMA_REGISTRY_API_SECRET = "X63Nvgi2HJgT46gTFhPF0C9XYwNdDWZ2/l9vAom8DTe5nNK5EpGUquMnhrR4k1df"


def sasl_conf():

    sasl_conf = {'sasl.mechanism': SSL_MACHENISM,
                 # Set to SASL_SSL to enable TLS support.
                #  'security.protocol': 'SASL_PLAINTEXT'}
                'bootstrap.servers':BOOTSTRAP_SERVER,
                'security.protocol': SECURITY_PROTOCOL,
                'sasl.username': API_KEY,
                'sasl.password': API_SECRET_KEY
                }
    print(sasl_conf)
    return sasl_conf



def schema_config():
    return {'url':ENDPOINT_SCHEMA_URL,
    
    'basic.auth.user.info':f"{SCHEMA_REGISTRY_API_KEY}:{SCHEMA_REGISTRY_API_SECRET}"

    }

if __name__ == '__main__':
    sasl_conf()

