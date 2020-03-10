import os

REQUIRED_CONFIGS = [
    'CTFNC_PORT',
    'CTFNC_BIND',
    'CTFNC_MAX_CONN',
]

class Config:
    '''
    The class that holds the minimum set of configurations so that
    the ctfnc can run.
    '''
    CTFNC_PORT: int
    CTFNC_BIND: str
    CTFNC_MAX_CONN: int

def validate_config(config: object):
    validated_config = Config()
    for required_config in REQUIRED_CONFIGS:
        environment = os.environ.get(required_config, None)
        if environment is not None:
            validated_config.__setattr__(required_config, environment)
            continue
        
        # Auto-raises error if not found
        validated_config.__setattr__(required_config, config.__getattribute__(required_config))

    return validated_config