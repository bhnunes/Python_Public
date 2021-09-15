import pandas as pd

def convert(input_Path,output_Path):
    try:
        df_json = pd.read_json(input_Path)
        df_json.to_excel(output_Path)
        status="File Converted Succesfully"
    except Exception as e:
        status="Process Failed - "+str(e)
    
    print(str(status))
    return status

if __name__ == "__main__":
    input_Path = sys.argv[1]
    output_Path = sys.argv[2]
    convert(input_Path,output_Path)



