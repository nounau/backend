class mongo_utils:

    mongo = None

    @staticmethod
    def set_mongo(mongo):
        mongo_utils.mongo = mongo
        #print("set: ",mongo_utils.mongo)

    @staticmethod
    def get_mongo():
        #print("get: ",mongo_utils.mongo)
        return mongo_utils.mongo
