import requests
import matplotlib.pyplot as plt


# creates requests in HTTP to the web service
# gets data in json format from the web service


def home_message() -> dict:
    r = requests.get('http://127.0.0.1:5050')
    return r.json()


def get_component_names() -> list[str]:
    r = requests.get('http://127.0.0.1:5050/component_names')
    return r.json()


def get_components_features(collection_name: str = None) -> list | dict:
    if collection_name:
        collection = get_a_collection(collection_name)
        a_component = collection[0]
        return list(a_component.keys())

    collection_feat = {}
    for col_name in get_component_names():
        collection = get_a_collection(col_name)
        a_component = collection[0]
        collection_feat[col_name] = list(a_component.keys())
    return collection_feat


def get_all_collections() -> list[dict]:
    r = requests.get('http://127.0.0.1:5050/all_components')
    return r.json()


def get_a_collection(collection_name: str) -> list[dict] | dict:
    if collection_name in get_component_names():
        r = requests.get(f'http://127.0.0.1:5050/{collection_name}')
        return r.json()
    raise ValueError(f"collection {collection_name} not available")


def check_if_component_exists(data) -> bool:
    if not isinstance(data, dict):
        data = data.get_dict()

    collections = get_component_names()
    for col in collections:
        if get_specific_component_s(col, data):
            return True
    return False


def get_specific_component_s(collection_name: str, query: dict = None):
    # can also get all collection if no query
    if collection_name in get_component_names():
        r = requests.get(f'http://127.0.0.1:5050/{collection_name}', params=query)
        return r.json()
    raise ValueError(f"collection {collection_name} not available")


def add_data(collection_name: str, data) -> None:
    # only for 1 component
    collections = get_component_names()
    if collection_name in collections:
        if not isinstance(data, dict):
            data = data.get_dict()

        r = requests.post(f'http://127.0.0.1:5050/{collection_name}', json=data)
        print(r.json())
    else:
        raise ValueError(f"collection {collection_name} not available")


def add_many(collection_name: str, data: list[dict] | list) -> None:
    collections = get_component_names()
    if collection_name in collections:
        if not data:
            raise ValueError(f"no data provided")

        for data_component in data:
            add_data(collection_name, data_component)
    else:
        raise ValueError(f"collection {collection_name} not available")


def update_a_component(collection_name: str, query: dict, data) -> None:
    collections = get_component_names()

    if not isinstance(data, dict):
        data = data.get_dict()

    if collection_name in collections:
        r = requests.put(f'http://127.0.0.1:5050/{collection_name}', json=data, params=query)
        print(r.json())
    else:
        raise ValueError(f"collection {collection_name} not available")


def delete_component_s(collection_name: str, query: dict = None, obj_list: list = None) -> None:
    # can delete more than one component, whole collection if no query
    collections = get_component_names()
    if collection_name not in collections:
        raise ValueError(f"collection {collection_name} not available")

    if obj_list:
        for obj in obj_list:
            r = requests.delete(f'http://127.0.0.1:5050/{collection_name}', params=obj.get_dict())
            print(r.json())

    if query:
        r = requests.delete(f'http://127.0.0.1:5050/{collection_name}', params=query)
        print(r.json())

    elif not query and not obj_list:
        r = requests.delete(f'http://127.0.0.1:5050/{collection_name}', params={})
        print(r.json())


def delete_collection(collection_name: str) -> None:
    r = requests.delete(f'http://127.0.0.1:5050/{collection_name}', params={})
    print(r.json())


def _is_number(val):
    try:
        float(val)
        return True
    except (ValueError, TypeError):
        return False


def _check_if_feature_is_numeric(feature: str, collections: list[str]) -> bool | Exception:
    for collection_name in collections:
        collection = get_a_collection(collection_name)
        value = "NA"
        try:

            i = 0
            while value == "NA":
                value = collection[i][feature]
                i += 1

            if not _is_number(value):
                return False

        except Exception as e:
            return e

    return True


def _sort_by_component_feature(collection_name: str, feature: str) -> list[dict] | Exception:
    collection = get_a_collection(collection_name)
    value = "NA"
    try:

        i = 0
        while value == "NA":
            value = collection[i][feature]
            i += 1

        if not _is_number(value):
            raise ValueError("feature has to be integer or float")

    except Exception as e:
        return e

    filtered = [doc for doc in collection if _is_number(doc.get(feature))]
    return sorted(filtered, key=lambda x: x.get(feature, 0))


def plot_components(collection_names: list[str] | str, feature: str, logged: bool = False):
    if type(collection_names) == str and collection_names not in get_component_names():
        raise ValueError(f"all {collection_names} not available")

    elif set(collection_names) != set(get_component_names()):
        raise ValueError(f"all {collection_names} not available")

    for col in get_component_names():
        if feature not in get_components_features(col):
            raise ValueError(f"feature {feature} must be in common for all components")

    if isinstance(collection_names, str):
        collection_names = [collection_names]

    if _check_if_feature_is_numeric(feature, collection_names) and feature != "date_of_introduction":

        fig, ax = plt.subplots(1, len(collection_names))

        fig.suptitle(f"{feature} vs. Time")

        for i, col_name in enumerate(collection_names):
            sorted_collection = _sort_by_component_feature(col_name, "date_of_introduction")
            years = [d["date_of_introduction"] for d in sorted_collection if d[feature] != "NA"]
            tr_counts = [d[feature] for d in sorted_collection if d[feature] != "NA"]

            if logged:
                if len(collection_names) > 1:
                    ax[i].set_yscale("log")
                else:
                    ax.set_yscale("log")

            if len(collection_names) > 1:
                ax[i].scatter(years, tr_counts)
                ax[i].set_title(f"{col_name}")
                ax[i].set_xlabel("Year")
                ax[i].set_ylabel(f"{feature}")
            else:
                ax.scatter(years, tr_counts)
                ax.set_title(f"{col_name}")
                ax.set_xlabel("Year")
                ax.set_ylabel(f"{feature}")

        plt.show()

    else:
        raise ValueError("features not present in all components given or feature is not numeric")
