import json
import csv
from typing import Dict, List, Any
from pathlib import Path


def parse_openapi_json(file_path: str) -> Dict[str, Any]:
    """解析OpenAPI JSON文件并返回结构化数据"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            openapi_data = json.load(f)
        return openapi_data
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
        return {}
    except json.JSONDecodeError:
        print(f"错误：文件 {file_path} 不是有效的JSON格式")
        return {}

def extract_api_info(openapi_data: Dict[str, Any]) -> List[Dict[str, Any]]:

    data =[]
    paths = openapi_data.get('paths', {})
    
    for path, methods in paths.items():
        for method, details in methods.items():
            operation_id = details.get('operationId', '')
            data.append([path,method,operation_id])
            #print(path+'\t'+method+'\t'+operation_id)
            #print(f'{path}\t{method}\t{operation_id}')
    
    return data

def save_csv(file_path:str,suffix:str):
    p = file_path.find('.')
    file_out =file_path[:p]+".csv"
    # 解析JSON
    json_data = parse_openapi_json(file_path)
    data = extract_api_info(json_data)
    with open(file_out,'w',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)     

if __name__ == "__main__":
    # 替换为实际的JSON文件路径
    file_path = "bmpqnr-product-v2.json"
    json_path = Path.cwd()
    print(json_path)
    names =json_path.glob("*.json")
    for name in names:
#        print(name)
        print(name.stem)
#        print(name.suffix)
#        print(name.parent)
#        print(name.name)
       


   # json_files = [f for f in cwd.iterdir() if f.suffix == '.json' and f.is_file()]
 
   # save_csv(file_path)

  


    
  