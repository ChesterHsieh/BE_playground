import numpy as np
import uvicorn
import pandas as pd
from itertools import combinations
from fastapi import FastAPI,Form
from fastapi.responses import HTMLResponse
app = FastAPI()

# def read_file(f_handle):
#     df = pd.read_excel(f_handle)
#     print(df.head())
#     return df
def extract_url2table(url:str)-> float:
    df =pd.read_html(url)[0]
    NUM_STOCK = df.shape[0]
    arr = df.iloc[:, 2:2 + NUM_STOCK].replace('-', 1).to_numpy(dtype=float)
    return arr

def cal_table(arr,weights):
    NUM_STOCK = arr.shape[0]
    num_sum = 0
    for x,y in combinations(list(range(NUM_STOCK)),2):
        num_sum += arr[x][y]*(weights[x]+weights[y])
    return num_sum/(NUM_STOCK-1)

@app.post("/asset_col/")
async def create_upload_files(url:str = Form(...)):
    arr = extract_url2table(url)
    ret = cal_table(arr,np.ones(arr.shape[0])/arr.shape[0])
    return {"weighted_correlation": ret}


@app.get("/")
async def main():
    content = """
<body>
    <form action="/asset_col/" enctype="multipart/form-data" method="post">
    <input name="url" type="text" multiple>
    <input type="submit">
    </form>

</body>
    """
    return HTMLResponse(content=content)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8051)
