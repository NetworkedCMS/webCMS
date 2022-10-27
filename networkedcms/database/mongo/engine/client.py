from mongoengine import connect


class MongoClient:
    _client:str = None

    @classmethod    
    def connect(cls, db:str, host:str, port:int = 3356):
        """Initializes a mongo connection client"""
        if cls._client:
            return cls._client
        else:
            cls._client = connect(db, host, port)    
        return cls._client   



        