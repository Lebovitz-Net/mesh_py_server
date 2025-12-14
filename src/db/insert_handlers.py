# src/db/insertHandlers.py

from src.db.inserts.channel_inserts import channel_inserts
from src.db.inserts.config_inserts import config_inserts
from src.db.inserts.contact_inserts import contact_inserts
from src.db.inserts.device_inserts import device_inserts
from src.db.inserts.diagnostic_inserts import diagnostic_inserts
from src.db.inserts.message_inserts import message_inserts
from src.db.inserts.metric_inserts import metric_inserts
from src.db.inserts.node_inserts import node_inserts


# Merge all insert dicts into one registry
allHandlers = {
    **channel_inserts,
    **config_inserts,
    **contact_inserts,
    **device_inserts,
    **diagnostic_inserts,
    **message_inserts,
    **metric_inserts,
    **node_inserts,
}


class InsertHandlersClass:
    """
    Singleton class of all insert functions.
    Dynamically attaches each insert function as an instance method.
    """

    _instance = None

    def __new__(cls, db=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, db=None):
        if self._initialized:
            return
        self.db = db

        # Dynamically attach each insert function as an instance method
        for name, func in allHandlers.items():
            def make_method(f):
                def method(self, *args, **kwargs):
                    if self.db is not None:
                        return f(self.db, *args, **kwargs)
                    return f(*args, **kwargs)
                return method

            setattr(self, name, make_method(func).__get__(self, InsertHandlersClass))

        self._initialized = True

    def handle_insert(self, name: str, payload: dict, *args, **kwargs):
        fn = allHandlers.get(name)
        if not fn:
            print(f"[InsertHandlers] Unknown insert function: {name}")
            return None
        try:
            if self.db is not None:
                return fn(self.db, payload, *args, **kwargs)
            return fn(payload, *args, **kwargs)
        except Exception as err:
            print(f"[InsertHandlers] Error in {name}: {err}")
            return None


# Export the singleton instance under the name InsertHandlers
InsertHandlers = InsertHandlersClass()
