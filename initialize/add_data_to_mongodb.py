from pymongo import MongoClient
import re


def add_data(client):

    try:

        db = client["moores_law_db"]

        cpu_collection = db["cpu"]
        gpu_collection = db["gpu"]
        ram_collection = db["ram"]

        with open("./data/cpu.csv", "r") as cpu_file:
            col_labels = cpu_file.readline().strip().split(",")

            for line in cpu_file:
                cpu = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', line.strip())
                cpu[0] = cpu[0].strip('"')
                insert_dic = {}

                for i, col_label in enumerate(col_labels):
                    if col_label == "transistor_count":
                        if cpu[i] != "NA":
                            insert_dic[col_label] = int(cpu[i])
                        else:
                            insert_dic[col_label] = cpu[i]

                    elif col_label == "date_of_introduction":
                        if cpu[i] != "NA":
                            insert_dic[col_label] = int(cpu[i])
                        else:
                            insert_dic[col_label] = cpu[i]

                    elif col_label == "process":
                        if cpu[i] != "NA":
                            insert_dic[col_label] = int(cpu[i])
                        else:
                            insert_dic[col_label] = cpu[i]

                    elif col_label == "area":
                        if cpu[i] != "NA":
                            insert_dic[col_label] = int(cpu[i])
                        else:
                            insert_dic[col_label] = cpu[i]

                    else:
                        insert_dic[col_label] = cpu[i]

                cpu_collection.insert_one(insert_dic)

        with open("./data/gpu.csv", "r") as gpu_file:
            col_labels = gpu_file.readline().strip().split(",")

            for line in gpu_file:
                gpu = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', line.strip())
                insert_dic = {}

                for i, col_label in enumerate(col_labels):
                    if col_label == "transistor_count":
                        if gpu[i] != "NA":
                            insert_dic[col_label] = int(gpu[i])
                        else:
                            insert_dic[col_label] = gpu[i]

                    elif col_label == "date_of_introduction":
                        if gpu[i] != "NA":
                            insert_dic[col_label] = int(gpu[i])
                        else:
                            insert_dic[col_label] = gpu[i]

                    elif col_label == "process":
                        if gpu[i] != "NA":
                            insert_dic[col_label] = int(gpu[i])
                        else:
                            insert_dic[col_label] = gpu[i]

                    elif col_label == "area":
                        if gpu[i] != "NA":
                            insert_dic[col_label] = int(gpu[i])
                        else:
                            insert_dic[col_label] = gpu[i]

                    elif col_label == "ref":
                        continue

                    else:
                        insert_dic[col_label] = gpu[i]

                gpu_collection.insert_one(insert_dic)

        with open("./data/ram.csv", "r") as ram_file:
            col_labels = ram_file.readline().strip().split(",")

            for line in ram_file:
                ram = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', line.strip())
                insert_dic = {}

                for i, col_label in enumerate(col_labels):
                    if col_label == "transistor_count":
                        if ram[i] != "NA":
                            insert_dic[col_label] = int(ram[i])
                        else:
                            insert_dic[col_label] = ram[i]

                    elif col_label == "capacity_bits":
                        if ram[i] != "NA":
                            insert_dic[col_label] = int(ram[i])
                        else:
                            insert_dic[col_label] = ram[i]

                    elif col_label == "date_of_introduction":
                        if ram[i] != "NA":
                            insert_dic[col_label] = int(ram[i])
                        else:
                            insert_dic[col_label] = ram[i]

                    elif col_label == "process":
                        if ram[i] != "NA":
                            insert_dic[col_label] = int(ram[i])
                        else:
                            insert_dic[col_label] = ram[i]

                    elif col_label == "area":
                        if ram[i] != "NA":
                            insert_dic[col_label] = int(ram[i])
                        else:
                            insert_dic[col_label] = ram[i]

                    elif col_label == "ref":
                        continue

                    else:
                        insert_dic[col_label] = ram[i]

                ram_collection.insert_one(insert_dic)

        print("successfully migrated data to mongodb!")

    except Exception as e:
        print(f"failed to migrate data to mongodb due to {e}")

    finally:
        print("done")


def clear_database(client):

    try:
        client.drop_database("moores_law_db")

        print("Successfully removed all data")

    except Exception as e:
        print(f"clearing data failed due to {e}")

    finally:
        print("done")


if __name__ == '__main__':
    client = MongoClient("mongodb://ml_user:securepassword@mongodb:27017/moores_law_db?authSource=moores_law_db")
    # client = MongoClient("mongodb://localhost:27017/")

    clear_database(client)
    add_data(client)
