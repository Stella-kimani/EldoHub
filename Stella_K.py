import argparse
import pandas as pd 
import numpy as np 


def wate_hole_analyser(json_string):
    url=f'{json_string}'
    df=pd.read_json(url)
    #number of waterpoints that are functional
    def water_functional(df):
        return len(df[df['water_functioning']=='yes'])

    ## Number of waterpoints per community
    def water_points_per_community(df):
        df2 = df.groupby(['water_point_id','communities_villages']).size().reset_index(name='count')
        return df2.to_json(orient='index')
    
    return print({'Number of Functionals':water_functional(df),'number_water_points':water_points_per_community(df)
    })





if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("data_url", help='add the json string url')
    args=parser.parse_args()
    print(args.data_url)
    wate_hole_analyser(args.data_url)
