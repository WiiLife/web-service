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


def get_components_features(collection_name: str) -> list | Exception:
    try:
        collection = get_a_collection(collection_name)
        a_component = collection[0]
        return list(a_component.keys())

    except Exception as e:
        return e


def get_all_collections() -> list[dict]:
    r = requests.get('http://127.0.0.1:5050/all_components')
    return r.json()


def get_a_collection(collection_name: str) -> list[dict] | dict:
    r = requests.get(f'http://127.0.0.1:5050/{collection_name}')

    return r.json()


def check_if_component_exists(data) -> bool:

    if not isinstance(data, dict):
        data = data.get_dict()

    collections = get_component_names()
    for col in collections:
        if get_specific_component_s(col, data):
            return True
    return False


def get_specific_component_s(collection_name: str, query: dict = None) -> dict | list[dict]:
    # can also get all collection if no query

    r = requests.get(f'http://127.0.0.1:5050/{collection_name}', params=query)

    return r.json()


def add_data(collection_name: str, data) -> None:
    # only for 1 component

    if not isinstance(data, dict):
        data = data.get_dict()

    r = requests.post(f'http://127.0.0.1:5050/{collection_name}', json=data)
    print(r.json())


def add_many(collection_name: str, data: list[dict]) -> None:
    for data_component in data:
        add_data(collection_name, data_component)


def update_a_component(collection_name: str, query: dict, data: dict) -> None:
    r = requests.put(f'http://127.0.0.1:5050/{collection_name}', json=data, params=query)
    print(r.json())


def delete_component_s(collection_name: str, query: dict = None) -> None:
    # can delete more than one component, whole collection if no query
    if query:
        r = requests.delete(f'http://127.0.0.1:5050/{collection_name}', params=query)

    else:
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

