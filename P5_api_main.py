from fastapi import FastAPI
import joblib
import numpy as np
import pandas as pd
# from P5_custom_module import TfidfVectorsToArray

def tags_calculation(pred):
    results_preds = np.zeros(pred.shape)
    pred_sorted = np.sort(pred, axis= 1)
    diff = pred_sorted[:, -1] - np.log10(pred_sorted[:, -1] +1)
    results_preds = np.where(pred > diff.reshape(-1, 1), 1, 0)

    with open("tags.txt", "r") as file:
        cols = file.read().split()
        results_df = pd.DataFrame(results_preds, columns= cols).T.reset_index()
        return " ".join(results_df.loc[results_df[0] > 0, "index"].values)


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/{post}")
def tags_predict(post: str):
    model = joblib.load("P5_tags_prediction.sav")
    
    pred = model.predict_proba([post])
    return tags_calculation(pred)
    # return f"Hello {post} !!! :)"
