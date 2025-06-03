def parse_query_string(query_params):
    mongo_query = {}
    for key, value in query_params.items():
        if key and value:
            # If value is a number, we convert it to an int
            try:
                value = int(value)
            except ValueError:
                pass

            if key.endswith('__gt'):
                mongo_query[key[:-4]] = {'$gt': value}
            elif key.endswith('__lt'):
                mongo_query[key[:-4]] = {'$lt': value}
            elif key.endswith('__gte'):
                mongo_query[key[:-5]] = {'$gte': value}
            elif key.endswith('__lte'):
                mongo_query[key[:-5]] = {'$lte': value}
            else:
                mongo_query[key] = value
    return mongo_query
