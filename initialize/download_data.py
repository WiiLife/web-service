import requests
import os


if __name__ == '__main__':

    try:

        # URLs of the data files
        cpu_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2019/2019-09-03/cpu.csv"
        gpu_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2019/2019-09-03/gpu.csv"
        ram_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2019/2019-09-03/ram.csv"

        # Function to download and save the data
        def download_data(url, filename):
            response = requests.get(url)
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded {filename}")
            else:
                print(f"Failed to download {filename}")


        # Download the files
        download_data(cpu_url, "cpu.csv")
        download_data(gpu_url, "gpu.csv")
        download_data(ram_url, "ram.csv")

        # move data to data folder
        if not os.path.exists("./data"):
            os.mkdir("./data")

        if os.path.exists("cpu.csv"):
            os.rename("cpu.csv", "./data/cpu.csv")
        else:
            os.remove("cpu.csv")

        if os.path.exists("gpu.csv"):
            os.rename("gpu.csv", "./data/gpu.csv")
        else:
            os.remove("gpu.csv")

        if os.path.exists("ram.csv"):
            os.rename("ram.csv", "./data/ram.csv")
        else:
            os.remove("ram.csv")

    except FileExistsError:
        print("Files already exist!")
        os.remove("cpu.csv")
        os.remove("gpu.csv")
        os.remove("ram.csv")
        print("removed extra files")

    finally:
        print("done")
